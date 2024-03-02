from datetime import date
import sys

def lab_3_g():
    try:
        file = sys.stdin
        for line in file:
            try:
                dt = line.split()[3]
                day = dt.split(':')[0]
                day = day.split('/')
                day[0] = day[0][1:]
                currentDay = date(int(day[2]), nameTonumber(day[1]), int(day[0]))
                if(currentDay.weekday()==4):
                    sys.stdout.write(line)
            except ValueError: continue
    except EOFError:
        print("EOF")
    except IndexError:
        print("Bad format")

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
        lab_3_g()