# Write your python code here
print("-------------------")
print("Tarea 1")
print("Roses are #ff0000 Violets are #0000ff why my code´s working I haven´t a clue ")

print("-------------------")
print("Tarea 4")
altura=200
altura=altura+50
print(altura)

print("-------------------")
print("Tarea 5, introduzca la edad")
precio_helado=100
incremento_precio=0.2
edad_hambreinicial=18
porcentaje_hambre = edad_hambreinicial
incremento_hambre=10
rango_inicial_hambre=85

def calculate_helado(p_helado, edad):
    num_helados= round((rango_inicial_hambre-edad)/incremento_hambre)
    print("num_helados para satisfacer el hambre", num_helados)
    i = 2
    precio_total = p_helado
    while i <= num_helados:
        p_helado = p_helado + (p_helado*incremento_precio)
        precio_total = precio_total + p_helado
        i = i + 1 
    print ("precio_total ", precio_total)
    return precio_total

def calculate_hambre(edad):

    dinero=2000
    if edad >= 85 and edad <= 100 and dinero>0:
        print("Satisfecho")
    else: 
        print("No Satisfecho, necesito comida")
        ph = calculate_helado(precio_helado,edad)
        dinero = dinero - ph
        if dinero > 0:
            print(" Puedo satisfacer el hambre")
        else:
            print("no tengo suficiente dinero para satisfacer el hambre")

print("Edad ", edad_hambreinicial)
calculate_hambre(edad_hambreinicial)

print("-------------------")
print("Tarea 7")
for i in range(51):
    print(i)


import random

edad=random.randint(1,100)
print("Edad random", edad)
calculate_hambre(edad)

print("-------------------")
print("Tarea 9")
f = open("flag.txt","w")
f.write("hola, he creado un fichero")
f.close()

f = open("flag.txt", "r")
print(f.read())

print("-------------------")
print("Tarea 10")
import datetime
current_time = datetime.datetime.now()
print(current_time)