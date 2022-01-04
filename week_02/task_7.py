x1 = int(input())
y1 = int(input())

x2 = int(input())
y2 = int(input())

# расстояние между клетками четное
isEvenX = (x1-x2) % 2 == 0
isEvenY = (y1-y2) % 2 == 0

# print(isEvenX, isEvenY)

if (isEvenX and isEvenY):
    print("YES")
elif not isEvenX and not isEvenY:
    print("YES")
else:
    print("NO")
