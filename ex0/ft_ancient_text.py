import sys


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    file_name = sys.argv[1]

    print("=== Cyber Archives Recovery ===")
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


if __name__ == "__main__":
    main()
