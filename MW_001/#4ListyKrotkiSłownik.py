# -*- coding: utf-8 -*-

a=R'"maja"i',r'm i \n"'
print(a)

#lista i jej format
lista= [3,4,'txt', False]
print('lista 1: {} \nformat 1 to: {}'.format(lista, type(lista)))

#zmiany w liscie
lista[3]=4
print('\nlista 1 po zmianie poz3=4 {}'.format(lista))

#krotki
z=(1,2,3,'mama',"ka")
print('\nkrotka  {} \nformat {}'.format(z,type(z)))
#print('Typ z to {}'.format((type(z))))
print('krotka poz 2 to: {}'.format(z[2]))
print('!!!! elementów krotki nie da się zmienić lecz tylko wyświetlić!!!!!')

#słownik
slownik = { "kawa": "czarna", "herbata" : "zielona", "cukier kostka": 4, 0: "zero"}
print('\nsłownik 1 to: {}'.format(slownik))
print('wartość w słowniku dla klucza herbata to: {}'.format(slownik["herbata"]))
print(slownik["herbata"])

print('wartość w słowniku dla klucza "0" to: {}'.format(slownik[0]))
print(slownik[0])

#dodawanie elementu do słownika
slownik[1] = "jeden"
slownik["mleko"]=True
#slownik = { "kawa": "czarna", "herbata" : "zielona", "cukier kostka": 4, 0: "zero", 1: "jeden" }
print('\ndodanie elementu do słownika klucz 1="jeden" {}'.format(slownik))
print('\nformat słownika to: {}'.format(type(slownik)))

# wyświetlanie kluczy slownik.keys()
print('\nklucze słownika to: {}'.format(slownik.keys()))
print(slownik.keys())

# wyświetlanie wartości
print('\nwartości słownika to: {}'.format(slownik.values()))
print(slownik.values())

#zamiena kluczy/wartości słownika na listę
a=list(slownik.keys())
print("\nklucze słownika zamienione na listę to: {}".format(a))
print("klucze słownika zamienione na listę to:{}",a)

print("\nwartości słownika zamienione na listę to: {}".format(list(slownik.values())))

print(list(slownik.keys()))

#zamiana słownika na listę - wypisze klucze
print('\nsłownik zamieniony na liste - wypisuje tylko klucze',list(slownik))


print("Moja {} o wadze {}g ma ok. {} kcal i {:.5f} węglowodanów".format('czekolada', 100, 545, 58.543210))
print('\nklucze :{}'.fotmat(list(slownik.keys())))
