import requests, os, sys
from time import sleep
os.system('clear')
while (True):
 linkfb=input("Nhập Link Facebook hoặc Bài Viết: ")
 head={
  'Host':'id.traodoisub.com',
  'content-length':'54',
  'sec-ch-ua':'"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
  'accept':'application/json, text/javascript, */*; q=0.01',
  'content-type':'application/x-www-form-urlencoded; charset=UTF-8',
  'x-requested-with':'XMLHttpRequest',
  'sec-ch-ua-mobile':'?1',
  'user-agent':'Mozilla/5.0 (Linux; Android 11; vivo 1906) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36',
  'sec-ch-ua-platform':'"Android"',
  'origin':'https://id.traodoisub.com',
  'sec-fetch-site':'same-origin',
  'sec-fetch-mode':'cors',
  'sec-fetch-dest':'empty',
  'referer':'https://id.traodoisub.com/',
  'cookie':'cf_clearance=z1jER0ZpxOgJR09akK8mhmHGWP1dg8.AV8p7xOxQOsc-1661855178-0-150'
 }
 data=(f"link={linkfb}")
 get=requests.post("https://id.traodoisub.com/api.php",headers=head,data=data).text
 a=get.find("error")
 sleep(2)
 check=requests.post("https://id.traodoisub.com/api.php",headers=head,data=data)
 if a>=0:
  checkerror=check.json()['error']
  print("error:",checkerror)
  break
 else:
  sleep(2)
  id=check.json()['id']
  print("Id của Bạn Là:",id)
