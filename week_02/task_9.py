n = int(input())

last_digit = n % 10
#
if (n > 10 and n < 20) or last_digit == 0:
    print(n, "korov")
elif last_digit >= 5 and last_digit <= 9:
    print(n, "korov")
elif last_digit == 1:
    print(n, "korova")
else:
    print(n, "korovy")
