#Ingredientes para el quesillo:
torta_chocolate ={
    "leche condensada": "1 lata(397 g)",
    "leche liquida": "1 lata (200 g)",
    "huevos": "4 unidades",
    "esencia de vainilla": "una cucharada",
    "sal": " una pizca",

    }


Caramelo= {
     "azúcar": "media taza",
     "agua": "media taza"

    }

# Usamos un ciclo for para recorrer el quesillo
print("Ingredientes de la torta de chocolate:")
for key, value in torta_chocolate.items():
    print(key, value)

   
print("Ingredientes para el caramelo:")
for key, value in Caramelo.items():
    print(key, value) 
