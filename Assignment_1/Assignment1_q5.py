marks1 = int(input("Enter marks1: "))
marks2 = int(input("Enter marks2: "))
marks3 = int(input("Enter marks3: "))

avg = (marks1 + marks2 + marks3)/3
print(f" avg = {(marks1 + marks2+ marks3)/3}")

if avg>=90 and avg<=100:
    print("A grade")
    
elif avg>=80 and avg<=89:
    print("B grade")

elif avg>=70 and avg<=79:
    print("C grade")

elif avg>=60 and avg<=69:
    print("D grade")

else:
    print("F grade")

