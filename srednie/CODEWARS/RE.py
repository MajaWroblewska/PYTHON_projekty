import re

# vowelRegex=re.compile(r'\S')
# a=vowelRegex.findall('   5[(6%')
# print(vowelRegex.findall('MajaO 45')+[0])
# print(type(vowelRegex.findall('Maja')))
# print(a)
# print(a[:2])

# phoneRegex=re.compile(r'(\d\d)- (\d\d\d)- (\d\d\d\d)')
# phon=phoneRegex.findall('34- 344- 5448 fdfd33-333-4565 434 ')
# print(phon)

phoneRegex=re.compile(r'\d+')
phon=phoneRegex.search('34- 344- 5448 fdfd33-333-4565 434 ')
print(phon.group(),type(phon.group()))

phon=phoneRegex.findall('34- 344- 5448 fdfd33-333-4565 434 ')
print(phon, type(phon))

phoneRegex=re.compile(r'(ha){,3}')
phon=phoneRegex.findall('haha ha hahaha haha ha ha')
print(phon)
print(type(phon))


