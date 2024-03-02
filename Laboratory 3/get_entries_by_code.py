from read_log import read_log
from print_entries import print_entries
import sys

def get_entries_by_code(code, logs):
    returnList = []
    for tuple in logs:
        try:
            code = int(code)
            if tuple[4] == code:
                returnList.append(tuple)
        except ValueError:
            print('Bad value')
            break
    return returnList

if __name__ == '__main__':
    print_entries(get_entries_by_code(sys.argv[1], read_log()))