import calendar
import datetime
import json

import requests
from bs4 import BeautifulSoup as BS
from colorama import Fore, Back, init

from INFO import average
from dictionary import getname

#  Colorama
init(autoreset=True)
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
}


# https://unixtime.org/

def cfrange(group, m, d, m1, d1):
    localtime = 14400
    t1 = datetime.datetime(2022, m, d, 0, 0, 0)
    t2 = datetime.datetime(2022, m1, d1, 0, 0, 0)
    L = calendar.timegm(t1.timetuple()) - localtime
    R = calendar.timegm(t2.timetuple()) - localtime
    cflr(group, L, R)


def cflr(x, L, R):
    l = str(datetime.datetime.fromtimestamp(L))[:10]
    r = str(datetime.datetime.fromtimestamp(R))[:10]
    print(Fore.RED + l, "~", Fore.RED + r)
    print(Fore.YELLOW + "group", x)

    path = 'groups/codeforces/' + str(x) + '.txt'
    with open(path) as f:
        users = f.readlines()

    for i in range(len(users)):
        if users[i][-1] == '\n':
            users[i] = users[i][:-1]

    for user in users:
        if x == 7:
            prevname = user
            user = getname(user)
            if user[:5] == 'Error':
                print(Fore.RED + "Error " + prevname)
                continue
        flag = 1
        while flag:
            flag = 0
            d = dict()
            try:
                url = f"https://codeforces.com/api/user.status?handle={user}"
                r = requests.get(url, headers=headers)
                soup = BS(r.content, 'html.parser')
                # with open(f"status/{user}.json", "w") as file:
                #     file.write(str(soup))
                # data = json.load(open(f'status/{user}.json'))
                # print(data)
                data = json.loads(str(soup))
                for item in data["result"]:
                    # print(item)
                    try:
                        name = str(item["problem"]["contestId"]) + str(item["problem"]['index'])
                        verdict = item['verdict']
                        rating = int(item["problem"]["rating"])
                        # print(item["problem"]["rating"])
                        timesolved = int(item["creationTimeSeconds"])
                        if verdict == 'OK':
                            d[name] = [timesolved, rating]
                        # print(name)
                    except Exception:
                        pass
                        # acmsguru type problems
                        # print(item)

                cnt = 0
                sumrating = 0
                for key, value in d.items():
                    if value[0] >= L and value[0] <= R:
                        cnt += 1
                        sumrating += int(value[1])
                        # print(key, value)

                isok = 1
                while isok:
                    isok = 0
                    try:
                        # contests number in this interval
                        url = f"https://codeforces.com/api/user.rating?handle={user}"
                        r = requests.get(url, headers=headers)
                        soup = BS(r.content, 'html.parser')
                        data = json.loads(str(soup))
                        contestNumber = 0
                        for item in data["result"]:
                            cur = int(item["ratingUpdateTimeSeconds"])
                            if cur >= L and cur <= R:
                                contestNumber += 1
                        print(Back.BLACK + user,
                              Fore.RED + str(cnt),
                              Fore.BLUE + str(round(sumrating / max(cnt, 1))),
                              Fore.GREEN + str(contestNumber))
                    except Exception:
                        isok = 1
            except Exception:
                flag = 1


if __name__ == "__main__":
    cfrange(7, 11, 1, 11, 30)
