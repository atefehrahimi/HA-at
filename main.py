from lib import ping
import time


if __name__ == "__main__":
    while True:
        result = ping()
        print("the result is" + str(result))
        time.sleep(3)
