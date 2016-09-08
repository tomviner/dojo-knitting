"""
Human to computer knitt-o-mattic
"""
def to_symbol(s):
    if s.lower().startswith('m'):
        return s
    if s.lower() == 'rs':
        return ''
    if s.lower().startswith('k'):
        if len(s) == 1:
            return '.'
        try:
            int(s[1])
            return '.' * int(s[1])
        except ValueError:
            print s
            raise
        except IndexError:
            print s
            raise
    try:
        return s
    except ValueError:
        pass

    if s.lower() == 'sts':
        return "\\"
    if s.lower() == 'p':
        return '-'

    return s


def main():

    parts = {

    }



    with open('bird.knitting.pattern.txt', 'r') as f:
        partname = ''
        for line in f:
            if line.strip()== '':
                continue

            words = line.split(' ')
            if len(words) == 1:
                parts[words[0]] = []
                partname = words[0]
                continue
            try:
                int(words[0][0])
                # Strip nonsense
                row = words[1:]
                row = [i.strip() for i in row]
                row = [i.replace(',', '') for i in row]
                row = [i.replace('.', '') for i in row]
                row = [i.replace('(', '') for i in row]
                row = [i.replace(')', '') for i in row]
                row = [i for i in row if i != 'row']

                # To pattern language
                print row
                row = [to_symbol(i) + ' ' for i in row]


                parts[partname].append(row)

            except ValueError:
                continue

    for k in parts:
        print k
        for r in parts[k]:
            print "".join(r)


if __name__ == '__main__':
    main()
