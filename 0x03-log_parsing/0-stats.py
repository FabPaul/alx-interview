#!/usr/bin/python3
""" Log parsin script that reads stdin line by line and computes metrics"""

import sys

status = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0,
          '404': 0, '405': 0, '500': 0}

total_size = 0
count = 0

try:
    for line in sys.stdin:
        line_list = line.split(" ")

        if len(line_list) > 4:
            code = line_list[-2]
            file_size = int(line_list[-1])

            if code in status.keys():
                status[code] += 1

            total_size += file_size

            count += 1

        if count == 10:
            count = 0
            print(f'File size: {total_size}')

            for key, value in sorted(status.items()):
                if value != 0:
                    print(f'{key}: {value}')

except Exception as err:
    pass

finally:
    print(f'File size: {total_size}')
    for key, value in sorted(status.items()):
        if value != 0:
            print(f'{key}: {value}')
