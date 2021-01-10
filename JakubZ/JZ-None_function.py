def foo1(lst=[]):           #dopisuje cały czas do tej samej listy
    lst.append('a')
    print(lst)
    return(lst)


def foo2(lst=[]):           #tworzy nowy lst (nowy adres)
    lst = lst + ['a']
    print(lst)
    return(lst)


def foo3(lst=None):         #stosować to rozwiazanie, bo jest jedyne poprawne
    if lst is None:
        lst = []
    lst.append('a')
    print(lst)
    return(lst)


foo1()
foo1()
foo1()
foo1()
foo1()

foo2()
foo2()
foo2()
foo2()
foo2()

foo3()
foo3()
foo3()
foo3()
foo3()





