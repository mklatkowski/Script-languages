from read_log import read_log
from print_entries import print_entries
import sys

def get_failed_reads(logs, param=True):
    returnList4xx = []
    returnList5xx = []

    for tuple in logs:
        if tuple[4] >=400 and tuple[4]<500:
             returnList4xx.append(tuple)
        elif tuple[4] >=500 and tuple[4]<600:
            returnList5xx.append(tuple)
    if not bool(param):
        print('dupa')
        return returnList4xx + returnList5xx
    return returnList4xx, returnList5xx


if __name__ == '__main__':
    print_entries(get_failed_reads(read_log()))