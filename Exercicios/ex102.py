def fatorial(num, show = False):
    result = num
    num2 = num
    while num2 != 0:
        if show:
            if num2 > 1:
                print(num2, end = " x ")
            else:
                print(num2, end = " = ")

        if num2 == 1:
            num2 = 0
        else:
            num2 -= 1
            result *= num2

    return result

print(fatorial(5, True))
