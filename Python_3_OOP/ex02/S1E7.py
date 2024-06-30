from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""

    def __init__(self, first_name, is_alive=True):
        """Baratheon class Constructor."""
        super().__init__(first_name, is_alive)
        self.family_name = 'Baratheon'
        self.eyes = 'brown'
        self.hairs = 'dark'

    def die(self):
        """Method to change Baratheon to dead."""
        super().die()  # inherits from parent

    def __str__(self):
        """Informal string representation of an object aimed at the user"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """Oficial str representation of an object aimed at the programmer"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"


class Lannister(Character):
    """Representing the Lannister family."""

    def __init__(self, first_name, is_alive=True):
        """Lannister class Constructor."""
        super().__init__(first_name, is_alive)
        self.family_name = 'Lannister'
        self.eyes = 'blue'
        self.hairs = 'light'

    def die(self):
        """Method to change Lannister to dead."""
        super().die()

    def __str__(self):
        """User-friendly string representation of an object"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """Developer-focused string representation of an object"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    @classmethod  # used here as a alternative constructor
    def create_lannister(cls, first_name, is_alive=True):
        """Class method to create Lannister character"""
        return cls(first_name, is_alive)


def main():
    try:
        # Create Baratheon character
        char1 = Baratheon('Robert')
        print(f'Baratheon __str__ {char1}')
        print(f'Baratheon __repr__ {repr(char1)}')
        char1.die()
        print(f"Character: {char1.first_name} {char1.family_name}, "
              f"Alive: {char1.is_alive}")
        print('---------')

        # Create Lannister character
        char2 = Lannister("Joffrey")
        print(f"Lannister __str__ {char2}")
        print(f"Character: {char2.first_name} {char2.family_name}, "
              f"Alive: {char2.is_alive}")
        print('---------')

        # Create Lannister character using class method
        char3 = Lannister.create_lannister("Cersei")
        print(f"Character: {char3.first_name} {char3.family_name}, "
              f"Alive: {char3.is_alive}")

    except Exception as e:
        print(f"Exception: {e}")


if __name__ == "__main__":
    main()
