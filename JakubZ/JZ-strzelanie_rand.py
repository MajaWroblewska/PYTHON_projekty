import random

def strzal(seria):
    print(f'seria {seria} strzalow: ')
    for i in range(seria):
        a = random.randint(0,99)
        if a > 40 and a < 60:
            print('trafienie!')
        elif a > 95:
            print('HEADSHOT!')
        else:
            print('pudło')



strzal(5)
