#!/usr/bin/python3
""" Module for task 0
Reads standard input line by line and computes metrics.
"""


def print_statistics(total_size, status_counts):
    """Pending input of doc"""
    print(f"File size: {total_size}")
    for status in sorted(status_counts.keys()):
        if status_counts[status] > 0:
            print(f"{status}: {status_counts[status]}")


def process_line(line, total_size, status_counts):
    """Pending input of docs"""
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
    """pending input of docs for main function"""
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
