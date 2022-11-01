#'''Создать структуру данных для студентов из имен и фамилий, можно случайных. Придумать структуру данных, чтобы указывать, в какой группе учится студент (Группы Python, FrontEnd, FullStack, Java). Студент может учиться в нескольких группах. Затем вывести:
#студентов, которые учатся в двух и более группах
#студентов, которые не учатся на фронтенде
#студентов, которые изучают Python или Java'''

students = {'ivanov', 'petrov', 'sidorov', 'goroxov', 'moxov'}

python_g ={'ivanov', 'petrov'}

front_end_g ={'petrov', 'sidorov'}

full_stack_g ={'sidorov', 'goroxov'}

Java_g ={'goroxov', 'moxov'}






print(students - front_end_g)  #студентов, которые не учатся на фронтенде
print(python_g|Java_g )        #студентов, которые изучают Python или Java



