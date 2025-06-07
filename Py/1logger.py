import sys
import datetime

def log(message):
    time = str(datetime.datetime.now())
    sys.stderr.write(f'[{time}] {message}\n')
