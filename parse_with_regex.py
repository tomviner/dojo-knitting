import re

pattern = open('example.txt')

map = {
    '/': 'knit 2 together',
    '\\': 'slip',
    'o': 'yarn over',
    '-': 'purl',
    '.': 'skip',
}


def parse_line(line):
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
