from read_log import read_log
from log_to_dict import log_to_dict

def get_addrs(dict):
    return list(dict.keys())

if __name__ == '__main__':
        for i in get_addrs(log_to_dict(read_log())):
            print(i)