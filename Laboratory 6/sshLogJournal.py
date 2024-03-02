import re
import datetime
import sshEntry


def str_to_dict(line):
    pattern = r'^(\w{3}\s+\d{1,2}\s+\d{2}:\d{2}:\d{2})\s+(\S+)\s+sshd\[(\d+)\]:\s+(.*)'
    match = re.match(pattern, line)
    if match:
        timestamp, hostname, process, description = match.groups()
        timestamp = datetime.datetime.strptime(timestamp, '%b %d %H:%M:%S')
        return {
            'timestamp': timestamp,
            'hostname': hostname,
            'process': process,
            'description': description
        }
    else:
        return None


def to_SSHLogEntry(log):
    log_to_dic = str_to_dict(log)
    regex_pattern = r'error|Accepted|Failed'

    match_error = re.search(regex_pattern, log_to_dic['description'])

    if not match_error:
        return sshEntry.SSHAOther(log_to_dic['timestamp'], log_to_dic['description'], log_to_dic['process'], log, log_to_dic['hostname'])

    group = match_error.group(0)

    if group == 'error':
        return sshEntry.SSHAError(log_to_dic['timestamp'], log_to_dic['description'], log_to_dic['process'], log, log_to_dic['hostname'])
    elif group == 'Accepted':
        return sshEntry.SSHAcceptedPassword(log_to_dic['timestamp'], log_to_dic['description'], log_to_dic['process'], log, log_to_dic['hostname'])
    else:
        return sshEntry.SSHFailedPassword(log_to_dic['timestamp'], log_to_dic['description'], log_to_dic['process'], log, log_to_dic['hostname'])


class SSHLogJournal:

    def __init__(self, *args) -> None:
        self.logs = []
        for log in args:
            self.logs.append(log)

    def __len__(self):
        return len(self.logs)

    def __iter__(self):
        return iter(self.logs)

    def __contains__(self, element):
        return element in self.logs

    def __getitem__(self, index):
        if index < self.__len__():
            return self.logs[index]

    def append(self, log):
        self.logs.append(to_SSHLogEntry(log))

    def get(self, starting_data, end_data):
        logs = []
        for log in self.logs:
            if starting_data < log.date < end_data:
                logs.append(log)
        return logs

    def __str__(self):
        return str(self.logs)