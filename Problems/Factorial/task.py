n = int(input())
result = 1

while 100 > n > 0:
    result *= n
    n -= 1

print(result)
