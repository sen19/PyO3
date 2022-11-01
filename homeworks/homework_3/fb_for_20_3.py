#Написать fizzbuzz для 20 троек чисел, которые записаны в файл. Читаете из файла первую строку, берете из нее числа, считаете для них fizzbuzz, выводите, повторяете со всеми остальными строками.
numbers = []
with open('3.txt', 'r') as f:
    
    items = f.read().split('\n')
   
    for j in items:
        if j == '':
            continue
        
        numbers.append([int(n) for n in j.split(',')])

for nums in numbers:
    for num in range(1, nums[2]+1):
        if num % nums[0] == 0 and num % nums[1] == 0:
            print('FB', end = ' ')
        elif num % nums[0] == 0:
            print('F', end = ' ')
        elif num % nums[1] == 0:
            print('B', end = ' ')
        else:
            print(num, end = ' ')

#файл 3.txt повинен знаходитись в тій самій папці що й fb_for_20_3.py


