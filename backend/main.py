def main():
    """Entry point for the fizzbuzz program."""
    from .fizzbuzz import fizzbuzz
    for i in range(1, 16):
        print(fizzbuzz(i))

if __name__ == "__main__":
    main()
