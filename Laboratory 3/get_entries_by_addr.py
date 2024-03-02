from read_log import read_log
from print_entries import print_entries
import sys

def get_entries_by_addr(ip, logs):
    returnList = []
    for tuple in logs:
        if tuple[0] == ip:
            print(tuple)
            returnList.append(tuple)
    return returnList

if __name__ == '__main__':
    print_entries(get_entries_by_addr(sys.argv[1], read_log()))
