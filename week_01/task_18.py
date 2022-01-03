secs = int(input())

h = (secs // 3600) % 24
mm = (secs // 60) % 60
ss = secs % 60

# h1 = str(h // 10)
# h2 = str(h % 10)

m1 = str(mm // 10)
m2 = str(mm % 10)

s1 = str(ss // 10)
s2 = str(ss % 10)

print(h, m1 + m2, s1 + s2, sep=":")
