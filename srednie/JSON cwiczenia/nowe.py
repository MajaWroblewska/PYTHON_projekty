# Pyt 8 - Sprawdź, czy poniższy plik json jest prawidłowy lub nieprawidłowy. Jeśli jest nieprawidłowy, popraw go
#czy jest poprawny zapis JSON?
'''
{
   "company": {
      "
         worker ": { 
         "name": "emma", "payble": {
            "salary": 7000
            "bonus": 800
         }
      }
   }
}
'''

import json

def czyJSON(jsonX):
    try:
        json.loads(jsonX)
    except ValueError as err:
        return False
    return True

SprawdzCzyJsonData = '''{
   "company": 
   {
   "worker ": 
         {
         "name": "emma", 
         "payble": 
         {
            "salary": 7000,
            "bonus": 800
         }
      }
   }
}
'''
# SprawdzCzyJsonData = """{ "company":{ "employee":{ "name":"emma", "payble":{ "salary":7000, "bonus":800} } } }""" #wstaw przecinek po 7000,
isValid = czyJSON(SprawdzCzyJsonData)

print('Pyt 8 - Sprawdź, czy poniższy plik json jest prawidłowy lub nieprawidłowy. Jeśli jest nieprawidłowy, popraw go')
print("Czy zapis jest poprawny w JSON:", isValid)

#w terminalu wpisz:
# echo { "company":{ "employee":{ "name":"emma", "payble":{ "salary":7000, "bonus":800} } } } | python -m json.tool
# zwoci: Expecting ',' delimiter: line 1 column 68 (char 67) lub zapis JSON jeśli jest OKExpecting ',' delimiter: line 1 column 68 (char 67)

#############################################################################################################################

#Pyt 9- Przeanalizuj następujący kod JSON, aby uzyskać wszystkie wartości klucza „nazwa” w tablicy
'''
[ 
   { 
      "id":1,
      "name":"name1",
      "color":[ 
         "red",
         "green"
      ]
   },
   { 
      "id":2,
      "name":"name2",
      "color":[ 
         "pink",
         "yellow"
      ]
   }
]
Expected Output: ["name1", "name2"]
'''

import json

danaJSON='''[ 
   { 
      "id":1,
      "name":"name1",
      "color":[ 
         "red",
         "green"
      ]
   },
   { 
      "id":2,
      "name":"name2",
      "color":[ 
         "pink",
         "yellow"
      ]
   }
]
'''
# odp 1

# data = []
# try:
#     data = json.loads(danaJSON)
# except Exception as e:
#     print(e)

#lub odp 2

data = json.loads(danaJSON)
dataList = [item.get('name') for item in data]
print('Pyt 9- Przeanalizuj następujący kod JSON, aby uzyskać wszystkie wartości klucza „nazwa” w tablicy\n',dataList)





