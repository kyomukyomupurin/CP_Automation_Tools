import requests
from bs4 import BeautifulSoup
import argparse
from pathlib import Path
from time import sleep
import string
import shutil
import subprocess
from http.cookiejar import LWPCookieJar
import logging


COOKIE_SAVE_LOCATION = "cookie.txt"


def save_sample(id: str) -> None:
    problem_url = f"https://atcoder.jp/contests/{contest}/tasks/{contest.replace('-', '_')}_{id}"
    session = requests.Session()
    if not Path(COOKIE_SAVE_LOCATION).exists():
        logging.warning(" Please login before downloading problems.")
        return
    else:
        cookiejar = LWPCookieJar(COOKIE_SAVE_LOCATION)
        cookiejar.load()
        logging.info(" Loaded an exsisting cookie from \"%s\"", COOKIE_SAVE_LOCATION)
        session.cookies.update(cookiejar)
    response = session.get(problem_url)
    try:
        response.raise_for_status()
    except:
        logging.error(" HTTP request for \"%s\" failed.", problem_url)
        return
    bs = BeautifulSoup(response.text, "html.parser")
    Path(f"{contest}/{id}/sample").mkdir(parents=True)
    number = 1
    for h3 in bs.find_all("h3"):
        h3_text: str = h3.get_text()
        if h3_text.startswith("Sample Input"):
            Path(f"{contest}/{id}/sample/input{number}.txt").write_text(
                h3.find_next_sibling("pre").get_text())
        elif h3_text.startswith("Sample Output"):
            Path(f"{contest}/{id}/sample/output{number}.txt").write_text(
                h3.find_next_sibling("pre").get_text())
            number += 1
    shutil.copy(Path(".template/template.cc"),
                Path(f"{contest}/{id}/task{id}.cc"))
    shutil.copy(Path(".template/Makefile"), Path(f"{contest}/{id}/Makefile"))
    logging.info(" Saved task%s", id)
    if id == "A":
        subprocess.Popen(["make", "-s", "-C", f"{contest}/{id}", "run"])


if __name__ == "__main__":
    logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.INFO)
    parser = argparse.ArgumentParser()
    parser.add_argument("contest")
    args = parser.parse_args()
    contest: str = args.contest
    print(f"{contest=}")
    number_of_tasks = 6
    for task_id in string.ascii_uppercase[:number_of_tasks]:
        save_sample(task_id)
        if task_id != string.ascii_uppercase[number_of_tasks - 1]:
            sleep(1.0)
    Path(f"{contest}/A/taskA").unlink()
