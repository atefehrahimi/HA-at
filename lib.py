import os
import telnetlib
import configparser

config = configparser.ConfigParser()
config.read("sample.ini")


def ping(hostname):
    response = os.system("ping -c 2 " + hostname)
    if response == 0:             # and then check the response...
        result = 1
    else:
        result = 0
    return result


def telnet(hostname, port):       # function for telnet ip
    try:
        tel = telnetlib.Telnet()
        tel.open(hostname, port)
        result = 1
    except IOError:
        result = 0
    return result


def ports(section):               # function for return ports of sample.ini in a list
    dict1 = {}
    options = config.options(section)
    for option in options:
            dict1[option] = config.get(section, option)
    list_ports = dict1.values()
    return list_ports


def host():                       # function for return name of my section that is server
    list_host = config.sections()
    item_host = list_host[0]
    return item_host
