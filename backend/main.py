from fizzbuzz import fizzbuzz
if __name__ == "__main__":
    import sys
    for arg in sys.argv[1:]:
        print(fizzbuzz(int(arg)))
