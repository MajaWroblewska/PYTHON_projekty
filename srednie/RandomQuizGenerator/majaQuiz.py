# Tworzy 35 różnych wersji quizu z 50 pytaniami i odpowiedziami w formie A/B/C/D
# utwożonymi w losowej kolejności wraz z plikiem z kluczem odpowiedzi

import random

# dane do quizu - słownik = {stan: stolica} - 50stanów
# key - nazwa stanów USA
# value - stolica stanu

# capitals = {
#     'Alabama': 'Montegomery',
#     'Alaska' : 'Juneu',
#     'Arizona' : 'Phoenix',
#     'Arkansas' : 'Little Rock'
# }

capitals = {1:'a',2:'b',3:'c',4:'d',5:'e',6:'f'}

##1
# generowanie 35 plików quizu -dla 35 ucznów
for quizNum in range(6):
    # utworzenie plików pytań-quizeFile oraz pliku odpowiedzi-answwerKeyFile

    with open(f'capitalsQuiz{quizNum + 1}.txt', 'w', encoding='utf-8') as quizeFile:

        # zapis nagłówków w pliku pytań-quizeFile
        quizeFile.write('Imię i nazwisko:\n\nData:_________\n\nKlasa:\n\n\n')
        quizeFile.write(f'Quiz stolic stanów USA nr {quizNum + 1}'.center(150, '-'))
        quizeFile.write('\n')

        answerKeyFile = open(f'capitalsQuiz_Answers{quizNum + 1}.txt', 'w', encoding='utf-8')
    ##2
    # lista wszystkich możliwych stanów(pytań) - capitals.key oraz wszystkich możliwych odpowiedzi - capitals.value
        states = list(capitals.keys())
        answer = list(capitals.values())
    # losowe ustalonej kolejności stanów USA na przekazanej liście stanów -states
        random.shuffle(states)
        print('wylosowano kolejność: ', states)
    ##3

        # iteracja przez 50 stanów i utworzenie 50 pytania dotyczącego każdego z nich
        # 4 to tyle ile chcemy stworzyć ptyań (max tyle ile jest key w słowniku capitals)
        for questionNum in range(5):
            print('pyt nr.',questionNum+1)
            # print(questionNum+1)- numer pytania

        # przygotowanie listy 1 prawidłowej i 3 błędnych odpowiedzi
            corectAnswer = capitals[states[questionNum]]    #to str
            print('dobra odp:',corectAnswer, type(corectAnswer))
            wrongAnswer = list(capitals.values()) #lista wszystkich odpowiedzi
            # print(wrongAnswer)
            del wrongAnswer[wrongAnswer.index(corectAnswer)]
            print('wszystkie złe odpowiedzi:',wrongAnswer)  # lista tyllko złych odpowiedzi

        # losowanie tylko 3 błednych odpowiedzi
            wrongAnswer = random.sample(wrongAnswer,3)
            print('3 losowe złe odp: ',wrongAnswer)

        # możliwe odpowiedzi = 1 dobra + 3 złe
            answerOptions = list(corectAnswer) + wrongAnswer
            print('odp w kolejności dodania:',answerOptions)
        # wymieszanie 4 odpowiedzi
            random.shuffle(answerOptions)
            print('wymieszane 4 odp:',answerOptions)

    ##4
        # zapis pytania i odpowiedzi w pliku quizu
            quizeFile.write(f'\n\n{questionNum+1}. Co jest stolicą stanu {states[questionNum]}?')
            for i in range(4):
                quizeFile.write(f'\n\t {"ABCD"[i]}. {answerOptions[i]}')
                # quizeFile.write('\n')

            # zapis odpowiedzi w pliku answwerKeyFile dla wygenerowanego pytania


        answerKeyFile.write(f'{questionNum + 1}. {"ABCD"[answerOptions.index(corectAnswer)]}\n')
##5
# zamknięcie plików
# quizeFile.close()
            answwerKeyFile.close()




