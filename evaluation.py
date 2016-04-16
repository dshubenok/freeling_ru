#!/usr/bin/python
# coding: utf-8


import sys

file1 = sys.argv[1]
file2 = sys.argv[2]

f = lambda s: s.strip().replace('=', ',').split(',') # функция приходит теги к нужному виду

with open(file1) as f1, open(file2) as f2:
    line1 = f1.readline()
    line2 = f2.readline() #читаем построчно
    lemma = pos = c = 0.0 # устанавливаем начальные значения
    while line1 and line2:
        str1 = line1.split(' ')
        str2 = line2.split(' ') # делим строки по пробелам на три части
        if len(str1) == 3 and len(str2) == 3:
            word1, line1, tags1 = str1
            word2, line2, tags2 = str2
            if word1 == word2:
                tags1, tags2 = f(tags1), f(tags2)
                if line1 == line2:
                    lemma += 1
                w = 0
                if tags1[0] == tags2[0]:
                    pos += 1

                c += 1
        line1 = f1.readline()
        line2 = f2.readline()
print ("lemma - %f%% \n\tcount - %d" % (lemma / c, lemma))
print ("PoS-tagging - %f%% \n\tcount - %d" % (pos / c, pos))
print ('-'*25, '\ncount - ', c)
