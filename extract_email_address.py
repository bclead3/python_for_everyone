i_counter = 0
fname = input("Enter file name:")
fh = open(fname)
for line in fh:
    if not line.startswith('From '): continue
    words = line.split()
    email = words[1]
    i_counter += 1
    print(email)

print('There were {} lines in the file with From as the first word'.format(i_counter))