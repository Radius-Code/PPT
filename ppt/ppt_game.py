from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import random
import time

raiz=Tk()
raiz.title("Piedra, papel o tijeras")
barraMenu=Menu(raiz)
raiz.config(menu=barraMenu, width=100, height=100)
jugada=""
jugada_ia=""
valorAnterior=0
victorias=1 #por defecto las victorias estarán establecidas en 1 para que puedas jugar sin configurar nada al principio
endgame=False
partidaAnterior=False
contador=0 #cuenta el nº de partidas
contador_ia=0
partidas=0
ganando=perdiendo=False
inicioDelJuego=True

'''Para ejecutar el programa ir al menú "Archivo" y luego a "Nueva Partida". En el menú desplegable elegir el número
de victorias y darle al botón "Crear".

Tras la creación de la partida podremos jugar presionando los botones "Piedra", "Papel" o "Tijeras", solo uno una vez, tras lo
cual se ejecutaran las funciones que harán que el programa devuelva unos prints en la consola que nos irán diciendo como vamos
en el juego jugada tras jugada.

*(Al lado de cada comentario he puesto un número indicando el orden en que creé todos los métodos y conjuntos de widgets de este
programa)

'''


#---------configurar partida------------ 

def configuracion(): #ventana de configuracion de la partida -4º-

	global victorias
	global partidaAnterior
	global valorAnterior

	opciones=["1 Victoria", "3 Victorias", "5 Victorias"]

	ventana=Tk()
	ventana.title("Configurar Partida")
	ventanaConf=Frame(ventana)
	ventanaConf.grid()

	etiqueta=Label(ventana, text="Elige el nº de Victorias:")
	etiqueta.grid(row=0, column=0, padx=10, pady=10)

	variable=StringVar(ventana)
	variable.set("")
	opcion=OptionMenu(ventana, variable, *opciones) #crea el menu desplegable
	opcion.config(width=10)
	opcion.grid(row=1, column=0, padx=10, pady=10)

	botonCrear=Button(ventana, text="Nueva Partida", command=lambda:boton())
	botonCrear.grid(row=2, column=0, padx=10, pady=10)

	if partidaAnterior: #si se ha almacenado algo en partidaAnterior, el campo del menu desplegable será el almacenado
		variable.set(variableAnterior)


	def boton(): #boton de la ventana para crear la partida -4º-

		global victorias
		global contador
		global contador_ia
		global valorAnterior
		global inicioDelJuego

		contador=0
		contador_ia=0


		if variable.get()==opciones[0]:
			victorias=1

		elif variable.get()==opciones[1]:
			victorias=3

		elif variable.get()==opciones[2]:
			victorias=5

		variableAnterior=variable.get() #almacena en variable global Anterior el valor seleccionado al seleccionar una opcion
		#no sabía que podía crear la variable global dentro de un metodo y llamarlo desde el metodo padre sin haberla declarado 
		#antes fuera de este metodo padre

		inicioDelJuego=False
		ventana.destroy()
		inicio()

		print("Has seleccionado " + str(victorias) + " victorias")
		print("--------------------------------------------")


	
#--------lógica----------

def inicio(): #oculta los widgets o los muestro segun si es el inicio del juego, es decir si se abre la ventana por primera vez o no

	global inicioDelJuego

	if inicioDelJuego:
		miFrame1.pack_forget()
		miFrame2.pack_forget()
		miFrame3.pack_forget()
	else:
		miFrame1.pack()
		miFrame2.pack()
		miFrame3.pack()

def newGame():
	global inicioDelJuego
	inicioDelJuego=False
	inicio()

def resolucion(): #mensaje de diálogo que da el final del juego

	global victorias
	global contador
	global contador_ia
	global endgame
	global partidaAnterior
	global valorAnterior
	ganador=""

	while endgame == True:
		if contador==victorias:
			ganador="Has ganado\n ¿Quieres volver a jugar?"

		elif contador_ia==victorias:
			ganador="Has perdido\n ¿Quieres volver a jugar?"

		elif (contador and contador_ia)==victorias:
			ganador="Empate\n ¿Quieres volver a jugar?"

		valor=messagebox.askquestion("Partida terminada", ganador)
		if valor=="yes": 
			partidaAnterior=True
			valorAnterior=victorias
			contador=0
			contador_ia=0				
			break							
		else:
			raiz.destroy()
			break


def botonPresionado(mano): #función que almacena el botón presionado -1º- (no hace falta crear la clase para coger de la lista
							#misImagenes cada campo

	labelResultado.config(text="") # quita el texto de la etiqueta al darle a un boton

	global jugada

	for i in range(3):		# ejecuta el bucle 3 veces
		imageLabel1.config(image=misImagenes[1])
		imageLabel1.update() #siempre hay que llamar al metodo update() antes del time.sleep()
		time.sleep(0.1)
		imageLabel1.config(image=misImagenes[2])
		imageLabel1.update()
		time.sleep(0.1)
		imageLabel1.config(image=misImagenes[3])
		imageLabel1.update()
		time.sleep(0.1)


	if mano==1:
		jugada="piedra"
		imageLabel1.config(image=misImagenes[1])

	elif mano==2:
		jugada="papel"
		imageLabel1.config(image=misImagenes[2])

	else:
		jugada="tijeras"
		imageLabel1.config(image=misImagenes[3])

	imageLabel1.update()
	print("Elegiste " + jugada)
	time.sleep(1)

	IA_maquina()
	arbitro()

	
def IA_maquina(): #función que hace elegir a la maquina una opción -2º-

	global jugada
	global jugada_ia

	for i in range(3):		
		imageLabel2.config(image=misImagenes[1])
		imageLabel2.update()
		time.sleep(0.1)
		imageLabel2.config(image=misImagenes[2])
		imageLabel2.update()
		time.sleep(0.1)
		imageLabel2.config(image=misImagenes[3])
		imageLabel2.update()
		time.sleep(0.1)


	num=random.randint(1, 3)


	if num==1:
		jugada_ia="piedra"
		imageLabel2.config(image=misImagenes[1])

	elif num==2:
		jugada_ia="papel"
		imageLabel2.config(image=misImagenes[2])

	else:
		jugada_ia="tijeras"
		imageLabel2.config(image=misImagenes[3])

	imageLabel2.update()
	print("La máquina eligió " + jugada_ia)
	print("--------------------------------")
	time.sleep(2)




def arbitro(): #función que compara el boton presionado con el elegido por la maquina -3º-

	global jugada
	global jugada_ia
	global contador
	global contador_ia
	global victorias
	global endgame
	global ganando, perdiendo


#PROBLEMA: solucionar texto para que salga dentro del frame correctamente como los prints en la consola

	if jugada == jugada_ia:
		
		print("MARCADOR")
		print(contador)
		print(contador_ia)
		print("----------------")
		labelResultado.config(text=f"Empate. Sigue jugando\nTienes {contador} puntos" +
								 f"\nLa máquina tiene {contador_ia} puntos")
		time.sleep(1)


	elif (jugada=="piedra" and jugada_ia=="tijeras") or (jugada=="tijeras" and jugada_ia=="papel") or (jugada=="papel" and jugada_ia=="piedra"):
		
		contador+=1
		print("MARCADOR")
		print(contador)
		print(contador_ia)
		print("----------------")
		finDelJuego()
		'''hacer que cuando se gane la partida y se inicie un nuevo juego no se muestre 
		lo siguiente pero en las siguientes jugadas si'''
		if endgame:
			labelResultado.config(text="Ganaste") 
			'''hacer que este texto aparezca antes de la ventana del resultado y despues antes de que apa
			rezca pare con un time.sleep()'''
		else:
			time.sleep(1)
			labelResultado.config(text=f"Ganas esta jugada\nTienes {contador} puntos" +
								f"\nLa máquina tiene {contador_ia} puntos")


	elif (jugada=="piedra" and jugada_ia=="papel") or (jugada=="tijeras" and jugada_ia=="piedra") or (jugada=="papel" and jugada_ia=="tijeras"):
		
		contador_ia+=1
		print("MARCADOR")
		print(contador)
		print(contador_ia)
		print("----------------")
		finDelJuego()
		if endgame:
			labelResultado.config(text="Perdiste")
		else:
			time.sleep(1)
			labelResultado.config(text=f"Pierdes esta jugada\nTienes {contador} puntos" +
								f"\nLa máquina tiene {contador_ia} puntos")

	time.sleep(1)

	if endgame==False:

		print("Tengo " + str(contador) + " puntos")
		print("La máquina tiene " + str(contador_ia) + " puntos")
		print("--------------------")

	time.sleep(2)

	if contador>contador_ia and contador!=victorias:
		ganando=True
		perdiendo=False
		print("Vas ganando")
		time.sleep(2)

	elif contador<contador_ia and contador_ia!=victorias:
		ganando=False
		perdiendo=True
		print("Vas perdiendo")
		time.sleep(2)

	elif contador==contador_ia:
		ganando=perdiendo=False
		print("Empate")

	print("----------------")
	
	if (ganando or perdiendo)==True and (contador or contador_ia)!=victorias:
		print("--------------------")
		print("Te quedan " + str(victorias - contador) + " victorias para ganar")



def finDelJuego():

	global endgame

	while (contador or contador_ia)==victorias:
		endgame=True
		resolucion()
		break




#----------menu------------ -1º-


menuArchivo=Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Archivo", menu=menuArchivo)

menuArchivo.add_command(label="Nueva partida", command=newGame)
menuArchivo.add_command(label="Configurar partida", command=configuracion)
menuArchivo.add_command(label="Salir", command=lambda:raiz.destroy())



#----------botones------------ -1º-

miFrame1=Frame(raiz)
miFrame1.pack()

boton1=Button(miFrame1, text="piedra", command=lambda:botonPresionado(1))
boton1.grid(row=0, column=0, padx=10, pady=10)

boton2=Button(miFrame1, text="papel", command=lambda:botonPresionado(2))
boton2.grid(row=0, column=1, padx=10, pady=10)

boton3=Button(miFrame1, text="tijeras", command=lambda:botonPresionado(3))
boton3.grid(row=0, column=2, padx=10, pady=10)





#-----------resultado------------- -1º-

miFrame2=Frame(raiz)
miFrame2.pack()

miLabel=Label(miFrame1, text="Jugador")
miLabel.grid(row=1, column=0, padx=10, pady=10)

miLabe2=Label(miFrame1, text="Máquina")
miLabe2.grid(row=1, column=1, padx=10, pady=10)

#aqui me faltaria cuadrar cada palabra con su cuadro debajo

imagenes=[
(Image.open("blanco.png").resize((100,100))),
(Image.open("piedra.png").resize((100,100))),
(Image.open("papel.png").resize((100,100))),
(Image.open("tijeras.png").resize((100,100)))]

misImagenes=[
(ImageTk.PhotoImage(imagenes[0])),
(ImageTk.PhotoImage(imagenes[1])),
(ImageTk.PhotoImage(imagenes[2])),
(ImageTk.PhotoImage(imagenes[3]))]

imageLabel1=Label(miFrame2, image=misImagenes[0])
imageLabel1.grid(row=2, column=0, padx=10, pady=10)
imageLabel2=Label(miFrame2, image=misImagenes[0])
imageLabel2.grid(row=2, column=1, padx=10, pady=10)
'''imagen2=Image.open("blanco.png").resize((100,100))
miImagen2=ImageTk.PhotoImage(imagen2)
imageLabel2=Label(miFrame2, image=miImagen2)
imageLabel2.grid(row=2, column=1, padx=10, pady=10)'''

miFrame3=Frame(raiz)
miFrame3.pack()
labelResultado=Label(miFrame3)
labelResultado.pack()

inicio()



raiz.mainloop()