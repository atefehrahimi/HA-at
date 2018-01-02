import lib
import time
import signal
import sys
import configparser

config = configparser.ConfigParser()
config.read("sample.ini")

result = 1                                               # for done the first while loop
hostname = config.get("server", "server_1")              # return value of server_1 in section server
ports_option = (dict(config.items("ports"))).values()    # list of values in section ports
port = lib.check_ports(hostname, ports_option)           # return a port that was not close
time_sleep = config.getint("time", "delay")              # return time.sleep in config file
dic_result = {"ping": [], "telnet": [port]}                  # save our result in dictionary


def signal_handler(signal, frame):                       # manage our program with CTRL+C
        print(dic_result)
        sys.exit(0)


while True:
    while result == 1:                                  # for check result with ping
        result = lib.ping(hostname)
        dic_result["ping"].append(result)
        time.sleep(time_sleep)

    result = 1                                         # change result , for check next function(telnet)

    while result == 1:                                 # for check result with Telnet
        result = lib.telnet(hostname, port)
        dic_result["telnet"].append(result)            # for check my result , it is not essential
        time.sleep(time_sleep)
        signal.signal(signal.SIGINT, signal_handler)
