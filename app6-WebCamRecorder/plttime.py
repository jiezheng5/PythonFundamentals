import cv2
import os,sys,time,datetime,glob2,glob,pylab, csv, re, sys, os, glob, time, datetime, random
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np 
import pandas as pd
import pylab, csv, re, sys, os, glob, time, datetime, random
from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool, ColumnDataSource
#from motion_detector import df

folderpath=r'C:\Users\PythonExercise\_PythonFundamentals\11282017_Udemy10PythonProject\app6-WebcamDetector'
filepath=glob2.glob(folderpath + '/*.csv')[0]

dtypes=[float, datetime, datetime]
df1=pd.read_csv(filepath, index_col=0,parse_dates=True)
df1['Start_time']=df1['Start'].apply(lambda x: pd.to_datetime(x, format='%Y-%m-%d %H:%M:%S', errors='coerce',infer_datetime_format=True))
df1['End_time']=df1['End'].apply(lambda x: pd.to_datetime(x, format='%Y-%m-%d %H:%M:%S', errors='coerce'))
df1['Start_str']=df1['Start_time'].dt.strftime('%H:%M:%S')
df1['End_str']=df1['End_time'].dt.strftime('%H:%M:%S')

print(df1.dtypes, '\n', df1.head())

#df1['Start_time'].plot(kind='bar')
#plt.plot_date(x=df1['Start_time'],y=df1['End_time'])
#df1['Start_time']=df1['Start'].apply(lambda x: datetime.datetime.strptime(x, '%Y-%m-%d %H:%M:%S'))

cds=ColumnDataSource(df1)

p=figure(x_axis_type='datetime', height=100, width=500, responsive=True, 
	title='Motion Graph')
p.yaxis.minor_tick_line_color=None
p.ygrid[0].ticker.desired_num_ticks=1

hover=HoverTool(tooltips=[('Start', '@Start_str'), ('End','@End_str')])
p.add_tools(hover)

q=p.quad(left=df1['Start_time'],right=df1['End_time'],bottom=0,top=1, color='green', source=cds)
output_file('record.html')
show(p)