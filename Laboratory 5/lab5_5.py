import argparse
import logging
from pathlib import Path
import sys
import lab5_1
import lab5_2
import lab5_3
import lab5_4


def show():
    parser = argparse.ArgumentParser(description="Logs commander")
    parser.add_argument('file', help="Path to file")
    parser.add_argument('--l', help="Logging level")
    subparser = parser.add_subparsers(dest='function', help='dostępne funkcje')
    subparser.add_parser('get_ipv4', help='Show ipv4 adresses')
    subparser.add_parser('get_user', help='Show users')
    subparser.add_parser('get_messages', help='Show messages')
    subparser.add_parser('to_dict', help='Convert line to dict')
    subparser.add_parser('users_freq', help='Show most and least frequent users appearances')

    subparser4c = subparser.add_parser('random_users_logs', help='Show random users logs')
    subparser4c.add_argument('--n', required=True, help="Count of random user logs")

    args = parser.parse_args()

    if args.function == 'random_users_logs':
        n = int(args.n)
    else:
        n = None

    if args.l is not None:
        change_logging_level(args.l)

    file = Path(args.file)
    if not file.exists():
        print("That file doesn't exist")
        raise SystemExit(1)

    run(file, args.function, n)

def change_logging_level(level):
    log_level = logging.INFO
    if level=='DEBUG':
        log_level = logging.DEBUG
    elif level == 'WARNING':
        log_level = logging.WARNING
    elif level == 'ERROR':
        log_level = logging.ERROR
    elif level == 'CRITICAL':
        log_level = logging.CRITICAL
    lab5_3.logger.setLevel(log_level)
    logging.basicConfig(level=log_level)


def run(file, function, n):
    if function == 'get_ipv4':
        lab5_1.read_ssh(file, lab5_2.get_ipv4s_from_log)
    elif function == 'get_user':
        lab5_1.read_ssh(file, lab5_2.get_user_from_log)
    elif function == 'get_messages':
        lab5_1.read_ssh(file, lab5_2.get_message_type)
    elif function == 'random_users_logs':
        print(lab5_4.get_random_logs_from_random_user(n))
    elif function == 'users_freq':
        print(lab5_4.get_most_and_least_frequent_users())
    elif function == 'to_dict':
        lab5_1.read_ssh(file)

if __name__ == '__main__':
    show()