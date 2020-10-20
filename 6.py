a = int(input('Введите результат первого дня... '))
b = int(input('Введите желаемый результат... '))
d = 1
while a < b:
    d += 1
#    print(d)
    a = a + (a / 100 * 10)
#    print(a)
print(d)