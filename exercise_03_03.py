score = input("Enter Score: ")
grade = float(score)
if grade > 1.0 :
  print("Please enter a value between 0.0 and 1.0")
elif grade >=0.9 :
    print("Grade A")
elif grade >=0.8 :
    print("Grade B")
elif grade >=0.7 :
    print("Grade C")
elif grade >=0.6 :
    print("Grade D")
elif grade <=0.6 :
    print("Grade F")
