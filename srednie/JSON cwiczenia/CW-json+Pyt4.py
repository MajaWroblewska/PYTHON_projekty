# Pyt 1-Przekonwertuj dane na format JSON
# data = {"key1" : "value1", "key2" : "value2"}
import json
data = {"key3" : "value1", "key2" : "value2"}

jsonData=json.dumps(data, indent=5, sort_keys=True) #
print('Pyt 1-Przekonwertuj data = {"key1" : "value1", "key2" : "value2"} '
      'na format JSON:\n',jsonData)

###############################################################################################################
#Pyt 2-Uzyskaj dostęp do wartości 'key 2' z następującego kodu JSON:
# {"key1": "value1", "key2": "value2"}
import json
danaJson = '''{"key1": "value1", "key2": "value2"}'''

dostep = json.loads(danaJson)
print('Pyt 2-Uzyskaj dostęp do wartości klucza 2 z kodu: {"key1": "value1", "key2": "value2"} \n'
      ,dostep['key2'])

###############################################################################################################
# Pyt 3-Wcięcia (ident) i separator (separators=(',','='))
# danaJson = {"key1" : "value2", "key2" : "value2", "key3" : "value3"}

import json

danaJson = {"key1" : "value2", "key2" : "value2", "key3" : "value3"}
prettyPrintedJson  = json.dumps(danaJson, indent=10, separators=(",", " *+= "),)
print('Pyt 3-Wcięcia i separatory:\n',prettyPrintedJson)

'''
indent= poziom wcięcia (akapit)
separators= zamiana separatora ',' na '=' 
sort_keys= True/ False --> alfabetycznie
'''
###############################################################
#Pyt4- Sortuj klucze alfabetycznie JSON w Pythonie i zapisz je do pliku: Pyt4-slownikJson.json
import json

slownikJson = {"id" : 1, "name" : "value2", "age" : 29}

print('Pyt4- Sortuj klucze JSON w Pythonie i zapisz je do pliku')
print("Started writing JSON data into a file: Pyt4-slownikJson.json")
with open("Pyt4-slownikJson.json", "w") as write_file:
    json.dump(slownikJson,write_file, indent=4, sort_keys=True) #dla dumps slownikJson ma być w "" jak string
print("Done writing JSON data into a file: Pyt4-slownikJson.json")
'''
sort_keys=True ---> sort alfabetyczny
zapis do pliku: Pyt4-slownikJson.json
'''
###############################################################################################################
# Pyt 5-napisz kod, aby wydrukować wartość wynagrodzenia 7000

import json

firma = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payble":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""


data=json.loads(firma)
print('Pyt 5-wynagrodzenie: ',data['company']['employee']['payble']['salary']) #7000
print('Pyt 5-bonus: ',data['company']['employee']['payble']['bonus']) #800
#######################################
# Pyt 6- Zamień obiekt pojazdu na JSON:
'''
class Vehicle:
    def __init__(self, name, engine, price):
        self.name = name
        self.engine = engine
        self.price = price

vehicle = Vehicle("Toyota Rav4", "2.5L", 32000)
'''

import json
from json import JSONEncoder

class Vehicle:
    def __init__(self, name, engine, price):
        self.name = name
        self.engine = engine
        self.price = price

class VehicleEncoder(JSONEncoder):  #dodana klasa konwersji (??nie znam co ??)
    def default(self, obiektX):
        return obiektX.__dict__

vehicle = Vehicle("Toyota Rav4", "2.5L", price=32000)   #zmienna nazwane na koniec a pozycyjne na początek!!!

print('Pyt 6-konwersja na obiekt JSON')
vehicleJson1 = json.dumps(vehicle, indent=5, cls=VehicleEncoder)
vehicleJson2 = json.dumps(vehicle,  cls=VehicleEncoder)
print('z indent=5:\n', vehicleJson1)
print('bez indent=5:\n', vehicleJson2)
print('1-szczegóły obiektu vehicule:', {vehicle.name},vehicle.engine, {vehicle.price}, sep='**')
print('2-szczegóły obiektu vehicule: ',[vehicle.name],vehicle.engine, vehicle.price, sep='**')
print(f'3-szczegóły obiektu vehicule: {vehicle.name} + {vehicle.engine} + {vehicle.price}')
print()
'''
cls=VehicleEncoder --> coś związane z klasą
indent=5 ---> wcięcie-akapit
'''

###############################################################################################################
#Pyt 7 Zamień JSON na obiekt pojazdu
# slownik={"name": "Toyota Rav4", "engine": "2,5 l", "price": 32 000}

import json

class Vehicle:  #standardowa klasa zodpowiednimi polami
    def __init__(self, name, engine, price):
        self.name = name
        self.engine = engine
        self.price = price

def vehicleDecoder(cos):    #funkcja kodująca
        # return Vehicle(cos['price'], cos['name'], cos['price'])    #jak zwrócić obiekt w jakiej kolejności do wyświetlenia
        return Vehicle(cos['name'], cos['engine'], cos['price'])    #jak zwrócić obiekt w jakiej kolejności do wyświetlenia

vehicleObject = json.loads('{ "name": "Toyota Rav4", "engine": "2.5L", "price": 32000 }',
          object_hook=vehicleDecoder,)  #wczytanie json jako obiekt vehicleObj ze slownik={..zadany slownik...} ale w jako str ('slownik')

print("Pyt 7-Zamień następujący JSON na obiekt pojazdu")
print('typ obiektu vehicleObj:',type(vehicleObject))
print("Vehicle - szczegóły:")
print(vehicleObject.name, vehicleObject.engine, vehicleObject.price, sep='--')

'''object_hook=vehicleDecoder -->hak obiektu (??) chyba wskazanie co mamy przerobić/zakodować na obiekt

'''
###############################################################################################################
#Pyt 8-