from sys import argv
from ft_filter import ft_filter

def main():
    """
    Main function to handle command-line arguments and filter words based on length.
    """
    if len(argv) != 3:
        print("AssertionError: the arguments are bad")
        return

    try:
        S = str(argv[1])
        N = int(argv[2])
    except ValueError:
        print("AssertionError: the arguments are bad")
        return

    # Split the string into words
    words = S.split()

    # Use ft_filter with a lambda function to filter words longer than N
    filtered_words = [word for word in ft_filter(lambda word: len(word) > N, words)]

    print(filtered_words)

if __name__ == "__main__":
    main()
