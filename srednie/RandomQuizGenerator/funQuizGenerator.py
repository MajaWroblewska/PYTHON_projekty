# Tworzy 35 różnych wersji quizu z 50 pytaniami i odpowiedziami w formie A/B/C/D
# utwożonymi w losowej kolejności wraz z plikiem z kluczem odpowiedzi

import random

# dane do quizu -> słownik = {stan: stolica} - 50 stanów
# key - nazwa stanów USA
# value - stolica stanu

capitals = {
    'Alabama':'Montegomery', 'Alaska':'Juneu', 'Arizona':'Phoenix', 'Arkansas':'Little Rock','Kalifornia':'Sacramento',
    'Kolorado':'Denver', 'Connecticut':'Hartford', 'Delaware':'Dover','Floryda':'Tallahassee', 'Georgia':'Atlanta',
    'Hawaje':'Honolulu', 'Idaho':'Boise', 'Ilinois':'Springfield', 'Indiana': 'Indianapolis','Iowa':'Des Moines',
    'Kansas':'Topeka','Kentucky':'Frankfort', 'Luizjana':'Baton Rouge', 'Maine':'Augusta','Marylnd':'Annapolis',
    'Massachusetts':'Boston', 'Michigen':'Lansing', 'Minnesota':'Saint Paul', 'Mississipi':'Jackson', 'Missouri':'Jefferson City',
    'Montana':'Heena', 'Nebraska':'Lincoln', 'Nevada':'Carson City', 'New Hampshire':'Concord', 'New Jersey':'Trenton',
    'Nowy Meksyk':'Santa Fe','Nowy Jork': 'Alabama', 'Karolina Północna': 'Raleigt', 'DakotaPółnocna':'Bismarck', 'Ohio':'Columus',
    'Oklahoma':'Oklahoma City', 'Oregon':'Salem', 'Pensylwania':'Harrisburg', 'Rhode Island':'Providence','Karolina Południowa':'Columbia',
    'Dakota Południowa':'Pierre', 'Tennessee':'Nashville', 'Teksas': 'Austin', 'Utah':'Salt Like City', 'Vermont':'Montpelier',
    'Wirginia':'Richmond', 'Waszyngton':'Olimpia', 'Wirginia Zachodnia':'Charlston', 'Wisconsis':'Madison','Wyoming':'Cheyenne'
    }

slownik = {1:'a',2:'b',3:'c',4:'d',5:'e',6:'f'}

# dictionary - dane w postaci słownika
# stunent - ilość genreowanych plików
# questions - ilość pytań w teście

def QuizGenarator(dictionary, student,questions):
    if questions > len(dictionary):
        print(f'Maksymalna liczba pytań: {len(dictionary)}')
    else:
    ##1
    # generowanie 35 plików quizu -dla 35 ucznów# student - ilość uczniów:
    ## for quizNum in range(6):
        for quizNum in range(student):
            # utworzenie plików pytań-quizeFile oraz pliku odpowiedzi-answwerKeyFile
            quizeFile = open(f'capitalsQuiz{quizNum + 1}.txt', 'w', encoding='utf-8')
            answwerKeyFile = open(f'capitalsQuiz_Answers{quizNum + 1}.txt', 'w', encoding='utf-8')

            # zapis nagłówków w pliku pytań-quizeFile
            quizeFile.write('Imię i nazwisko:'.ljust(70,'_'))
            quizeFile.write('\n\nData:'.ljust(72,'_'))
            quizeFile.write('\n\nKlasa:'.ljust(72,'_'))
            quizeFile.write('\n\n\n')
            quizeFile.write(f'Quiz stolic stanów USA nr {quizNum + 1}'.center(70, '_'))
            quizeFile.write('\n')
    ##2
    # lista wszystkich możliwych stanów(pytań) -> capitals.key
    # lista wszystkich możliwych odpowiedzi -> capitals.value
            states = list(dictionary.keys())
            # answer = list(capitals.values())
    # losowe ustalonej kolejności stanów USA na zadanej liście -> states
            random.shuffle(states)
            ## states -> lista wymieszanych ptyań (stanów)

    ##3
    # questions-ilość pytań w quizie - max tyle ile jest key w słowniku capitals
    # iteracja przez 50 stanów i utworzenie 50 pytania dotyczącego każdego z nich
            for questionNum in range(questions):
    # przygotowanie listy 1 prawidłowej i 3 błędnych odpowiedzi
                corectAnswer = dictionary[states[questionNum]]    #   to str
                # print(type(corectAnswer))
                wrongAnswer = list(dictionary.values())           #   lista wszystkich odpowiedzi
                del wrongAnswer[wrongAnswer.index(corectAnswer)]    # usunięcie dobrej odp z listy wszystkich złych odpowiedzi
                ## wrongAnswer ->  # lista tylko złych odpowiedzi
                ## corectAnswer -> # str poprawnej odp

    # losowanie tylko 3 błednych odpowiedzi
                wrongAnswer = random.sample(wrongAnswer,3)
                ## wrongAnswer to lista 3 złych odp

    # możliwe odpowiedzi = 1 dobra + 3 złe
                answerOptions = [corectAnswer] + wrongAnswer
                ## answerOptions -> lista odp w kolejności 1 ok + 3 wrong)
    # wymieszanie 4 odpowiedzi
                random.shuffle(answerOptions)
                ## answerOptions -> lista wymiesanych odp

    ##4
    # zapis pytania i odpowiedzi w pliku quizu
                quizeFile.write(f'\n\n{questionNum+1}. Co jest stolicą stanu {states[questionNum]}?')
    ## utworzenie odp w postaci A/B/C/D
                for i in range(4):
                    quizeFile.write(f'\n\t {"ABCD"[i]}. {answerOptions[i]}')
                    # quizeFile.write('\n')

    # zapis odpowiedzi w pliku answwerKeyFile dla wygenerowanego pytania
                answwerKeyFile.write(f'{questionNum+1}. {"ABCD"[answerOptions.index(corectAnswer)]}\n')
                # print([answerOptions.index(corectAnswer)])
    ##5
    # zamknięcie plików
        quizeFile.close()
        answwerKeyFile.close()

QuizGenarator(slownik,2,6)
QuizGenarator(capitals,2,3)


