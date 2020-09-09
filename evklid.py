m = int(input())
n = int(input())
while m != n:
    if m > n:
        m = m - n
    else:
        n = n - m
print(m)
