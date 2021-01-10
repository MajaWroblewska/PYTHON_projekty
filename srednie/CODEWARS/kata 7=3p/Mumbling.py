def accum(s):
    napis=[]
    for i in range(len(s)):
        litera=s[i]*(i+1)
        napis.append(litera.title())
    return '-'.join(napis)
######################################################
def accum(s):
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))
#######################################################
def accum(s):
    return '-'.join((a * i).title() for i, a in enumerate(s, 1))
####################################################################
def accum(s):   #Kris
    count = 1
    mumbling = ''
    for char in s:
        mumbling += (char * count).capitalize() + '-'
        count += 1
    return mumbling[:-1]
#####################################################
def accum(s):   #Bartek
    s = list(s)
    accum_s = ""
    accum_s2 = ""
    for x,y in enumerate(s):
        accum_s2 = accum_s2 + y * (int(x) + 1)
        accum_s2 = accum_s2.capitalize()
        if (x + 1 == len(s)):
            accum_s = accum_s + accum_s2
        else:
            accum_s = accum_s + accum_s2 + "-"
        accum_s2 = ""
    return accum_s
############################################################



print(accum("ZpglnRxqenU"))
                       # "Z-Pp-Ggg-Llll-Nnnnn-Rrrrrr-Xxxxxxx-Qqqqqqqq-Eeeeeeeee-Nnnnnnnnnn-Uuuuuuuuuuu"
# print(accum("NyffsGeyylB"))
#                        "N-Yy-Fff-Ffff-Sssss-Gggggg-Eeeeeee-Yyyyyyyy-Yyyyyyyyy-Llllllllll-Bbbbbbbbbbb"
# print(accum("MjtkuBovqrU"))
#                       "M-Jj-Ttt-Kkkk-Uuuuu-Bbbbbb-Ooooooo-Vvvvvvvv-Qqqqqqqqq-Rrrrrrrrrr-Uuuuuuuuuuu"
# print(accum("EvidjUnokmM"))
                      # "E-Vv-Iii-Dddd-Jjjjj-Uuuuuu-Nnnnnnn-Oooooooo-Kkkkkkkkk-Mmmmmmmmmm-Mmmmmmmmmmm"
# print(accum("HbideVbxncC"))
                       # "H-Bb-Iii-Dddd-Eeeee-Vvvvvv-Bbbbbbb-Xxxxxxxx-Nnnnnnnnn-Cccccccccc-Ccccccccccc"