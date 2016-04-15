import numpy as np

file1 = 'texts.txt'
file2 = 'convert_out.txt'

f = lambda s: s.strip().replace('=', ',').split(',') #функция приводит теги в нужный вид

with open(file1) as f1, open(file2) as f2:
    #читаем построчно
    line1 = f1.readline()
    line2 = f2.readline()
    lemma = pos = 0.0 # устанавливаем начальные значения
    list = []
    while line1 and line2:

        str1 = line1.split(' ')
        str2 = line2.split(' ') # делим строки на три части

        if len(str1) == 3 and len(str2) == 3:

            tags1 = str1[2]
            tags2 = str2[2] # берем только теги
            tags1, tags2 = f(tags1), f(tags2) #применяем фукцию для приведения тегов к нужному виду

            if tags1[0] == tags2[0]:
                pos += 1
            set_1 = set(tags1)
            set_2 = set(tags2)
            n = len(set_1.intersection(set_2))
            m = n / float(len(set_1) + len(set_2) - n)
            list.append(m) # объединяем все в один список

        line1 = f1.readline()
        line2 = f2.readline() # зацикливаем, пока строки не кончатся
    average = np.average(list) # находим среднее значение по индексу
    print(average)
