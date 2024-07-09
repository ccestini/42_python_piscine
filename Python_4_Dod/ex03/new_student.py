import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """Represents student data."""
    name: str
    surname: str
    id: str = field(init=False)
    login: str = field(init=False)
    active: bool = field(init=False, default=True)

    def __post_init__(self):
        # Validate name and surname
        if not self.name or not self.surname:
            raise ValueError("Name and surname cannot be empty.")
        if not self.name.isalpha() or not self.surname.isalpha():
            raise ValueError("Name/Surname accepts only alphabetic chars.")

        self.login = self.name.upper()[0] + self.surname.lower()
        self.id = generate_id()


def main():
    """Main function to test."""
    try:
        student = Student(name="Edward", surname="agle")
        print(student)
        print("---")
        student2 = Student(name="Edward", surname="agle", id="toto")
        print(student2)

    except Exception as msg:
        print(f"An error occurred: {msg}")


if __name__ == "__main__":
    main()
