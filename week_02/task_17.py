a, b, c = int(input()), int(input()), int(input())
d, e = int(input()), int(input())

# de = d*e
if (d >= a) or (d >= b) or (d >= c):
    if (e >= a) or (e >= b) or (e >= c):
        print("YES")
    else:
        print("NO")
else:
    print("NO")
