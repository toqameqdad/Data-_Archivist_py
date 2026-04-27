import sys

if len(sys.argv) != 2:
    sys.stdout.write("Usage: ft_stream_management.py <file>\n")
    exit()

file_name = sys.argv[1]

sys.stdout.write("=== Cyber Archives Recovery & Preservation ===\n")
sys.stdout.write(f"Accessing file '{file_name}'\n")

try:
    f = open(file_name, "r")
    content = f.read()
    f.close()

    sys.stdout.write("---\n")
    sys.stdout.write(content)
    sys.stdout.write("---\n")
    sys.stdout.write(f"File '{file_name}' closed.\n")

except Exception as e:
    sys.stderr.write(
        f"[STDERR] Error opening file '{file_name}': {e}\n"
    )
    exit()

new_content = ""
lines = content.split("\n")

for line in lines:
    new_content += line + "#\n"

sys.stdout.write("Transform data:\n")
sys.stdout.write("---\n")
sys.stdout.write(new_content)
sys.stdout.write("---\n")

sys.stdout.write("Enter new file name (or empty): ")
new_file = sys.stdin.readline().strip()

if new_file == "":
    sys.stdout.write("Not saving data.\n")
else:
    sys.stdout.write(f"Saving data to '{new_file}'\n")
    try:
        f = open(new_file, "w")
        f.write(new_content)
        f.close()
        sys.stdout.write(
            f"Data saved in file '{new_file}'.\n"
        )
    except Exception as e:
        sys.stderr.write(
            f"[STDERR] Error opening file '{new_file}': {e}\n"
        )
        sys.stdout.write("Data not saved.\n")
