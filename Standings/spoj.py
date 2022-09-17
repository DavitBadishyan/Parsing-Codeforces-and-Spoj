import requests
from bs4 import BeautifulSoup as BS

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

for group in users:
    for name in group:
        path = "https://gm.spoj.com/users/" + name
        r = requests.get(path)
        html = BS(r.content, 'html.parser')
        for el in html.select(".table-condensed"):
            data = (el.text.strip().split())
            # print(data)
            USERS[name] = 0
            for x in data:
                USERS[name] += x[0:4] != "EASY"
            break

for i in range(5):
    print("\nGroup", i + 1, "\n")
    for name in users[i]:
        print(name, end=" ")
        data = USERS[name]
        print(data)
