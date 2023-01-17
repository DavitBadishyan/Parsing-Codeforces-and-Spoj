import requests
from bs4 import BeautifulSoup as BS
from colorama import Fore, Back, Style, init

users = [[], [], [], [], []]
for i in range(5):
    path = 'groups/spoj/' + str(i + 1) + '.txt'
    with open(path) as f:
        users[i] = f.readlines()

for group in users:
    for i in range(len(group)):
        if group[i][-1] == '\n':
            group[i] = group[i][:-1]
# print(users)

USERS = dict()
groupnumber = 1
for group in users:
    print(Fore.YELLOW + "group " + str(groupnumber))
    groupnumber += 1
    for name in group:
        path = "https://am.spoj.com/users/" + name
        r = requests.get(path)
        html = BS(r.content, 'html.parser')
        for el in html.select(".table-condensed"):
            data = (el.text.strip().split())
            # print(data)
            USERS[name] = 0
            for x in data:
                USERS[name] += 1
            print(Fore.GREEN + name, USERS[name])
            break

#
# for i in range(5):
#     print("\nGroup", i + 1, "\n")
#     for name in users[i]:
#         print(name, end=" ")
#         data = USERS[name]
#         print(data)
