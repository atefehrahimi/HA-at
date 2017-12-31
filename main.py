import lib
import time


result = 1                         # for done the first while loop
hostname = lib.host()              # return name of server
ports = lib.ports(hostname)        # return ports


for port_choice in ports:         # a loop for that check ports , if every port was up the loop break
    result = lib.telnet(hostname, port_choice)
    if result == 1:
        port = port_choice
        break
    else:
        continue


while True:
        while result == 1:       # for check result with ping
            result = lib.ping(hostname)
            time.sleep(3)

        result = 1            # change result , for check next function(telnet)

        while result == 1:    # for check result with Telnet
            result = lib.telnet(hostname, port)
            print(result)     # for check my result , it is not essential
            time.sleep(3)
