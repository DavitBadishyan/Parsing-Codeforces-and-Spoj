import requests
from bs4 import BeautifulSoup as BS

#
# r = requests.get("https://ejudge.rau.am/ejudge/VYcup2021.xml")
# html = BS(r.content, 'html.parser')
#
# for el in html.select(".line > .html-tag"):
#     title = el.select('.html-attribute-value')
#     print(title[0].text)
#     # print(el.text)

s = requests.Session()

# get CSRF
auth_html = s.get("https://smartprogress.do/")
auth_bs = BS(auth_html.content, "html.parser")
csrf = auth_bs.select("input[name=YII_CSRF_TOKEN]")[0]['value']
# login
payload = {
    "YII_CSRF_TOKEN": csrf,
    'returnUrl': '/',
    "UserLoginForm[email]": "davit.badishyan60@gmail.com",
    "UserLoginForm[password]": "parsingisfun",
    "UserLoginForm[rememberMe]": 1

}

answ = s.post("https://smartprogress.do/user/login/", data=payload)
answ_bs = BS(answ.content, "html.parser")
print(f"Name: {answ_bs.select('.user-menu__name')[0].text.strip()}")
