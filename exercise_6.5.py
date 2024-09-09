# Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below.
# Convert the extracted value to a floating point number and print it out.
# output: 0.8475
text = "X-DSPAM-Confidence:    0.8475"
ipos = text.find("0")
piece = text[ipos-1:]
value = float(piece)
print(value)