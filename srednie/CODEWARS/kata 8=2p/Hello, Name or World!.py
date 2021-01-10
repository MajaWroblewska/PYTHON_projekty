def hello(name=None):     #Maja
    if not name:
        return 'Hello, World!'
    elif name=='':
        return 'Hello, World!'
    elif name:
        name.lower()
        return f'Hello, {name.capitalize()}!'
    return
#########################################################################
def hello(name=''):
    return f"hello, {name or 'world'}!".title()
#########################################################################
def hello(name=''):
    return 'Hello, ' + (name.capitalize() or 'World') + '!'
#########################################################################
def hello(name=''):
    return f'Hello, {(name or "world").capitalize()}!'
##########################################################################
hello = lambda n='': f"Hello, {n.title() or 'World'}!"
##########################################################################
def hello(*name):
    if name:
        if name[0]:
            return ('Hello, ' + name[0].title() + '!')
        else:
            return 'Hello, World!'
    else:
        return 'Hello, World!'
###########################################################################
def hello(name='World'):
    if not name: name = 'World'
    return f'Hello, {name.title()}!'
#############################################################################
def hello(name=None):
    try:
        test = name + str(name)
        print('No Error')
    except:
        name = ''
        print('Error Handled!!!')

    if name == '' or name == None:
        new_name = 'World'
    else:
        new_name = ''
        letter = 0
        for i in name:
            if letter == 0 and i.islower:
                new_name += i.upper()
            elif letter == 0:
                new_name += i
            elif letter > 0 and i.isupper:
                new_name += i.lower()
            else:
                new_name += i

            letter += 1

    return 'Hello, ' + new_name + '!'
#####################################################################################33
def hello(name='World'):
    if not name:
        return "Hello, World!"
    name =name.casefold()
    return f"Hello, {name.title()}!"
##############################################################################
def hello(name = ""):
    if len(name) >= 2:
        name = name.lower()
        name = name.replace(name[0], name[0].upper(), 1)
        return "Hello, " + name + "!"
    else:
        return "Hello, World!"
print(hello('maJa uuu'))    #>>Hello, Maja uuu!
print(hello())  #>>Hello, World!
print(hello(''))    #>>Hello, World!
# print(hello(9))
