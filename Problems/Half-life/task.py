n = int(input())
r = int(input())
result = 0
while n > r:
    n /= 2
    result += 1
print(result * 12)
