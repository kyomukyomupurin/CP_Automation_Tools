import requests
from bs4 import BeautifulSoup
from pathlib import Path
from http.cookiejar import LWPCookieJar, LoadError
import logging
from datetime import datetime
import sys

from login import handle_errors, is_user_logged_in


COOKIE_SAVE_LOCATION = "./../../cookie.txt"


def submit() -> None:
    directory_path = str(Path.cwd()).split("/")
    contest, task_id = directory_path[-2], directory_path[-1]
    submit_url = f"https://atcoder.jp/contests/{contest}/submit"
    cookiejar = LWPCookieJar(COOKIE_SAVE_LOCATION)
    try:
        cookiejar.load()
    except LoadError as err:
        logging.error(f" Load Error: {err}")
        sys.exit(1)
    logging.info(" Loaded an exsisting cookie from [%s].", COOKIE_SAVE_LOCATION)
    for cookie in cookiejar:
        logging.info(" This cookie expires at %s", datetime.fromtimestamp(float(str(cookie.expires))))
    session = requests.Session()
    session.cookies.update(cookiejar)
    if not is_user_logged_in(session):
        logging.error(" Please login before doanloading problems.")
        sys.exit(1)
    response = session.get(submit_url)
    handle_errors(response)
    bs = BeautifulSoup(response.text, "html.parser")
    token: str = bs.find(attrs={"name": "csrf_token"}).get("value")
    payload = {"data.TaskScreenName": f"{contest}_{task_id.lower()}",
               "data.LanguageId": 4003,
               "sourceCode": Path(f"task{task_id}.cc").read_text(),
               "csrf_token": token
               }
    result = session.post(submit_url, data=payload)
    handle_errors(result)
    logging.info(" Successfully submitted!")


if __name__ == "__main__":
    logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.INFO)
    submit()
