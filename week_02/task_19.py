n = int(input())

i = 0
square = 0

while square <= n:
    i += 1
    square = i**2
    if square <= n:
        print(square, end=" ")
