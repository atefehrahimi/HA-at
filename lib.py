import os
import telnetlib
hostname = '37.228.138.115'  # sample_ip for test


def ping():
    response = os.system("ping -c 2 " + hostname)

    #and then check the response...
    if response == 0:
        result = 1
    else:
        result = 0
    return result


def telnet():       # function for telnet ip
    port = 80
    try:
        telnet = telnetlib.Telnet()
        open_tel = telnet.open(hostname, port)
        return 1
    except IOError:
        return 0
