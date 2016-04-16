file1 = '1.txt'
file2 = '2.txt'

with open(file1) as f1, open(file2) as f2:
    line1 = f1.readline()
    line2 = f2.readline() #читаем два файла построчно
    c = 0.0 # устанавливаем начальное значения счетчика
    while line1 and line2:
        str1 = line1.split(' ')
        str2 = line2.split(' ') # делим строки по пробелам на три части
        if str1[0] == str2[0]: 
            c += 1 # пока словоформы совпадают, прибавлять 1 к счетчику
            print(c)

        line1 = f1.readline()
        line2 = f2.readline()

print ('-'*25, '\ncount - ', c)
