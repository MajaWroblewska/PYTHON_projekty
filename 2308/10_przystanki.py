# test    number([[3, 0], [9, 1], [4, 8], [12, 2], [6, 1], [7, 8]]), 21)

def number(bus_stops):
    suma1 = 0
    suma2 = 0
    for i in bus_stops:
        print('Wsiadło:', i[0])
        print('Wysiadło:', i[1])
        suma1 = suma1 + i[0]
        suma2 = suma2 + i[1]
        print(suma1)
        print(suma2)

        zostalo = suma1 - suma2
        print('Zostało:', zostalo)
    return zostalo

bus_stop=([[3, 0], [9, 1], [4, 8], [12, 2], [6, 1], [7, 8]])
number(bus_stop)

