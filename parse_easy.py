
pattern = open('example.txt')

map = {
    '/': 'knit 2 together',
    '\\': 'slip',
    'o': 'yarn over',
    '-': 'purl',
    '.': 'skip',
}

lines = [line.rstrip("\n") for line in pattern]
row = 0

while row < len(lines):
    line = lines[row]
    print "Line ", row + 1
    for col, char in enumerate(line, 1):
        print "\tdo a ", map.get(char, repr(char))

    command = raw_input("> ")
    if command == "u":
        row -= 1
    else:
        row += 1
