# lista -> str
# wypisanie z listy liczby jako zakresy liczbowe np[1,2,3,4,8] >>'1-4,8'

def solution(args):
    # print(len(args))
    for i in range(len(args)):
        for j in range(len(args) - i - 1):
            if args[j] == args[j + 1]+1:
                print(args[j])
        # print(i,j)

        # print(i+1)





print(solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]))   #'-6,-3-1,3-5,7-11,14,15,17-20'
# print(solution([-3, -2, -1, 2, 10, 15, 16, 18, 19, 20]))    #, '-3--1,2,10,15,16,18-20'