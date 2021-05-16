import requests
from bs4 import BeautifulSoup
from pathlib import Path
from http.cookiejar import LWPCookieJar, LoadError
import logging
from datetime import datetime
import sys

from login import handle_errors, is_user_logged_in


COOKIE_SAVE_LOCATION: str = "./../../cookie.txt"


def submit() -> None:
    cookiejar = LWPCookieJar(COOKIE_SAVE_LOCATION)
    try:
        cookiejar.load()
    except LoadError as err:
        logging.error(" Load Error: %s", err)
        sys.exit(1)
    logging.info(
        " Loaded an exsisting cookie from [%s].", COOKIE_SAVE_LOCATION)
    for cookie in cookiejar:
        if cookie.expires:
            logging.info(" This cookie expires at %s",
                         datetime.fromtimestamp(float(cookie.expires)))
    session = requests.Session()
    session.cookies.update(cookiejar)
    if not is_user_logged_in(session):
        logging.error(" Please login before doanloading problems.")
        sys.exit(1)
    directory_path: list[str] = str(Path.cwd()).split("/")
    contest, task_id = directory_path[-2], directory_path[-1]
    submit_url: str = f"https://atcoder.jp/contests/{contest}/submit"
    response = session.get(submit_url)
    handle_errors(response)
    bs = BeautifulSoup(response.text, "html.parser")
    csrf_token: str = bs.find(attrs={"name": "csrf_token"}).get("value")
    data = {"data.TaskScreenName": f"{contest}_{task_id.lower()}",
            "data.LanguageId": 4003,
            "sourceCode": ("// This code is generated and submitted by [CP_Automation_Tools](https://github.com/kyomukyomupurin/CP_Automation_Tools)\n\n"
                           f"{Path(f'task{task_id}.cc').read_text()}"
                           ),
            "csrf_token": csrf_token
            }
    result = session.post(submit_url, data=data)
    handle_errors(result)
    logging.info(" Successfully submitted!")


if __name__ == "__main__":
    logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.INFO)
    submit()
