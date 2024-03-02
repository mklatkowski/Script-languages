import sys

def entry_to_dict(tuple):
    return {
        "ip": tuple[0],
        "date": tuple[1],
        "method": tuple[2],
        "file": tuple[3],
        "code": tuple[4],
        "bytes": tuple[5]
    }


if __name__ == '__main__':
        entry_to_dict(sys.argv[1])