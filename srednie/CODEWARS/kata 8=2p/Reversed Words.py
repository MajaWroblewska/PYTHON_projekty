def reverseWords(string):
    s=string.split(' ')
    print('s=',s)
    # rew=s[::-1]
    rew=list(reversed(s))
    print('rew=',rew)
    new_string=' '.join(rew)
    return new_string

print(reverseWords("hello world!"))    #>> "world! hello"



# string="hello world!"
# string=string.split()
# s=string[::-1]
# a=' '.join(s)
# # print(a)
#
#
# print(sorted(string))
# print(string[::-1])
# print(string)
#####################################################
def reverseWords(str):
    return " ".join(str.split(" ")[::-1])
def reverseWords(str):
    return ' '.join(reversed(str.split(' ')))
def reverseWords(string):
    return ' '.join(reversed(string.split()))

def reverseWords(str):
    k = str.split(' ')
    k.reverse()
    str = ' '.join(k)
    return str
###################################################
def reverseWords(string):
    # """ reverse_words == PEP8, forced camelCase by CodeWars """
    return ' '.join(reversed(string.split()))
#########################################################
reverseWords = lambda _:' '.join(_.split(' ')[::-1])

reverseWords= lambda the_word_i_need_to_reverse_to_complete_this_kata:' '.join(the_word_i_need_to_reverse_to_complete_this_kata.split()[::-1])

reverseWords = lambda s: " ".join(s.split(" ")[::-1])

import re
def reverseWords(str):
    return "".join(re.split(r'(\s+)', str)[::-1])

###############################################################
reverseWords=lambda ss:' '.join(ss.split(' ')[-1::-1])


