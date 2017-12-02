r'''
Interative Dictionary: user input a word, the program automatically searches the dictionary (data.json)
if found: print the explaination
else: found the closest words in the dictionary and let user chose
'''

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib,urllib, pylab,csv, re,sys,os, math, glob,glob2, time,datetime,json,distance, collections
from itertools import islice
from difflib import SequenceMatcher,get_close_matches

def translate_sol_while(word='',dict1={},continu_flag='Y'):
	data=readinfile()
	#print(take(2,data)) ###check the data strucutre
	choice_ask='Please enter Y for yes, N for no. '
	continu_ask='Do you want to continue? ' 
	while continu_flag.upper()=='Y':
		cword=input('Enter word: ',)
		print(translateword_sol(word=cword,dict1=data))#.encode("utf8").decode("cp950", "ignore"))
		continu_flag=input('{0} {1}'.format(continu_ask,choice_ask))
		while continu_flag.upper() not in ['Y','N']:
			continu_flag=input("We didn't understand your entry. {}".format(choice_ask)) 
	print('Have a wonderful day, bye!')

def translateword_sol(word='',dict1={}):
	word=word.lower()
	choice_ask='Please enter Y for yes, N for no. '
	noword='No such word. Please double check.'
	#result=collections.namedtuple('result','explain, word_choice, continue_choice')
	if word in dict1:
		return '\n'.join(dict1.get(word)) 
	elif get_close_matches(word,dict1.keys(),3,0.6):
		word_suggestion=get_close_matches(word,dict1.keys(),3,0.6)[0]
		word_choice=input('Did you mean {0:s}? {1:s}'.format(word_suggestion, choice_ask))
		while word_choice.upper() not in ['Y','N']:
			word_choice=input("We didn't understand your entry. {}".format(choice_ask)) 
		if word_choice.upper()=='Y': return  '\n'.join(dict1.get(word_suggestion))
		else: return noword 
	else:
		return noword 

def take(n, iterable):
	'''Return first n items of the iterable as a list'''
	return list(islice(iterable.items(), n))

def readinfile():
	'''open().read() a single string while open() a list'''
	data=json.load(open(os.getcwd()+'/data.json'))
	data2={k.lower():data[k] for k in data}
	return data2

def main():
	translate_sol_while()

if __name__ == '__main__':
	main()
