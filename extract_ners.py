# Two steps to check before run the script:
# Step1: make sure the window size (window = x) you want to consider
# Step2: under main function, release the type of context you want to generate
import sys
import itertools
from collections import defaultdict
vocab_file = sys.argv[1]
try:
    THR = int(sys.argv[2])
except IndexError:
    THR = 100

lower = True
window = 3  # set window size as you need


def read_vocab(fh):
    v = {}
    for line in fh:
        if lower:
            line = line.lower()
        line = line.strip().split()
        if len(line) != 2:
            continue
        if int(line[1]) >= THR:
            v[line[0]] = int(line[1])
    return v


vocab = set(read_vocab(open(vocab_file, "r")).keys())

print(sys.stderr, "vocab:", len(vocab))

positions = [(x, "l%s_" % x) for x in range(-window, +window + 1) if x != 0]

# store pos, word, lemma three separate lists
pos = []
word = []
lemma = []
for line in sys.stdin:
    if lower:
        line = line.lower()
    toks = ['<s>']
    if not line.startswith("#"):
        toks.extend(line.strip().split())
        if len(toks) == 1:
            pos.extend(toks)
            word.extend(toks)
            lemma.extend(toks)
        else:
            pos.append(toks[4])
            word.append(toks[2])
            lemma.append(toks[3])

# split lis of word into sub-lists separated by "<s>"
new_word = [
    list(x[1]) for x in itertools.groupby(word, lambda x: x == '<s>')
    if not x[0]
]
new_pos = [
    list(x[1]) for x in itertools.groupby(pos, lambda x: x == '<s>')
    if not x[0]
]
new_lemma = [
    list(x[1]) for x in itertools.groupby(lemma, lambda x: x == '<s>')
    if not x[0]
]


# convert to word-based context, pos-based context or lemma-based context
def c2word():
    for sent in new_word:
        for i, w in enumerate(sent):
            for j, s in positions:
                if i + j >= len(sent):
                    continue
                if i + j < 0:
                    continue
                c = sent[i + j]
                print(w, "%s%s" % (s, c))


def c2pos():
    for sent in new_pos:
        for i, w in enumerate(sent):
            for j, s in positions:
                if i + j >= len(sent):
                    continue
                if i + j < 0:
                    continue
                c = sent[i + j]
                print(new_word[new_pos.index(sent)][i], "%s_%s%s" % (w, s, c))


def c2lem():
    for sent in new_li_lemma:
        for i, w in enumerate(sent):
            for j, s in positions:
                if i + j >= len(sent):
                    continue
                if i + j < 0:
                    continue
                c = sent[i + j]
                print(new_word[new_lemma.index(sent)][i],
                      "%s_%s%s" % (w, s, c))


if __name__ == "__main__":
    c2word()
    # c2lem()
    # c2pos()
