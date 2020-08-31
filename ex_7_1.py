
fname = input("Enter file name:")
handle = open(fname)

for line in handle:
    new_line = line.rstrip()
    print(new_line.upper())
