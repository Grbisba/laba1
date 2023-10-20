a, b, c = map(int, input().split()) #Не использовать если не знаешь
f = True
while f:

    if a == 0:
        x1 = x2 = (-b)/c
        print("x1 = x2 =", x1)
        f = False
        break

    elif b == 0:
        if (-c)/a < 0:
            print("Корней нет")
            f = False
            break
        else:
            x1 = ( (-c) / a) ** 0.5
            x2 = -( ((-c) / a) ** 0.5)
            print("x1 = ", x1)
            print("x2 = ", x2)
            f = False
            break

    elif c == 0:
        x1 = 0
        x2 = (-b)/a
        print("x1 = ", x1)
        print("x2 = ", x2)
        f = False
        break

    else:

        d = b**2 - 4 * a * c

    if d == 0:
        x1 = x2 = -b/2*a
        print("x1 = ", x1)
        print("x2 = ", x2)
        f = False
        break

    if d > 0:
        x1 = (-b + (d**(0.5)))/(2*a)
        x2 = (-b - (d**(0.5)))/(2*a)
        print("x1 = ", x1)
        print("x2 = ", x2)
        f = False
        break

    if d < 0:
        print("Корней нет")
        f = False
        break