import os


def ping():
    hostname = '192.168.1.5'# sample_ip for test
    response = os.system("ping -c 5 " + hostname)

    #and then check the response...
    if response == 0:
        print(hostname, 'is up!')
    else:
        print(hostname, 'is down!')
