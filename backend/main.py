def main():
    """Entry point for the fizzbuzz program."""
    import sys
    from .fizzbuzz import fizzbuzz

    # If a number is provided as command-line argument, use it; else default to 1..100
    if len(sys.argv) > 1:
        try:
            n = int(sys.argv[1])
            print(fizzbuzz(n))
        except ValueError:
            print("Please provide an integer", file=sys.stderr)
            sys.exit(1)
    else:
        for i in range(1, 101):
            print(fizzbuzz(i))

if __name__ == "__main__":
    main()
