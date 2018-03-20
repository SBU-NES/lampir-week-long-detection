# README #

### This project consists several parts: ###
 * LAMPIR driven code, based on arduino
 * Raspberry Pi code for PiCam, data storage
 * Human detection of photos/videos and analog data analyzing


### How do I get set up? ###
1. LAMPIR is as a slave of Raspi. it runs arduino continuously. 
2. Raspi runs python code, with multithread to collect data (plot) and storage photos. See [python multithreading](https://www.tutorialspoint.com/python/python_multithreading.htm).
3. Filename ID is based on the time.
4. Picamera takes record video continously, the video files are seperated by 1 min.
5. (2/21/18) The current running code is `./videolog/videolog.py`.
   
### How to use code to synchronized log video and PIR output ###
1. The code <b>MUST</b> run under raspberry PI3. PiCam must connected to Raspi as well as LAMPIR node.
2. Final code is in `./videolog/videolog.py`
3. After running, the video and analog output will be stored in `videodir='/home/pi/datalog/videolog/'` and `datadir='/home/pi/datalog/lampirdata/'`, with 1 min intervals. 

### Contribution guidelines ###



copyright by Libo Wu, 2018
