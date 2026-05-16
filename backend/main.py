#!/usr/bin/env python3
import sys
from .fizzbuzz import fizzbuzz

def main(args=None):
    if args is None:
        args = sys.argv[1:]
    if not args:
        print("Usage: main.py <n>")
        return 1
    try:
        n = int(args[0])
    except ValueError:
        print("Invalid integer")
        return 1
    print(fizzbuzz(n))
    return 0

if __name__ == "__main__":
    sys.exit(main())

# Added runner entry point for bead te-4kj
