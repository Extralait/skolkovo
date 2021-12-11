#!/usr/bin/env python3
from hyper.contrib import HTTP20Adapter
import requests
import json
import sys

try:
    s = requests.Session()

    url = f'https://talosintelligence.com/sb_api/query_lookup?query=/api/v2/details/ip/&query_entry={sys.argv[1]}&offset=0&order=ip asc'

    s.mount('https://http2bin.org', HTTP20Adapter())

    headers = {"Accept": "application/json, text/javascript, */*; q=0.01",
               "Accept-Encoding": "gzip, deflate, br",
               "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0",
               "Referer": "https://talosintelligence.com/reputation_center/lookup?search=69.167.146.13"}

    r = s.get(url, headers=headers, timeout=10)
    j = json.loads(r.text)


    del j["display_ipv6_volume"]
    del j["daily_mag"]
    del j["monthly_mag"]
    del j["email_score"]
    del j["daily_spam_level"]
    del j["web_score"]
    del j["category"]
    del j["monthly_spam_level"]
    del j["block_lists"]

    data = json.dumps(j, sort_keys=False, indent=4)

    print(data)

except:
    print(-1)
    exit(-1)
