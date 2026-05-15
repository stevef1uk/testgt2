def fizzbuzz(n: int) -> str:
    """Return 'Fizz' if n divisible by 3, 'Buzz' if divisible by 5,
    'FizzBuzz' if divisible by both, else the number as string."""
    if n % 15 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return str(n)
