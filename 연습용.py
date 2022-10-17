a = []

for i in range(5):
    a.append(int(input()))
    sorted(a[i])

print(int(sum(a)/5))
print(a[2])