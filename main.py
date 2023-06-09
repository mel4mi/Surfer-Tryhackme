import requests
from bs4 import BeautifulSoup
import io
import PyPDF2

ip = "10.10.240.103"  # change to target ip


def get_cookie(ip):
    url = f"http://{ip}/login.php"
    verify = f"http://{ip}/verify.php"

    session = requests.Session()

    response = session.post(verify, data={'username': 'admin', 'password': 'admin'})

    cookies = session.cookies.get_dict()
    phpsessid = cookies['PHPSESSID']
    return phpsessid


print(get_cookie(ip))
