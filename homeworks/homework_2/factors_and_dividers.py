print('Введіть число: ')
n = abs(int(input()))
num=str(n)
r_z=len(num)

print((r_z),"- Розрядність числа, " , "Множники: " )

def dv(n):
    if n == 1: return [1]
    lst = []
    i = 2
    while n != 1:
        if n % i == 0:
            n = n // i
            lst.append(i)
            continue
        i+=1
    return lst
 
print(dv(n))





