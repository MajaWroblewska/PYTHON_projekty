def first_non_consecutive(arr):         #Maja x2
    for i in range(len(arr)):
        for j in range(len(arr)-1-i):
            if not arr[j]==arr[j+1]-1:
                return (arr[j+1])

# def first_non_consecutive(arr):
#     for i in range(len(arr)-1):
#             if not arr[i]==arr[i+1]-1:
#                 return (arr[i+1])

def first_non_consecutive(arr):
    for b in range(len(arr) - 1):
        if arr[b + 1] - arr[b] != 1:
            return arr[b + 1]
#################################################################
def first_non_consecutive(arr):
    if not arr: return 0
    for i, x in enumerate(arr[:-1]):
        if x + 1 != arr[i + 1]:
            return arr[i + 1]

###########################################
def first_non_consecutive(arr):
    for i in range(1, len(arr)):
        if arr[i] - arr[i-1] > 1:
            return arr[i]

############################################
def first_non_consecutive(arr):     #!!!!!!!!!!!!!!!!!!!super
    for i, v in enumerate(arr, arr[0]):
        print(i,v)
        if v != i:
            return v

###################################################
def first_non_consecutive(arr): #???? zip i abs
    for i, j in zip(arr, arr[1:]):
        if abs(j-i) > 1:
            return j
    return None
#########################################################
def first_non_consecutive(a):       #????
    return [e for i,e in enumerate(a + [None]) if e != a[0] + i][0]
###########################################################


print(first_non_consecutive([1,2,3,4,6,7,8]))  # 6)
print(first_non_consecutive([1,2,3,4,5,6,7,8]))  # None)
print(first_non_consecutive([4,6,7,8,9,11])) # 6)
print(first_non_consecutive([4,5,6,7,8,9,11]))   # 11)
print(first_non_consecutive([31,32]))    # None)
print(first_non_consecutive([-3,-2,0,1]))    # 0)
print(first_non_consecutive([-5,-4,-3,-1]))  # -1)
print(first_non_consecutive([7,8,9,11,12,13]))  # 11)