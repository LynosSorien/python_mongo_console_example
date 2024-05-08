from pymongo import MongoClient
from pymongo import cursor
import sys

def execute_query(collection, query):
    try:
        full_query = "collection." + query
        result = eval(full_query)
        if isinstance(result, (list, cursor.Cursor)):
            for item in result:
                print(item)
        else:
            print(result)
    except Exception as e:
        print("Error al ejecutar la consulta:", e)

client = MongoClient('mongodb://root:example@localhost:27017/')

print("Seleccionando 'testdatabase' como base de datos")
db = client['testdatabase']
print("Seleccionando/Creando 'testcollection' como colección")
collection = db['testcollection']

#collection.insert_one({'name': 'John', 'age': 30})
print("Insertando un valor de ejemplo...")
execute_query(collection, "insert_one({'name': 'Freya', 'tail': '1', 'breed': 'Welsh Pembroke Corgi'})")

execute_query(collection, "find()")

print("Ingresa tus consultas MongoDB (escribe 'exit' para salir):")
while True:
    user_input = input("MongoDB> ")
    if user_input.lower() == "exit":
        print("Cerrando el programa...")
        sys.exit(0)
    else:
        execute_query(collection, user_input)
