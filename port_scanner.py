import sys
import subprocess
import socket


subprocess.call("clear",shell="True")
if len(sys.argv) < 2:
	print "Usage: python <filename> <'ipaddr/hostname'> <'ports to scan'>"
	sys.exit(1)



host = sys.argv[1]
ports = ""
port_name = "tcp"
if ".com" or ".in" or ".edu" or ".ng" in host:
	host = socket.gethostbyname(host)

print "-"*60
print "Starting scan on: "+ host
print "-"*60


if len(sys.argv) > 2:
	ports = sys.argv[2]
	if "," in ports:
		ports = ports.split(",")
		for port in ports:
			sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
			result = sock.connect_ex((host,int(port)))
			if result == 0:
            			try:
					print "[Open] "+str(port)+"	"+socket.getservbyport(int(port),"tcp")
				except socket.error as e:
					print "[Open] "+port+" service name not found!!"
			else:
				print "[Closed] "+port
        		sock.close()
else:
	for port in range(10000):
		sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		result = sock.connect_ex((host,port))
		if result == 0:
			try:
				print "[Open] "+str(port)+"	"+socket.getservbyport(int(port),"tcp")
			except socket.error as e:
				print "[Open] "+str(port)+" service name not found!!"
		sock.close()
print "-"*60
print "Done scanning host: "+host+".........."
	
