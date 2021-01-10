# return masked string  #Maja
def maskify(s):
    # print('sl:', sl)
    # sa = list(s)
    # print(list(sa))
    new = []
    if len(s)<=4:
        result=str(s)
    else:
        sl = s[len(s) - 4:]
        l = len(s) - 4
        for i in range(l):
            new.append('#')
            haslo = new + list(sl)
    # print(haslo)
            result=''.join(haslo)
    return result
##################################################################################
# return masked string
def maskify(cc):
    return "#"*(len(cc)-4) + cc[-4:]
####################################################################################
# return masked string
def maskify(cc):
    l = len(cc)
    if l <= 4: return cc
    return (l - 4) * '#' + cc[-4:]
####################################################################################
# return masked string
def maskify(cc):
    return "#" * len(cc[:-4]) + cc[-4:]
####################################################################################
# return masked string
def maskify(cc):
    return f"{'#'*len(cc[:-4])}{cc[-4:]}"
#####################################################################################
# return masked string
def maskify(cc):
    return cc[-4:].rjust(len(cc), "#")
#####################################################################################
# return masked string
def maskify(cc):
    newstring = ''
    for _ in cc[0:-4]:
        newstring += '#'
    for number in cc[-4:]:
        newstring += number
    return newstring
#######################################################################################
# return masked string
def maskify(cc):
    return "#" * (len(cc) - 4) + cc[-4::]

print(maskify("4556364607935616"))  # == "############5616"
print(maskify("123"))  # ==  "123"
print(maskify("1"))  # == "1"
print(maskify("")) ==""

s='bbkokolinop'
# s="4556364607935616"
# s=     "64607935616"
# s=(               "1")
# s=''
print(s[-4:])
# sl=s[len(s)-4:]
# print('s:',sl)
# sa=list(s)
# print(list(sa))
# new=[]
# l=len(s)-4
# for i in range(l):
#     new.append('#')
# haslo=new+list(sl)
# t=''.join(haslo)
# print(t)
