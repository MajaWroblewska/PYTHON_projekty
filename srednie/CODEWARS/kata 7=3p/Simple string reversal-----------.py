def solve(s):
    lista=list(s)
    for chain in s:
        # print(chain)
        # print('*',lista[::-1])
        if chain.isspace():
            print('--')
        else:
            for i in range(len(lista)):
                continue
            print(lista[::-1][-i:])
    print(s)

def solve(s):
    lista=list(s)
    for chain in s:
        # print(chain)
        # print('*',lista[::-1])
        if chain.isspace():
            print('--')
        else:
            for i in range(len(lista)):
                continue
            print(lista[:][:i+1])
    print(s)



# print(solve("codewars"))    #>>"srawedoc"
# print(solve("your code"))   #>>"edoc ruoy"
# print(solve("your code rocks")) #>>"skco redo cruoy"
solve("i love codewars") #>>"s rawe docevoli"


