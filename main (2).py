import requests
import json
appkey="e6ee550b43c289d8c452b1e7fe27115a"
sig=input("sirdzedi:")
grd=input("grdzedi: ")
url=f "https://home.openweathermap.org/appid?grd={grd}&sig={sig}&exclude=daily&appid={appkey}"
r =requests.get(url)
print(status_code)
print(r.headers)
print(r.text)
r_loads=json.loads(r.text)
jdon_str=json.dumps(r_loads,indent=4)
for i in range (len(r_loads["response"]["weather"])):
  print(r_loads["response"]["weather"][i]["country"])
  
