lower_limit = int(input("Lower Limit: "))
upper_limit = int(input("Upper Limit: "))


def sum_odd(l_limit, u_limit):
    _sum = 0
    for i in range(l_limit, u_limit):
        if i % 2 == 1:
            _sum += i
    print(_sum)


def sum_even(l_limit, u_limit):
    _sum = 0
    for i in range(l_limit, u_limit):
        if i % 2 == 0:
            print(i)
            _sum += i
    print(_sum)


sum_even(lower_limit, upper_limit)
sum_odd(lower_limit, upper_limit)
