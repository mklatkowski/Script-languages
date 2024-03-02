import re


class SSHUser:

    def __init__(self, name, date_of_last_login):
        self.name = name
        self.date_of_last_login = date_of_last_login

    def validate(self):
        regex_pattern = r'^[a-z_][a-z0-9_-]{0,31}$'
        match = re.search(regex_pattern, self.name)
        if match:
            return True
        else:
            return False

    def __str__(self):
        return f'Name: {self.name}, date of last login: {self.date_of_last_login}'
