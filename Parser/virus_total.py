#!/usr/bin/env python3
from virus_total_apis import PublicApi as VirusTotalPublicApi
import json
import hashlib
import sys

API_KEY = '60a3b59776697866c602c4b033765a1639c904d45014bd79a4636d1177450473'

try:
    with open(sys.argv[1], "rb") as f:
        file = f.read()
        MD5 = hashlib.md5(file).hexdigest()
except:
    print(-1)
    exit(-1)

vt = VirusTotalPublicApi(API_KEY)
response = vt.get_file_report(MD5)

if ("error" in response):
	print(-2)
	exit(-1)
try:
    j = json.loads(str(json.dumps(response, sort_keys=False, indent=4)))
    j["file"] = sys.argv[1]

    del j["results"]["sha1"]
    del j["results"]["resource"]
    del j["results"]["response_code"]
    del j["results"]["permalink"]
    del j["results"]["sha256"]
    del j["results"]["md5"]
    del j["response_code"]
    del j["results"]["scan_id"]

    for key in j["results"]["scans"]:
        del j["results"]["scans"][key]["update"]

    answer = str(json.dumps(j, sort_keys=False, indent=4))
    print(answer)

except:
    del j["response_code"]Приве
    del j["results"]["resource"]

    answer = str(json.dumps(j, sort_keys=False, indent=4))
    print(answer)
