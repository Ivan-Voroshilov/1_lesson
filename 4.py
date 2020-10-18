x = int(input('Input number... '))
max = 0
while x >= max:
    x1 = x % 10
    if x1 >= max:
        max = x1
    x //= 10
print(max)