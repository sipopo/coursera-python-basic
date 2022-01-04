x1 = int(input())
y1 = int(input())

x2 = int(input())
y2 = int(input())

# узнаем максимум для Y и вычисляем шаг
if y1 >= y2:
    delta_Y = y1 - y2
else:
    delta_Y = y2 - y1

# узнаем максимум для X и вычисяем шаг
if x1 >= x2:
    delta_X = x1 - x2
else:
    delta_X = x2 - x1

# проверяем
if delta_X == 1 and delta_Y == 1:
    print("YES")
elif delta_X == 1 and delta_Y == 0:
    print("YES")
elif delta_X == 0 and delta_Y == 1:
    print("YES")
else:
    print("NO")
