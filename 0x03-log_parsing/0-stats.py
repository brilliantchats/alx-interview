#!/usr/bin/python3
"""
Reads stdin line by line and prints some stats
"""
import sys
import re


def print_files(size, statuses):
    """Prints"""
    status_codes = sorted(list(statuses.keys()))
    print('File size: {}'.format(size))
    for status in status_codes:
        print('{}: {}'.format(status, statuses[status]))


i = 0
file_size = 0
status_codes = {200: 200, 301: 301, 400: 400, 401: 401,
                403: 403, 404: 404, 405: 405, 500: 500}
status_list = dict()
try:
    for line in sys.stdin:
        regex1 = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[.+\] '
        regex2 = r'"GET /projects/260 HTTP/1.1" \S+ \S+'
        regex = regex1 + regex2
        line = line.rstrip('\n')
        match = re.match(regex, line)
        line_arr = line.split()
        if match:
            file_size += int(line_arr[-1])
            status_str = line_arr[-2]
            if status_str.isdigit():
                status = int(status_str)
                if status in status_codes:
                    current_status = status_list.get(status, 0)
                    status_list[status] = current_status + 1
            i += 1
        if i == 10:
            print_files(file_size, status_list)
            i = 0
except (KeyboardInterrupt):
    print_files(file_size, status_list)
    raise
