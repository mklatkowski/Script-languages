import sys

def lab_3_c():
    try:
        file = sys.stdin
        log_count = 0
        graphics_count = 0
        for line in file:
            address = line.split()[-4]
            log_count+=1
            try:
                type = address.split('.')[1]
                if(type == 'gif' or type == 'jpg' or type == 'jpeg' or type == 'xbm'):
                    graphics_count+=1
            except IndexError: continue
        print('Ratio:')
        print(graphics_count/(log_count-graphics_count))
    except EOFError:
        print("EOF")
    except IndexError:
        print("Bad format")

if __name__ == '__main__':
        lab_3_c()