import requests
import hashlib
import sys

# ввод пароля(тестовый)
password = sys.argv[1]


def check(passwd):
    i = hashlib.sha1(passwd.encode()).hexdigest().upper()
    r = i[:5]
    req = requests.get('https://api.pwnedpasswords.com/range/' + r)
    if req.status_code == 200:
        u = req.content.decode().split('\n')
        e = i[5:40]
        for j in range(len(u)):
            f = u[j].split(':')[0]
            t = int(u[j].split(":")[1])
            if t > 0 and e == f:
                res = 'Oh no, pwned!'
                if t == 1:
                    time = 'time'
                else:
                    time = 'times'
                kol = f'This password has been seen {t} {time} before'
                return res + '\n' + kol
        else:
            return "Good news — no pwnage found!"
    else:
        return "Something went wrong! Try again"


print(check(password))