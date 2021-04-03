import requests
from bs4 import BeautifulSoup
from pathlib import Path


def submit() -> None:
    directory_path = str(Path.cwd()).split("/")
    contest, task_id = directory_path[-2], directory_path[-1], 
    submit_url = f"https://atcoder.jp/contests/{contest}/submit"
    session = requests.Session()
    response = session.get(submit_url)
    bs = BeautifulSoup(response.text, "html.parser")
    token: str = bs.find(attrs={"name": "csrf_token"}).get("value")
    payload = {"data.TaskScreenName": f"{contest}_{task_id.lower()}", "data.LanguageId": 4003,
               "sourceCode": Path(f"task{task_id}.cc").read_text(), "csrf_token": token}
    result = session.post(submit_url, data=payload)
    if result.status_code != 200:
        print("Failed")
    else:
        print("Successfully submitted!")

if __name__ == "__main__":
    submit()
