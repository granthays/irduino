#!/usr/bin/python

#----------------------------------------------------------------------------------
#
# XBMC Arduino IR Interpreter
#
# Author: Grant Hays
# Version: 0.0.1
# Date: 2012-06-30
#
# Description: This script reads the serial input from a USB connected Arduino
#	running the accompanying program and maps the decoded hex value of a cheap,
#	shitty Coby dvd player remote to keyboard keystrokes
#
#----------------------------------------------------------------------------------

import irduino
import irduino.collect
import irduino.codes
import irduino.mac_controls
import os, serial, serial.tools.list_ports, sys

def main():
	print "*************************************************************************"
	print "*\tXBMC Arduino IR Interpreter for Windows 7 [Version 0.0.1]\t*"
	print "*\tJul 11 2012 - Grant Hays ( granthays@gmail.com)\t\t\t*"
	print "*************************************************************************"

	print ""
	port = irduino.collect.getport()
	print ""
	remote = irduino.collect.getremote()
	print ""

	connected = False
	ser = serial.Serial(port, 9600)
	while not connected:
		serin = ser.read()
		connected = True
	
	while connected:
		try:	
			serin = repr(ser.readline())
			#print serin
			if serin in remote:
				sercall = remote[serin]
				sercall()
			else:
				print "Unrecognized code: {}".format(serin)
		except KeyboardInterrupt	:
			break
			
	sys.stderr.write('\n--- exit ---\n')

if __name__ == '__main__':
	main()
