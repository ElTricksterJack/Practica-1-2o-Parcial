from os import system #Invoquemos el system para el cls, esta invocasion no requiere sangre
print("\nNombre: Ruvalcaba Valverde Miguel Angel")
print("--------Punto 1--------")
print("--Compra las Exetrisidades del Cuervo Cornudo Atintado--")
print("paquete de duslses de frut Horo Horo - 43$","\nCalabazas de Jack'o lantern - 57$","\nNugets verdes de Duolingo - 92$","\nKetchup con el eslogan, \n*Hoy hiciste un Esquele-Ton de trabajo descansa un poco y Bones-appétit - 20$","\nDoritos Dorinachos Dorilocos Bill Cypher - 37$","\nFeastable de pay calabaza - 5$","\nPapaya payairus - 9$","\n-+-+-+-+-")
#Nota el yo de las 3:38 del 3/10/2024: acabo de descuri esto \n, esto permite dar un espasio en un print.
#Nota par el yo de las 3:38 del 3/10/2024 de parte del de las 3:46 del 3/10/2024: porque no lo intetamos antes =( .
max = max(43, 57, 92, 20, 37, 5, 9) #esto ya lo explique pero las palabras max y min te permien sacar el valor minimo y maximo de un grupo de valores
min = min(43, 57, 92, 20, 37, 5, 9)
print("Lo mas Caro esta a",max,"$")#imprimimos variables y el texto
print("Lo mas Barato esta a",min,"$")
ok = input("Continuar?:") 
system("cls")#continuar y borrar cache
print("--------Punto 2--------")
print("Tienes 7 materias cuales son?:")#ingresemos las variables
M1 = input("Materia 1: ")
M2 = input("Materia 2: ")
M3 = input("Materia 3: ")
M4 = input("Materia 4: ")
M5 = input("Materia 5: ")
M6 = input("Materia 6: ")
M7 = input("Materia 7: ") 
MATE = (M1,M2,M3,M4,M5,M6,M7)#Mink:A QUIEN MATASTE¡¡¡.
#Mr.Ink:A nadie es solo un conjunto de valores que los reuni para haser una lista

print(type(MATE))#con esto estoy comprobando de que tipo es esta varaible
print("Las materias son",MATE[0:])#aqui se ve elr esutaldo de la anteril
print("--------Punto 3--------")
print("Estoy cursando",MATE[0])
print("Estoy cursando",MATE[1])
print("Estoy cursando",MATE[2])
print("Estoy cursando",MATE[3])
print("Estoy cursando",MATE[4])
print("Estoy cursando",MATE[5])
print("Estoy cursando",MATE[6])
ok = input("Continuar?:")
system("cls")#continuar y borrar cache
print("--------Punto 4--------")
C1 = int(input(f"Calisficasion de {MATE[0]}:"))#truco si pones una f antes con unas {} podras meter valores dentro del print
C2 = int(input(f"Calisficasion de {MATE[1]}:"))
C3 = int(input(f"Calisficasion de {MATE[2]}:"))
C4 = int(input(f"Calisficasion de {MATE[3]}:"))
C5 = int(input(f"Calisficasion de {MATE[4]}:"))
C6 = int(input(f"Calisficasion de {MATE[5]}:"))
C7 = int(input(f"Calisficasion de {MATE[6]}:"))
CAL = [C1,C2,C3,C4,C5,C6,C7]
print("-+-+-+-")
print(f"La calificasion de {MATE[0]} es {CAL[0]}")
print(f"La calificasion de {MATE[1]} es {CAL[1]}")
print(f"La calificasion de {MATE[2]} es {CAL[2]}")
print(f"La calificasion de {MATE[3]} es {CAL[3]}")
print(f"La calificasion de {MATE[4]} es {CAL[4]}")
print(f"La calificasion de {MATE[5]} es {CAL[5]}")
print(f"La calificasion de {MATE[6]} es {CAL[6]}")
ok = input("Continuar?:")
system("cls")#continuar y borrar cache
print("--------Punto 5--------")
import random#traigamos a la mesa el random, o que random este comentario... eso fue random? na que iporta aunque sea algo EGG-trallo
C = 1
while C > 0:#con este while se hase un bucle con el que nos permite randomisar barios numeros que usaremos para la loteria
    LO1 = random.randint(1, 10000)
    LO2 = random.randint(1, 10000)
    LO3 = random.randint(1, 10000)
    LO4 = random.randint(1, 10000)
    LO5 = random.randint(1, 10000)
    LO6 = random.randint(1, 10000)
    LO7 = random.randint(1, 10000)
    LO8 = random.randint(1, 10000)
    LO9 = random.randint(1, 10000)
    LO10 = random.randint(1,10000)# y con el if evitaremos que algun numero se repita y si no hay repetisiones pues se cierra el bucle
    if LO1 == LO2 or LO1 == LO3 or LO1 == LO4 or LO1 == LO5 or LO1 == LO6 or LO1 == LO7 or LO1 == LO8 or LO1 == LO9 or LO1 == LO10:
        C = 2
        print("Los numeros no se repiten 1")
    elif LO2 == LO3 or LO2 == LO4 or LO2 == LO5 or LO2 == LO6 or LO2 == LO7 or LO2 == LO8 or LO2 == LO9 or LO2 == LO10:
        C = 2
        print("Los numeros no se repiten 2")
    elif LO3 == LO4 or LO3 == LO5 or LO3 == LO6 or LO3 == LO7 or LO3 == LO8 or LO3 == LO9 or LO3 == LO10:
        C = 2
        print("Los numeros no se repiten 3")
    elif LO4 == LO5 or LO4 == LO6 or LO4 == LO7 or LO4 == LO8 or LO4 == LO9 or LO4 == LO10:
        C = 2
        print("Los numeros no se repiten 4")
    elif LO5 == LO6 or LO5 == LO7 or LO5 == LO8 or LO5 == LO9 or LO5 == LO10: 
        C = 2
        print("Los numeros no se repiten 5")
    elif LO6 == LO7 or LO6 == LO8 or LO6 == LO9 or LO6 == LO10:
        C = 2
        print("Los numeros no se repiten 6")
    elif LO7 == LO8 or LO7 == LO9 or LO7 == LO10:
        C = 2
        print("Los numeros no se repiten 7")
    elif LO8 == LO9 or LO8 == LO10:
        C = 2
        print("Los numeros no se repiten 8")
    elif LO9 == LO10:
        C = 2
        print("Los numeros no se repiten 9")
    else:
        C = 0
LOTE = [LO1,LO2,LO3,LO4,LO5,LO6,LO7,LO8,LO9,LO10]
#esto es puro show solo disfrutalo
print("Los primeros premios de la noche, estos 5 autos de la marca Ink King Crow son para los numeros¡¡¡¡")
print(f"{LOTE[5:9]} Ellos son nuestros afortunados ganadores")
print("a continuasion por 2 premios de 50Mil pesos sera para los sigentes 2 numeros")
print("*Pausa Dramatica, pero sale mal se cae el microfono asiendo que suene un eco estruendoso en la sala*")
ok = input("conti:")
system("cls")#continuar y borrar cache
print("... =/")
ok = input("conti:")
print("...... =P")
ok = input("conti:")
print("......... -W- ya taradaron mucho no?. -W-")
ok = input("conti:")
system("cls")#continuar y borrar cache
print("*Cuando el presentador que estaba dando los números se agacha a recogerlos, se le rompen los pantalones y tiene que abandonar el lugar por un rato.*")
print("*Luego viene un reemplazo para continuar la lotería y Con gran profesionalismo, el espectáculo continúa como si nada hubiera pasado.*")
print(f"y los ganadores de los 50Mil pesos son los numeros {LOTE[3:4]}")
print("...")
ok = input("conti:")
system("cls")#continuar y borrar cache
#los primeros 3 lugares
print("y los tres primeros lugares con la mayor de dinero en los premios")
print(f"El terser lugar por 350Mil pesos de de parte del Numero {LOTE[2]}¡¡¡¡¡¡¡")
print(f"El segundo lugar de 500Mil pesos es para el Numero {LOTE[1]}¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡")
print("Y para serrar el premio la noche")
print("El premio godro de 1M de pesos es para...")
print("*Pausa Dramatica*")
ok = input("conti:")
system("cls")#continuar y borrar cache
print(f"el numero {LOTE[0]}¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡")
print("Felisidades porfabor contacte con nosotros si es alguno de estos afortunados ganadores, lo esperamos con ansias no vemos pronto.")
print("*Termina el programa y aparece rapidos y furiosos 30, y eso hase que apagué la tele.*")
LOTE.sort()
print(LOTE)
print("--------------------------------------")
print("Resultado:Fue divertido \n")
