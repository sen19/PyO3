#Создать словарь оценок предполагаемых студентов (Ключ - ФИ студента, значение - список оценок студентов). Найти самого успешного и самого отстающего по среднему баллу.

s_marks = {
    'sherlock holmes ' : [2,2,3,2,3,5],
    'colombo lieutenant' : [0,3,2,5,1,1],
    'jason bourne' : [5,6,6,6,9,10],
    'james bond' : [4,4,4,5,2,10]
}

def mean(lst):
    return sum(lst) / len(lst)

sortedIds = sorted(s_marks.keys(), key=lambda studentId: mean(s_marks[studentId]))

print('The Best:', sortedIds[-1])
print('Loser:', sortedIds[0])
