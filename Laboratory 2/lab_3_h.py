import sys

def lab_3_h():
    try:
        file = sys.stdin
        for line in file:
            url = line.split()[0]
            if(url.split('.')[-1]=='pl'):
                sys.stdout.write(line)
    except EOFError:
        print("EOF")
    except IndexError:
        print("Bad format")

if __name__ == '__main__':
        lab_3_h()