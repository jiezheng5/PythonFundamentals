r'''
Build a Web Map
https://www.udemy.com/the-python-mega-course/learn/v4/t/lecture/7221320?start=0
'''

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib,urllib, pylab,csv, re,sys,os, math, glob,glob2, time,datetime,json,distance, collections
from itertools import islice
from difflib import SequenceMatcher,get_close_matches
import folium

def volcano_df():
	data=pd.read_csv('http://pythonhow.com/data/Volcanoes_USA.txt',sep=',')
	print(data.head())
	lat=list(data['LAT'])
	lon=list(data['LON'])
	marker_list=[[x,y] for x, y in zip(lat,lon)]
	return marker_list

def color_elev(elev):
	if elev<=1000: return 'green'
	elif elev<=3000: return 'blue'
	else: return 'red' 

def map_builder(marker_list=[]):
	location=[33.9,-117.86]
	map=folium.Map(location=location, zoom_start=6, tiles='Mapbox Bright')

	###READ in volacano data
	data=pd.read_csv('http://pythonhow.com/data/Volcanoes_USA.txt',sep=',')
	print(data.head())
	lat=list(data['LAT'])
	lon=list(data['LON'])
	elev=list(data['ELEV'])
	#map.add_child(folium.Marker(location=[32,-117],popup='Hi, I am a Marker', icon=folium.Icon(color='green')))
	fgv=folium.FeatureGroup(name='My Map_volocanoes')
	#marker_list=[[location[0]-i,location[1]+i] for i in np.linspace(0.1,0.3,3)]
	for la,lo,le in zip(lat,lon,elev):
		#print(coordinates)
		fgv.add_child(folium.CircleMarker(location=[la,lo],popup=str(le)+' m', icon=folium.Icon(), color=color_elev(le),fill=True, fill_color=color_elev(le)))
	

	###READ in population data
	filename=glob2.glob('C:\\Users\PythonExercise\\_PythonFundamentals\\11282017_Udemy10PythonProject\\app2-web-map'+'\\*.json')[0]
	print(filename)
	#data_js=pd.read_json(filename,enconding='utf-8', dtype=object)
	data=open(filename,'r',encoding='utf-8-sig').read()
	#for line in data:
	#	print(data.encode("utf8").decode("cp950", "ignore"))
	fgp=folium.FeatureGroup(name='My Map_Population')
	fgp.add_child(folium.GeoJson(data=data, style_function=lambda x: 
		{'fillColor': 'yellow' if x['properties']['POP2005']<1000000 
		else 'orange' if x['properties']['POP2005']<2000000
		else 'red'}))	
	#map.add_child(folium.LayerControl()) # won't work before add the feature group
	
	map.add_child(fgv)
	map.add_child(fgp)
	map.add_child(folium.LayerControl())
	map.save('Map1.html')

def main():
	#volcano_df()
	map_builder()

if __name__ == '__main__':
	main()
