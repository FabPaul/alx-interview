#!/usr/bin/python3
""" Log parsin script that reads stdin line by line and computes metrics"""

import sys


if __name__ == '__main__':
    total_size, line_count = 0, 0
    codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    stats = {code: 0 for code in codes}

    def print_stats(stats: dict, total_size: int) -> None:
        """Print statistics"""
        print(f"File size: {total_size}")
        for code, count in sorted(stats.items()):
            if count:
                print(f"{code}: {count}")

    try:
        for line in sys.stdin:
            line_count += 1
            data = line.split()

            try:
                status_code = data[-2]
                if status_code in stats:
                    stats[status_code] += 1
            except (IndexError, ValueError):
                pass

            try:
                total_size += int(data[-1])
            except (IndexError, ValueError):
                pass

            if line_count % 10 == 0:
                print_stats(stats, total_size)
        print_stats(stats, total_size)
    except KeyboardInterrupt:
        print_stats(stats, total_size)
        raise
