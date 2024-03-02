from entry_to_dict import entry_to_dict
from read_log import read_log

def log_to_dict(logs):
    returnDict = {}
    for tuple in logs:
        if tuple[0] in returnDict:
            returnDict[tuple[0]].append(entry_to_dict(tuple))
        else:
            returnDict[tuple[0]] = [entry_to_dict(tuple)]
    return returnDict

if __name__ == '__main__':
        log_to_dict(read_log())