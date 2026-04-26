import sys
import typing


def write_stdout(message: str) -> None:
    sys.stdout.write(message)
    sys.stdout.flush()


def write_stderr(message: str) -> None:
    sys.stderr.write(message)
    sys.stderr.flush()


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


def get_user_input() -> str:
    user_input: str

    user_input = sys.stdin.readline()

    if user_input.endswith("\n"):
        user_input = user_input[:-1]

    return user_input


def main() -> None:
    content: str
    new_content: str
    new_file_name: str

    if len(sys.argv) != 2:
        write_stdout("Usage: ft_stream_management.py <file>\n")
        return

    file_name: str = sys.argv[1]

    write_stdout("=== Cyber Archives Recovery & Preservation ===\n")
    write_stdout(f"Accessing file '{file_name}'\n")

    try:
        content = read_file(file_name)
        write_stdout("---\n")
        write_stdout(content)
        write_stdout("---\n")
        write_stdout(f"File '{file_name}' closed.\n")
    except Exception as error:
        write_stderr(
            f"[STDERR] Error opening file '{file_name}': {error}\n"
        )
        return

    new_content = transform_data(content)

    write_stdout("Transform data:\n")
    write_stdout("---\n")
    write_stdout(new_content)
    write_stdout("---\n")

    write_stdout("Enter new file name (or empty): ")
    new_file_name = get_user_input()

    if new_file_name == "":
        write_stdout("Not saving data.\n")
        return

    write_stdout(f"Saving data to '{new_file_name}'\n")

    try:
        save_file(new_file_name, new_content)
        write_stdout(f"Data saved in file '{new_file_name}'.\n")
    except Exception as error:
        write_stderr(
            f"[STDERR] Error opening file '{new_file_name}': {error}\n"
        )
        write_stdout("Data not saved.\n")


if __name__ == "__main__":
    main()
