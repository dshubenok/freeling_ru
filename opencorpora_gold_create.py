# скрипт создает золотой стандарт, очищенный от пунктуации (PNKT) и неопределенных тегов (UNKN)
import opencorpora

corpus = opencorpora.CorpusReader('annot.opcorpora.no_ambig.xml')
gold = corpus.parsed_words()

with open('texts2.txt', 'w') as f:
	for elems in gold:
		if elems[1][0][1] != 'PNCT' and elems[1][0][1] != 'UNKN':
			f.write( elems[0] + ' ' + elems[1][0][0] + ' ' + elems[1][0][1] + '\n')
