import socket
import sys
from datetime import datetime
# input the targeted IP to scan
target = input (str("Target IP: "))
#easier interface to read whats going on
print("_" * 25)
print("Target Port: " + target)
print("Scan started at: " + str(datetime.now()))
print("_" * 25)


# scanning all the ports in range on the targeted IP
try:

    for port in range(1, 300):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)

    result = sock.connect_ex((target,port))
    if result == 0:
        print("[*] Port {} is open".format(port))
    sock.close()

except KeyboardInterrupt:
    print ("\n Existing...")
    sys.exit()
except socket.error:
    print("\n Host not responding...")
    sys.exit()
