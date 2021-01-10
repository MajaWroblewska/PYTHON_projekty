'''Zadanie 3*
Wyobraź sobie, że jesteś bioinformatykiem i otrzymujesz kod genetyczny do analizy.

Kod DNA składa się z 4 zasad azotowych: adeniny(A), cytozyny(D), guaniny(G), tyminy(T).
Idealny kod DNA wygląda następująco: TGCACGATCATGTCTACTATCCTCTCTATGGTGGGGTT.
Zdarza się, jednak, że kod zawiera małe jak i duże litery.
Kolejny problem to maszyny sekwencjonujące nie są wolne od błędów.
W zależności od maszyny błędy sekwencjonowania mogą zostać zamienione na znak – czy literę N.

W jaki sposób łatwo rozpoznasz, że otrzymany kod DNA zawiera błędy?
Dotarł do ciebie następujący kod genetyczny

Skopiuj kod genetyczny do swojego skryptu i zapisz jako DNA = ACTG...

Policz ile razy występuje w kodzie każda zasada azotowa – adenina, cytozyna, guanina, tymina.
Na pewno zauważysz błędy sekwencjonowania – znaki, które nie są żadną z 4 zasad.
W panice szukasz pliku z dokumentacją.
Ufff… znalazł się!
Co więcej, w dokumentacji pojawił się następujący zapis:

gdy jakość sekwencji nie pozwala dokładnie odczytać rodzaju zasady azotowej wstawiany jest znak „-”
Natomiast, gdy laser sczytujący ześlizgnie się, wstawiane są litery „N”,
jednocześnie ostatnia wartość zasady jest ponownie odczytywana bez ubytku zasady w tym miejscu.

Co za przydatna informacja!

+Policz ile razy występuje w kodzie każda zasada azotowa – adenina, cytozyna, guanina, tymina.
+Policz wystąpienia sekwencji GAGA i zamień je na AGAG
+Znajdź miejsce (indeks) w łańcuchu, gdzie występuje 7 guanin z rzędu
+Znajdź miejsce (indeks) , gdzie od końca łańcucha występuje 6 cytozyn
+Policz ile razy w kodzie pojawiła się sekwencja CTGAAA
+W sekwencji CTGAAA czasem mutuje ostania litera A, wówczas jakość ostatniej litery może być wątplia.
 Ile sekwencji znajdziesz, jeśli weźmiesz pod uwagę wątpliwą, ostatnią adeninę?
+Oczyść DNA z wszystkich błędów.
+Na podstawie czystej nici utwórz odpowiadającą jej nić RNA
(nić RNA w miejscu tyminy będzie mieć uracyl (U))'''


DNA = "ACTGTGCTGACTCCCGGTGCTGCCGCTGCCATAGCTAAAGCCCGGGTCCTGGTAGGCAGGCGGGAAGCAG \
GGTGGGGGTCCCGGGTACTGGTAGGGGTAGCCCTGACCCAGAGGCGGGGGGGCAGCCGGGTGGGGCAGCG \
GGGCCAGCGTGTCCTGAA-CGAAGTCCCACTGGAGCCACTGTTGAGGTTCAGGGTGGCGAGATCTGGCGG \
NNNAGGGTAGGTGAGGGCCGCGGAGGGGCCTCCGGCGTTCCCCTCCCCCCCGCCCTGAAACCCGAAGCCC \
CCACTCACTGCTGCAGAGATCCCCTGAAAACGTAGTAGCACTGCTCgagacAGGTGATCTGTTGACCTGA \
AACCGCAGGAAGCCGTGCTTCAGCAAGCTGCTGGCGTACTTCCGGGCCT---GCCGCTCCTTGAAGCCCT \
CCACGTGTGTGTACAGCCAGTCCACCACGTCCGCCCCTGGCCGGCACCAGCGGTCAGCCCGCAGCCTCGA \
GGCAAGCAGCCCTGCCNNTGGCACTATCCGC-CGCGGGGACGGCCACTCACCGATGACGGCATNNGCGAT \
GGTGATCTTGAGCCACATGCGGTCGCGGATCTCCAGTCCCGAG---GGCAGCTGCATGACCCGGACGACG \
GCGCTCATGTCACtcaccgtcagcggcgcctcttccagCCAGCTCTGCAAAGCACAGACAGCCCCGCTTC \
GCCCCAGCATCTGAAAGCGGGGGACTCggcAcgCTGCACCCCCAGGGGAGCCTCTGGGCAGAGCCTGCGC \
CAGGGCGCAAGCTGGACGGTGCGTGACAGCAGGGCCCCGGCCCACTGCAGGATGCACCCCCGTGAGGCTG \
GGGCGTGAGCAGGGGGGTTGGACAtttAGTCTCCCACTTCTACAGACACTTTTCATCAGGATCCTAGGCA \
CAAACTGGGCTGAAACCCCACCCTGCAGACCAGGAAGTAATGAGAACAGGGCAGGCCCCTTCCCCTCNNC \
GCATGCC-CACCCGAGAGCGCAGGCTGTTAGTCGTGTTAATGGCAGGAAGCAGAATGGAGACCTGGCCCC \
TGCCTCTGAA-CCGTGGGTGCTCaactggctaGCCCTACGTACATCCCCTGTTCcggCCAACACACAGAC \
ATGAGCAGGATGGGCTGCACAAGGTGGGCACGGGTGCCTGTGCACACGTCTGTGCAGGGAGTTGGGGACA \
GGCAACACACACGTGTCACAGCCCCATGACGGggcaattgcGCCATGCTGGCTGAATGGCAGAGACGCCC \
CTCCAAGCCTCGGTTTCTGCTGGGGCCCTCAGGAGCTGCCACTTACGTGGAGCACCAGGCACGGAGCTGG \
TTAGTGAGGAGGAGCTGGTGCGCGTGACGGCGCTGGAGCAGGGACTCGTACCGTAGCGGGGCAGGGCNNN \
TGTCAGTGCCGCCGTGTGGtcagcggcgatCGGCG-GGTCGATGGGCCGCACCGGGTCAGCTGGGTGNAG \
ACACGTGGCGATGACAGGCGGACAGATGGACAGGGTGGGAGGGCAGGGTGCAGGGCACAGAGGAGAGAGG \
CCTTCAGGCTAGGTAGGCGCCCCCTCCCCATCCCGccccGTGTGCCCCGAGGGCCACTCACCCCGTGGGA \
CGGTGAAGTAGCTTCG-GGCGTTGGGTCCAGCACTTGGCCACAGTGAGGCTGNAAATGGCTGCAGGAACG \
GTGGTCCCCCCGCAAGGCCCCCATGGTCCCACCTCCCTGCCTGGCCCCTCCCGCTCCAGCGCCNCCAGCC"

#oryginalny kod DNA
print(DNA)
# Zamiana kodu DNA małe na duże
DNA = DNA.upper()
print('DNA tylko dużymi literami\n', DNA)

# Czyszczenie DNA z wszystkich błędów-spacji i N.
DNA = DNA.replace(" ", "")  # bez spacji
DNA = DNA.replace("N", "")  # bez N
DNA = DNA.replace("-", "")  # bez -
print('DNA bez spacij i błednego N\n',DNA)

# Policz ile razy występuje w kodzie każda zasada azotowa – adenina, cytozyna, guanina, tymina.
A = DNA.count("A")
C = DNA.count("C")
G = DNA.count("G")
T = DNA.count("T")
print("adenina: {}, cytozyna: {}, guanina: {}, tymina: {}".format(A, C, G, T))

# Policz wystąpienia sekwencji GAGA i zamień je na AGAG
GAGA = DNA.count("GAGA")
print("Liczba wystąpień sekw. GAGA to", GAGA)

# Zamiana sekwencji GAGA na AGAG
DNA = DNA.replace("GAGA", "AGAG")

# Znajdź miejsce (indeks) w łańcuchu, gdzie występuje 7 guanin z rzędu od początku
G7=DNA.find("GGGGGGG")
print('7 Guanin pod rząd występuję w miejscu (licząc od 0):\n', G7)

# Znajdź miejsce (indeks) , gdzie występuje 6  cytozyn od końca łańcucha
C6=DNA.rfind("CCCCCC")
print('6 Cytozyn pod rząd występuję w miejscu (licząc od 0):\n', C6)

# Ilość wystpień sekw. CTGAAA
CTGAAA = DNA.count("CTGAAA")
print("Liczba wystąpień sekw. CTGAAA", CTGAAA)

# W sekwencji CTGAAA czasem mutuje ostania litera A, wówczas jakość ostatniej litery może być wątplia.
# Ile sekwencji znajdziesz, jeśli weźmiesz pod uwagę wątpliwą, ostatnią adeninę?
CTGAA_ = DNA.count("CTGAA-")
print("Liczba wystąpień sekw. CTGAAA i CTGAA-", CTGAAA + CTGAA_) #czemu CTGAA(-)?

# Na podstawie czystej nici utwórz odpowiadającą jej nić RNA (nić RNA w miejscu tyminy będzie mieć uracyl (U))
''' G ->C
    C ->G
    T ->A
    A ->Uracyl
'''

DNA = DNA.replace("-", "") #kasowanie -
RNA = DNA.replace("G","C")# kolejność zmian psuje końcowy efekt->inny sposób na transkrypcje DNA na RNA!!!!!!!!
RNA = DNA.replace("C","G")
RNA = DNA.replace("T","A")
RNA = DNA.replace("A","U")
print('DNA to\n',DNA)
print('RNA z nici DNA to\n',RNA)