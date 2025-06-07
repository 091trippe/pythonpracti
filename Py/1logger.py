import sys
from datetime import datetime

def log(message):
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    sys.stderr.write(f'[{current_time}] {message}\n')

