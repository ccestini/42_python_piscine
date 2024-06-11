from os import get_terminal_size


def ft_tqdm(lst: range) -> None:
    """
    Display a progress bar while iterating through a range.

    Args:
        lst (range): The range to iterate over.

    Returns:
        None.
    """
    total = len(lst)  # this is the range ex 333
    progress = 0
    bar_length = int(get_terminal_size().columns - 40)

    for x in lst:
        progress += 1
        percentage = progress / total * 100
        slices = int(percentage * bar_length / 100)
        bar = '=' * slices + '>' + '.' * (bar_length - slices)
        print(f"\r{int(percentage):3}%|[{bar}]| {progress}/{total}",
              end='', flush=True)
        yield x
    print()


"""
to display correctly the loading bar, i could have used:
from sys import stdout
stdout.write(f"\r{int(percentage)}%|[{bar}]| {progress}/{total}")
stdout.flush()

to use print i needed to put end='' to prevent the newline default and
flush to ensure the output is immediately flushed to the terminal and
the :3 is to always to show with 3 chars (so '  1%').
"""
