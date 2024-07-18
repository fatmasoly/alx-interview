#!/usr/bin/python3
"""Log parsing module."""
import re
import sys


def extract_input(input_line):
    """Extract status code and file size from input line."""
    fp = (
        r"\s*(?P<ip>\S+)\s*",
        r"\s*\[(?P<date>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\]",
        r'\s*"(?P<request>[^"]*)"\s*',
        r"\s*(?P<status_code>\S+)",
        r"\s*(?P<file_size>\d+)(?:\s*(?P<extra_info>\S*))?",
    )

    status_code = 0
    file_size = 0

    log_fmt = "{}\\-{}{}{}{}\\s*".format(fp[0], fp[1], fp[2], fp[3], fp[4])
    resp_match = re.fullmatch(log_fmt, input_line)
    if resp_match is not None:
        status_code = resp_match.group("status_code")
        file_size = int(resp_match.group("file_size"))

    return status_code, file_size


def process_line(line, status_codes, itr_num, file_size):
    """Process a single line of input."""
    status_code, extracted_file_size = extract_input(line)

    if status_code in status_codes:
        status_codes[status_code] += 1

    itr_num += 1
    file_size += extracted_file_size

    return itr_num, file_size


def print_statistics(file_size, status_codes):
    """Print the statistics."""
    print(f"File size: {file_size}")

    non_zero_items = {key: value for key, value
                      in status_codes.items() if value != 0}

    sorted_items = sorted(non_zero_items.items(), key=lambda x: x[0])

    for key, value in sorted_items:
        print(f'{key}: {value}')


def main():
    """Main function."""
    itr_num = 0
    status_codes = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0
    }
    file_size = 0

    try:
        for line in sys.stdin:
            itr_num, file_size = process_line(line,
                                              status_codes,
                                              itr_num,
                                              file_size)

            if itr_num % 10 == 0:
                print_statistics(file_size, status_codes)

        print_statistics(file_size, status_codes)

    except KeyboardInterrupt:
        print_statistics(file_size, status_codes)
        raise


if __name__ == '__main__':
    main()
