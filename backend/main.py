if __name__ == "__main__":
    import sys
    from backend.fizzbuzz import fizzbuzz
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    print(fizzbuzz(n))
