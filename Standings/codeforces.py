import requests
from bs4 import BeautifulSoup as BS
from time import sleep
import json
from colorama import Fore, Back, Style, init

# https://codeforces.com/api/user.rating?handle=
# https://codeforces.com/api/user.status?handle=
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
# print(users)

USERS = dict()

for group in users:
    for name in group:
        problems = -1
        CurrentRating = -1
        MaximumRating = -1
        path = "https://codeforces.com/profile/" + name
        r = requests.get(path, headers=headers)
        html = BS(r.content, 'html.parser')
        for el in html.select("._UserActivityFrame_counterValue"):
            problems = (el.text.strip().split()[0])
            break
        c = 0
        for el in html.select(".info > ul > li > span"):
            data = (el.text.strip()).split(" ")[-1]
            if c == 1:
                data = data[0:-1]
                MaximumRating = data
                if not data.isnumeric():
                    MaximumRating = 0
                    CurrentRating = 0
            else:
                CurrentRating = data
            c += 1
            if c == 2:
                break
        USERS[name] = str(problems) + '$' + str(CurrentRating) + '$' + str(MaximumRating)

# ###############################
# contests number and rank

for i in range(6):
    for user in users[i]:
        flag = 1
        while flag:
            flag = 0
            try:
                url = f"https://codeforces.com/api/user.rating?handle={user}"
                r = requests.get(url, headers=headers)
                soup = BS(r.content, 'html.parser')

                with open(f"data/{user}.json", "w") as file:
                    file.write(str(soup))
                data = json.load(open(f'data/{user}.json'))
                contestsNumber = len(data["result"])
                rank = 50000
                for item in data["result"]:
                    rank = min(rank, int(item["rank"]))
                if rank == 50000:
                    rank = -1
                USERS[user] += "$" + str(contestsNumber) + "$" + str(rank)
            except Exception:
                flag = 1
# we can add sleep(2) instead of while
# if we remove while | the site would not be loaded at time

#  Colorama
init(autoreset=True)
for i in range(6):
    print(Fore.GREEN + "\nGroup", i + 1)
    for name in users[i]:
        print(Back.BLACK + name, end="\t")
        data = USERS[name].split('$')
        print(Fore.RED + data[0], Fore.MAGENTA + data[3], Fore.CYAN + data[4], Fore.GREEN + Fore.YELLOW + data[1],
              Fore.BLUE + data[2], sep="   ")
        # print(Fore.RED + data[0], Fore.GREEN + Fore.YELLOW + data[1], Fore.BLUE + data[2], Fore.MAGENTA + data[3],
        #       Fore.CYAN + data[4], sep="   ")
        print(Fore.WHITE, end="")
