r'''
Build a Website Using Python and Flask
https://www.udemy.com/the-python-mega-course/learn/v4/t/lecture/4775310?start=0
'''

# import matplotlib.pyplot as plt
# import numpy as np
# import pandas as pd
# import matplotlib,urllib, pylab,csv, re,sys,os, math, glob,glob2, time,datetime,json,distance, collections,memory_profiler
# from itertools import islice
# from difflib import SequenceMatcher,get_close_matches
# import folium
# from datetime import datetime as dt
from flask import Flask, redirect, render_template, request, session, url_for

app=Flask(__name__)

@app.route('/')
def home():
	#return 'website content goes here!'
	return render_template('home.html')

@app.route('/about/')
def about():
	return render_template('about.html')

if __name__ == '__main__':
	#main()
	app.run(debug=True)