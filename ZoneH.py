#!/usr/bin/python2

# Creator :  ./FUKUR0-3XP
# Team : Black Coders Satanic Exploiter Team ( BCA - X666X )
# Thanks To All Member Python Tutorial
# Recode Tidak Akan Membuat Anda Menjadi Pencipta Kode :3

# - - - Panduan - - -

# Buat File Dengan Extensi .txt Dan Masukkan Kumpulan Site Yang Sudah Kalian Deface Ke File Tersebut Lalu Simpan ( Simpan File Ini Dengan Syarat : Harus 1 Direktori Bersamaan Dengan File ZoneH.py ), Kalo Ga Mau Ribet Isi Aja Kumpulan Sitenya Di Mirror.txt Yang Udah Disediain Caranya $ nano Mirror.txt, Tinggal Isi Sama Site Yang Mau Di Mirror

# - - - - - - - - - - - -

from requests.exceptions import ConnectionError
from time import sleep
import requests
import random
import sys
import os

M = '\033[1;31m'
H = '\033[1;32m'
K = '\033[1;33m'
U = '\033[1;34m'
P = '\033[1;35m'
C = '\033[1;36m'
W = '\033[1;37m'
A = '\033[90m'

def banner():
	print(''+C+'''
  __  __                 _____                      _   _ 
 |  \/  | __ _ ___ ___  |__  /___  _ __   ___      | | | |
 | |\/| |/ _` / __/ __|   / // _ \| '_ \ / _ \_____| |_| |
 | |  | | (_| \__ \__ \  / /| (_) | | | |  __/_____|  _  |
 |_|  |_|\__,_|___/___/ /____\___/|_| |_|\___|     |_| |_|
                   '''+W+'Creator : ./Fukur0\n\t\t   YT : Jejak Cyber')
                   
def main():
	try:
		success = []
		error = []
		os.system('clear')
		print(C+'Subscribe YT'+W+' Gua Dlu Su !'+C+' :V')
		sleep(1.5)
		os.system('xdg-open https://www.youtube.com/channel/UCzsADl8XRJeZXJ6CKZLX5KQ')
		os.system('clear')
		banner()
		print
		print
		site = raw_input(''+C+'FILE SITE'+W+' ('+H+' Ex :'+C+' Mirror.txt '+W+') : ')
		nickname = raw_input(''+C+'NAMA DEFACER'+W+' ('+H+' Ex :'+C+' BCA-X666X '+W+') : ')
		print
		print(''+C+'-------------- '+W+'Starting'+C+' --------------')
		print
		f = open(site)
		u = f.readlines()
		
		for i in u:
			try:
				k = i.strip()
				agent = requests.get('https://pastebin.com/raw/zkCXTGcm').text.split('\n')
				acak = random.choice(agent)
				
				headers = {
				'Content-Length' : '69',
				'Cache-Control' : 'max-age=0',
				'Origin' : 'http://zone-h.org',
				'Upgrade-Insecure-Requests' : '1',
				'Content-Type' : 'application/x-www-form-urlencoded',
				'User-Agent' : '{acak}',
				'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
				'Accept-Encoding' : 'gzip, deflate',
				'Referer' : 'http://zone-h.org/notify/single?hz=1',
				}
				
				data = {
				'defacer' : nickname,
				'domain1' : k,
				'hackmode' : '5',
				'reason' : '4',
				}
				send = requests.post('http://zone-h.org/notify/single', headers = headers, data = data)
				if 'ERROR:' in send.text:
					print('' + W + str(k.replace('\n','') + C + ' : ' + A + ' Error !'))
					error.append(k)
				
				else:
					print('' + W + str(k.replace('\n','') + C + ' : ' + H + ' Success \xe2\x9c\x93\x1b'))
					success.append(k)
					
			except ConnectionError:
					print(M+'Cek Koneksi !')
					print
					break
					
	except IOError:
		print(M+'File Site Tidak Ditemukan !')
		print
		sys.exit()
		
	print
	r = (len(success))
	s = (len(error))
	t = success
	v = error
	print(''+C+'----------- '+W+'Selesai & Hasil'+C+' -----------')
	print
	print(W+'Total Berhasil'+C+' : '+W+ str(r))
	print
	print('\n'.join(t))
	print
	print(W+'Total Gagal'+C+' : '+W+ str(s))
	print
	print('\n'.join(v))
	print
	print(C+40*'-')
	print
	print(C+'>>>'+W+' Silahkan Cek Zone-H Kamu'+C+' ( '+W+nickname+C+' )'+W+' *_*'+C+' <<<')
	print

if __name__ == '__main__':
	main()
