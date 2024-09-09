xhrs = input("Enter Hours ")
xr = input("Enter Rate ")
h = float(xhrs)
r = float(xr)
def computepay(h):
    if h <= 40:
        return r*h
    elif h > 40 :
        reg = 40 * r
        otp = (h - 40.0) * (r * 1.5)
        xp = reg + otp
        return xp
print ("Pay",computepay(h))
