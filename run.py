

import os,sys,time
#warna
un,bl,a,h,b,p,bn,o = [
'\033[4m',
'\033[1m',
'\033[90m',
'\033[32m',
'\033[94m',
'\033[97m',
'\033[104m',
'\033[0m',
]

try:
	import pyshorteners
except ModuleNotFoundError:
	print(f'\n- Installing pyshorteners\n')
	os.system('pip3 install pyshorteners')
except ImportError:
	print(f'\n- Installing pyshorteners\n')
	os.system('pip3 install pyshorteners')

import pyshorteners
banner = f'''\n
{p} ────────────────────────────────────
 {bn}      Shortlink Tinyurl Ugex95      {o}
{p} ────────────────────────────────────
'''
def cls():
	os.system('clear')
def wrt(t,tm):
	for i in t + '\n':
		sys.stdout.write(i)
		sys.stdout.flush()
		time.sleep(tm)

cls()
wrt(banner,0.005)
link = input(f' {b}- {p}Link {b}:{h} ')
resp = pyshorteners.Shortener().tinyurl.short(link)
#
add = open('tinyurl.txt','a')
add.write('\n'+resp)
add.close()
#
wrt(f'''{p} ────────────────────────────────────
  {b}- {p}Url {b}: {h}{un}{resp}{o}
  {b}- {p}Long Url {b}: {p}{bl}{link}{o}
  {b}~ {p}Url File {b}: {a}./tinyurl.txt
 {p}────────────────────────────────────\n\n''',0.001)





