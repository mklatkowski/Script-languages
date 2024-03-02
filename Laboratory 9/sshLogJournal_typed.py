import re
import datetime
from typing import List, Union, Optional, Dict, Any
import sshLogEntry_typed


def str_to_dict(line: str) -> Optional[Dict[str, Any]]:
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


def to_SSHLogEntry(log: str) -> sshLogEntry_typed.SSHLogEntry:
    log_to_dict = str_to_dict(log)
    if log_to_dict is None:
        return sshLogEntry_typed.SSHAOther(datetime.datetime.now(), '', '', log, '')

    regex_pattern = r'error|Accepted|Failed'
    match_error = re.search(regex_pattern, log_to_dict['description'])

    if not match_error:
        return sshLogEntry_typed.SSHAOther(log_to_dict['timestamp'], log_to_dict['description'], log_to_dict['process'], log, log_to_dict['hostname'])

    group = match_error.group(0)

    if group == 'error':
        return sshLogEntry_typed.SSHAError(log_to_dict['timestamp'], log_to_dict['description'], log_to_dict['process'], log, log_to_dict['hostname'])
    elif group == 'Accepted':
        return sshLogEntry_typed.SSHAcceptedPassword(log_to_dict['timestamp'], log_to_dict['description'], log_to_dict['process'], log, log_to_dict['hostname'])
    else:
        return sshLogEntry_typed.SSHFailedPassword(log_to_dict['timestamp'], log_to_dict['description'], log_to_dict['process'], log, log_to_dict['hostname'])

class SSHLogJournal:

    def __init__(self, *args: str) -> None:
        self.logs: List[sshLogEntry_typed.SSHLogEntry] = []
        for log in args:
            self.logs.append(to_SSHLogEntry(log))

    def __len__(self) -> int:
        return len(self.logs)

    def __iter__(self):
        return iter(self.logs)

    def __contains__(self, element: sshLogEntry_typed.SSHLogEntry) -> bool:
        return element in self.logs

    def __getitem__(self, index: int) -> sshLogEntry_typed.SSHLogEntry:
        if index < self.__len__():
            return self.logs[index]
        else:
            raise IndexError

    def append(self, log: str) -> None:
        self.logs.append(to_SSHLogEntry(log))

    def get(self, starting_date: datetime.datetime, end_date: datetime.datetime) -> List[sshLogEntry_typed.SSHLogEntry]:
        logs: List[sshLogEntry_typed.SSHLogEntry] = []
        for log in self.logs:
            if starting_date < log.timestamp < end_date:
                logs.append(log)
        return logs

    def __str__(self) -> str:
        return str(self.logs)

if __name__ == '__main__':
    print(to_SSHLogEntry("Dec 10 07:11:42 LabSZ sshd[24224]: input_userauth_request: invalid user chen [preauth]").timestamp)
    print(datetime.datetime.strptime("Dec 10 07:11:42", '%b %d %H:%M:%S'))
