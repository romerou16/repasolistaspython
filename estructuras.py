#se declaran diccionarios(Objetos)
ClienteUno={
    "id":5,
    "nombre":"edificioUno",
    "consumo":200
}
ClienteDos={
    "id":58,
    "nombre":"edificioDos",
    "consumo":500
}

#Se declara una lista (arreglo)
clientesAsociados=[
    ClienteUno,
    ClienteDos
]

#Y ahora que hago con esa lista?
# mi objetivo sera obtener la informacion de la lista
# recorrer una lista o arreglo 
'''for i in range(2):
    print(clientesAsociados[i]["consumo"])'''
#programemos un foreach que es un fot 
#especializado en recorrer arreglos (listas)
for cliente in clientesAsociados:
    print(cliente["id"],'=>',cliente["consumo"],'KWH')
    print(f"{cliente["id"]}=>{cliente['consumo']}KWH")
