import re

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
    res = re.findall(r'((.)\2*)', line)
    for runs in res:
        run = runs[0]
        n = len(run)
        char = run[0]
        print '\tdo', map.get(char, repr(char)),
        if n > 1:
            print 'x', n
        else:
            print

    # for char in line:
    #     print '\tdo a', map.get(char, repr(char))
