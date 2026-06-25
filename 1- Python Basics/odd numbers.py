"""Odd numbers utilities.

Provides simple functions to check for odd numbers and generate odd
numbers in a range, plus a small CLI example.
"""

from typing import Iterator, List


def is_odd(n: int) -> bool:
    """Return True if `n` is odd."""
    return n % 2 != 0


def odd_numbers_in_range(start: int, end: int) -> Iterator[int]:
    """Yield odd numbers from `start` to `end` inclusive."""
    if start > end:
        return
    for n in range(start, end + 1):
        if is_odd(n):
            yield n


def odd_list(start: int, end: int) -> List[int]:
    """Return a list of odd numbers between `start` and `end` (inclusive)."""
    return list(odd_numbers_in_range(start, end))


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Print odd numbers in a range")
    parser.add_argument("--start", type=int, default=1, help="range start (inclusive)")
    parser.add_argument("--end", type=int, default=20, help="range end (inclusive)")
    args = parser.parse_args()

    print(f"Odd numbers between {args.start} and {args.end}:")
    print(odd_list(args.start, args.end))
