def factorial(num):
    result = 1
    for i in range(1, num + 1):
        result = result*i
    return result

for i in range(11):
    print(f"Factorial of {i} is {factorial(i)}")
