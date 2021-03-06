#! python3

import sys
import glob
import serial
from serial import SerialException
import numpy as np
import matplotlib.pyplot as plt
from time import time

def serial_port():
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
	
port_list=serial_port()
port=port_list[0]
port=''.join(port)
ser=serial.Serial(port, 38400)


# class that holds analog data for N samples
class AnalogData:
  # constr
  def __init__(self, maxLen):
    self.ax = deque([0.0]*maxLen)
    self.ay = deque([0.0]*maxLen)
    self.maxLen = maxLen

  # ring buffer
  def addToBuf(self, buf, val):
    if len(buf) < self.maxLen:
      buf.append(val)
    else:
      buf.pop()
      buf.appendleft(val)

  # add data
  def add(self, data):
    assert(len(data) == 2)
    self.addToBuf(self.ax, data[0])
    self.addToBuf(self.ay, data[1])
    

# plot class
class AnalogPlot:
  # constr
  def __init__(self, analogData):
    # set plot to animated
    plt.ion() 
    self.axline, = plt.plot(analogData.ax)
    self.ayline, = plt.plot(analogData.ay)
    plt.ylim([0, 1023])

  # update plot
  def update(self, analogData):
    self.axline.set_ydata(analogData.ax)
    self.ayline.set_ydata(analogData.ay)
    plt.draw()


# main() function
def main():
  # expects 1 arg - serial port string
  if(len(sys.argv) != 2):
    print 'Example usage: python showdata.py "/dev/tty.usbmodem411"'
    exit(1)

 #strPort = '/dev/tty.usbserial-A7006Yqh'
  strPort = sys.argv[1];

  # plot parameters
  analogData = AnalogData(100)
  analogPlot = AnalogPlot(analogData)

  print 'plotting data...'

  # open serial port
  ser = serial.Serial(strPort, 9600)
  while True:
    try:
      line = ser.readline()
      data = [float(val) for val in line.split()]
      #print data
      if(len(data) == 2):
        analogData.add(data)
        analogPlot.update(analogData)
    except KeyboardInterrupt:
      print 'q'
      break
  # close serial
  ser.flush()
  ser.close()

# call main
if __name__ == '__main__':
  main()











