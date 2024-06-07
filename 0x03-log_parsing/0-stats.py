#!/usr/bin/python3
""" Module for task 0
Reads standard input line by line and computes metrics.
Input format:
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>.
(if the format is not this one, the line must be skipped).
After every 10 lines and/or a keyboard interruption (CTRL + C), print these
statistics from the beginning:
    Total file size: File size: <total size>
    where <total size> is the sum of all previous <file size> (format above)
    Number of lines by status code:
        possible status code: 200, 301, 400, 401, 403, 404, 405 and 500.
        if a status code doesn’t appear or is not an integer, don’t
        print anything for this status code.
        format: <status code>: <number>.
        status codes should be printed in ascending order.
"""


def print_statistics(total_size, status_counts):
    print(f"File size: {total_size}")
    for status in sorted(status_counts.keys()):
        if status_counts[status] > 0:
            print(f"{status}: {status_counts[status]}")


def process_line(line, total_size, status_counts):
    parts = line.split()
    if len(parts) < 9:
        return total_size, status_counts

    try:
        file_size = int(parts[-1])
        status_code = int(parts[-2])
    except ValueError:
        return total_size, status_counts

    if parts[2] != '"GET':
        return total_size, status_counts

    total_size += file_size
    if status_code in status_counts:
        status_counts[status_code] += 1
    return total_size, status_counts


def main():
    total_size = 0
    status_counts =
    {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0

    try:
        while True:
            line = input()
            total_size, status_counts =
            process_line(line, total_size, status_counts)
            line_count += 1
            if line_count % 10 == 0:
                print_statistics(total_size, status_counts)
    except EOFError:
        if line_count % 10 != 0:
            print_statistics(total_size, status_counts)


if __name__ == "__main__":
    main()
