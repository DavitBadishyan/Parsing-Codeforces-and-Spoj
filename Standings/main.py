from codeforces import cf
from spoj import spoj
from codeforcesLR import cflr
from solo import solo
from dictionary import getname
from colorama import Fore, Back, Style, init
from INFO import info, average
import datetime
import calendar


def cfrange(group, m, d, m1, d1):
    localtime = 14400
    t1 = datetime.datetime(2022, m, d, 0, 0, 0)
    t2 = datetime.datetime(2022, m1, d1, 0, 0, 0)
    L = calendar.timegm(t1.timetuple()) - localtime
    R = calendar.timegm(t2.timetuple()) - localtime
    cflr(group, L, R)


def spojAll():
    for i in range(1, 6):
        spoj(i)


def cfAll():
    for i in range(1, 7):
        cf(i)


# for key, value in translate.items():
#     print(key, value)

# print(getname())

#
cfAll()
cfrange(2, 11, 1, 11, 30)
cfrange(3, 11, 1, 11, 30)
cfrange(4, 11, 1, 11, 30)
cfrange(5, 11, 1, 11, 30)
cfrange(7, 11, 1, 11, 30)


# d = [

# ]

# cfrange(7, 12, 1, 12, 31)
# for k in d:
# print(getname(k))
#     if getname(k)[:5] == 'Error':
#         print(Fore.RED + "Error " + k)
#         continue
#
# cfrange(7, 10, 1, 10, 30)
