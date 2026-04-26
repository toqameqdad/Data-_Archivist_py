import sys
import typing


def transform_data(content: str) -> str:
    lines: list[str] = content.splitlines(True)
    transformed: str = ""

    for line in lines:
        if line.endswith("\n"):
            transformed += line[:-1] + "#\n"
        else:
            transformed += line + "#"

    return transformed


def read_file(file_name: str) -> str:
    file_obj: typing.IO[str]
    content: str

    file_obj = open(file_name, "r")
    content = file_obj.read()
    file_obj.close()

    return content


def save_file(file_name: str, content: str) -> None:
    file_obj: typing.IO[str]

    file_obj = open(file_name, "w")
    file_obj.write(content)
    file_obj.close()


def main() -> None:
    content: str
    new_content: str
    new_file_name: str

    if len(sys.argv) != 2:
        print("Usage: ft_archive_creation.py <file>")
        return

    file_name: str = sys.argv[1]

    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{file_name}'")

    try:
        content = read_file(file_name)
        print("---")
        print(content, end="")
        print("---")
        print(f"File '{file_name}' closed.")
    except Exception as error:
        print(f"Error opening file '{file_name}': {error}")
        return

    new_content = transform_data(content)

    print("Transform data:")
    print("---")
    print(new_content, end="")
    print("---")

    new_file_name = input("Enter new file name (or empty): ")

    if new_file_name == "":
        print("Not saving data.")
        return

    print(f"Saving data to '{new_file_name}'")

    try:
        save_file(new_file_name, new_content)
        print(f"Data saved in file '{new_file_name}'.")
    except Exception as error:
        print(f"Error opening file '{new_file_name}': {error}")
        print("Data not saved.")


if __name__ == "__main__":
    main()
