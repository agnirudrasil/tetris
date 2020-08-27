n = int(input("Enter number of terms of the series to be displayed: "))


def fibonacci(_n):
    if _n <= 1:
        return _n
    else:
        return fibonacci(_n - 1) + fibonacci(_n - 2)


for i in range(n):
    print(fibonacci(i), end=", ")
