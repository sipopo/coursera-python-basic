a = int(input())
b = int(input())
c = int(input())

isEven = (a % 2 == 0) or (b % 2 == 0) or (c % 2 == 0)
isOdd = (a % 2 != 0) or (b % 2 != 0) or (c % 2 != 0)

if isEven and isOdd:
    print("YES")
else:
    print("NO")
