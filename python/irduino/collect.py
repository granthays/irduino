

import irduino
import codes
import serial.tools.list_ports

def getport():
	portList = list(serial.tools.list_ports.comports())

	print ""
	print "Please select the communications port that your arduino is connected to:"
	print ""
	
	for index, openPort in enumerate(portList):
		print "\t[" + str(index + 1) + "]. " + openPort[0]
	print ""
	
	portChoice = int(raw_input("Enter a choice [1-" + str(len(portList)) + "]: ")) - 1

	#while ((portChoice < 1) or (portChoice > len(portList)):
	while (not(0 < int(portChoice) <= len(portList))):
		portChoice = int(raw_input("Invalid entry. Enter a choice [1-" + str(len(portList)) + "]: ")) - 1

	return (portList[int(portChoice)][0])


def getremote():
	CodeKeys = codes.CodeNames.keys()

	print ""
	print "Please select the remote you will be using: "
	print ""
	
	for index, key in enumerate(CodeKeys):
		print "\t[" + str(index + 1) + "]. " + key
	
	print ""
	
	remoteChoice = int(raw_input("Enter a choice [1-" + str(len(CodeKeys)) + "]: ")) - 1

	while not(0 < int(remoteChoice) <= len(CodeKeys)):
		remoteChoice = int(raw_input("Invalid entry. Enter a choice [1-" + str(len(CodeKeys)) + "]: ")) - 1
	
	print ""
	print "\tConnected. System is now paired with", CodeKeys[remoteChoice], "remote."

	return (codes.CodeNames[CodeKeys[remoteChoice]])
