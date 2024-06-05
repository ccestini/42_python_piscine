from sys import argv
from string import punctuation
from ft_filter import ft_filter

def main():
    """
    Main function to handle command-line arguments and filter words based on length.
    """
    try:

        if len(argv) != 3:
            raise AssertionError(": the arguments are bad")

        try:
            S = str(argv[1])
            N = int(argv[2])
        except ValueError:
            raise AssertionError(": the arguments are bad")
        
        # Check if the string contains any special characters (excluding normal space)
        if any(char in punctuation or (char != ' ' and not char.isprintable()) for char in S):
            raise AssertionError(": the arguments are bad")
        
        # Check if N is not negative number
        if N < 0:
            raise AssertionError(": the arguments are bad")

        # Split the string into a list of words
        words = S.split()

        # Use ft_filter with a lambda function to filter words longer than N
        # List comprehension is like a compact loop that goes through each item in a list,
        # does something with it, and then puts the result into a new list
        # Lambda is a mini-function that you define inline, without giving it a name
        filtered_words = [word for word in ft_filter(lambda word: len(word) > N, words)]

        print(filtered_words)
    
    except Exception as message:
        print(f"{type(message).__name__}{message}")

if __name__ == "__main__":
    main()
