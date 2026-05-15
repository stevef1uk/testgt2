#!/usr/bin/env python3
from fizzbuzz import fizzbuzz

def main():
    import sys
    if len(sys.argv) != 2:
        print("Usage: main.py <number>")
        return
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("Invalid integer")
        return
    print(fizzbuzz(n))

if __name__ == "__main__":
    main()
