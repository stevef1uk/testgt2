"""Entry point for the FizzBuzz implementation."""
from backend.fizzbuzz import fizzbuzz

def main(start: int = 1, end: int = 100) -> None:
    """Print FizzBuzz results from start to end inclusive."""
    for i in range(start, end + 1):
        print(fizzbuzz(i))

if __name__ == "__main__":
    main()
