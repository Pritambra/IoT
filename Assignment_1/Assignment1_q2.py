number = int(input("Enter a number: "))


thousands = number // 1000
hundreds = (number % 1000) // 100
tens = (number % 100) // 10
ones = number % 10

print("Face value of each digit:", thousands, hundreds, tens, ones)

print(f"Place value of each digit: {number} = {thousands}000 + {hundreds}00 + {tens}0 + {ones}")

reversed_number = ones * 1000 + tens * 100 + hundreds * 10 + thousands
print("Number in reverse order:", reversed_number)
