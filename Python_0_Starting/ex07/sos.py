from sys import argv


def encode_morse(text):
    """
    Encode the input text into Morse code.

    Args:
        text (str): The input text to be encoded.

    Returns:
        str: The encoded Morse code string.
    """

    encoded = ""

    # Dictionary to store Morse code representations
    NESTED_MORSE = {
        " ": "/",
        "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".",
        "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---",
        "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---",
        "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
        "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--",
        "Z": "--..", "0": "-----", "1": ".----", "2": "..---", "3": "...--",
        "4": "....-", "5": ".....", "6": "-....", "7": "--...", "8": "---..",
        "9": "----.",
        }

    for char in text.upper():
        if char in NESTED_MORSE:
            encoded += NESTED_MORSE[char] + " "
    return encoded.strip()


def main():
    try:

        if len(argv) != 2:
            raise AssertionError(": the arguments are bad")

        input_text = str(argv[1])

        if not input_text:  # check if empty
            raise AssertionError(": the arguments are bad")

        # check if only alpha, numbers and classic space only
        if not all(char.isalnum() or char.isspace() for char in input_text):
            raise AssertionError(": the arguments are bad")

        morse_code = encode_morse(input_text)
        print(morse_code)

    except Exception as message:
        print(f"{type(message).__name__}{message}")


if __name__ == "__main__":
    main()
