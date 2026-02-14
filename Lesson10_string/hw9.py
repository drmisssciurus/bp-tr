def count_divisible_by_three(number: int) -> int:
    if type(number) != int:
        print("please enter integer")
        return -1
    if number < 0:
        print("please enter positive number")
        return -1
    if number == 0:
        return 1
    count = 0
    while number > 0:
        if not number % 10 % 3:  # 12345%10->5%3->2
            # if number%10%3==0:
            # 1234%10->4%3->1 123%10->3%3->0
            count += 1
        number //= 10
    return count


print(count_divisible_by_three(12345))
print(count_divisible_by_three(120345))
print(count_divisible_by_three(0))


def lcm(a, b):
    if a < 0 or b < 0:
        print("please enter positive number")
        return -1
    if a == 0 or b == 0:
        return min(a, b)
    res = max(a, b)  # 1000000 1000001  4 8
    step_ = res
    while res <= a * b:
        if res % a == 0 and res % b == 0:
            return res
        res += step_
    return -1


# 2 11 res=11 max_=11
# 11%2!=0->False -> res=11+11
# 22%2==0 True 22%11==0 True =>return 22

print(lcm(11, 2))
print(lcm(4, 8))
print(lcm(11, 0))
print(lcm(1_000_000, 1_000_001))


def print_stars(stars: int) -> None:
    if type(stars) != int:
        print("not integer")
        return
    if stars <= 0:
        print("please enter number>0")
        return
    while stars > 0:
        print("*", end="")
        stars -= 1
    print()


print_stars(10)
print_stars(-10)


def print_stars(stars: int) -> None:
    if type(stars) != int:
        print("not integer")
        return
    if stars <= 0:
        print("please enter number>0")
        return
    print("*" * stars)


print_stars(10)
print_stars(-10)


def factorial(number: int) -> int:
    if type(number) != int:
        return -1
    if number < 0:
        return -1
    res = 1
    while number > 0:
        res *= number
        number -= 1
    return res

print(factorial(5))
print(factorial(0))
print(factorial(-5))
print(factorial(10))

def print_stars_adv(stars:int, column:int)->None:
    if type(stars)!=int or type(column)!=int:
        print("please enter integers")
        return
    if stars <= 0 or column <= 0:
        print("please enter positive number")
        return
    count=0
    while stars>0:
        print("*",end="")
        count+=1
        if count%column==0:#1 2 3
            print()
        stars-=1
    print()

print_stars_adv(10,3)
print("=================")
print_stars_adv(10,4)
print("=================")
print_stars_adv(10,5)


def print_stars_adv(stars:int, column:int)->None:
    if type(stars)!=int or type(column)!=int:
        print("please enter integers")
        return
    if stars <= 0 or column <= 0:
        print("please enter positive number")
        return
    count=0
    while stars>count:
        print("*",end="")
        count+=1
        if count%column==0:#1 2 3
            print()
    print()

print_stars_adv(10,3)
print("=================")
print_stars_adv(10,4)
print("=================")
print_stars_adv(10,5)

def print_stars_adv(stars:int, column:int)->None:
    if type(stars)!=int or type(column)!=int:
        print("please enter integers")
        return
    if stars <= 0 or column <= 0:
        print("please enter positive number")
        return
    while stars>column:
        print("*"*column)
        stars-=column
    print("*"*stars)


print("=================")
print_stars_adv(10, 3)
print("=================")
print_stars_adv(10, 4)
print("=================")
print_stars_adv(10, 5)
