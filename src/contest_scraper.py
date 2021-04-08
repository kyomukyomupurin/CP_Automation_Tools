import requests
from bs4 import BeautifulSoup
import argparse
from pathlib import Path
from time import sleep
import string
import shutil
import subprocess


def save_sample(id: str) -> None:
    response = requests.get(
        f"https://atcoder.jp/contests/{contest}/tasks/{contest.replace('-', '_')}_{id}")
    try:
        response.raise_for_status()
    except:
        print("Error")
        return
    bs = BeautifulSoup(response.text, "html.parser")
    print(f"Saving task{id}...", end="")
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
    print(" OK")
    shutil.copy(Path("template.cc"), Path(f"{contest}/{id}/task{id}.cc"))
    shutil.copy(Path("Makefile"), Path(f"{contest}/{id}/Makefile"))
    if id == "A":
        subprocess.Popen(["make", "-s", "-C", f"{contest}/{id}", "run"])

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("contest")
    args = parser.parse_args()
    contest: str = args.contest
    print(f"{contest=}")
    Path(contest).mkdir()
    number_of_tasks = 6
    for task_id in string.ascii_uppercase[:number_of_tasks]:
        save_sample(task_id)
        if task_id != string.ascii_uppercase[number_of_tasks - 1]:
            sleep(1.0)
    Path(f"{contest}/A/taskA").unlink()
