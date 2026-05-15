def fizzbuzz(n: int) -> str:
    """Return 'Fizz' if n divisible by 3, 'Buzz' if divisible by 5,
    'FizzBuzz' if divisible by both, else empty string."""
    result = ""
    if n % 3 == 0:
        result += "Fizz"
    if n % 5 == 0:
        result += "Buzz"
    return result
