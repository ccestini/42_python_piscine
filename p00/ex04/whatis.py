from sys import argv

def check_even_odd(num):
    num = int(num)
    if num % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")

def main():
    if len(argv) > 2:
        print("AssertionError: more than one argument is provided") 
    if len(argv) == 2:
        argument = argv[1]
        try:
            int_argument = int(argument)
        except ValueError:
            print("AssertionError: argument is not an integer")
            return
        check_even_odd(argument)

if __name__ == "__main__":
    main()
