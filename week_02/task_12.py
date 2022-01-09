x1 = int(input())
y1 = int(input())

x2 = int(input())
y2 = int(input())

# определяем цвет клетки для двух шашок
isStartBlack = (x1 % 2 == 0 and y1 % 2 != 0) or (x1 % 2 != 0 and y1 % 2 == 0)
isEndBlack = (x2 % 2 == 0 and y2 % 2 != 0) or (x2 % 2 != 0 and y2 % 2 == 0)

# print(isStartBlack, isEndBlack)

if isStartBlack == isEndBlack and y2 > y1:
    # левая диагональ
    if x2 >= x1 and y2 >= x2 - x1:
        print("YES")
    # правая диагональ
    elif x1 >= x2 and y2 >= x1 - x2:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
