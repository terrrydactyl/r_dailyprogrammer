import sys

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "No name given"
        exit()

    name = sys.argv[1].capitalize()[:-1]

    if name[0] in 'AEIOU':
        name = name.lower()
        bname = 'B' + name
        fname = 'F' + name
        mname = 'M' + name
        name = name.capitalize()

    else:
        bname = 'B' + name[1:]
        fname = 'F' + name[1:]
        mname = 'M' + name[1:]

    song = """
        %s, %s bo %s,
        Bonana fanna fo %s,
        Fee fy mo %s,
        %s!
        """ % (name, name, bname, fname, mname, name)
    print song
