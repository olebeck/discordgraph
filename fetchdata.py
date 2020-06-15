import requests
from datetime import datetime
url = "https://discord.com/api/invite/2ccAkg3?with_counts=true"
current = requests.get(url).json()

count = current["approximate_member_count"]
online = current["approximate_presence_count"]
time = datetime.now()

out = [count,online,url,time]
f = None
try:
    f = open("data.csv","a")
except FileNotFoundError:
    f = open("data.csv","xa")

i = 0
for item in out:
    print(item)
    if i > 0:
        f.write(",")
    f.write(str(item))
    i = i + 1
f.write("\n")
f.close()
