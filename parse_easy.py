
pattern = open('example.txt')

map = {
    '/': 'knit 2 together',
    '\\': 'slip',
    'o': 'yarn over',
    '-': 'purl',
    '.': 'skip',
}

for row, line in enumerate(pattern, 1):
    line = line[:-1]
    print 'Line', row
    for col, char in enumerate(line, 1):
        print '\tdo a', map.get(char, repr(char))

