def to_weird_case(string):
    ret = ""
    i = True
    for char in string:
        if i:
            ret += char.upper()
        else:
            ret += char.lower()
        if char != ' ':
            i = not i
    return ret
print('***'*20)
def to_weird_case(string):
    a=string.split()
    print(a)
    new=[]
    for slowo in a:
        print('*',slowo)
        for i in range(len(slowo)):
            if i%2==0:
                new.append(slowo[i].upper())
            else:
                new.append(slowo[i].lower())
            if slowo ==[]:
                r=0

    print(new)
    return (''.join(new))

print('***' * 20)
############################################################
def to_weird_case(string):
    global w
    print('*',string)
    new=[]
    a = string.split()
    print('++',a)
    print('--',list(string))
    for w in list(string):
        if w==' ':
            new.append(w)
            print('w',w)
        else:
            for slowo in string.split():
                print('slowo=',slowo,len(slowo))
                for i in range(len(slowo)):
                    print('i',i, slowo[i])
                    if w ==' ':
                        new.append(w)
                    else:
                        if i%2==0:
                            print('ia', i, slowo[i].upper())
                            new.append(slowo[i].upper())
                        else:
                            print('ib',i, slowo[i].lower())
                            new.append(slowo[i].lower())

    print(new)
    return (''.join(new))

print('***' * 20)
############################################################


# print(to_weird_case('This'))    #, 'ThIs'
# print(to_weird_case('is')) #, 'Is'
print(to_weird_case('This is a test')) #, 'ThIs Is A TeSt'

def mock(s):
    ret = ""
    i = True
    for char in s:
        if i:
            ret += char.upper()
        else:
            ret += char.lower()
        if char != ' ':
            i = not i
    return ret
# print(mock("This is a test"))
# print(mock("abcd efgh ijkl"))

def mock(s):
    ret = ""
    i = True
    for char in s:
        if i:
            ret += char.upper()
        else:
            ret += char.lower()

        i = not i

    return ret
# print(mock("abcd efgh ijkl"))
####################################################

# s = 'abcd efgh ijkl'
# morph = ''.join([e.upper() if i%2==0 else e for i, e in enumerate(s)])
# print(morph)
###################################################
def function_name(input_string):
    should_capitalize = True
    chars = []
    for single_char in input_string:
        if not single_char.isalpha():
            chars.append(single_char)
            continue

        if should_capitalize:
            chars.append(single_char.upper())
        else:
            chars.append(single_char.lower())

        should_capitalize = not should_capitalize

    return ''.join(chars)
print(function_name('This is a test')) #, 'ThIs Is A TeSt'
