import sys

def lab_3_c():
    try:
        file = sys.stdin
        biggest_data = None
        biggest_value = 0
        for line in file:
            try:
                candidate_value = int(line.split()[-1])
            except ValueError:
                continue
            try:
                if candidate_value > biggest_value:
                    biggest_value = candidate_value
                    biggest_data = line.split()[-4]
            except TypeError: continue
        print(biggest_data)
        print(biggest_value)
    except EOFError:
        print("EOF")
    except IndexError:
        print("Bad format")

if __name__ == '__main__':
        lab_3_c()
