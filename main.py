from app.calculator import add, multiply
from app.greetings import greet


def main() -> None:
    name = "Alex"
    print(greet(name))
    print(f"2 + 3 = {add(2, 3)}")
    print(f"4 * 5 = {multiply(4, 5)}")


if __name__ == "__main__":
    main()
