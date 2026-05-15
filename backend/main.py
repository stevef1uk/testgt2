import sys
from .fizzbuzz import fizzbuzz

def main():
    if len(sys.argv) != 2:
        print("Usage: python -m backend <integer>")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("Argument must be an integer.")
        sys.exit(1)
    print(fizzbuzz(n))

if __name__ == "__main__":
    main()
