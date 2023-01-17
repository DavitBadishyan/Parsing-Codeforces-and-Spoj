import requests
from bs4 import BeautifulSoup as BS
import json
from colorama import Fore, Back, Style, init
from INFO import info
from dictionary import getname

# https://codeforces.com/api/user.rating?handle=
# https://codeforces.com/api/user.status?handle=
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
}

#  Colorama
init(autoreset=True)


def solo(name):
    data = info(name)
    print(Back.BLACK + name, end="\t")
    print(Fore.RED + data["problems"],
          Fore.MAGENTA + data["contests"],
          Fore.GREEN + Fore.YELLOW + data["currat"],
          Fore.BLUE + data["maxrat"],
          sep="   ")
    # print(Fore.WHITE, end="")



if __name__ == "__main__":
    solo(getname("davit badishyan"))
