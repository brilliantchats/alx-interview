#!/usr/bin/python3
"""
Reads stdin line by line and prints some stats
"""
import sys
from dateutil.parser import parse


def split_str(line):
    """
    Splits the given str in a format thats given
    """
    arr = line.split()
    line_arr = list()
    line_arr.append(arr[0])
    line_arr.append(arr[1])
    new_date = arr[2] + ' ' + arr[3]
    line_arr.append(new_date)
    new_http = arr[4] + ' ' + arr[5] + ' ' + arr[6]
    line_arr.append(new_http)
    line_arr.append(arr[7])
    line_arr.append(arr[8])
    return line_arr


def validate(line):
    """
    Validates stdin input for the compute_metrics function
    """
    status_codes = {200: 200, 301: 301, 400: 400, 401: 401,
                    403: 403, 404: 404, 405: 405, 500: 500}
    line_arr = split_str(line)
    ip_address = line_arr[0].split('.')
    for num in ip_address:
        if not num.isdigit():
            return False
    if line_arr[1] != '-':
        return False
    if line_arr[2][0] == '[' and line_arr[2][-1] == ']':
        date = line_arr[2].strip('[]')
        try:
            parse(date, fuzzy=False)
        except ValueError:
            return False
    else:
        return False
    if line_arr[3] != '"GET /projects/260 HTTP/1.1"':
        return False
    if line_arr[4].isdigit():
        status = int(line_arr[4])
        if status not in status_codes:
            return False
    else:
        return False
    if not line_arr[5].isdigit():
        return False
    return True


def print_files(files, statuses, size):
    """
    Prints the total file size in the dict and status codes
    """
    status_codes = sorted(list(statuses.keys()))
    total_file_size = sum(files.values()) + size
    print('File size: {}'.format(total_file_size))
    for status in status_codes:
        print('{}: {}'.format(status, statuses[status]))
    return total_file_size


def compute_metrics():
    """
    Reads stdin line by line and computes some metrics
    """
    file_list = dict()
    status_list = dict()
    i = 0
    file_size = 0
    try:
        for line in sys.stdin:
            line = line.rstrip('\n')
            if (validate(line)):
                arr = split_str(line)
                status = int(arr[4])
                size = int(arr[5])
                if status in file_list:
                    file_list[status] = size + file_list.get(status)
                    status_list[status] = status_list.get(status) + 1
                else:
                    file_list[status] = size
                    status_list[status] = 1
                i += 1
                if i == 10:
                    file_size = print_files(file_list, status_list, file_size)
                    file_list = {}
                    i = 0
            else:
                if i == 10:
                    file_size = print_files(file_list, status_list, file_size)
                    file_list = {}
                    i = 0
                i += 1
    except KeyboardInterrupt:
        print_files(file_list, status_list, file_size)
        raise


if __name__ == '__main__':
    compute_metrics()
