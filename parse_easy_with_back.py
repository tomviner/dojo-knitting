import os
from parse_with_regex import parse_line

pattern = open('example.txt')

map = {
    '/': 'knit 2 together',
    '\\': 'slip',
    'o': 'yarn over',
    '-': 'purl',
    '.': 'skip',
}

lines = [line.rstrip("\n") for line in pattern]
if os.path.exists(".save"):
    with open(".save") as save:
        row = int(save.read())
else:
    row = 0

print("u to go up, x to save progress and exit")
while row < len(lines):
    line = lines[row]
    print "Line ", row + 1
    parse_line(line)

    command = raw_input("> ")
    if command == "u":
        if row == 0:
            print("You're at the start!")
        else:
            row -= 1
    elif command == "x":
        with open(".save", "w+") as save:
            save.write(str(row))
        break
    else:
        row += 1
