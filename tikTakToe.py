#Juego Tik Tak Toe
from tkinter import *
from tkinter import messagebox     #imports de Tkinter para la interfaz
from tkinter import simpledialog

def block(): #función que bloquea un botón después de ser clickeado
    for i in range(9):
        btnList[i].config(state = "disable")
def startGame(): #función que inicializa el juego y lo reinicia a sus datos base para juegos nuevos
    for i in range(9):
        btnList[i].config(state = "normal", bg = "black", text = "")
        table[i] = "N"
    global player1, player2, cont, turn
    turn = 0
    cont = 0
    player1 = simpledialog.askstring("Jugadores","Nombre Jugador 1: ")
    player2 = simpledialog.askstring("Jugadores","Nombre Jugador 2: ")
    playerTurn.set("Es el turno de "+player1)

def change(n): #función que cambia el tablero interno y además en la niterface para visualizar los cambios
    global turn, player1, player2, cont
    if table[n] == "N" and turn == 0: #revisa si el espacio esta con nada y de quien es el turno para asignarle un valor
        btnList[n].config(text = "X", fg = "black", bg = "#DA3818")
        turn = 1
        table[n] = "X"
        cont+=1
        playerTurn.set("Es el turno de "+player2)
    elif table[n] == "N" and turn == 1: #revisa si el espacio esta con nada y de quien es el turno para asignarle un valor
        btnList[n].config(text = "O", fg = "black", bg = "#18129D")
        turn = 0
        table[n] = "O"
        cont+=1
        playerTurn.set("Es el turno de "+player1)
    btnList[n].config(state = "disable") #bloquea el boton clickeado por si quieren cambiar su valor durante el juego
    check()

def check(): #función que revisa si hay un ganador o empate
    global cont
    if (table[0] == "X" and table[1]=="X" and table[2] == "X") or (table[3] == "X" and table[4]=="X" and table[5] == "X") or(table[6] == "X" and table[7]=="X" and table[8] == "X") or(table[0] == "X" and table[3]=="X" and table[6] == "X") or(table[1] == "X" and table[4]=="X" and table[7] == "X") or(table[2] == "X" and table[5]=="X" and table[8] == "X") or(table[0] == "X" and table[4]=="X" and table[8] == "X") or(table[6] == "X" and table[4]=="X" and table[2] == "X"):
        block() #bloquea los botones porque acabó el juego
        messagebox.showinfo("Fin del Juego", "Ha ganado: "+player1) #muestra quien ganó
        messagebox.showinfo("Juego Nuevo", "Si quiere volver a jugar de click en el boton de start") # sugiere como se puede reiniciar el juego
    elif (table[0] == "O" and table[1]=="O" and table[2] == "O") or(table[3] == "O" and table[4]=="O" and table[5] == "O") or(table[6] == "O" and table[7]=="O" and table[8] == "O") or(table[0] == "O" and table[3]=="O" and table[6] == "O") or(table[1] == "O" and table[4]=="O" and table[7] == "O") or(table[2] == "O" and table[5]=="O" and table[8] == "O") or(table[0] == "O" and table[4]=="O" and table[8] == "O") or(table[6] == "O" and table[4]=="O" and table[2] == "O"):
        block() #bloquea los botones porque acabó el juego
        messagebox.showinfo("Fin del Juego", "Ha ganado: "+player2) #muestra quien ganó
        messagebox.showinfo("Juego Nuevo", "Si quiere volver a jugar de click en el boton de start") # sugiere como se puede reiniciar el juego
    elif cont == 9:
        block() #bloquea los botones porque acabó el juego
        messagebox.showinfo("Fin del Juego", "Esto es un empate") #muestra que fue un empate
        messagebox.showinfo("Juego Nuevo", "Si quiere volver a jugar de click en el boton de start") # sugiere como se puede reiniciar el juego
#Declara los elementos para el código 
frame = Tk() #Este es el frame en el que se trabaja
frame.geometry("600x850") #El tamaño del frame
frame.title("Tik Tak Toe") #titulo del frame
frame.configure(background="#C9CBCF") #color del fondo 
frame.resizable(height = False, width = False) #hace que el tamaño del frame no se modifique
turn = 0 #nidicador para saber el turno de cada jugador
cont = 0 #contador para saber el numero de turnos tomados en el juego en total (para saber si es empate o no)
player1 = " " #variable del nombre de jugador1
player2 = " " #variable del nombre de jugador2
btnList = [] #Lista de los botones del tablero (las 9 casillas para poner tu marca)
table = [] #Simula la cantidad y posiciones del tablero de forma interna para evaluar qué valor ocupa cada casilla
playerTurn = StringVar() #layer de interfaz que mostrará de quien es el turno
#llena el tablero con N que indica que todo el tablero está vacío
for i in range (9):
    table.append("N")
#Crea y acomoda todos los botones en la lista y en el frame
btn0 = Button(frame,width = 25,height = 15,bg='black',command = lambda:change(0))
btnList.append(btn0)
btn0.place(x=12,y=100)
btn1 = Button(frame,width = 25,height = 15,bg='black',command = lambda:change(1))
btnList.append(btn1)
btn1.place(x=208,y=100)
btn2 = Button(frame,width = 25,height = 15,bg='black',command = lambda:change(2))
btnList.append(btn2)
btn2.place(x=405,y=100)
btn3 = Button(frame,width = 25,height = 15,bg='black',command = lambda:change(3))
btnList.append(btn3)
btn3.place(x=12,y=348)
btn4 = Button(frame,width = 25,height = 15,bg='black',command = lambda:change(4))
btnList.append(btn4)
btn4.place(x=208,y=348)
btn5 = Button(frame,width = 25,height = 15,bg='black',command = lambda:change(5))
btnList.append(btn5)
btn5.place(x=405,y=348)
btn6 = Button(frame,width = 25,height = 15,bg='black',command = lambda:change(6))
btnList.append(btn6)
btn6.place(x=12,y=600)
btn7 = Button(frame,width = 25,height = 15,bg='black',command = lambda:change(7))
btnList.append(btn7)
btn7.place(x=208,y=600)
btn8 = Button(frame,width = 25,height = 15,bg='black',command = lambda:change(8))
btnList.append(btn8)
btn8.place(x=405,y=600)
#Crea un label para mostrar de quien es el turno
turnLbl = Label(frame, textvariable = playerTurn, height = 5, width = 50, bg='#766B46' ).place(x=12,y=12)
#el boton que inicia y reinicia el juego
btnStrt = Button(frame, bg ='#675826', fg= 'black', text = 'Start', height = 3, width = 10, font = "Times 14", command = startGame).place(x = 370, y=11)
block()
frame.mainloop()