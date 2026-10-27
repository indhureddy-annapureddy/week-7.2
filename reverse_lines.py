# Reverse each line of a file, processing lines from last to first.

file_name = "example.txt"

try:
    with open(file_name, "r", encoding="utf-8") as file:
        lines = file.readlines()

    for line in reversed(lines):
        print(line.rstrip("\n\r")[::-1])

except FileNotFoundError:
    print(f"Error: The file '{file_name}' was not found.")
except OSError as error:
    print(f"Error reading the file: {error}")
