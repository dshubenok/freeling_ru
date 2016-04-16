# скрипт чистит снятник opencorpora от тегов пунктуции (PNCT) и отсутствующих разборов (UNKN), получаем чистый текст для анализа.
import opencorpora

corpus = opencorpora.CorpusReader('annot.opcorpora.no_ambig.xml')
gold = corpus.parsed_words()

with open('texts_op.txt', 'w') as f:
	for elems in gold:
		if elems[1][0][1] != 'PNCT' and elems[1][0][1] != 'UNKN':
			f.write( elems[0] + ' ')
