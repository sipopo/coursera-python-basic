n = int(input())

p3 = n % 10
p2 = (n // 10) % 10
p1 = n // 100

print(p1 + p2 + p3)
