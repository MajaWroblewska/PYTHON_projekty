# ile jest każdej litery w napisie + wielkość liter + tylko litery
slowo=input('Wpisz słowo')
slowo=slowo.lower()  #wielkośc liter
s={}
for litera in slowo:
    if litera.isalpha():  #czy znak
        if litera in s:
            s[litera]+=1
        else:
            s[litera]=1

print(s)
