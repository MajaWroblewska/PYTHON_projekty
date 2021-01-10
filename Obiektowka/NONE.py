# a=None
# print(type(a))
def foo1(lst=[]):
    lst.append('a')
    print(lst)
    return lst

def foo2(lst=[]):
    lst=lst+['a']
    print(lst)
    return lst

def foo3(lst=None):  #jedyna słuszna!!!!
    if lst is None:
        lst=[]
    lst.append('a')
    print(lst)
    return lst


#5 razy wywołać foo1, foo2, foo3,

foo1()
foo1()
foo1()
foo1()
foo1()

# foo2()
# foo2()
# foo2()
# foo2()
# foo2()

# foo3()
# foo3()
# foo3()
# foo3()
# foo3()
# foo3()