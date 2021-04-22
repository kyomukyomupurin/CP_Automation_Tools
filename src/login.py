import requests
from bs4 import BeautifulSoup
from getpass import getpass
from http.cookiejar import LWPCookieJar
import logging
import sys
from requests import ConnectionError, HTTPError, URLRequired
from datetime import datetime


HOME_URL = "https://atcoder.jp"
LOGIN_URL = "https://atcoder.jp/login"
COOKIE_SAVE_LOCATION = "cookie.txt"


def handle_errors(response: requests.Response) -> None:
    try:
        response.raise_for_status()
    except ConnectionError as err:
        logging.error(f" Connection Error: {err}")
        sys.exit(1)
    except HTTPError as err:
        logging.error(f" HTTP Error: {err}")
        sys.exit(1)
    except URLRequired as err:
        logging.error(f" URL Required: {err}")
        sys.exit(1)
    except Exception as err:
        logging.error(f" Unexpected Error: {err}")
        sys.exit(1)


def is_user_logged_in(session: requests.Session) -> bool:
    response = session.get(HOME_URL)
    handle_errors(response)
    bs = BeautifulSoup(response.text, "html.parser")
    return bs.find("a", href=f"/settings") is not None


def login() -> None:
    response = session.get(LOGIN_URL)
    handle_errors(response)
    bs = BeautifulSoup(response.text, "html.parser")
    token: str = bs.find(attrs={"name": "csrf_token"}).get("value")
    payload = {"username": username,
               "password": password,
               "csrf_token": token
               }
    result = session.post(LOGIN_URL, data=payload)
    handle_errors(result)
    if is_user_logged_in(session):
        logging.info(" Successfully logged in.")
        print(f"Welcome, {username}.")
    else:
        logging.error(" Failed to login. Please try again.")
        sys.exit(1)
    cookiejar = LWPCookieJar(COOKIE_SAVE_LOCATION)
    for cookie in session.cookies:
        cookiejar.set_cookie(cookie)
    cookiejar.save()
    logging.info(" Saved cookie to [%s].", COOKIE_SAVE_LOCATION)
    for cookie in cookiejar:
        if cookie.expires is not None:
            logging.info(" This cookie expires at %s", datetime.fromtimestamp(float(str(cookie.expires))))

if __name__ == "__main__":
    logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.INFO)
    username: str = input("UserName: ")
    password: str = getpass()
    session = requests.Session()
    login()
