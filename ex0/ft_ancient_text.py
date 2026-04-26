import sys
import typing


def main() -> None:
    file_obj: typing.IO[str]

    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    file_name: str = sys.argv[1]

    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{file_name}'")

    try:
        file_obj = open(file_name, "r")
        print("---")
        print(file_obj.read(), end="")
        print("---")
        file_obj.close()
        print(f"File '{file_name}' closed.")
    except Exception as error:
        print(f"Error opening file '{file_name}': {error}")


if __name__ == "__main__":
    main()
