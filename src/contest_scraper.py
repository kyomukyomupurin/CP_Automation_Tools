import requests
from bs4 import BeautifulSoup
import argparse
from pathlib import Path
from time import sleep
import string
import shutil
import subprocess
from http.cookiejar import LWPCookieJar, LoadError
from subprocess import TimeoutExpired
import logging
from datetime import datetime
import re

from login import handle_errors


COOKIE_SAVE_LOCATION = "cookie.txt"


def save_sample(id: str) -> None:
    problem_url = f"https://atcoder.jp/contests/{contest}/tasks/{contest.replace('-', '_')}_{id}"
    response = session.get(problem_url)
    handle_errors(response)
    bs = BeautifulSoup(response.text, "html.parser")
    flag_YesNo: bool = False
    flag_YESNO: bool = False
    flag_998244353: bool = False
    flag_1000000007: bool = False
    Path(f"{contest}/{id}/sample").mkdir(parents=True)
    number = 1
    for h3 in bs.find_all("h3"):
        h3_text: str = h3.get_text(strip=True)
        if h3_text.startswith("Sample Input"):
            Path(f"{contest}/{id}/sample/input{number}.txt").write_text(
                h3.find_next_sibling("pre").get_text())
        elif h3_text.startswith("Sample Output"):
            Path(f"{contest}/{id}/sample/output{number}.txt").write_text(
                h3.find_next_sibling("pre").get_text())
            number += 1
        elif h3_text == "Output":
            codes = h3.find_next_sibling("p").find_all("code")
            vars = h3.find_next_sibling("p").find_all("var")
            flag_float: bool = "absolute or relative error" in h3.find_next_sibling(
                "p").get_text()
            pattern = re.compile(r"10\^{-[0-9]}")
            for code in codes:
                if code.get_text(strip=True) == "YES":
                    flag_YESNO = True
                if code.get_text(strip=True) == "Yes":
                    flag_YesNo = True
            for var in vars:
                if var.get_text(strip=True) in ["998244353", "998,244,353"]:
                    flag_998244353 = True
                if "10^9+7" in var.get_text(strip=True).replace(" ", ""):
                    flag_1000000007 = True
                if var.get_text(strip=True) in ["1000000007", "1,000,000,007"]:
                    flag_1000000007 = True
                if flag_float:
                    allowable_error: str = var.get_text(
                        strip=True).replace(" ", "").strip("()")
                    if pattern.fullmatch(allowable_error):
                        Path(f"{contest}/{id}/allowable_error.txt").write_text(
                            re.split('[{}]', allowable_error)[1])
    if flag_YesNo and Path(".template/template_YesNo.cc").exists():
        shutil.copy(Path(".template/template_YesNo.cc"),
                    Path(f"{contest}/{id}/task{id}.cc"))
    elif flag_YESNO and Path(".template/template_YESNO.cc").exists():
        shutil.copy(Path(".template/template_YESNO.cc"),
                    Path(f"{contest}/{id}/task{id}.cc"))
    elif flag_998244353 and Path(".template/template_998244353.cc").exists():
        shutil.copy(Path(".template/template_998244353.cc"),
                    Path(f"{contest}/{id}/task{id}.cc"))
    elif flag_1000000007 and Path(".template/template_1000000007.cc").exists():
        shutil.copy(Path(".template/template_1000000007.cc"),
                    Path(f"{contest}/{id}/task{id}.cc"))
    else:
        shutil.copy(Path(".template/template.cc"),
                    Path(f"{contest}/{id}/task{id}.cc"))
    shutil.copy(Path(".template/Makefile"), Path(f"{contest}/{id}/Makefile"))
    logging.info(" Saved task%s", id)


if __name__ == "__main__":
    logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.INFO)
    parser = argparse.ArgumentParser()
    parser.add_argument("contest")
    args = parser.parse_args()
    contest: str = args.contest
    if Path(f"{contest}").exists():
        logging.error(" %s is already exists.", contest)
        exit(1)
    print(f"{contest=}")
    session = requests.Session()
    if not Path(COOKIE_SAVE_LOCATION).exists():
        logging.warning(" Please login before downloading problems.")
        exit(1)
    else:
        cookiejar = LWPCookieJar(COOKIE_SAVE_LOCATION)
        try:
            cookiejar.load()
        except LoadError as err:
            logging.error(f" Load Error: {err}")
            exit(1)
    logging.info(" Loaded an exsisting cookie from [%s].", COOKIE_SAVE_LOCATION)
    for cookie in cookiejar:
        logging.info(" This cookie expires at %s", datetime.fromtimestamp(float(str(cookie.expires))))
    session.cookies.update(cookiejar)
    number_of_tasks: int = 6
    first: bool = True
    for task_id in string.ascii_uppercase[:number_of_tasks]:
        if not first:
            sleep(1.0)
        save_sample(task_id)
        if first:
            premake_process = subprocess.Popen(
                ["make", "-s", "-C", f"{contest}/{task_id}", "run"])
        first = False
    try:
        premake_process.wait(timeout=10)
    except TimeoutExpired as err:
        logging.error(f" Timeout Expired: {err}")
    try:
        Path(f"{contest}/A/taskA").unlink()
    except FileExistsError as err:
        logging.error(f" File Exists Error: {err}")
