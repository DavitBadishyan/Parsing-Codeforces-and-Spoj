import requests
from bs4 import BeautifulSoup as BS
import json
from colorama import Fore, Back, Style, init
from solo import solo
from dictionary import getname

# https://codeforces.com/api/user.rating?handle=
# https://codeforces.com/api/user.status?handle=
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
}

#  Colorama
init(autoreset=True)
USERS = dict()


def cf(x):
    USERS.clear()
    print("cf: ", Fore.YELLOW + "group", x)
    path = 'groups/codeforces/' + str(x) + '.txt'
    with open(path) as f:
        users = f.readlines()
        # print(users)

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
        solo(user)


# we can add sleep(2) instead of while
# if we remove while | the site would not be loaded at time

if __name__ == "__main__":
    # cf(1)
    # cf(2)
    # cf(3)
    # cf(4)
    # cf(5)
    # cf(6)
    cf(7)
