import requests
from bs4 import BeautifulSoup
import argparse
import sys
from pathlib import Path
from time import sleep


# AtCoder
def save_sample(problem_id: str):
    problem_url = contest_url + "/tasks/" + contest_name + '_' + problem_id
    response = requests.get(problem_url)
    status = response.status_code
    if status != 200:
        print("Error")
        return
    print("Status : " + str(response.status_code))
    bs = BeautifulSoup(response.text, "html.parser")
    print(bs.title.get_text())

    for h3_element in bs.find_all("h3"):
        h3_text = h3_element.get_text()
        if h3_text.startswith("Sample Input") or h3_text.startswith("Sample Output"):
            print(h3_text)
            print(h3_element.next_sibling.get_text())


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("contest_url")
    args = parser.parse_args()
    contest_url = args.contest_url
    contest_name = contest_url.split('/')[-1]
    print("Contest Name : " + contest_name)

    problems_number = 6

    for id in range(problems_number):
        save_sample(chr(ord('a') + id))
        sleep(1.0)
