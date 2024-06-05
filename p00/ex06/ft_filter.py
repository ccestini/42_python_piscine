"""    This function mimics the built-in filter function. """


def ft_filter(function, iterable):
    """
ft_filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true.
"""
    if function is None:
        return (item for item in iterable if item)
    else:
        return (item for item in iterable if function(item))


def main():
    """
    Main function to test ft_filter against the built-in filter function.
    """
    try:
        # Test case 1: Filtering names with lower initial char
        names = ["Lili", "Sosso", "lalau", "me", "Other"]
        filtered_names_builtin = list(filter(str.islower, names))
        filtered_names_custom = list(ft_filter(str.islower, names))
        print(f"return B: {filtered_names_builtin}")
        print(f"return C: {filtered_names_custom}")
        assert filtered_names_builtin == filtered_names_custom, \
            "Test case 1 failed"
        print("***Test case 1 passed***\n")

        # Test case 2: Filtering even numbers
        numbers = [1, 2, 3, 4, 5, 6]
        filtered_numbers_builtin = list(filter(lambda x: x % 2 == 0, numbers))
        filtered_numbers_custom = list(ft_filter(lambda x: x % 2 == 0, numbers))
        print(f"return B: {filtered_numbers_builtin}")
        print(f"return C: {filtered_numbers_custom}")
        assert filtered_numbers_builtin == filtered_numbers_custom, \
            "Test case 2 failed"
        print("***Test case 2 passed***")
        print(f"\n***built-in docstring:***\n{filter.__doc__}\n***")
        print(f"\n***my docstring:***{ft_filter.__doc__}***\n")
  
    except Exception as message:
        print(f"{type(message).__name__}{message}")

if __name__ == "__main__":
    main()
