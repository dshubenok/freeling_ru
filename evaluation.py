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
    l1 = f1.readline()
    l2 = f2.readline()
    s = l = p = c = 0.0
    while l1 and l2:
        tla1 = l1.split(' ')
        tla2 = l2.split(' ')
        if len(tla1) == 3 and len(tla2) == 3:
            t1, l1, a1 = tla1
            t2, l2, a2 = tla2
            if t1 == t2:
                a1, a2 = f(a1), f(a2)
                if l1 == l2:
                    l += 1
                w = 0
                if a1 and a2 and a1[0].upper() == a1[0] and a1[0] == a2[0]:
                    p += 1
                for a in a1:
                    if a in a2:
                        w += weight
                c += 1
                s += w
        l1 = f1.readline()
        l2 = f2.readline()
print "lemma - %f%% \n\tcount - %d" % (l / c, l)
print "PoS-tagging - %f%% \n\tcount - %d" % (p / c, p)
print "annotation with weight - ", s / c
print '-'*25, '\ncount - ', c
