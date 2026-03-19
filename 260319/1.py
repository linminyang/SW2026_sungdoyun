#오전 오후 판단

import datetime

now = datetime.datetime.now()

if now.hour < 12 :
   print("현재시간은 {h}시로 오전입니다.".format(h = now.hour))
else :
   print("현재시간은 {h}시로 오전입니다.".format(h = now.hour))