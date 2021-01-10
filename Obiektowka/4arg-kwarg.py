def argumenty_arggs_kwargsy(x,y=1, *argsy, **kwargsy):
    print(x,y,argsy,kwargsy)

argumenty_arggs_kwargsy(3, a=7)     #x=3 y=1 arg=() kwarg={'a':7}
argumenty_arggs_kwargsy(3, 7, a=7)  #x=3, y=7, arg=() kwar={a:7}
argumenty_arggs_kwargsy(3, 7,8,a=7)  #x=3 y=7 agr=(8,) kwar={a:7} jak skończą sie argumenty wej to wypełnia arg
argumenty_arggs_kwargsy(3)      #x=3 y=1 arg=() kwarg={}
argumenty_arggs_kwargsy(7,y=53)     #x=7 y=53 arg=() kwarg={}
argumenty_arggs_kwargsy(x=8)        #x=8 y=1 () {}
argumenty_arggs_kwargsy(x=8,b=66)  #x=8 y=1 arg=() kwar={b:66} -niezdefiniowane=arg ,pozycyjne =kwargs
# argumenty_arggs_kwargsy()         # wymagany jest min 1 dana
# argumenty_arggs_kwargsy(x=5, 2)       #pierw bez pozycji, ostatnie pozycyjne
argumenty_arggs_kwargsy(3, y=5,a=7,b=33) #x=3 y=5 arg=() kwarg={a:7 , b:33}