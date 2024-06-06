from sys import argv


def check_even_odd(num):
    num = int(num)
    if num % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")


def main():
    try:
        if len(argv) > 2:
            raise AssertionError("more than one argument is provided")
        if len(argv) == 2:
            argument = argv[1]
            try:
                int_argument = int(argument)
            except ValueError:
                raise AssertionError("argument is not an integer")
            check_even_odd(int_argument)
    except Exception as message:
        print(f"{type(message).__name__}: {message}")


if __name__ == "__main__":
    main()
