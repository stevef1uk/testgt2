def fizzbuzz(n: int) -> str:
    """Return FizzBuzz string for a given integer.

    - Multiples of 3 return "Fizz"
    - Multiples of 5 return "Buzz"
    - Multiples of both 3 and 5 return "FizzBuzz"
    - Otherwise return the integer as a string
    """
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return str(n)
