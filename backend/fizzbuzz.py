def fizzbuzz(n: int) -> str:
    """Return FizzBuzz string for integer n.

    - If n is divisible by 3 and 5, return 'FizzBuzz'.
    - If only divisible by 3, return 'Fizz'.
    - If only divisible by 5, return 'Buzz'.
    - Otherwise return the decimal representation of n.
    """
    if n % 15 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return str(n)
