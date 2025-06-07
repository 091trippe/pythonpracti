import sys
import datetime

class Logger:
    def __init__(self, out_stream=None, time_formatter='%Y-%m-%d %H:%M:%S'):
        self.out_stream = out_stream if out_stream is not None else sys.stderr
        self.time_formatter = time_formatter

    def set_time_formatter(self, time_formatter):
        self.time_formatter = time_formatter

    def log(self, message):
        current_time = datetime.datetime.now().strftime(self.time_formatter)
        formatted_message = f"[{current_time}] {message}"
        print(formatted_message, file=self.out_stream)

if __name__ == "__main__":
    logger = Logger()
    logger.log('message for logging')
    logger.set_time_formatter('%H:%M:%S')
    logger.log('another message with new time format')
