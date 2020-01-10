import socket
import sys
import subprocess

subprocess.call('clear', shell=True)
if len(sys.argv) < 2:
	print "[!] Usage: the ip address is given as a commandline argument"
	print "Ex: python port_scanner.py 'XXX.XXX.XX.X'" 
	sys.exit(1)

ip = sys.argv[1]
print "-" * 60
print "Please wait, scanning remote host", ip
print "-" * 60
try:
	for port in range(1,10000):
		sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		result = sock.connect_ex((ip,port))
		if result == 0:
			print "[+] Port {}:		 Open".format(port)
		sock.close() 
except socket.error:
	print "[!] Unable to connect to remote host...." 
print "[!] Scanning done.." 
