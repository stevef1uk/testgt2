def fizzbuzz(n: int) -> str:
    """
    Return FizzBuzz representation for a single integer n.
    - If n is divisible by 3 and 5, return "FizzBuzz".
    - If divisible only by 3, return "Fizz".
    - If divisible only by 5, return "Buzz".
    - Otherwise return the integer as a string.
    """
    if n % 15 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return str(n)

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        try:
            num = int(sys.argv[1])
            print(fizzbuzz(num))
        except ValueError:
            print("Invalid integer")
    else:
        print("Usage: python fizzbuzz.py <int>")
