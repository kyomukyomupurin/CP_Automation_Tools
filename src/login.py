import requests
from bs4 import BeautifulSoup


login_url = "https://atcoder.jp/login"

def login() -> None:
    session = requests.Session()
    response = session.get(login_url)
    if response.status_code != 200:
        print("Error")
        return
    bs = BeautifulSoup(response.text, "html.parser")
    token: str = bs.find(attrs={"name": "csrf_token"}).get("value")
    print(token)    
    payload = {"username" : "", "password" : "", "csrf_token" : token}
    result = session.post(login_url, data=payload)
    if result.status_code != 200:
        print("Failed...")
    else:
        print("Successfull logged in!")

if __name__ == "__main__":
    login()
