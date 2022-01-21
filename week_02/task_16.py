a, b, c = int(input()), int(input()), int(input())

count = 0

if a == b:
    if a == c:
        count += 1
    else:
        count += 2

if a == c:
    if b == c:
        count += 1
    else:
        count += 2

if b == c:
    if a == c:
        count += 1
    else:
        count += 2

print(count)
