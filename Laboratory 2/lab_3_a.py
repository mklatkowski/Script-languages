import sys

def lab_3_a(cd):
    try:
        file = sys.stdin
        codes_count = 0
        for line in file:
            try:
                code = line.split()[-2]
                if code == cd:
                    codes_count += 1
            except IndexError: continue
    except EOFError:
        print("EOF")
    print("Requests count by HTTP code " + cd)
    print(codes_count)
