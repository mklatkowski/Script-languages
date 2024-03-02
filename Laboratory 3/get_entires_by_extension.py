from read_log import read_log
from print_entries import print_entries
import sys

def get_entires_by_extension(extention, logs):
    returnList = []
    for tuple in logs:
        ext = tuple[3].split('.')[-1]
        if ext == extention:
            returnList.append(tuple)
    return returnList
if __name__ == '__main__':
    print_entries(get_entires_by_extension(sys.argv[1], read_log()))