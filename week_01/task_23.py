A = int(input())
B = int(input())

sum = (A + B)
print((A%B)//A)
print((B%A)//B)
print( (A//B)*A )

print(sum - ((A%B)//A)*A - ((B%A)//B)*B)

# not works
