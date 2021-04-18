import requests
from bs4 import BeautifulSoup
from getpass import getpass
from http.cookiejar import LWPCookieJar
import logging
from datetime import datetime


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
        logging.error(" HTTP request for [%s] failed.", LOGIN_URL)
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
        logging.error(" Failed to login.")
        return
    # Confirm login
    response = session.get(HOME_URL)
    bs = BeautifulSoup(response.text, "html.parser")
    if bs.find("a", href=f"/users/{username}") is None:
        logging.error(" Failed to login.")
        return
    else:
        logging.info(" Successfully logged in.")
        print(f"Welcome, {username}.")
    for cookie in session.cookies:
        cookiejar.set_cookie(cookie)
    cookiejar.save()
    logging.info(" Saved cookie to \"%s\".", COOKIE_SAVE_LOCATION)
    logging.info(" This cookie expires at %s.", )
    for cookie in cookiejar:
        logging.info(" This cookie expires at %s", datetime.fromtimestamp(float(str(cookie.expires))))

if __name__ == "__main__":
    logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.INFO)
    login()
