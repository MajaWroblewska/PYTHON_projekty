import string
from collections import Counter


def duplicate_encode(word):
    word=word.lower()
    # word=list(word)
    cnt=Counter()
    for litera in word:
        cnt[litera]+=1
    # print(cnt)

    end=[]
    for i in word:
        if cnt[i]==1:
            end.append('(')
        else:
            end.append(')')

    return (''.join(end))
##########################################################
# def duplicate_encode(word):
#     return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])
# #################################################################
# from collections import Counter
#
# def duplicate_encode(word):
#     word = word.lower()
#     counter = Counter(word)
#     return ''.join(('(' if counter[c] == 1 else ')') for c in word)
# ########################################################
# from collections import Counter
# def duplicate_encode(word):
#     #your code here
#     word=word.lower()
#     c=Counter(word)
#     return ''.join('(' if c[x]==1 else ')' for x in word )
# ############################################################
def duplicate_encode(word):
    """a new string where each character in the new string is '('
    if that character appears only once in the original word, or ')'
    if that character appears more than once in the original word.
    Ignores capitalization when determining if a character is a duplicate. """
    word = word.upper()
    result = ""
    for char in word:
        if word.count(char) > 1:
            result += ")"
        else:
            result += "("

    return result
###########################################
def duplicate_encode(word):
    new_string = ""
    word = word.lower()

    for char in word:
        new_string += (")" if (word.count(char) > 1) else "(")

    return new_string
###################################################
def duplicate_encode(word):
    word = word.lower()

    dict = {}
    for char in word:
        dict[char] = ')' if char in dict else '('

    return ''.join(dict[char] for char in word)
########################################################




print(duplicate_encode("din"))  #, "((("
print(duplicate_encode("Success"))  # ")())())",
print(duplicate_encode("recede"))   # "()()()"
print(duplicate_encode("(( @"))    # "))(("

cnt=Counter()

# for w in ['a','b','c','d','a']:
#     cnt[w]+=1
# print(cnt)
# print(string.ascii_lowercase)

# for litera in string.ascii_lowercase:

litery=[x for x in string.ascii_lowercase]
for w in litery:
    cnt[w]+=1
# print(cnt)


