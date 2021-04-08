import requests
from bs4 import BeautifulSoup
from getpass import getpass


login_url = "https://atcoder.jp/login"


def login() -> None:
    username: str = input("UserName: ")
    password: str = getpass()
    session = requests.Session()
    response = session.get(login_url)
    try:
        response.raise_for_status()
    except:
        print("Error")
        return
    bs = BeautifulSoup(response.text, "html.parser")
    token: str = bs.find(attrs={"name": "csrf_token"}).get("value")
    print(token)
    payload = {"username": username,
               "password": password,
               "csrf_token": token
               }
    result = session.post(login_url, data=payload)
    try:
        result.raise_for_status()
    except:
        print("Failed to login...")
        return


if __name__ == "__main__":
    login()
