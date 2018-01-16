import cv2
import os,sys,time,datetime,glob2,glob
import pandas as pd

folderpath=os.getcwd()+'\\OpenCVPracice\\videos'
folderpath=r'C:\Users\PythonExercise\_PythonFundamentals\11282017_Udemy10PythonProject\app6-WebcamDetector\OpenCVPractice\videos'
os.chdir(folderpath)

first_frame=None
status_list=[None, None]
time_list=[]
df=pd.DataFrame(columns=['start', 'end'])
# video=cv2.VideoCapture(0) using webcam
video=cv2.VideoCapture(glob2.glob('*.mp4')[0])

#a=0
while True:
	#a=a+1
	check, frame=video.read()
	status=0
	#print('check: \n', check, '\nframe: \n', frame)
	frame=cv2.resize(frame, (300, 300))
	gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	#time.sleep(1)
	gray=cv2.GaussianBlur(gray, (21,21),0)

	if first_frame is None:
		first_frame=gray
		continue #start the next loop without executing the rest code

	delta_frame=cv2.absdiff(first_frame, gray)
	thresh_delta=cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
	thresh_frame=cv2.dilate(thresh_delta, None, iterations=2)

	'''python 2 uses (cnts, _)'''
	(_, cnts, _)=cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE
		)

	for contour in cnts:
		if cv2.contourArea(contour) < 10000:
			#print('area less than 1000')
			continue
		status=1
		(x,y,w,h)=cv2.boundingRect(contour)
		cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 3)

	status_list.append(status)

	try:
		status_list=status_list[-2:] #make the script more memory efficient
		if status_list[-1]!=status_list[-2]:
			time_list.append(datetime.datetime.now())
	except:
		pass

	cv2.imshow('Gray Frame', gray)
	cv2.imshow('Delta Frame', delta_frame)
	cv2.imshow('Thresh Frame', thresh_frame)
	cv2.imshow('Frame', frame)

	key=cv2.waitKey(10)
	#print(gray, '\n' ,delta_frame)

	if key==ord('q'):
		if status==1: time_list.append(datetime.datetime.now())
		break

print(status_list, '\n', time_list)	

for i in range(0, len(time_list)-1, 2):
	print(i)
	df=df.append({'start': time_list[i], 'end': time_list[i+1]}, 
		ignore_index=True)

#video.release() using webcam
#print('total frames: ', a)
cv2.destroyAllWindows()

df.to_csv(folderpath+'/TimeRecord.csv')
# df=pd.read_csv('TimeRecord.csv', parse_dates=True)
# df.plot()

