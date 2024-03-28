#!/usr/bin/python3
"""Log parsing: reads stdin line by line and computes metrics"""
from sys import stdin
import re


def initialize_log():
    """Initialize log dictionary"""
    status_codes = {200, 301, 400, 401, 403, 404, 405, 500}
    log = {"file_size": 0, "code_list":
           {str(code): 0 for code in status_codes}}
    return log


def process_line(line, regex, log):
    """processes each log line"""
    match = regex.match(line)
    if match:
        stat_code, file_size = match.group(1, 2)

        log["file_size"] += int(file_size)
        if stat_code.isdecimal():
            log["code_list"][stat_code] += 1

        return log


def print_stats(log):
    """Prints statistics for file size and status codes."""
    print("File size: {}".format(log['file_size']))
    for code in sorted(log["code_list"]):
        if log["code_list"][code]:
            print(f"{code}: {log['code_list'][code]}")


def main():
    """main function"""
    regex = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d+\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)')

    log = initialize_log()
    line_count = 0

    try:
        for line in stdin:
            line = line.strip()

            line_count += 1

            log = process_line(line, regex, log)

            if line_count % 10 == 0:
                print_stats(log)

    except KeyboardInterrupt:
        print_stats(log)


if __name__ == "__main__":
    main()
