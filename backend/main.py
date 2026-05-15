#!/usr/bin/env python3
from fizzbuzz import fizzbuzz

def main():
    for i in range(1, 101):
        fb = fizzbuzz(i)
        print(fb if fb else i)

if __name__ == "__main__":
    main()
