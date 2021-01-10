def alphabet_position(text):
    a=[str(ord(znak.lower())-96) for znak in list(text) if znak.isalpha()]
    return (' '.join(a))
    # for znak in list(text):
    #     if znak.isalpha():
    #         print(znak,str(ord(znak.lower())-96))
###############################################################
def alphabet_position(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())
#####################################################################################
def alphabet_position(text):
  al = 'abcdefghijklmnopqrstuvwxyz'
  return " ".join(filter(lambda a: a != '0', [str(al.find(c) + 1) for c in text.lower()]))
#####################################################################################



print(alphabet_position("The sunset sets at twelve o' clock.")) #, "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11")
print(alphabet_position("The narwhal bacons at midnight."))    #, "20 8 5 14 1 18 23 8 1 12 2 1 3 15 14 19 1 20 13 9 4 14 9 7 8 20")

