import requests
from bs4 import BeautifulSoup
import argparse
from pathlib import Path
from time import sleep


def save_sample(problem_id: str) -> None:
    response = requests.get(f"{contest_url}/tasks/{contest_name}_{problem_id}")
    if response.status_code != 200:
        print("Error")
        return
    bs = BeautifulSoup(response.text, "html.parser")
    print(bs.title.get_text())
    Path(f"{contest_name}/{problem_id}").mkdir()
    number = 1
    for h3 in bs.find_all("h3"):
        h3_text: str = h3.get_text()
        if h3_text.startswith("Sample Input"):
            print(h3_text)
            print(h3.next_sibling.get_text())
            Path(f"{contest_name}/{problem_id}/input{number}.txt").write_text(
                h3.next_sibling.get_text())
        elif h3_text.startswith("Sample Output"):
            print(h3_text)
            print(h3.next_sibling.get_text())
            Path(f"{contest_name}/{problem_id}/output{number}.txt").write_text(
                h3.next_sibling.get_text())
            number += 1
    Path(f"{contest_name}/{problem_id}/task{problem_id}.cc").touch()
    Path(f"{contest_name}/{problem_id}/Makefile").touch()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("contest_url")
    args = parser.parse_args()
    contest_url: str = args.contest_url
    contest_name = contest_url.split("/")[-1].replace("-", "_")
    print(f"{contest_name=}")
    Path(contest_name).mkdir()

    problems_number = 6

    for num in range(problems_number):
        save_sample(chr(ord("A") + num))
        sleep(1.0)
