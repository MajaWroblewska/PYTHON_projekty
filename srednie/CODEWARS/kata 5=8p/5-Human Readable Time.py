# przlicznik sekund na format HH:MM:SS

def make_readable(seconds):
    sek=seconds/60
    sekundy=seconds//60
    # print('sek=',sek)
    # print('sekundy ',sekundy)
    SS=round((sek-seconds//60)*60)  #zaokrąglić w górę co poprzecinku bo int obcina to co jest po przecinku
    # print('SS=',SS)
    # print('pozostałe sekundy1: ', sekundy)

    minu= sekundy/60
    minuty=sekundy//60
    # print('minu ',minu)
    # print('minity ' ,minuty)
    MM=round((minu-minuty)*60)  #zaokrąglić w górę co poprzecinku bo int obcina to co jest po przecinku
    # print('MM=',MM)
    # print('pozostałe sekundy2: ',minuty)
    HH=minuty
    # return (int(sek))
    if SS<10:
        SS='0'+ str(SS)
    if MM<10:
        MM='0'+ str(MM)
    if HH<10:
        HH='0'+ str(HH)

    return f'{(HH)}:{(MM)}:{(SS)}'

#####################################
# Maja 2 88%60=28 ->reszta z dzielenia


#############################################################
def make_readable(s):
    return '{:02}:{:02}:{:02}'.format(s / 3600, s / 60 % 60, s % 60)
##########################################################
def make_readable(seconds):
    s = str(seconds % 60).zfill(2)
    m = str((seconds // 60 )%60).zfill(2)
    h = str((seconds //3600 )% 100).zfill(2)
    return f"{h}:{m}:{s}"
###########################################################



#######################################################
def make_readable(seconds):
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    return "{:02}:{:02}:{:02}".format(h, m ,s)

def make_readable(seconds):
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)
    return '{:0>2}:{:0>2}:{:0>2}'.format(hours, minutes, seconds)
###################################################################
def make_readable(seconds):
    h= seconds/60**2
    m= (seconds%60**2)/60
    s= (seconds%60**2%60)
    return "%02d:%02d:%02d" % (h, m, s)
########################################################
def make_readable(seconds):
    '''Returns the time in `seconds` as a human-readable format (HH:MM:SS).
    '''
    minute, hour = 60, 60 ** 2
    return "%02d:%02d:%02d" % (
        seconds / hour,
        seconds % hour / minute,
        seconds % hour % minute
    )
################################################################
def make_readable(seconds):
    SS = seconds%60
    MM=int((seconds-SS)/60)%60
    HH=int(((seconds-SS)/3600))

    if SS < 10:
        SS = '0' + str(SS)
    if MM < 10:
        MM = '0' + str(MM)
    if HH < 10:
        HH = '0' + str(HH)

    return f'{(HH)}:{(MM)}:{(SS)}'


print(make_readable(0)) #, "00:00:00")
print(make_readable(5)) #, "00:00:05")
print(make_readable(60)) #, "00:01:00")
print(make_readable(86399)) #, "23:59:59")
print(make_readable(359999)) #, "99:59:59")
print(make_readable(65605)) #, "18:13:25")
print(make_readable(65665)) #, "18:14:25")

