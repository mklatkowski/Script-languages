import re
from ipaddress import IPv4Address
from abc import ABC
from abc import abstractmethod
import datetime

REGEX = r'^(\w{3}\s+\d{1,2}\s+\d{2}:\d{2}:\d{2})\s+(\w+)\s+sshd\[(\d+)\]:\s+(.*)$'


class SSHLogEntry(ABC):

    def __init__(self, timestamp, description, pid, raw_entry, hostname=None):
        self.timestamp = timestamp
        self.description = description
        self._raw_entry = raw_entry
        self.pid = pid
        self.hostname = hostname

    def __str__(self):
        return self._raw_entry

    def get_ipv4(self):
        pattern = r'(\b25[0-5]|\b2[0-4][0-9]|\b[01]?[0-9][0-9]?)(\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}'
        ipv4 = re.search(pattern, self.description)
        if ipv4:
            return IPv4Address(ipv4.group(0))
        else:
            return None

    @property
    def has_ip(self):
        return self.get_ipv4() is not None

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self._raw_entry == other.raw_entry

    def __lt__(self, other):
        return self.timestamp < other.timestamp

    def __gt__(self, other):
        return self.timestamp > other.timestamp

    @abstractmethod
    def validate(self):
        pass


class SSHFailedPassword(SSHLogEntry):

    def __init__(self, timestamp, description, pid, raw_entry, hostname=None):
        super().__init__(timestamp, description, pid, raw_entry, hostname)
        self.port = self.get_port()

    def validate(self):
        regex_pattern_failed = r'Failed password'
        match = re.match(REGEX, self._raw_entry)
        time = datetime.datetime.strptime(match.group(0), '%b %d %H:%M:%S')
        return (re.search(regex_pattern_failed, self.description) and
                time == self.timestamp and
                match.group(1) == self.hostname and
                match.group(2) == self.pid and
                match.group(3) == self.description)

    def get_port(self):
        regex_port = r'port\s(\d+)'
        return re.search(regex_port, self.description).group(1)


class SSHAcceptedPassword(SSHLogEntry):

    def __init__(self, timestamp, description, pid, raw_entry, hostname=None):
        super().__init__(timestamp, description, pid, raw_entry, hostname)
        self.port = self.get_port()

    def validate(self):
        regex_pattern_accepted = r'Accepted password'
        match = re.match(REGEX, self._raw_entry)
        time = datetime.datetime.strptime(match.group(0), '%b %d %H:%M:%S')
        return (re.search(regex_pattern_accepted, self.description) and
                time == self.timestamp and
                match.group(1) == self.hostname and
                match.group(2) == self.pid and
                match.group(3) == self.description)

    def get_port(self):
        regex_port = r'port\s(\d+)'
        return re.search(regex_port, self.description).group(1)


class SSHAError(SSHLogEntry):

    def __init__(self, timestamp, description, pid, raw_entry, hostname=None):
        super().__init__(timestamp, description, pid, raw_entry, hostname)
        self.port = self.get_reason()

    def validate(self):
        regex_pattern_error = r'error'
        match = re.match(REGEX, self._raw_entry)
        time = datetime.datetime.strptime(match.group(0), '%b %d %H:%M:%S')
        return (re.search(regex_pattern_error, self.description) and
                time == self.timestamp and
                match.group(1) == self.hostname and
                match.group(2) == self.pid and
                match.group(3) == self.description)

    def get_reason(self):
        regex_extra = r'error:(.*)from'
        return re.search(regex_extra, self.description).group(1)


class SSHAOther(SSHLogEntry):

    def __init__(self, timestamp, description, pid, raw_entry, hostname=None):
        super().__init__(timestamp, description, pid, raw_entry, hostname)

    def validate(self):
        return True
