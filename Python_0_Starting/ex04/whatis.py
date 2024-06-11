from sys import argv


try:
    if len(argv) > 2:
        raise AssertionError("more than one argument is provided")
    if len(argv) == 2:
        argument = argv[1]
        try:
            int_argument = int(argument)
        except ValueError:
            raise AssertionError("argument is not an integer")

        num = int(int_argument)
        if num % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")

except Exception as message:
    print(f"{type(message).__name__}: {message}")
