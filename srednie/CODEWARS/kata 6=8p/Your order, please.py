def order(sentence):    #Maja
    word_list=sentence.split()
    # print(word_list)
    list_new_sentence=sorted(word_list, key = lambda x: sorted(x))
    return (' ').join(list_new_sentence)
########################################################################
def order(words):
  return ' '.join(sorted(words.split(), key=lambda w:sorted(w)))
###########################################################################
def order(sentence):
    if not sentence:
        return ""
    result = []  # the list that will eventually become our setence

    split_up = sentence.split()  # the original sentence turned into a list

    for i in range(1, 10):
        for item in split_up:
            if str(i) in item:
                result.append(item)  # adds them in numerical order since it cycles through i first

    return " ".join(result)
##########################################################################
def order(s):
    z = []
    for i in range(1,10):
        for j in list(s.split()):
            if str(i) in j:
               z.append(j)
    return " ".join(z)
#########################################################################
def extract_number(word):
    for l in word:
        if l.isdigit(): return int(l)
    return None

def order(sentence):
    return ' '.join(sorted(sentence.split(), key=extract_number))
########################################################################
import re

class Word(object):
    digit_regex = re.compile(r'[0-9]')

    def __init__(self, word):
        self._index = self.digit_regex.findall(word)[0]
        self._word = word

    def __repr__(self):
        return self._word

    @property
    def word(self):
        return self._word

    @property
    def index(self):
        return self._index

class Sentence(object):

    def __init__(self, words):
        self._words = words

    def __repr__(self):
        return ' '.join([str(x) for x in self.ordered()])

    def ordered(self):
        return sorted(self._words, key=lambda word: word.index)

def order(sentence):
    return str(Sentence(map(Word, sentence.split())))
###########################################################################
order = lambda xs: ' '.join(sorted(xs.split(), key=min))
######################################################################
def order(sentence):
    return ' '.join(sorted([x for x in sentence.split()], key=lambda x: [int(n) for n in x if n.isdigit()][0]))
#############################################################################
def order(sentence):
    if sentence == "":
        return sentence

    output = []

    for ordernum in range(1, len(sentence.split()) + 1):
        for word in sentence.split():
            for letter in word:
                if letter == str(ordernum):
                    output.append(word)

    return " ".join(output)
#########################################################################


print(order("is2 Thi1s T4est 3a")) #, "Thi1s is2 3a T4est")
print(order("4of Fo1r pe6ople g3ood th5e the2"))   #, "Fo1r the2 g3ood 4of th5e pe6ople")
print(order(""))    #, "")
print(order("hand1 3the 2number to5 aft4er"))    #, "")
print('**'*30)


