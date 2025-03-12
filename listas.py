#Colecciones
#Lista
serplist= ["Boa","pitón","culebra venosa","vibora rayada"]
#Enocntrar los elementos de una lista
print(serplist[2])
#usar len para contar los elementos de la lista
cantidad_serpientes= len (serplist)
print(cantidad_serpientes)

#acceder a los elementos de la lista
serpiente_uno=serplist [0]
serpiente_dos=serplist [1]
print(serpiente_uno,serpiente_dos)

#modificar elementos de la lista
serplist[0] = "Boa constricto"
serplist[1] = "pitón gigante"
serplist [2] = "culebra de la selva"
print(serplist) 

#agregar: (append) elementos a la lista
serplist.append ("Vibora rayada, culebra coral")
print(serplist)

#eliminar: (remove elementos de la lista
serplist.remove ("vibora rayada")
print(serplist)

#ordenar (sort) la lista
serpiente_dos.sort()
print(serplist)

#invertir (reverse) la lista
serplist.reverse()
print(serplist)

#comprobar (in:dentro) si un elemnto esa está en la lista
print ("pinton" in serplist)

#contar (contar) numero de veces que está un elemento
print(serplist.count("pitón"))
