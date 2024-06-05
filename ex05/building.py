from sys import argv


def count_chars(text):
    """
    Count upper-case, lower-case, punctuation, digits, and spaces in the text.

    Args:
        text (str): The input text to count characters in.

    Returns:
        dict: A dictionary containing counts of different types of characters.
    """
    counts = {
        'upper': 0,
        'lower': 0,
        'punctuation': 0,
        'digits': 0,
        'spaces': 0
    }

    for char in text:
        if char.isupper():
            counts['upper'] += 1
        elif char.islower():
            counts['lower'] += 1
        elif char.isdigit():
            counts['digits'] += 1
        elif char.isspace():
            counts['spaces'] += 1
        else:
            counts['punctuation'] += 1

    return counts


def main():
    try:
        if len(argv) == 1:
            while True:
                text = input("What is the text to count?\n")
                if text:
                    break
        elif len(argv) == 2:
            text = argv[1]
        else:
            print("AssertionError: more than one argument is provided")
            return

        if not text:
            text = input("What is the text to count?\n")

        counts = count_chars(text)

        total_characters = sum(counts.values())
        print(f"The text contains {total_characters} characters:")
        print(f"{counts['upper']} upper letters")
        print(f"{counts['lower']} lower letters")
        print(f"{counts['punctuation']} punctuation marks")
        print(f"{counts['spaces']} spaces")
        print(f"{counts['digits']} digits")
    
    except Exception as message:
        print(f"{type(message).__name__}{message}")


if __name__ == "__main__":
    main()
