# Write a program to prompt the user for hours and rate per hour using input to compute gross pay.
# Use 35 hours and a rate of 2.75 per hour to test the program (the pay should be 96.25).
# You should use input to read a string and float() to convert the string to a number.
# Do not worry about error checking or bad user data.
# Desired Output: Pay: 96.25
h=float(input("Hours worked: "))
r=float(input("Rate per hour: "))
print("Pay: ",r*h)

