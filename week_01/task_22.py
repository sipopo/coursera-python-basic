num = int(input())

d1 = str(num // 1000)
d2 = str(num // 100 % 10)
d3 = str(num // 10 % 10)
d4 = str(num % 10)

num1 = d1+d2
num2 = d4+d3

print((int(num1) - int(num2)) + 1)
