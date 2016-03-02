# -*- coding: utf-8 -*-

import os
from lxml import etree

basedir = os.path.dirname(os.path.realpath(__file__))


def func(p):
    for i in (os.path.join(p, j) for j in os.listdir(p)):
        if os.path.isfile(i):
            if i.endswith('.xhtml'):
                yield i
        else:
            for a in func(i):
                yield a
with open('texts.txt', 'w') as f:
    for i in func(basedir):
        print i
        root = etree.parse(i)
        for s in root.iterfind('.//se'):
            f.write(' '.join([word[-1].tail.encode('utf-8').replace('`', '') for word in s.iterfind('.//w')]) + '\n')
