fname = input("Enter fine name: ")
fh = open(fname)
abclist=[]
for line in fh:
    words = line.split()                # Splits line into array of words
    for word in words:
        if word in abclist:
            continue                    # Discards duplicates
        abclist.append(word)            # Updates the list
print(sorted(abclist))
