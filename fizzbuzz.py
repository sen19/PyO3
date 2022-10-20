x = input('Введіть 3 числа через пробіл: ')
fizz, buzz, end = map(int, x.split())

for i in range(1, end + 1):
    if i % fizz == 0 and i % buzz == 0:
        print('FB', end=' ')
    elif i % fizz == 0:
        print('F', end=' ')
    elif i % buzz == 0:
        print('B', end=' ')
    else:
        print(i, end= ' ')


    


