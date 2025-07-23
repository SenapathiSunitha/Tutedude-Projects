try:
    with open("sample.txt", "r") as file:
        print("Reading file content:")
        line_number = 1
        for line in file:
            print("Line " + str(line_number) + ": " + line.strip())
            line_number += 1
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
