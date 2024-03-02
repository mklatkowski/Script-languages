from log_to_dict import log_to_dict
from read_log import read_log

def print_dict_entry_dates(dict):
    for key in dict:
        requestCount = len(dict[key])
        dateList = [elem["date"] for elem in dict[key]]
        maxDatetime = max(dateList)
        minDatetime = min(dateList)
        withCode200 = len([elem["code"] for elem in dict[key] if elem["code"]==200])

        print(f"Key: {key}, Request count: {requestCount}, max date: {maxDatetime}, min date: {minDatetime}, ratio: {withCode200/requestCount}")

if __name__ == '__main__':
        print_dict_entry_dates(log_to_dict(read_log()))