import requests
from bs4 import BeautifulSoup
import argparse
from pathlib import Path
from time import sleep
import string


def save_sample(id: str) -> None:
    response = requests.get(
        f"https://atcoder.jp/contests/{contest}/tasks/{contest}_{id}")
    if response.status_code != 200:
        print("Error")
        return
    bs = BeautifulSoup(response.text, "html.parser")
    print(bs.title.get_text())
    Path(f"{contest}/{id}/sample").mkdir(parents=True)
    number = 1
    for h3 in bs.find_all("h3"):
        h3_text: str = h3.get_text()
        if h3_text.startswith("Sample Input"):
            print(h3_text)
            print(h3.next_sibling.get_text())
            Path(f"{contest}/{id}/sample/input{number}.txt").write_text(
                h3.next_sibling.get_text())
        elif h3_text.startswith("Sample Output"):
            print(h3_text)
            print(h3.next_sibling.get_text())
            Path(f"{contest}/{id}/sample/output{number}.txt").write_text(
                h3.next_sibling.get_text())
            number += 1
    Path(f"{contest}/{id}/task{id}.cc").write_text(Path("template.cc").read_text())
    Path(f"{contest}/{id}/Makefile").write_text(Path("Makefile").read_text())


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("contest")
    args = parser.parse_args()
    contest: str = args.contest
    print(f"{contest=}")
    Path(contest).mkdir()

    problems_number = 6

    for problem_id in string.ascii_uppercase[:problems_number]:
        save_sample(problem_id)
        sleep(1.0)
