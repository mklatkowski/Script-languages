import sys

def lab_3_f():
    try:
        file = sys.stdin
        for line in file:
            date = line.split()[3]
            hour = date.split(':')[1]
            if(int(hour)>=22 or int(hour)<=6):
                sys.stdout.write(line)
    except EOFError:
        print("EOF")
    except IndexError:
        print("Bad format")

if __name__ == '__main__':
        lab_3_f()