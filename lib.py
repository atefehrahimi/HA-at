import os


def ping():
    hostname = '192.168.1.5'# sample_ip for test
    response = os.system("ping -c 5 " + hostname)

    #and then check the response...
    if response == 0:
        result = 1
    else:
        result = 0
    return result
