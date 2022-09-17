# import requests
# from bs4 import BeautifulSoup as BS
# from time import sleep
# import json
#
# # https://codeforces.com/api/user.rating?handle=
# # https://codeforces.com/api/user.status?handle=
# url = "https://codeforces.com/api/user.rating?handle=boris_7"
# headers = {
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
# }
# r = requests.get(url, headers=headers)
# soup = BS(r.content, 'html.parser')
#
# with open("data.json", "w") as file:
#     file.write(str(soup))
# data = json.load(open('data.json'))
# contestsNumber = len(data["result"])
# rank = 100000
# for item in data["result"]:
#     rank = min(rank, int(item["rank"]))
#
# print(rank, contestsNumber)
