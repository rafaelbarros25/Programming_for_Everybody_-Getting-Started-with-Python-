fname = input("Enter file name: ")
fh = open(fname)
total = 0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    ly = line.rstrip()
    ipos = ly.find("0")
    piece = (ly[ipos-1:])
    xpam = float(piece)
    total = total + xpam
    count = count + 1
avg = total/count
print("Average spam confidence:", avg)

#print (xpam)



#print (type(xpam))


# print("Average spam confidence:", total/len(piece))
