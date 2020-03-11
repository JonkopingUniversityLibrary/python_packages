import io
from datetime import datetime
import re


class Logger:

    def __init__(self, dateformat, separator, log_to_print=True, log_name='default.log'):
        self.dateformat = dateformat
        self.separator = separator
        self.log_to_print = log_to_print
        self.log_name = self._convert(log_name)

    @staticmethod
    def _convert(name):
        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

    def log(self, severity, *messages):
        # Remove whitespace from the messages
        messages = [message.strip() for message in messages]
        # Convert the messages to one string
        message = self.separator.join(messages)

        timestamp = self.dateformat.format(datetime.now())

        row = timestamp + self.separator +\
            severity + self.separator +\
            message
        if self.log_to_print:
            print(row)
        else:
            with io.open(self.log_name, "a", encoding='UTF-8') as file:
                file.write(row + '\n')
