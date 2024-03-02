import re
from ipaddress import IPv4Address
from abc import ABC, abstractmethod
import datetime
from typing import Optional

REGEX = r'^(\w{3}\s+\d{1,2}\s+\d{2}:\d{2}:\d{2})\s+(\w+)\s+sshd\[(\d+)\]:\s+(.*)$'


class SSHLogEntry(ABC):
    def __init__(
        self,
        timestamp: datetime.datetime,
        description: str,
        pid: str,
        raw_entry: str,
        hostname: str = '',
    ) -> None:
        self.timestamp: datetime.datetime = timestamp
        self.description: str = description
        self._raw_entry: str = raw_entry
        self.pid: str = pid
        self.hostname: str = hostname

    def __str__(self) -> str:
        return self._raw_entry

    def get_ipv4(self) -> Optional[IPv4Address]:
        pattern = r'(\b25[0-5]|\b2[0-4][0-9]|\b[01]?[0-9][0-9]?)(\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}'
        ipv4 = re.search(pattern, self.description)
        if ipv4:
            return IPv4Address(ipv4.group(0))
        else:
            return None

    @property
    def has_ip(self) -> bool:
        return self.get_ipv4() != None

    def __repr__(self) -> str:
        return str(self)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, SSHLogEntry):
            return False
        return self._raw_entry == other._raw_entry

    def __lt__(self, other: 'SSHLogEntry') -> bool:
        return self.timestamp < other.timestamp

    def __gt__(self, other: 'SSHLogEntry') -> bool:
        return self.timestamp > other.timestamp

    @abstractmethod
    def validate(self) -> bool:
        pass


class SSHFailedPassword(SSHLogEntry):
    def __init__(
        self,
        timestamp: datetime.datetime,
        description: str,
        pid: str,
        raw_entry: str,
        hostname: str = '',
    ) -> None:
        super().__init__(timestamp, description, pid, raw_entry, hostname)
        self.port: str = self.get_port()

    def validate(self) -> bool:
        regex_pattern_failed = r'Failed password'
        match = re.match(REGEX, self._raw_entry)
        if match:
            time = datetime.datetime.strptime(match.group(1), '%b %d %H:%M:%S')
            return (
                bool(re.search(regex_pattern_failed, self.description))
                and time == self.timestamp
                and match.group(2) == self.hostname
                and match.group(3) == self.pid
                and match.group(4) == self.description
            )
        return False

    def get_port(self) -> str:
        regex_port = r'port\s(\d+)'
        if self.description and isinstance(self.description, str):
            match = re.search(regex_port, self.description)
            if match:
                return match.group(1)
        return ''


class SSHAcceptedPassword(SSHLogEntry):
    def __init__(
        self,
        timestamp: datetime.datetime,
        description: str,
        pid: str,
        raw_entry: str,
        hostname: str = '',
    ) -> None:
        super().__init__(timestamp, description, pid, raw_entry, hostname)
        self.port: str = self.get_port()

    def validate(self) -> bool:
        regex_pattern_accepted = r'Accepted password'
        match = re.match(REGEX, self._raw_entry)
        if match:
            time = datetime.datetime.strptime(match.group(1), '%b %d %H:%M:%S')
            return (
                bool(re.search(regex_pattern_accepted, self.description))
                and time == self.timestamp
                and match.group(2) == self.hostname
                and match.group(3) == self.pid
                and match.group(4) == self.description
            )
        return False

    def get_port(self) -> str:
        regex_port = r'port\s(\d+)'
        if self.description and isinstance(self.description, str):
            match = re.search(regex_port, self.description)
            if match:
                return match.group(1)
        return ''


class SSHAError(SSHLogEntry):
    def __init__(
        self,
        timestamp: datetime.datetime,
        description: str,
        pid: str,
        raw_entry: str,
        hostname: str = '',
    ) -> None:
        super().__init__(timestamp, description, pid, raw_entry, hostname)
        self.reason: str = self.get_reason()

    def validate(self) -> bool:
        regex_pattern_error = r'error'
        match = re.match(REGEX, self._raw_entry)
        if match:
            time = datetime.datetime.strptime(match.group(1), '%b %d %H:%M:%S')
            return (
                bool(re.search(regex_pattern_error, self.description))
                and time == self.timestamp
                and match.group(2) == self.hostname
                and match.group(3) == self.pid
                and match.group(4) == self.description
            )
        return False

    def get_reason(self) -> str:
        regex_extra = r':\s(.+)$'
        if self.description and isinstance(self.description, str):
            match = re.search(regex_extra, self.description)
            if match:
                return match.group(1)
        return ''


class SSHAOther(SSHLogEntry):
    def __init__(
        self,
        timestamp: datetime.datetime,
        description: str,
        pid: str,
        raw_entry: str,
        hostname: str ='',
    ) -> None:
        super().__init__(timestamp, description, pid, raw_entry, hostname)

    def validate(self) -> bool:
        return True
