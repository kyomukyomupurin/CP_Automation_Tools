import requests
from bs4 import BeautifulSoup
from getpass import getpass
from http.cookiejar import LWPCookieJar
import logging
import sys
from requests import ConnectionError, HTTPError, URLRequired
from datetime import datetime


HOME_URL: str = "https://atcoder.jp"
LOGIN_URL: str = "https://atcoder.jp/login"
COOKIE_SAVE_LOCATION: str = "cookie.txt"


def handle_errors(response: requests.Response) -> None:
    try:
        response.raise_for_status()
    except ConnectionError as err:
        logging.error(" Connection Error: %s", err)
        sys.exit(1)
    except HTTPError as err:
        logging.error(" HTTP Error: %s", err)
        sys.exit(1)
    except URLRequired as err:
        logging.error(" URL Required: %s", err)
        sys.exit(1)
    except Exception as err:
        logging.error(" Unexpected Error: %s", err)
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
    csrf_token: str = bs.find(attrs={"name": "csrf_token"}).get("value")
    data = {"username": username,
            "password": password,
            "csrf_token": csrf_token
            }
    result = session.post(LOGIN_URL, data=data)
    handle_errors(result)
    if is_user_logged_in(session):
        logging.info(" Successfully logged in as \"%s\".", username)
    else:
        logging.error(" Failed to login. Please try again.")
        sys.exit(1)
    cookiejar = LWPCookieJar(COOKIE_SAVE_LOCATION)
    for cookie in session.cookies:
        cookiejar.set_cookie(cookie)
        if cookie.expires:
            logging.info(" This cookie expires at %s",
                         datetime.fromtimestamp(float(cookie.expires)))
    cookiejar.save()
    logging.info(" Saved cookie to [%s].", COOKIE_SAVE_LOCATION)


if __name__ == "__main__":
    logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.INFO)
    username: str = input("UserName: ")
    password: str = getpass()
    session = requests.Session()
    login()
