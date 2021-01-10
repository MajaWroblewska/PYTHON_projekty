replaceNounPhrases(sentence, pronouns, dictionary):
    print(sentence)
    print(pr)


dictionary = {
  'a': 'aux',
  'the': 'aux',
  'girl' : 'N',
  'cookie' : 'N',
  'big' : 'adj',
  'tall' : 'adj',
  'scary' : 'adj'
}

print(replaceNounPhrases("a girl", ["she"], dictionary))    #,"she");
print(replaceNounPhrases("a girl ate the cookie", ["she", "it"], dictionary))   #,"she ate it");
print(replaceNounPhrases("a a a big big a cookie", ["it"], dictionary)) #,"a a a big big it");
print(replaceNounPhrases("a scary girl", ["she"], dictionary))    #,"she");
print(replaceNounPhrases("a big tall scary girl ate the big cookie", ["she", "it"], dictionary))    #,"she ate it");
