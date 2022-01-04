x = int(input())
y = int(input())
k = int(input())

# общее кол-во долек
total = x*y

# узнаем делиться ли отстаток долек на одну из сторон
if k % x == 0:
    divider = k // x
elif k % y == 0:
    divider = k // y
else:
    divider = -1

# print(divider)

if divider > 0:
    if k < total and ((divider*x == k) or (divider*y == k)):
        print("YES")
    else:
        print("NO")
else:
    print("NO")
