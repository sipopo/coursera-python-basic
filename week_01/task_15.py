import time


n = int(input())

# следующее четное
start_time = time.time()
for i in range(1000000):
    # answer = n + (n % 2) + ((n + 1) % 2 * 2)
    answer = 2*(n//2 + 1)

print(answer)
print("--- %s seconds ---" % (time.time() - start_time))
# print(n + (n % 2) + ((n + 1) % 2 * 2))
# print(2*(n//2 + 1))
