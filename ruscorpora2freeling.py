import codecs, re

res_f = codecs.open('fr2.txt', 'w', 'utf-8')

pos_dict = {
'A': 'A', 
'ADV': 'D', 
'ADV-PRO': 'P', 
'A-NUM': 'Y', 
'A-PRO': 'R', 
'CONJ': 'C', 
'INTJ': 'J', 
'PRAEDIC': '0',
'PRAEDIC-PRO': '0',
'PARENTH': '0',
'NUM': 'Z', 
'PART': 'T', 
'PR': 'B', 
'S': 'N', 
'S-PRO': 'E', 
'V': 'V'
}

attrDict = {
    "A": ['case', 'num', 'gen', 'animate', 'form', 'degree', 'other', 'obscene'],
    "B": ['other'],
    "C": ['other'],
    "D": ['degree',   'other',  'obscene'],
    "E": ['case', 'num', 'gen', 'animate', 'person', 'other'],
    "J": ['other',  'obscene'],
    "M": ['other'],
    "N": ['type', 'case', 'num', 'gen', 'animate',   'info',  'other',  'obscene', 'neclass'],
    "P": ['other'],
    "Q": ['mood', 'num', 'gen', 'tense', 'person', 'aspect', 'voice', 'transitive', 'other', 'obscene'],
    "R": ['case',   'num',  'gen', 'animate',   'other'],
    "T": ['other'],
    "V": ['mood',   'num',  'gen', 'tense',   'person',  'person',  'aspect',  'voice',  'transitive', 'other', 'obscene'],
    "Y": ['case',   'num',  'gen', 'animate'],
    "Z": ['case',   'num',  'gen', 'animate', 'other'],
            }

props = {
    'case': {'nom': 'N', 'gen': 'G', 'dat': 'D', 'acc': 'F', 'ins': 'C', 'loc': 'O', 'gen2': 'P', 'loc2': 'L', 'voc': 'V'},
    'number': {'sg' : 'S', 'pl': 'P'},
    'gender': {'f': 'F', 'm': 'M', 'n': 'A', 'm-f': 'C'},
    'animation': {'anim': 'A', 'inan': 'I'},
    'others': {'anom': 'D', 'distort': 'V', 'anum': 'I', 'abbr': 'B'},
    'abuse': {'obsc': 'H'},
    'mood': {'indic': 'D', 'imper': 'M', 'inf': 'I'},
    'tense': {'praer': 'P', 'fut': 'F', 'praet': 'S'},
    'person': {'1p': 'P1', '2p': 'P2', '3p': 'P3'},
    'finiteness': {'pf': 'F', 'ipf': 'N', 'inf': 'I'},
    'voice': {'act': 'A', 'pass': 'S'},
    'status': {'tran': 'M', 'intr': 'A'},
    'aform': {'brev': 'S', 'plen': 'F'},
    'clevel': {'supr': 'E', 'comp': 'C'}
}

res = codecs.open('fr1.txt', 'r', 'utf-8') #открываем файл на чтение
for line in res.readlines(): #читаем построчно, делим 
    line = line.strip()
    try:
        word, lemma, tag = line.split(' ') # делим строку на три части - слово, лемма, разбор
        tag_separated = tag.split(',') #получаем список элементов морфологического разбора
        #print(tag_separated)

    except ValueError:
        print('Ошибка. Что-то отсутствует') #на случай, если что-то пойдет не так
        break

    try:
        tag_freeling = pos_dict[tag_separated[0]]  #конвертируем часть речи
        # print(tag_separated[0], '=>', tag_freeling)
    except:
        print('Что-то не так.')
        break
    # try:
    #     if tag_separated[0] == 'S':
    #         tag_separated[1] = 
