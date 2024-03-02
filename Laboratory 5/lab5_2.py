import re

def str_to_dict(line):
    pattern = r'^(\w{3}\s+\d{1,2}\s+\d{2}:\d{2}:\d{2})\s+(\S+)\s+sshd\[(\d+)\]:\s+(.*)'
    match = re.match(pattern, line)
    if match:
        timestamp, hostname, process, description = match.groups()
        return {
            'timestamp': timestamp,
            'hostname': hostname,
            'process': process,
            'description': description
        }
    else:
        return None

def get_ipv4s_from_log(dict):
    if dict is not None:
        pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
        ipv4s = re.findall(pattern, dict['description'])
        return ipv4s
    else:
        return None

def get_user_from_log(dict):
    if dict is not None:
        pattern = r'user ((?!unknown|authentication)\w+)|(root)'
        match = re.search(pattern, dict['description'])
        if match:
            user = match.group(1) or match.group(2)
            return user
        else:
            return None
    else:
        return None


def get_message_type(log_entry):
    login_successful = re.compile(r'Accepted password')
    login_failed = re.compile(r'Failed password')
    connection_closed = re.compile(r'Connection closed')
    incorrect_password = re.compile(r'authentication failure')
    incorrect_username = re.compile(r'Invalid user')
    login_attempt = re.compile(r'POSSIBLE BREAK-IN ATTEMPT')

    log_entry = log_entry['description']
    if login_successful.search(log_entry):
        return "login_successful"
    elif login_failed.search(log_entry):
        return "login_failed"
    elif connection_closed.search(log_entry):
        return "connection_closed"
    elif incorrect_password.search(log_entry):
        return "incorrect_password"
    elif incorrect_username.search(log_entry):
        return "incorrect_username"
    elif login_attempt.search(log_entry):
        return "login_attempt"
    else:
        return "other"

if __name__ == '__main__':
        get_message_type()