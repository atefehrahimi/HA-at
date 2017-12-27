import lib
import time

result = 1         # for
if __name__ == "__main__":
    while True:

        while result == 1:     # for check result with ping
            result = lib.ping()
            time.sleep(3)

        result = 1            # change result , for check next function(telnet)

        while result == 1:    # for check result with Telnet
            result = lib.telnet()
            print(result)     # for check my result , it is not essential
            time.sleep(3)
