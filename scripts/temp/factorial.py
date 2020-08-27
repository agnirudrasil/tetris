n = int(input("Enter a number: "))

factorial = 1

for i in range(1, n + 1):
    factorial *= i

print(f"Factorial of {n} is {factorial}")
