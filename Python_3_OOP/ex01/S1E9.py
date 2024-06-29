"""The ABC module is used to define abstract base classes in Python."""
from abc import ABC, abstractmethod


class Character(ABC):
    """Docstring for Abstract Class."""

    def __init__(self, first_name, is_alive=True):
        """Abstract class Constructor."""

        if not isinstance(first_name, str) or ' ' in first_name.strip():
            raise ValueError("first_name must be a string, with one word")
        if not isinstance(is_alive, bool):
            raise ValueError("is_alive must be a boolean (True or False)")
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """Abstract method to change the health state of the character."""
        self.is_alive = False


class Stark(Character):
    """Docstring for Stark Class."""

    def __init__(self, first_name, is_alive=True):
        """Stark Class Constructor."""
        super().__init__(first_name, is_alive)

    def die(self):
        """Method to change the state of Stark character to dead."""
        super().die()


def main():
    try:
        stark_character = Stark('Arya')
        print(stark_character.first_name)
        print(stark_character.is_alive)
        stark_character.die()
        print(stark_character.is_alive)
    except Exception as message:
        print(f"{type(message).__name__}: {message}")


if __name__ == "__main__":
    main()
