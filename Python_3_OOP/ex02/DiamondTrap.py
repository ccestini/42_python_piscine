from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Representing the King."""

    def __init__(self, first_name, is_alive=True):
        """King class Constructor."""
        super().__init__(first_name, is_alive)
        # it inherits eyes and hair from Baratheon as it is first listed

    def set_eyes(self, value):
        """Method to set the eye color."""
        if not isinstance(value, str) or ' ' in value.strip():
            raise ValueError("Eye color must be a one word string")
        self.eyes = value

    def set_hairs(self, value):
        """Method to set the hair color."""
        if not isinstance(value, str) or ' ' in value.strip():
            raise ValueError("Hair color must be a one word string")
        self.hairs = value

    def get_eyes(self):
        """Method to get the eye color."""
        return self.eyes

    def get_hairs(self):
        """Method to get the hair color."""
        return self.hairs


"""
The "diamond problem" occurs in multiple inheritance when a class inherits
 from two classes that have a common base class. This can create ambiguity
 in the method resolution order (MRO), i.e., the order in which methods
 should be inherited when they are called.

To resolve this ambiguity, Python uses the C3 linearization algorithm.
 This algorithm was introduced in Python 2.3 and ensures a consistent and
 predictable MRO.

How C3 Linearization Works:
-> A class always precedes its parents.
-> The order of parent classes in the MRO respects the order in which
 they are listed in the class definition.
-> The MRO of each parent is preserved.
"""


def main():
    try:
        # Create a King
        char1 = King('Joffrey')
        print(char1.__dict__)
        print('---------')
        char1.set_eyes('blue')
        char1.set_hairs('black')
        print('After Change the Eye and Hair colors:')
        print(char1.__dict__)

    except Exception as e:
        print(f"Exception: {e}")


if __name__ == "__main__":
    main()
