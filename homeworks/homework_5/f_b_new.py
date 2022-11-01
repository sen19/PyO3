#Продолжаем идеализировать fizzbuzz, теперь применяем функции и map везде, где можно и нельзя!
print(*map(lambda i: 'F'*(not i%3)+'B'*(not i%5)+'FB'*(not i%3 and not i%5) or i, range(2,19)))