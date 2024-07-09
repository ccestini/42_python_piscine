import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """Represents a student data."""
    name: str
    surname: str
    id: str = field(init=False)
    login: str = field(init=False)
    active: bool = field(init=False, default=True)

    def __post_init__(self):
        self.login = self.name[0] + self.surname
        self.id = generate_id()


def main():
    """Main function to test."""
    try:
        student = Student(name="Edward", surname="agle")
        print(student)

        student2 = Student(name="Edward", surname="agle")
        print(student2)

    except Exception as msg:
        print(f"An error occurred: {msg}")


if __name__ == "__main__":
    main()
