from sshUser import SSHUser
import datetime
from sshLogJournal import SSHLogJournal


def read(file):
    log_list = SSHLogJournal()
    with open(file) as f:
        for line in f:
            log_list.append(line)
    return log_list


if __name__ == '__main__':

    journal_list = read('ssh.txt')

    user1 = SSHUser('user1', datetime.datetime(2023, 12, 1, 12, 24, 54))
    user2 = SSHUser('user2', datetime.datetime(2019, 1, 24, 6, 12, 5))
    user3 = SSHUser('user3', datetime.datetime(2022, 4, 12, 23, 49, 4))
    user4 = SSHUser('user4', datetime.datetime(2022, 7, 30, 14, 24, 54))
    user5 = SSHUser('9', datetime.datetime(2022, 7, 30, 14, 24, 54))

    log1 = journal_list[0]
    log2 = journal_list[1]

    test_list = [user1, user2, user3, user4, user5, log1, log2]

    for i in test_list:
        print(i)
        print(i.validate())
        print()