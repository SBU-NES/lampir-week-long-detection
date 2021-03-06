#! python3

import sys
import glob
import serial
from serial import SerialException
import numpy as np
from matplotlib import pyplot as plt
from time import time
from datetime import datetime

def serial_port():	#get avalable ports
	'''list port names'''

	if sys.platform.startswith('win'):
		ports=['COM%s' % (i+1)for i in range (256)]
	elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
		ports=glob.glob('/dev/tty[A-Za-z]*')
	elif sys.platform.startswith('darwin'):
		ports=glob.glob('/dev/tty.*')
	else:
		raise EnvironmentError('Unsupported platform')
		
	result=[]
	for port in ports:
		try:
			s=serial.Serial(port)
			s.close()
			result.append(port)
		except(OSError, serial.SerialException):
			pass
	return result
	
def getfilename():	#get filename every minute
	
	
port_list=serial_port()
port=port_list[0]
port=''.join(port)
ser=serial.Serial(port, 38400)

voltage=[]


ser.flushInput()
filename=datetime.now().strftime("%Y-%m-%d %H-%M-%S")
outfile='/home/libowu/datalog/lampirdata/'+filename+'.csv'

run=True
while run:
	filename=datetime.now().strftime("%Y-%m-%d %H-%M-%S")
	outfile='/home/libowu/datalog/lampirdata/'+filename+'.csv'
	f=open(outfile,'a')
	while True:
		try: 
			data=ser.readline()
			f.write(str(data))
			f.write(str(datetime.now()))
			f.write('\n')
			#f.flush()
		except (KeyboardInterrupt, SystemExit):
			run=False
			raise
	
		

f=open(outfile, 'a')
'''
try:
	while run:
		data=ser.readline()
		f.write(str(data))
		f.write(str(datetime.now()))
		f.write('\n')
except (KeyboardInterrupt, SystemExit):
	run=False
	raise
'''	
while run:
	try:
		
		data=ser.readline()
		f.write(str(data))
		f.write(str(datetime.now()))
		f.write('\n')
		#f.flush()
	except (KeyboardInterrupt, SystemExit):
		run=False
		raise
f.close()
	
# close serial
ser.flush()
ser.close()
		



