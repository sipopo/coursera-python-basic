# первая квартира в подъезде
x = int(input())
# последняя квартира в подъезде
y = int(input())

# общее кол-во квартир в подъезде
flatsInEntrance = (y - x) + 1

if (y % flatsInEntrance) == 0:
    print("YES")
else:
    print("NO")
