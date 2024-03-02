import sys


def lab_3_b():
    try:
        file = sys.stdin
        data_count = 0
        for line in file:
            try:
                code = line.split()[-1]
                data_count += int(code)
            except ValueError:
                continue
        print("Requests data in GB:")
        print(f": {data_count/(1024**2)}")
    except EOFError:
        print("EOF")
    except IndexError:
        print("Bad format")

if __name__ == '__main__':
        lab_3_b()
