#condicionales
#if
temperatura=40
if temperatura > 30:
    print("hace calor")

#if-else
temperatura=20
if temperatura > 20:
    print("hace calor")
else:
    print("Hace frio")

#if-else-elif
temperatura=20
if temperatura > 20:
    print("Hace calor")
elif temperatura ==20:
    print("Hace fresco")
else:
    print("Hace frio")

#ciclos
#ciclos for
for numero in range (1,11):
    print("subiendo el escalón", numero)

word="python"
for letra in word:
    if letra == "h":
        break
    print(letra)

#ciclo while
caramelos=5

while caramelos > 0:
    print("me como un caramelo!🐱‍🏍")
    caramelos=caramelos-1  

    if caramelos == 2:
        print("Me cansé de comer caremelos!😭")
        break
