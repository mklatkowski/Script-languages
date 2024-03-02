import lab5_2
import lab5_3

def read_ssh(file, function=str):
    logs = []
    with open(file) as f:
        for line in f:
            logs.append(line)
            line_to_dic = lab5_2.str_to_dict(line)
            print(function(line_to_dic))
            lab5_3.show_line(line)
    return logs


# if __name__ == '__main__':
#     # print(read_ssh())