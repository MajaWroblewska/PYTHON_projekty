from statistics import mean

a=[1,8,3]
sr=mean(a)
print(sr)


from collections import defaultdict, Counter

from pip._vendor.progress import counter

normal_dict = {}
# print(normal_dict["key"]) # !!! KeyError

default_dict = defaultdict(list) #str to narzucona wartość słownika
print(default_dict)
default_dict = defaultdict(str)
print()



print("key:", default_dict["key"]) # key:
print(default_dict.items())
default_dict_2 = defaultdict(lambda: "default string")
print("key:", default_dict_2["key"]) # key: default string
print(default_dict.items())


a=['counter', 'das','das', 'rew' ]
b='ssdfdfreerefwqq'
cnt=Counter(a)
print(cnt)
print(Counter(b))

#zaokrąglenia
liczba=2.874456789
print(round(liczba, 2))
