import requests
from bs4 import BeautifulSoup
from getpass import getpass
from http.cookiejar import LWPCookieJar


HOME_URL = "https://atcoder.jp"
LOGIN_URL = "https://atcoder.jp/login"
COOKIE_SAVE_LOCATION = "cookie.txt"


def login() -> None:
    username: str = input("UserName: ")
    password: str = getpass()
    session = requests.Session()
    cookiejar = LWPCookieJar(COOKIE_SAVE_LOCATION)
    response = session.get(LOGIN_URL)
    try:
        response.raise_for_status()
    except:
        print(f"HTTP request for \"{LOGIN_URL}\" failed.")
        return
    bs = BeautifulSoup(response.text, "html.parser")
    token: str = bs.find(attrs={"name": "csrf_token"}).get("value")
    payload = {"username": username,
               "password": password,
               "csrf_token": token
               }
    result = session.post(LOGIN_URL, data=payload)
    try:
        result.raise_for_status()
    except:
        print("Failed to login...")
        return

    # Confirm login
    response = session.get(HOME_URL)
    bs = BeautifulSoup(response.text, "html.parser")
    if bs.find("a", href=f"/users/{username}") is None:
        print("Failed to login...")
        return
    else:
        print("Successfully logged in!")
        print(f"Welcome, {username}")
    # Update cookie
    for cookie in session.cookies:
        cookiejar.set_cookie(cookie)
    cookiejar.save()


if __name__ == "__main__":
    login()
