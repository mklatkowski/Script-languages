import sys
from datetime import datetime
from print_entries import print_entries

def read_log():
    returnList = []
    for line in sys.stdin:
        try:
            line = line.split()

            ip = line[0]
            date = getDate(line[3])
            method = line[5][1:]
            url = line[6]
            code = int(line[8])
            if(line[9]=='-'):
                bytes = 0
            else:
                bytes = int(line[9])
            returnList.append((ip, date, method, url, code, bytes))
        except EOFError:
            print("EOF")
        except ValueError: continue
        except IndexError: continue

    return returnList

def getDate(day):

    dt, hour = day.split(':')[0], day.split(':')[1:]
    day = dt.split('/')
    day[0] = day[0][1:]

    return datetime(int(day[2]), nameTonumber(day[1]), int(day[0]), int(hour[0]), int(hour[1]), int(hour[2]))

def nameTonumber(month):
    match month:
        case 'Jan': return 1
        case 'Feb': return 2
        case 'Mar': return 3
        case 'Apr': return 4
        case 'May': return 5
        case 'Jun': return 6
        case 'Jul': return 7
        case 'Aug': return 8
        case 'Sep': return 9
        case 'Oct': return 10
        case 'Nov': return 11
        case 'Dec': return 12

if __name__ == '__main__':
        print_entries(read_log())