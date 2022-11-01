#Разбираемся, что делает функция zip, и пробуем написать свой собственный zip.


lst1 = [0, 1, 2, 3, 4, 5]
lst2 = ['zero', 'one', 'two', 'three', 'four', 'five']
dict(zip(lst1, lst2))
d = {y: x for x, y in zip(lst1, lst2)}
print(d)