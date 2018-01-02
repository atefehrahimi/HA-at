import os
import telnetlib


def ping(hostname):
    response = os.system("ping -c 2 " + hostname)
    if response == 0:                                # and then check the response...
        result = 1
    else:
        result = 0
    return result


def telnet(hostname, port):                         # function for telnet ip
    try:
        tel = telnetlib.Telnet()
        tel.open(hostname, port)
        result = 1
    except IOError:
        result = 0
    return result


def check_ports(hostname, port_option):           # function for check that which port is not closed
    port = None                                   # if all of port was close , return None
    for port_choice in port_option:               # a loop for that check ports , if every port was up, the loop break
        result = telnet(hostname, port_choice)
        if result == 1:
            port = port_choice
            break
    return port
