x = int(input('Input seconds... '))
h = x // 3600
m = (x % 3600) // 60
s = (x % 3600) % 60
print(h, ':', m, ':', s)