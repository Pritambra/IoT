num1 = int(input("Enter number num1: "))
num2 = int(input("Enter number num2: "))
num3 = int(input("Enter number num3: "))

max = 0
if num1 > num2:
    print("num1 and num2 are equal")
    max = num1
elif num2 > num3:
    print("num2 is greater")
    max = num2
else:
    print("num3 is greater")
    max = num3
print(f"Max value = {max}")
