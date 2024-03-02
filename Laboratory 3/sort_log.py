import sys
from read_log import read_log
from print_entries import print_entries

def sort_log(index, logs):
    try:
        index = int(index)
    except ValueError:
        print("Bad value")
        return None
    if index < len(logs[0]) and index >=0:
        logs.sort(key=lambda x: x[index])
        return logs
    else:
        raise IndexError

if __name__ == '__main__':
    print_entries(sort_log(sys.argv[1], read_log()))
