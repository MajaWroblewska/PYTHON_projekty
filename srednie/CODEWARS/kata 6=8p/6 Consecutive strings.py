# strarr -> tablica ze str
# k -> ilość zlepionych elementów tablicy "strarr"

from pip._vendor.msgpack.fallback import xrange


def longest_consec(strarr, k):
    # print(strarr, k)  # wypisanie danych
    n = len(strarr)     # długość zadanej tablicy
    napis = ''
    end = []    #lista 'k'-elementowych zlepień
    if n == 0 or k > n or k <= 0:   #warunki brzegowe-pósta tab + ilość zlepianie k>dł tablicy +
        napis=''
    else:
        for i in range(len(strarr) - k + 1):    # i to ilość nowych zlepionych elementów po 'k'-elm z tablicy 'strarr'
            su = []
            # print('i=', i)
            for w in range(k):
                # print('w+i=', w + i)
                # print(b[w+i])

                su.append(strarr[w + i])    # 1 pętli=nowa lista zlepionych 'k'-elementów tablicy 'strarr'
                # print(su)

            # print(su) #  końcowa nowa lista zlepionych 'k'-elementów tablicy 'strarr'
            dl = ''.join(su)    #zlepianie 'k'-elementów w jeden
            # print(dl)
            end.append(dl)  #dodawanie do listy
            # print(end)
        # print('--------' * 10)
        end.sort(key=lambda x: len(x), reverse=True)    #sortowanie od najgłuższego
        # print(end)
        napis=end[0]

    return napis

print('-------'*20)
# nie dla wielkich tablic
'''
def longest_consec(strarr, k):
    print(strarr,k)
    n=len(strarr)
    napis=''
    if n==0 or k>n or k<=0:
        napis=""
    elif k==1:
        sor = sorted(strarr, key=lambda x: len(x), reverse=True)
        napis=sor[0]
    elif k==2:
        sor=[]
        for i in range(n-1):
            sor.append(strarr[i]+strarr[i+1])
        print(sor)
        sor=sorted(sor,key=lambda x: len(x),reverse=True)
        napis=sor[0]
    elif k==3:
        sor = []
        for i in range(n - 2):
            sor.append(strarr[i] + strarr[i + 1]+strarr[i+2])
        print(sor)
        sor = sorted(sor, key=lambda x: len(x), reverse=True)
        napis = sor[0]
    elif k==4:
        sor = []
        for i in range(n - (k-1)):
            sor.append(strarr[i] + strarr[i + (k-3)] + strarr[i + (k-2)]+strarr[i+(k-1)])
        print(sor)
        sor = sorted(sor, key=lambda x: len(x), reverse=True)
        napis=sor[0]

    return napis
'''
########################################################################################
def longest_consec(strarr, k):                                              #Kris
    if not strarr or k > len(strarr) or k <= 0:
        return ""
    elif k == 1:
        return max(strarr, key=lambda x: len(x))
    else:
        return max([''.join(strarr[i:i + k]) for i in range(len(strarr) - k+1)], key=lambda x: len(x))
############################################################################################
longest_consec=lambda arr, k: "" if(k<1 or k>len(arr)) else sorted(["".join(arr[i:i+k]) for i in xrange(0,len(arr)-k+1)],key=lambda a:-len(a))[0]
###############################################################################################
def longest_consec(strarr, k):
    result = ""

    if k > 0 and len(strarr) >= k:
        for index in range(len(strarr) - k + 1):
            s = ''.join(strarr[index:index + k])
            if len(s) > len(result):
                result = s

    return result
#########################################################################################
def longest_consec(s, k):
    return max(["".join(s[i:i+k]) for i in range(len(s)-k+1)], key=len) if s and 0 < k <= len(s) else ""
################################################################################################
def longest_consec(strarr, k):
    # Make sure that k is greater than zero and less that the
    # length of the array of strings. Otherwise return an empty string
    if k <= 0 or k > len(strarr):
        return ''

    # Finding the longest string consisting of k consecutive
    # strings is equivalent to finding the maximum sum of
    # k consecutive elements of an array that represents the
    # lengths of an array of strings.

    # star_lengths represents a list of lengths of the initial
    # array of strings.
    starr_lengths = list(map(len, strarr))
    # Find the maximum sum of k consecutive elements
    # requires keeping a temperary maximum length.
    temp_max_len = 0
    # We also need to keep the position of the first element of
    # each group.
    position = 0

    # Scan the whole list of lengths except the final k elements
    for p in range(len(starr_lengths) - (k - 1)):
        # We need to find the sum of the current set of elements
        # starting at position p
        set_sum = 0
        for i in range(k):
            set_sum += starr_lengths[p + i]

        if set_sum > temp_max_len:
            temp_max_len = set_sum
            position = p

    return ''.join([s for s in strarr[position:position + k]])
#######################################################################################
def longest_consec(strarr, k):
    if (len(strarr) == 0 or k <= 0) or len(strarr) < k:
        return ""
    lst = [''.join(strarr[i:i+k]) for i in xrange(len(strarr))] #xrange???
    return max(lst, key= lambda x: len(x))
#######################################################################################
def longest_consec(s, k):
    n = len(s)
    if n == 0 or k > n or k <= 0:
        return ''
    return sorted([''.join(s[i:i+k]) for i in range(0, n-k+1)], key=len, reverse=True)[0]
####################################################################################################
#Take the array of strings.
#FInd the length of the array.
#The number of consecutive strings = n - k + 1.

def longest_consec(strarr, k):
    n = len(strarr)
    var = []    #create a list to contain the different strings.
    if n == 0 or k > n or k <= 0: #Some failure conditions.
        return ""

    else:
        c = n - k + 1    #A control variable. Contains the number of possible strings formed by concatenating k consecutive strings.
        for i in range(c):  #Loop to set default element of the list to empty strings: seeding it basically.
            var.append("")
        for i in range(c):  #Outer loop, controls the individual elements of the list.
            for j in range(i,(i+k)):  #Inner loop, that is used to make each element of the list a cocatenation of some set of consecutive strings.
                var[i] += strarr[j]

    max = var[0]    #Variable to keep count of the longest string found so far.
    for i in range(1,c):    #Checks if string is longer than current maximum. If yes, resets current maximum.
        if len(var[i]) > len(max):
            max = var[i]

    return max
##############################################################################################################
def longest_consec(strarr, k):
    length = len(strarr)
    if not length or k > length or k <= 0:
        return ""
    else:
        lst = [''.join(strarr[i:i+k]) for i in range(length)]
        return max(lst, key=len)
###############################################################################################
def longest_consec(strarr, k):
    return max([''.join(tuple) for tuple in zip(*[strarr[i:] for i in range(k)])] + [''], key=len)
#####################################################################################################

# print(longest_consec(["1", "22", "333", "4444", "55555", "666666",'7777777','88888888','999999999','0000000000'], 7))    # "abigail theta"

# print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2))    # "abigail theta"
# print(longest_consec(["ejjjjmmtthh2", "zxxuueeg5", "aanlljrrrxx3", "dqqqaaabbb4", "oocccffuucccjjjkkkjyyyeehh1"], 1))    #"oocccffuucccjjjkkkjyyyeehh1"
# print(longest_consec([], 3)) # ""
# print(longest_consec(["itvayloxrp3", "wkppqsztdkmvcuwvereiupccauycnjutlv1", "vweqilsfytihvrzlaodfixoyxvyuyvgpck2"], 2)) #  "wkppqsztdkmvcuwvereiupccauycnjutlv1 vweqilsfytihvrzlaodfixoyxvyuyvgpck2"
# print(longest_consec(["wlwsasphmxx1", "owiaxujylentrklctozmymu2", "wpgozvxxiu3"], 2))   # "wlwsasphmxx owiaxujylentrklctozmymu")
# print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], -2)) # ""
print(longest_consec(["it", "wkppv", "ixoyx", "3452", "zzzzzzzzzzzz"], 3)) # "ixoyx3452zzzzzzzzzzzz"
print(longest_consec(["it", "wkppv", "ixoyx", "3452", "zzzzzzzzzzzz"], 15))    # ""
# print(longest_consec(["it", "wkppv", "ixoyx", "3452", "zzzzzzzzzzzz"], 0) )    # ""

##################################################################################################################3
'''
# próba 
k=5

a=["1", "22", "333", "4444", "55555", "666666",'7777777','88888888','999999999','0000000000']
b=["1a", "2b", "3cc", "4ddd", "5eeee", "6fffff",'7gggggg','8hhhhhhh','9iiiiiiii','0jjjjjjjjj']
print(a)
print('len(a)= ',len(a))
print('len(a)-k+1= ', len(a)-k+1)
print('-'.join(a))
                                                # for i,j in enumerate(a):
                                                    # print(i,j)
end=[]
for i in range(len(a)-k+1):
    su=[]
    print('i=',i)
    for w in range(k):
        print('w+i=',w+i)
        # print(b[w+i])

        su.append(a[w+i])

        # print(su)

    # print(su)
    dl=''.join(su)
    # print(dl)
    end.append(dl)
    print(end)
print('--------'*10)
end.sort(key=lambda x: len(x), reverse=True)
print(end)
print(end[0])
'''
a=["1", "22", "333", "4444", "55555", "666666",'7777777','88888888','999999999','0000000000']
# print(''.join(a[1:7:2]))