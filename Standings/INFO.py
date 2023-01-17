import requests
from bs4 import BeautifulSoup as BS
import json
from colorama import Fore, Back, Style, init
from dictionary import getname

# https://codeforces.com/api/user.rating?handle=
# https://codeforces.com/api/user.status?handle=
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
}


def info(name):
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
    res = dict()
    res["problems"] = str(problems)
    res["currat"] = str(CurrentRating)
    res["maxrat"] = str(MaximumRating)

    # -------------------------------------------------

    flag = 1
    while flag:
        flag = 0
        try:
            url = f"https://codeforces.com/api/user.rating?handle={name}"
            r = requests.get(url, headers=headers)
            soup = BS(r.content, 'html.parser')

            # with open(f"data/{user}.json", "w") as file:
            #     file.write(str(soup))
            # data = json.load(open(f'data/{user}.json'))

            data = json.loads(str(soup))
            contestsNumber = len(data["result"])
            # rank = 50000
            # for item in data["result"]:
            #     rank = min(rank, int(item["rank"]))
            # if rank == 50000:
            #     rank = -1
            # USERS[user] += "$" + str(contestsNumber) + "$" + str(rank)
            res["contests"] = str(contestsNumber)
        except Exception:
            flag = 1
    return res


def average(name):
    d = dict()

    flag = 1
    while flag:
        flag = 0
        try:
            url = f"https://codeforces.com/api/user.status?handle={name}"
            r = requests.get(url, headers=headers)
            soup = BS(r.content, 'html.parser')
            data = json.loads(str(soup))
            for item in data["result"]:
                try:
                    nm = str(item["problem"]["contestId"]) + str(item["problem"]['index'])
                    verdict = item['verdict']
                    rating = item["problem"]["rating"]
                    # print(verdict, rating)
                    # print(rating)
                    if verdict == 'OK':
                        d[nm] = rating
                except Exception:
                    pass
                    # acmsguru type problems
                    # print(item)

            # print(Fore.GREEN + name, av / cnt)
            sm = 0
            cnt = 0
            for key, val in d.items():
                # print(key, val)
                cnt += 1
                sm += val
            if cnt == 0:
                cnt = 1
            return round(sm / cnt)
        except Exception:
            flag = 1


if __name__ == "__main__":
    print(average("vahaghar"))
    print(average("__DAvit__"))
