import time

import requests
from bs4 import BeautifulSoup as BS
from time import sleep
import json
from colorama import Fore, Back, Style, init

#  Colorama
init(autoreset=True)
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
}
users = [[], [], [], [], [], []]
for i in range(6):
    path = 'groups/codeforces/' + str(i + 1) + '.txt'
    with open(path) as f:
        users[i] = f.readlines()

for group in users:
    for i in range(len(group)):
        if group[i][-1] == '\n':
            group[i] = group[i][:-1]

# https://unixtime.org/
timeFrom = 166292640
timeTo = 166429993150
for i in range(6):
    print(Fore.YELLOW + "group", i + 1)
    for user in users[i]:
        flag = 1
        while flag:
            flag = 0
            d = dict()
            try:
                url = f"https://codeforces.com/api/user.status?handle={user}"
                r = requests.get(url, headers=headers)
                soup = BS(r.content, 'html.parser')
                with open(f"status/{user}.json", "w") as file:
                    file.write(str(soup))
                data = json.load(open(f'status/{user}.json'))
                for item in data["result"]:
                    # print(item)
                    verdict = item['verdict']
                    name = str(item["problem"]["contestId"]) + str(item["problem"]['index'])
                    timesolved = item["creationTimeSeconds"]
                    if verdict == 'OK':
                        d[name] = timesolved
                cnt = 0
                for key, value in d.items():
                    if value >= timeFrom and value <= timeTo:
                        cnt += 1
                        # print(key, value)
                print(Fore.GREEN + user, cnt)
            except Exception:
                print(Fore.RED + user)
                pass
                # flag = 1
                # print("NO Connection")
