import codecs, re

res_f = codecs.open('test_freel.xhtml', 'w', 'utf-8')

pos_dic = {'A': 'A', 'D': 'ADV', 'P': 'ADV-PRO',
           'Y': 'A-NUM', 'R': 'A-PRO',
           'M': 'null', 'C': 'CONJ', 'J': 'INTJ', 'Z': 'NUM',
           'T': 'PART', 'B': 'PR', 'N': 'S', 'E': 'S-PRO',
           'V': 'V', 'Q': 'V'}

attrDict = {
    "N": ['taggerProp', 'case', 'number', 'gender', 'animation',   'addNounInfo',  'others',  'abuse'],
    "Y": ['case',   'number',  'gender', 'animation'],
    "R": ['case',   'number',  'gender', 'animation',   'others'],
    "V": ['mood',   'number',  'gender', 'tense',   'person',  'finiteness',  'voice',  'status',  'others',  'abuse'],
    "F": ['case',   'number',  'gender', 'tense',   'aform',  'finiteness',  'voice',  'status',  'others', 'abuse'],
    "D": ['clevel',   'others',  'abuse'],
    "P": ['others'],
    "E": ['case',   'number',  'gender', 'animation',     'person',   'others'],
    "B": ['others'],
    "T": ['others'],
    "Z": ['case',   'number',  'gender', 'animation', 'others'],
    "J": ['others',  'abuse'],
    "C": ['others'],
    "M": ['others'],
    "A": ['case',   'number',  'gender', 'animation', 'aform',   'clevel',  'others',  'abuse'],
            }

props = {
    'case': {'N': 'nom', 'G': 'gen', 'D': 'dat', 'F': 'acc', 'C': 'ins', 'O': 'loc', 'P': 'gen2', 'L': 'loc2', 'V': 'voc'},
    'number': {'S' : 'sg', 'P': 'pl'},
    'gender': {'F': 'f', 'M': 'm', 'A': 'n', 'C': 'm-f'},
    'animation': {'A': 'anim', 'I': 'inan'},
    'others': {'D': 'anom', 'V': 'distort', 'I': 'anum', 'B': 'abbr'},
    'abuse': {'H': 'obsc'},
    'mood': {'D': 'indic', 'M': 'imper', 'I': 'inf'},
    'tense': {'P': 'praer', 'F': 'fut', 'S': 'praet'},
    'person': {'P1': '1p', 'P2': '2p', 'P3': '3p'},
    'finiteness': {'F': 'pf', 'N': 'ipf', 'I': 'inf'},
    'voice': {'A': 'act', 'S': 'pass'},
    'status': {'M': 'tran', 'A': 'intr'},
    'aform': {'S': 'brev', 'F': 'plen'},
    'clevel': {'E': 'supr', 'C': 'comp'}
}

res = codecs.open('freeling.txt', 'r', 'utf-8')
for line in res.readlines():
    line = line.strip()
    try:
        w, lex, gr, prob = line.split(' ')
#      print line.split(' '), w
    except ValueError:
        continue
    try:
        pos = pos_dic[gr[0]]
    except KeyError:
        if '_' in w:
            l = w.count('_')
#            print (w, l + 1)
            word = w + '\n'
            res_f.write(word*(l + 1))
        continue
    if pos == 'NUM' and '_' in w:
        l = w.count('_')
#        print (w, l + 1)
        word = w + '\n'
        res_f.write(word*(l + 1))
        continue
    if gr[0] == 'Q':
        attrs = 'V'
    else:
        attrs = gr[0]
    pr = attrDict[attrs]
    ana = ''
    for prop in range(len(gr[1:])):
        if gr[1:][prop] == '0':
            continue
        try:
            means = pr[prop]
        except IndexError:
            continue
        if means == 'taggerProp' or means == 'addNounInfo':
            continue
        try:
            ms = props[means][gr[1:][prop]]
        except KeyError:
            continue
        ana += ms + ','
    if ana != '':
        ana = ',' + ana[:-1]
#    word = lex + pos + ana + w
    word = w + ' ' + lex + ' ' + pos + ana
    res_f.write(word + '\n')
res_f.close()
