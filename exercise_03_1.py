xhrs = input("Enter Hours ")
xr = input("Enter Rate ")
fh = float(xhrs)
fr = float(xr)
if fh > 40 :
  reg = 40 * fr
  otp = (fh - 40.0) * (fr * 1.5)
  xp = reg + otp
print("Pay:", xp)
