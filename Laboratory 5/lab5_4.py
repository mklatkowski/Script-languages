import sys
import random
from lab5_2 import get_user_from_log
from lab5_2 import str_to_dict


def get_random_logs_from_random_user(n, file='ssh.txt'):
    with open(file, "r") as f:
        users = set()
        for line in f:
            user = get_user_from_log(str_to_dict(line))
            if user is not None:
                users.add(user)
    chosen = random.choice(list(users))
    user_logs = []
    with open(file, "r") as f:
        for line in f:
            if get_user_from_log(str_to_dict(line))==chosen in line:
                user_logs.append(line)
        result = []
        for i in range(n):
            result.append(random.choice(user_logs))
    return result


def get_most_and_least_frequent_users(file='ssh.txt'):
    users_count = {}
    with open(file, "r") as f:
        for line in f:
            user = get_user_from_log(str_to_dict(line))
            if user is not None:
                users_count[user] = users_count.get(user, 0) + 1

    most_frequent_user = max(users_count, key=users_count.get)
    least_frequent_user = min(users_count, key=users_count.get)

    return most_frequent_user, least_frequent_user

if __name__ == '__main__':
        print(get_random_logs_from_random_user(2))
