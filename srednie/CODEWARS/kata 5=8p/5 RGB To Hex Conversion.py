'''
Zamiana na dec -> hex
a=20
print(a//3) #cz. całkowita
print(a%3)  #reszta
'''
def rgb(r, g, b):
    if r<0:
        r=0
    if g<0:
        g=0
    if b<0:
        b=0
    if r>255:
        r=255
    if g>255:
        g=255
    if b>255:
        b=255

    keys = [x for x in range(16)]
    values = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    # print(dict(zip(keys,values)))
    # print(r,g,b)

    r=(f'{dict(zip(keys,values))[r // 16]}{dict(zip(keys,values))[r % 16]}')
    g=(f'{dict(zip(keys,values))[g // 16]}{dict(zip(keys,values))[g % 16]}')
    b=(f'{dict(zip(keys,values))[b // 16]}{dict(zip(keys,values))[b % 16]}')
    return (f'{r}{g}{b}')
    print('-'*20)
    # return (f'{hex(r)[-2:].upper()}{hex(b)[-2:].upper()}{hex(b)[-2:].upper()}')
#######################################################################################
def rgb(r, g, b):                           #!!!!
    def get_hex(s):
        if s > 255: s = 255
        if s < 0: s = 0
        return hex(s)[2:].upper() if len(hex(s)[2:]) > 1 else "0" + hex(s)[2:]
    return get_hex(r) + get_hex(g) + get_hex(b)
###########################################################################################
def dec_to_hex(number):                                                 #kris
    if number >= 255:
        number = 255
    if number <= 0:
        number = 0

    converted = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    return converted[number // 16] + converted[number % 16]

def rgb(r, g, b):
    return dec_to_hex(r) + dec_to_hex(g) + dec_to_hex(b)
#####################################################
def rgb(r, g, b):
    def convert(x):
        if x < 0:
            x = 0
        if x >= 256:
            x = 255
        return '{0:02X}'.format(x)
    return ''.join(convert(x) for x in (r, g, b))
########################################################################################
def rgb(r, g, b):                                                        #   !!!!!!!!!!!!!!!!
    if 0<=r<=255 and 0<=g<=255 and 0<=b<=255:
        A='%02x%02x%02x' % (r, g, b)
        # print(A)
        return A.upper()
    elif r<0:
        return rgb(0,g,b)
    elif g<0:
        return rgb(r,0,b)
    elif b<0:
        return rgb(r,g,0)
    elif r>255:
        return rgb(255,g,b)
    elif g>255:
        return rgb(r,255,b)
    elif b>255:
        return rgb(r,g,255)
#######################################################################################
# def rgb(r, g, b):
#     round = lambda x: min(255, max(x, 0))
#     return ("{:02X}" * 3).format(round(r), round(g), round(b))
# ##########################################################################################
# def rgb(r, g, b):
#     clamp = lambda x: max(0, min(x, 255))
#     return "%02X%02X%02X" % (clamp(r), clamp(g), clamp(b))
#############################################################################################
def rgb(r, g, b):
    v = lambda v: min(255, max(0, v))
    return "%02X%02X%02X" % (v(r), v(g), v(b))
# ##########################################################################################
# def limit(num):
#     if num < 0:
#         return 0
#     if num > 255:
#         return 255
#     return num
#
# def rgb(r, g, b):
#     return "{:02X}{:02X}{:02X}".format(limit(r), limit(g), limit(b))
# ##################################################################################
# def rgb(*args):
#     return ''.join(map(lambda x: '{:02X}'.format(min(max(0, x), 255)), args));
# #####################################################################################
# def rgb(r, g, b):
#     return ''.join(['%02X' % max(0, min(x, 255)) for x in [r, g, b]])
# ####################################################################################
# def rgb(r, g, b):
#     """
#     Return hex string representation of ``r,g,b`` values. A saturation \
# will be applied to the input values to ensure they are betweem 0 \
# and 255.
#
#     :param r: Red channel
#     :type r: int
#
#     :param g: Green channel
#     :type g: int
#
#     :param b: Blue channel
#     :type b: int
#
#     :return: Hex representation.
#     :rtype: str
#
#     >>> rgb(123,45,67)
#     '7B2D43'
#     >>> rgb(-20,123,456)
#     '007BFF'
#     >>> rgb('no int',123,123)
#     Traceback (most recent call last):
#         ...
#     TypeError: 'r' is not of type int
#     >>> rgb(123,'no int',123)
#     Traceback (most recent call last):
#         ...
#     TypeError: 'g' is not of type int
#     >>> rgb(123,123,'no int')
#     Traceback (most recent call last):
#         ...
#     TypeError: 'b' is not of type int
#     """
#
#     if not type(r).__name__ == 'int':  # python2 does not have instanceof()
#         raise TypeError("'r' is not of type int")
#     if not type(g).__name__ == 'int':  # python2 does not have instanceof()
#         raise TypeError("'g' is not of type int")
#     if not type(b).__name__ == 'int':  # python2 does not have instanceof()
#         raise TypeError("'b' is not of type int")
#
#     return "{r:02X}{g:02X}{b:02X}".format(
#         r=saturate(r),
#         g=saturate(g),
#         b=saturate(b),
#     )
#
#
# def saturate(x):
#     """
#     Saturates an integer ``x`` to be ``0<=x<=255``.
#
#     :param x: Integer to be saturated
#     :type x: int
#
#     :return: Saturated integer
#     :rtype: int
#
#     >>> saturate(345)
#     255
#     >>> saturate(-3)
#     0
#     >>> saturate(123)
#     123
#     >>> saturate("no int")
#     Traceback (most recent call last):
#         ...
#     TypeError: given value is not of type int
#     """
#     if not type(x).__name__ == 'int':  # python2 does not have instanceof()
#         raise TypeError("given value is not of type int")
#
#     x = 0 if x < 0 else x
#     x = 255 if x > 255 else x
#
#     return x
#
#
# if __name__ == "__main__":
#     import doctest
#
#     doctest.testmod()
# ##########################################################################################
# def hex_con(color):
#     hex_dict = '0123456789ABCDEF'
#     d1 = color // 16
#     d2 = color % 16
#     if d1 > 15:
#         d1 = 15
#         d2 = 15
#     elif d1 < 0:
#         d1 = 0
#         d2 = 0
#     return str(hex_dict[d1]) + str(hex_dict[d2])
#
#
# def rgb(r, g, b):
#     R = hex_con(r)
#     G = hex_con(g)
#     B = hex_con(b)
#     return R + G + B
###########################################################################################
def rgb(r, g, b):
    r = hex(round(r))
    g = hex(round(g))
    b = hex(round(b))
    r = r[r.find('x')+1:]
    g = g[g.find('x')+1:]
    b = b[b.find('x')+1:]
    if len(r) ==1:
        r = '0'+r
    if len(g) ==1:
        g = '0'+g
    if len(b) ==1:
        b = '0'+b
    return (r+g+b).upper()

def round(n):
    if n >255: return 255
    if n< 0 : return 0
    return int(n)
##########################################################################

print(rgb(0,0,0))       #,"000000", "testing zero values")
print(rgb(1,2,3))       #,"010203", "testing near zero values")
print(rgb(-20,275,125)) #, "00FF7D", "testing out of range values")
print(rgb(255,255,255)) #, "FFFFFF", "testing max values")
print(rgb(254,253,252)) #, "FEFDFC", "testing near max values")
print(rgb(148,0,211)) #, "9400D3", "testing near max values")

