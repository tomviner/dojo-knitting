
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
    count, last = 0, None
    for col, char in enumerate(line, 1):
        if last is None:
            count = 1
        else:
            if last != char:
                print '\tdo a', map.get(last, repr(last)), count
                count = 1
            else:
                count += 1
        last = char

    print '\tdo a', map.get(char, repr(char)), ' x', count
