import requests, os, sys
from datetime import time
from sys import exit
import datetime
import time
from time import sleep
from colorama import Fore
from datetime import datetime
os.system('clear')
print("\033[1;32m╔═══════════════════════════════════════════════════════════════════════════╗\r")
print("\033[0;34m                         Copyright ©Trần Đăng Khoa                           ") 
print("\033[1;32m  _______             \033[0;37m   _____                   \033[1;93m   _  ___                 ")
print("\033[1;32m |__   __|            \033[0;37m  |  __ \                  \033[1;93m  | |/ / |                ")
print("\033[1;32m    | |_ __ __ _ _ __ \033[0;37m  | |  | | __ _ _ __   __ _\033[1;93m  | ' /| |__   ___   __ _ ")
print("\033[1;32m    | | '__/ _` | '_ \ \033[0;37m | |  | |/ _` | '_ \ / _` |\033[1;93m |  < | '_ \ / _ \ / _` |")
print("\033[1;32m    | | | | (_| | | | |\033[0;37m | |__| | (_| | | | | (_| |\033[1;93m | . \| | | | (_) | (_| |")
print("\033[1;32m    |_|_|  \__,_|_| |_|\033[0;37m |_____/ \__,_|_| |_|\__, |\033[1;93m |_|\_\_| |_|\___/ \__,_|")
print("\033[1;32m                       \033[0;37m                      __/ |\033[1;93m                         ")
print("\033[1;32m                       \033[0;37m                     |___/ \033[1;93m                         ")
print    ( "\033[1;32m╚════════════════════════════════════════════════════════════════════════════╝")
cookie=input("Nhập Cookie Facebook: ")
diachi=input("Nhập Tỉnh Cần Add(Nhập Đúng Viết Hoa, Viết Thường): ")
delay=int(input("Nhập Delay(>30s): "))

if delay<=29:
 print("Vui Lòng Nhập Delay Ít Trên 30 Để Tránh Block Tính Năng")
else:
 os.system('clear')
 head_fb ={
  'Host':'mbasic.facebook.com',
  'upgrade-insecure-requests':'1',
  'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5057.107 Safari/537.36',
  'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'sec-fetch-site':'cross-site',
  'sec-fetch-mode':'navigate',
  'sec-fetch-user':'?1',
  'sec-fetch-dest':'document',
  'cookie':cookie,
     }
 print("\033[1;32m╔═══════════════════════════════════════════════════════════════════════════╗\r")
 print("\033[0;34m                         Copyright ©Trần Đăng Khoa                           ") 
 print("\033[1;32m  _______             \033[0;37m   _____                   \033[1;93m   _  ___                 ")
 print("\033[1;32m |__   __|            \033[0;37m  |  __ \                  \033[1;93m  | |/ / |                ")
 print("\033[1;32m    | |_ __ __ _ _ __ \033[0;37m  | |  | | __ _ _ __   __ _\033[1;93m  | ' /| |__   ___   __ _ ")
 print("\033[1;32m    | | '__/ _` | '_ \ \033[0;37m | |  | |/ _` | '_ \ / _` |\033[1;93m |  < | '_ \ / _ \ / _` |")
 print("\033[1;32m    | | | | (_| | | | |\033[0;37m | |__| | (_| | | | | (_| |\033[1;93m | . \| | | | (_) | (_| |")
 print("\033[1;32m    |_|_|  \__,_|_| |_|\033[0;37m |_____/ \__,_|_| |_|\__, |\033[1;93m |_|\_\_| |_|\___/ \__,_|")
 print("\033[1;32m                       \033[0;37m                      __/ |\033[1;93m                         ")
 print("\033[1;32m                       \033[0;37m                     |___/ \033[1;93m                         ")
 print    ( "\033[1;32m╚════════════════════════════════════════════════════════════════════════════╝")
 home=requests.get('https://mbasic.facebook.com',headers=head_fb).text
 checkck=home.find('Đăng nhập hoặc đăng ký')
 if checkck==-1:
  fb=requests.get('https://mbasic.facebook.com/profile.php',headers=head_fb).text.split("Chỉnh sửa trang cá nhân")[0]
  id_fb=fb.split("lst=")[1].split("%")[0]
  ten_fb=fb.split('title>')[1].split('<')[0]
  print(Fore.GREEN+f"Bạn Đang Thêm Bạn Bè Vào Tài Khoản:{Fore.BLUE}{ten_fb}{Fore.GREEN} & Id Là:{Fore.BLUE}{id_fb}")
  while(True):
   now = datetime.now()
   thoigian = now.strftime("%H:%M:%S")
   check=requests.get("https://mbasic.facebook.com/friends/center/mbasic/?fb_ref=tn&sr=1&ref_component=mbasic_home_header&ref_page=MChatBuddyListController",headers=head_fb).text.split('Những người bạn có thể biết')[1]
   c=check.split('friends/hovercard/mbasic/?uid=')[1].split('&')[0]
   
   profile=requests.get(f"https://mbasic.facebook.com/profile.php?id={c}&_rdr",headers=head_fb).text
   xem=requests.get("https://mbasic.facebook.com/friends/center/mbasic/?fb_ref=tn&sr=1&ref_component=mbasic_home_header&ref_page=MChatBuddyListController",headers=head_fb).text.split('Những người bạn có thể biết')[1]
   x=xem.split('/friends/hovercard/mbasic/?')[1].split('</a><div')[0]
   id=x.split('uid=')[1].split('&')[0]
   ten=x.split('>')[1]
   spam=profile.find('Để bảo vệ cộng đồng khỏi spam, chúng tôi giới hạn tần suất bạn đăng bài, bình luận hoặc làm các việc khác trong khoảng thời gian nhất định. Bạn có thể thử lại sau.')
   if spam > -1:
    print(Fore.RED+'Để bảo vệ cộng đồng khỏi spam, chúng tôi giới hạn tần suất bạn đăng bài, bình luận hoặc làm các việc khác trong khoảng thời gian nhất định. Bạn có thể thử lại sau.')
    break
   else:
    now = datetime.now()
    thoigian = now.strftime("%H:%M:%S")
    find=profile.find(diachi)
    if find== -1:
     print(f"{Fore.GREEN}[{Fore.RED}{thoigian}{Fore.GREEN}] {Fore.YELLOW}{ten}{Fore.GREEN} Không Ở {diachi}                    ")
     xoa=requests.get("https://mbasic.facebook.com/friends/center/mbasic/?fb_ref=tn&sr=1&ref_component=mbasic_home_header&ref_page=MChatBuddyListController",headers=head_fb).text.split('Những người bạn có thể biết')[1].split('/friends/pymk/xout/sync/?')[1].split('"')[0].replace('amp;','')
     requests.get(f"https://mbasic.facebook.com/friends/pymk/xout/sync/?{xoa}",headers=head_fb)
     for i in range(1,-1,-1):
       print('Vui Lòng Chờ '+str(i)+' Giây ',end=('\r'))
       time.sleep(1)
    else:
     print(f"{Fore.GREEN}[{Fore.RED}{thoigian}{Fore.GREEN}] {Fore.YELLOW}{ten}{Fore.GREEN} Ở {diachi}                           ")
     proadd=f"https://mbasic.facebook.com/profile.php?id={id}"
   #  proadd=requests.get(f"{k}",headers=head_fb).url
     a=proadd.find("login")
     if a == -1:
      time.sleep(1)
      add=requests.get(f"{proadd}",headers=head_fb).text.split('/a/friends/profile/add/?')[1].split('"')[0].replace('amp;','')
      time.sleep(1)
      requests.get(f"https://mbasic.facebook.com/a/friends/profile/add/?{add}",headers=head_fb)
      print(f"{Fore.GREEN}[{Fore.RED}{thoigian}{Fore.GREEN}]{Fore.BLUE} Thành Công Đã Thêm {Fore.YELLOW}{ten}{Fore.BLUE} Id {Fore.YELLOW}{id}")
      for i in range(delay,-1,-1):
        print('Vui Lòng Chờ '+str(i)+' Giây ',end=('\r'))
        time.sleep(1)
     else:
      
      time.sleep(1)
      add=requests.get(f"{proadd}",headers=head_fb).text.split('/a/friends/profile/add/?')[1].split('"')[0].replace('amp;','')
      time.sleep(1)
      requests.get(f"https://mbasic.facebook.com/a/friends/profile/add/?{add}",headers=head_fb)
      print(f"{Fore.GREEN}[{Fore.RED}{thoigian}{Fore.GREEN}]{Fore.BLUE} Thành Công Đã Thêm {Fore.YELLOW}{ten}{Fore.BLUE} Id {Fore.YELLOW}{id}")
      for i in range(delay,-1,-1):
        print('Vui Lòng Chờ '+str(i)+' Giây ',end=('\r'))
        time.sleep(1)
 else:
  print(Fore.RED+"Cookie Die !")
  
