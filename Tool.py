# 2022-04-26

from urllib3 import PoolManager, disable_warnings
from json import loads

disable_warnings()
Http = PoolManager()
Domain = input("Enter Domain -> ").strip()
Request = Http.request("GET", "https://crt.sh?q={}&output=json".format(Domain))
Response = loads(Request.data)

List = []
for Object in Response:
  Domains = Object["name_value"].split("\n")
  for Domain in Domains:
    Domain = Domain.lower().replace("*.", "")
    if(Domain not in List and "@" not in Domain):
      with open("Result.txt", "a", encoding="utf-8") as File:
        File.write(Domain + "\n")
      print(Domain)
      List.append(Domain)
else:
  print("~ Done")
