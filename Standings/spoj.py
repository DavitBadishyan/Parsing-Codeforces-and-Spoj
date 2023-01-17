import time

import requests
from bs4 import BeautifulSoup as BS
from colorama import Fore, Back, Style, init

USERS = dict()


def spoj(x):
    USERS.clear()
    print("spoj: ", Fore.YELLOW + "group", x)
    path = 'groups/spoj/' + str(x) + '.txt'
    with open(path) as f:
        users = f.readlines()

    for i in range(len(users)):
        if users[i][-1] == '\n':
            users[i] = users[i][:-1]

    for user in users:
        path = "https://gm.spoj.com/users/" + user
        r = requests.get(path)
        html = BS(r.content, 'html.parser')
        for el in html.select(".table-condensed"):
            data = (el.text.strip().split())
            USERS[user] = 0
            for x in data:
                USERS[user] += x[0:4] != "EASY"
            print(Fore.GREEN + user, USERS[user])
            break


if __name__ == "__main__":
    spoj(1)
    spoj(2)
    spoj(3)
    spoj(4)
    spoj(5)
