import requests
from bs4 import BeautifulSoup


def login() -> None:
    session = requests.Session()
    response = session.get("https://atcoder.jp/login")
    bs = BeautifulSoup(response.text, "html.parser")
    token: str = bs.find(attrs={"name": "csrf_token"}).get("value")
    print(token)
    
    payload = {"username" : "", "password" : "", "csrf_token" : "token"}
    

if __name__ == "__main__":
    login()
