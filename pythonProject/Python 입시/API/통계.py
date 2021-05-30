




import json
import os
import sys
import urllib.request

client_id ="EHAD3_qMeYxT10CFrFSW"
client_secret = "vPIci1a8No"
url = "https://openapi.naver.com/v1/datalab/shopping/categories";
#body = "{\"startDate\":\"2017-08-01\",\"endDate\":\"2017-09-30\",\"timeUnit\":\"month\",\"category\":[{\"name\":\"패션의류\",\"param\":[\"50000000\"]},{\"name\":\"화장품/미용\",\"param\":[\"50000002\"]}],\"device\":\"pc\",\"ages\":[\"20\",\"30\"],\"gender\":\"f\"}";

body = {
    "startDate" : "2019-05-30",
    "endDate" : "2021-05-30",
    "timeUnit" : "date",
    "category" : [ {"name":"면세점","param":["50000010"]}],
    "device" : "",
    "gender" : "",
    "ages" : [ ]
}

body = json.dumps(body, ensure_ascii=False)


request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
request.add_header("Content-Type","application/json")
response = urllib.request.urlopen(request, data=body.encode("utf-8"))
rescode = response.getcode()

if(rescode==200):
    response_body = response.read()
    print()
else:
    print("Error Code:" + rescode)

검색결과 = response_body.decode('utf-8')
json결과 = json.loads(검색결과)

for i in json결과['results']:
    data = i['data']
    print(data)



