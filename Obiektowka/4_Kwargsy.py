def string(**dana):
    print(dana)
    print(f'argumenty:{dana.keys()}, wartości: {dana.values()} ')
    print('-'*30)

    for i in dana.items():
        print(i)  #wyświetli daną jako tuple
        print(f'argumenty:{i[0]}, wartości: {i[1]} ')
        print('-' * 30)
string(x=3)

def string1(**dana):
    for klucz, wartość in dana.items():         #kosmetyczne zmiany
        # print(klucz, wartość)
        print(f'argumenty :{klucz}, wartość: {wartość} ')

string1(x=8,y=9,z=7, a='pop', lok='oko')

def foo(**kwargs):
    return ''.join(f'argument: {j}, wartosc: {str(k)}, ' for j,k in kwargs.items())[:-2]

foo(w=3)