#Банкомат выдает сумму максимально возможными купюрами

def atm(n, c=0):    
    if n%10: return 'Введіть суму кратну 10'
    for i in (1000,500,200,100,50,20,10):
        c += n//i
        n = n%i
    return c

print(atm(29370))
