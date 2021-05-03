import requests
from googlesearch import search

def get_url(name):
    for j in search(name, tld="co.in", num=1):
        res = j
        break
    return res

print(get_url("باما 206"))