a = int(input())
b = int(input())
n = int(input())

# a - рублей
# b - копеек
# n - количество
price_kop = a*100 + b
total_kop = price_kop * n

print(total_kop // 100,  total_kop % 100)
