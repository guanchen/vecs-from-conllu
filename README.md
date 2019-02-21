# vecs-from-conllu
Scripts to generate arbitrary context from CoNLL-U format treebanks in order to integrate into word2vecf.
# SetUp
Download Universal Dependencies(UD) treebanks from UD website

Install word2vecf

Create vocabulary file for the treebank you will use by the command line:  cut -f 2 conll_file | python scripts/vocab.py [50]> counted_vocabulary 
# Usage
Run cat conll_file | python3 extract_ners.py counted_vocabulary [100] > dep.contexts

Options like the size of window, the Pos tag context, the word context or the lemma context can be updated in the script named extract_ners.py.
