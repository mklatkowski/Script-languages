import sys

def lab_3_e():
    try:
        file = sys.stdin
        for line in file:
            if line.split()[-2] == '404':
                sys.stdout.write(line)
    except EOFError:
        print("EOF")
    except IndexError:
        print("Bad format")

if __name__ == '__main__':
        lab_3_e()
