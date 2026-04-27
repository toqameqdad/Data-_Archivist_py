import sys


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_archive_creation.py <file>")
        return

    file_name = sys.argv[1]

    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{file_name}'")

    try:
        f = open(file_name, "r")
        content = f.read()
        f.close()

        print("---")
        print(content, end="")
        print("---")
        print(f"File '{file_name}' closed.")
    except Exception as e:
        print(f"Error opening file '{file_name}': {e}")
        return

    new_content = ""
    lines = content.splitlines(True)

    for line in lines:
        if line.endswith("\n"):
            new_content += line[:-1] + "#\n"
        else:
            new_content += line + "#"

    print("Transform data:")
    print("---")
    print(new_content, end="")
    print("---")

    new_file = input("Enter new file name (or empty): ")

    if new_file == "":
        print("Not saving data.")
        return

    print(f"Saving data to '{new_file}'")

    try:
        f = open(new_file, "w")
        f.write(new_content)
        f.close()
        print(f"Data saved in file '{new_file}'.")
    except Exception as e:
        print(f"Error opening file '{new_file}': {e}")
        print("Data not saved.")


if __name__ == "__main__":
    main()
