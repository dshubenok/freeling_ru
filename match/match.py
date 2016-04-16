#!/usr/bin/python2
#coding: utf-8

import sys

file1 = sys.argv[1] # Указываем имена файлов для сравнения
file2 = sys.argv[2]

with open(file1) as f1, open(file2) as f2:
    text1 = f1.readlines()
    text2 = f2.readlines() #читаем два файла построчно
    c = 0  # устанавливаем начальное значения счетчика
    for line1, line2 in zip(text1, text2):
        str1 = line1.split()
        str2 = line2.split() # делим строки по пробелам
        c += 1 # пока словоформы совпадают, прибавлять 1 к счетчику
        if str1[0] != str2[0]:
            print(c)
            print str1[0].strip(), str2[0].strip()
            break
