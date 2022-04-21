# Question 1: In the program, what is the line for creating a socket?
# Answer 1: Line 30.
# Question 2: In the program, what are the three lines that are used to obtain the start time, end time and elapsed time?
# Answer 2: Line 25, 50 and 53.
#!/usr/bin/env python
import socket
import subprocess
import sys
from datetime import datetime


# Clear the screen
subprocess.call('cls', shell=True)

# Ask for input
remoteServer = input("Enter a remote host to scan: ")
remoteServerIP = socket.gethostbyname(remoteServer)

# Print a nice banner with information on which host we are about to scan
print("-" * 60)
print("Please wait, scanning remote host", remoteServerIP)
print("-" * 60)

# Check what time the scan started
t1 = datetime.now()

# Using the range function to specify ports
try:
    for port in range(0,1024):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(10)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print ("Port {}: 	 Open".format(port))
        sock.close()
except KeyboardInterrupt:
    print ("You pressed Ctrl+C")
    sys.exit()
except socket.gaierror:
    print("Hostname could not be resolved")
    sys.exit()
except socket.timeout:
    print("Could not connect to the remote server")
    sys.exit()



    
# Checking the time again
t2 = datetime.now()

# Calculates the difference of time, to see how long it took to run the script
total = t2 - t1

# Printing the information to screen
print('Scanning Completed in: ', total)