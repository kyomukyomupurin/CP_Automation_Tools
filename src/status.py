import requests
from bs4 import BeautifulSoup
import logging
from pathlib import Path
import sys
from http.cookiejar import LWPCookieJar, LoadError

from color_printer import Color
from login import handle_errors, is_user_logged_in

COOKIE_SAVE_LOCATION: str = "./../../cookie.txt"


def get_status() -> None:
    directory_path: list[str] = str(Path.cwd()).split("/")
    contest: str = directory_path[-2]
    submission_url: str = f"https://atcoder.jp/contests/{contest}/submissions/me"
    cookiejar = LWPCookieJar(COOKIE_SAVE_LOCATION)
    try:
        cookiejar.load()
    except LoadError as err:
        logging.error(" Load Error: %s", err)
        sys.exit(1)
    session = requests.Session()
    session.cookies.update(cookiejar)
    if not is_user_logged_in(session):
        logging.error(" Please login before checking status.")
        sys.exit(1)
    response = session.get(submission_url)
    handle_errors(response)
    bs = BeautifulSoup(response.text, "html.parser")
    tbody = bs.find("tbody")
    if tbody is None:
        logging.info(" No submission was found.")
        sys.exit(0)
    for tr in tbody.find_all("tr"):
        submission_info: list[str] = [td.get_text(strip=True) for td in tr.find_all(
            "td") if len(td.find_all("a")) < 2 and td.get_text(strip=True) != "Detail"]
        [submission_time, task, language, score, code_size,
            status, exec_time, memory] = submission_info
        status_color = Color.GREEN if status == "AC" else Color.YELLOW
        print(
            f" {submission_time[:-5]}   {task[0]}   {language:>15}   {score:>4}   {code_size:>11}   {status_color}{status:>3}{Color.DEFAULT}   {exec_time:>7}   {memory:>9}")


if __name__ == "__main__":
    logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.INFO)
    get_status()
