N = int(input())

# в стуках  = 24 часа = 24 * 60 минут = 1440 минут
hours = (N % 1440) // 60
minutes = (N % 1440) % 60

print(hours, minutes)
