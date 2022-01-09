x1 = int(input())
y1 = int(input())

x2 = int(input())
y2 = int(input())

isXsTheSame = (x1 > 0 and x2 > 0) or (x1 < 0 and x2 < 0)
isYsTheSame = (y1 > 0 and y2 > 0) or (y1 < 0 and y2 < 0)

if isXsTheSame and isYsTheSame:
    print("YES")
else:
    print("NO")
