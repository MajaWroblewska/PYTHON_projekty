def open_or_senior(data):
    out=[]
    for i in data:
        if i[0]>=55 and i[1]>7:
            result='Senior'
            out.append(result)
        else:
            result='Open'
            out.append(result)

    return out
##############################################################
def openOrSenior(data):
  return ["Senior" if age >= 55 and handicap >= 8 else "Open" for (age, handicap) in data]

######################################################################################
def openOrSenior(members):
    return ["Senior" if m[0]>54 and m[1]>7 else "Open" for m in members]
#######################################################################################
def openOrSenior(data):
    list = []
    for age, hcap in data:

        if age >= 55 and hcap > 7:
            list.append('Senior')

        else:
            list.append('Open')

    return list
####################################################################################
def openOrSenior(data):
    return map(lambda d: 'Senior' if d[0] >= 55 and d[1] > 7 else 'Open', data)
###################################################################################



print(open_or_senior([(45, 12),(55,21),(19, -2),(104, 20)])) #,['Open', 'Senior', 'Open', 'Senior'])
print(open_or_senior([(16, 23),(73,1),(56, 20),(1, -1)]))    #,['Open', 'Open', 'Senior', 'Open'])