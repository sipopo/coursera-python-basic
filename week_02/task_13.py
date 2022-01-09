a = int(input())
b = int(input())
c = int(input())

# Вычесляем гиппотинузу
if a >= b and a >= c:
    side_max = a
    side_1 = b
    side_2 = c
elif b >= a and b >= c:
    side_max = b
    side_1 = a
    side_2 = c
elif c >= a and c >= b:
    side_max = c
    side_1 = a
    side_2 = b

# print(side_max, side_1, side_2)

check_1 = (a + c) <= b
check_2 = (a + b) <= c
check_3 = (b + c) <= a

if check_1 or check_2 or check_3:
    print('impossible')
elif side_max**2 == (side_1**2 + side_2**2):
    print('rectangular')
elif side_max**2 < (side_1**2 + side_2**2):
    print('acute')
elif side_max**2 > (side_1**2 + side_2**2):
    print('obtuse')
