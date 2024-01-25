#!/usr/bin/python3
"""Log parsing script that reads stdin line by line and computes metrics"""

import sys


def initialize_stats():
    """Initialize statistics"""
    results = {"200": 0, "301": 0, "400": 0,
               "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}

    return results


def process_lines(line, stats, total_size, line_count):
    """Process a single log line and update statistics"""
    try:
        parts = line.split()
        status_code = parts[-2]
        file_size = int(parts[-1])

        if status_code in stats:
            stats[status_code] += 1

        total_size += file_size
        line_count += 1

        if line_count % 10 == 0:
            print_stats(stats, total_size)

    except (IndexError, ValueError):
        pass

    return total_size, line_count


def print_stats(stats, total_size):
    """Print statistics"""
    print(f"File size: {total_size}")
    for code, count in sorted(stats.items()):
        if count:
            print(f"{code}: {count}")


if __name__ == "__main__":
    total_size, line_count = 0, 0
    statistics = initialize_stats()

    try:
        for line in sys.stdin:
            total_size, line_count = process_lines(line.strip(), statistics,
                                                   total_size, line_count)

        print_stats(statistics, total_size)

    except KeyboardInterrupt:
        print_stats(statistics, total_size)
        raise
