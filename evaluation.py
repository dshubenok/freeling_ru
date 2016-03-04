# -*- coding: utf-8 -*-
import os

file1 = 'texts.txt'
file2 = 'convert_out.txt'

weight = 0.5

basedir = os.path.dirname(os.path.realpath(__file__))
file1 = os.path.join(basedir, file1)
file2 = os.path.join(basedir, file2)

f = lambda s: s.strip().replace('=', ',').split(',')

with open(file1) as f1, open(file2) as f2:
    line1 = f1.readline()
    line2 = f2.readline()
    s = lemma = pos = c = 0.0
    while line1 and line2:
        str1 = line1.split(' ')
        str2 = line2.split(' ')
        if len(str1) == 3 and len(str2) == 3:
            word1, line1, tags1 = str1
            word2, line2, tags2 = str2
            if word1 == word2:
                tags1, tags2 = f(tags1), f(tags2)
                if line1 == line2:
                    lemma += 1
                w = 0
                if tags1 and tags2 and tags1[0].upper() == tags1[0] and tags1[0] == tags2[0]:
                    pos += 1
                for a in tags1:
                    if a in tags2:
                        w += weight
                c += 1
                s += w
        line1 = f1.readline()
        line2 = f2.readline()
print "lemma - %f%% \n\tcount - %d" % (lemma / c, lemma)
print "PoS-tagging - %f%% \n\tcount - %d" % (pos / c, p)
print "annotation with weight - ", s / c
print '-'*25, '\ncount - ', c
