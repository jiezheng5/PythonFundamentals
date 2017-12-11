r'''
Build a Website Blocker which prevents visiting of certain websites during certain time.
windows: C:\Windows\System32\drivers\etc\hosts
windows: save as .pyw, then schedule in Task scheduler with highest prioirty
Mac/Linux: /etc/hosts
Mac/Linus: $> sudo crontab -e, add 1 line '@reboot python ./WebsiteBlocker_App_12052017_3.py'
https://www.udemy.com/the-python-mega-course/learn/v4/t/lecture/5163364?start=0
'''

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib,urllib, pylab,csv, re,sys,os, math, glob,glob2, time,datetime,json,distance, collections,memory_profiler
from itertools import islice
from difflib import SequenceMatcher,get_close_matches
import folium
from datetime import datetime as dt

def website_list():
	redirect='127.0.0.1'
	websites=['facebook.com','mitbbs.com','cnn.com']
	str_list1=['{0}    {1}\n{0}    www.{1}\n'.format(redirect,website) for website in websites]
	str_list="\n'''\n" + '\n'.join(str_list1) + "\n'''\n"
	#print(str_list)
	return str_list

def website_blocker2(str_list=''):
	websites=['facebook.com','mitbbs.com','cnn.com']
	filename=r'C:\Windows\System32\drivers\etc\hosts'
	#filename=r'C:\Users\jie zheng\Documents\hosts2.txt'

	with open(filename, 'r+') as f:
		origin_str_list=[line for line in f.readlines() if not any(website in line for website in websites)]
		origin_str=''.join(origin_str_list)
		#print(origin_str)
		f.seek(0)
		if dt.now().replace(hour=8) < dt.now() < dt.now().replace(hour=17):
			f.write(origin_str+str_list)
		else: f.write(origin_str)

	while True:
		if dt.now().replace(hour=17)<=dt.now()<dt.now().replace(hour=17)+datetime.timedelta(seconds=5):
			with open(filename, 'r+') as f:
				f.write(origin_str)
			print('fun hours starts')	 
		elif dt.now().replace(hour=8)<=dt.now()<dt.now().replace(hour=8)+datetime.timedelta(seconds=5):
			with open(filename, 'r+') as f:
				f.write(origin_str+str_list)
			print('working hours starts')	 
		elif dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() \
		     < dt(dt.now().year, dt.now().month, dt.now().day, 17):
			print('working hours')
		else:
			print('fun hours')
		time.sleep(5) #more efficient, only check the time every 5 seconds

def website_blocker_sol():
	redirect='127.0.0.1'
	websites=['facebook.com','mitbbs.com','cnn.com']
	filename=r'C:\Windows\System32\drivers\etc\hosts'
	#filename=r'C:\Users\jie zheng\Documents\hosts2.txt'

	while True:
		if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() \
		   < dt(dt.now().year, dt.now().month, dt.now().day, 17):
			print('working hours')
			with open(filename, 'r+') as f_r:
				content=f_r.read()
				for website in websites:
					if not website in content:
						f_r.write(redirect+'    '+website+'\n')
		else:
			with open(filename, 'r+') as f_r:
				content=f_r.readlines()
				'''place file pointer in the beginning of file'''
				f_r.seek(0)
				for line in content:
					if not any(website in line for website in websites):
						f_r.write(line)
				f_r.truncate()
			print('fun hours')
		time.sleep(5) #more efficient, only check the time every 5 seconds

def main():
	website_blocker2(website_list())
	website_blocker_sol()

if __name__ == '__main__':
	main()
