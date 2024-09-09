#The basic outline of this problem is to read the file, look for integers using the re.findall(),
# looking for a regular expression of '[0-9]+' and then converting the extracted strings to integers and summing up the integers.
import re
fname = input("Enter file name: ")
if len(fname) < 1 : fname = "assig11.txt"
fh = open(fname)
sum=0
for line in fh:
    numbers = re.findall('[0-9]+', line)
    if not numbers:
        continue
    else:
        for number in numbers:
            print(number)
            sum += int(number)
print(sum)
