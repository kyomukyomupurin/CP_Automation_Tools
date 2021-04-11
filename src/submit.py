import requests
from bs4 import BeautifulSoup
from pathlib import Path
from http.cookiejar import LWPCookieJar


COOKIE_SAVE_LOCATION = "./../../cookie.txt"


def submit() -> None:
    directory_path = str(Path.cwd()).split("/")
    contest, task_id = directory_path[-2], directory_path[-1]
    submit_url = f"https://atcoder.jp/contests/{contest}/submit"
    session = requests.Session()
    if not Path(COOKIE_SAVE_LOCATION).exists():
        print("Please login before submit.")
        return
    else:
        cookiejar = LWPCookieJar(COOKIE_SAVE_LOCATION)
        cookiejar.load()
        session.cookies.update(cookiejar)
    response = session.get(submit_url)
    try:
        response.raise_for_status()
    except:
        print(f"HTTP request for \"{submit_url}\" failed.")
        return
    bs = BeautifulSoup(response.text, "html.parser")
    token: str = bs.find(attrs={"name": "csrf_token"}).get("value")
    payload = {"data.TaskScreenName": f"{contest}_{task_id.lower()}",
               "data.LanguageId": 4003,
               "sourceCode": Path(f"task{task_id}.cc").read_text(),
               "csrf_token": token
               }
    result = session.post(submit_url, data=payload)
    try:
        result.raise_for_status()
    except:
        print("Failed to submit...")
        return
    print("Successfully submitted!")


if __name__ == "__main__":
    submit()
