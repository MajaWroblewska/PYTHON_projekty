def set_alarm(employed, vacation):
    if employed == True and vacation == False:
        result = True
    else:
        result =False
    return result

print(set_alarm(True,False))
print(set_alarm(False,False))