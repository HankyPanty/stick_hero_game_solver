import subprocess
import matplotlib.image as img
import urllib
import time

subprocess.call(['adb','devices']);

while True:
	subprocess.call(['adb','shell','screencap','/sdcard/trial.png']);
	subprocess.call(['adb','pull','/sdcard/trial.png']);

	jpgdata=img.imread('trial.png');

	if jpgdata[1650,510,1]==0.5764706 and jpgdata[1650,510,1]==0.79607844 and jpgdata[1650,510,1]==0.39607844:
		subprocess.call(['adb','shell','input','tap','1650','520']);
		time.sleep(2);
		continue;
	elif ():
		subprocess.call(['adb','shell','input','keyevent','4']);
		time.sleep(2);
		continue;

	x=1712;y=200;start=0;mid=0;
	while True:
	    p1=jpgdata[x,y,0];
	    p2=jpgdata[x,y,1];
	    p3=jpgdata[x,y,2];
	    if (p1==0 and p2==0 and p3==0):
	        if start==0:
	            start=y;
	        y+=2;
	    elif start>0:
	        mid=y;
	        break;
	    else:
	        y+=2;
	    if y>1000:
	        mid=1000;
	        break;

	tt=(mid-152)*1.8;
	t=int(tt);
	xyz=['adb','shell','input','swipe','500','500','500','500',str(t)];
	subprocess.call(xyz);

	time.sleep(4);
	
