url = "http://inkuvi.com/folder_images/enero/caratula.jpeg"
filename = url.split("/")[-1] 
print(filename)


# * Teniendo una lista con N elementos numericos en una lista, 
# retornar todas las posiciones impares del mismo: 
# ej. [3,4,5,9,7,8,1] salida: [4,9,8],
#  ej: [9,7,5,1,3,2,4,8,6,5,0] salida: [7,1,2,8,5]

items = list([9,7,5,1,3,2,4,8,6,5,0])

new_list = list(map(lambda x: x[1], filter(lambda x: x[0] % 2 != 0, list(enumerate(items)))))
print(new_list)
