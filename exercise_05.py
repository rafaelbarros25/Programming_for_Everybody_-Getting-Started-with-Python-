largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        num = float(num)
    except:
        print("Invalid input")
        continue
    if largest is None:
        largest = num
    if smallest is None:
        smallest = num
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num
print("Maximum is", int(largest))
print("Minimum is", smallest)
