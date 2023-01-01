import requests,sys,os
from datetime import datetime
import random
mauden='\033[30m'
maudo='\033[31m'
mauluc='\033[32m'
mauvang='\033[33m'
mauxduong='\033[34m'
mauhong='\033[35m'
mauxlam='\033[36m'
mautrang='\033[37m'

maufullden='\033[40m'
maufulldo='\033[41m'
maufullxanh='\033[42m'
maufullvang='\033[43m'
maufullxduong='\033[44m'
maufullhong='\033[45m'
maufullxlam='\033[46m'
maufulltrang='\033[47m'
os.system('clear')
cookie=input(mauluc+"Nhập Cookie của bạn: ")
id_post=input(mauxduong+"Nhập id bài Viết: ")
solan=int(input(mauvang+"Nhập số lần share: "))
token=requests.get(f"https://thuongdz.name.vn/Api_tds/func_fb.php?get_token=EAAG&cookie={cookie}").text
headers = {
    'Host': 'graph.facebook.com',
    'cache-control': 'max-age=0',
    'sec-ch-ua': 'Chromium;v=107, Not=A?Brand;v=24',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': 'Android',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    # 'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'cookie': cookie
}
params = {
    'method': 'POST',
    'link': 'https://m.facebook.com/'+id_post,
    'published': '0',
    'access_token': token,
}
head_fb ={
  'Host':'mbasic.facebook.com',
  'sec-ch-ua':'"Chromium";v="107", "Not=A?Brand";v="24"',
  'sec-ch-ua-mobile':'?1',
  'sec-ch-ua-platform':'"Android"',
  'upgrade-insecure-requests':'1',
  'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5057.107 Safari/537.36',
  'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'sec-fetch-site':'same-origin',
  'sec-fetch-mode':'navigate',
  'sec-fetch-user':'?1',
  'sec-fetch-dest':'document',
  'accept-language':'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
  'cookie':cookie,
     }
a=requests.get("https://mbasic.facebook.com/profile.php",headers=head_fb).text
name=a.split("><head><title>")[1].split("</title><meta")[0]
id=a.split("Trang chủ")[1].split("Hồ sơ")[0].split("?lst=")[1].split("%")[0]
print(f"Bạn đang chạy tool trên tài khoản: {name}, id: {id}.")
dem=0
arraymau = ["\033[31m", "\033[32m", "\033[33m", "\033[34m", "\033[35m", "\033[36m", "\033[37m"]
for i in range(solan):
 share = requests.get('https://graph.facebook.com/me/feed', params=params, headers=headers).json()
 if "id" in share:
  i=i+1
  idshare=share["id"]
  # ngày giờ hiện tại
  now = datetime.now()
  t = now.strftime("%H:%M:%S")
  mau=random.choice(arraymau)
  print(f"{mau}[{i}]|[{t}]|{idshare}|Success")
 else:
  print(share)