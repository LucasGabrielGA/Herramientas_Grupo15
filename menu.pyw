from calculadora import Calculadora
from tareas import Agenda
from temporizador import Temporizador
from cronometro import Cronometro
import tkinter as tk
import time

def center_window(window): # Este método ayuda a centrar la ventanaCal de la aplicación en la pantalla
    screen_width = window.winfo_screenwidth() # Obtiene el ancho del monitor 
    screen_height = window.winfo_screenheight() # Obtiene el alto del monitor
    x = (screen_width - window.winfo_reqwidth()) // 2  # Se saca la mitad aproximada del ancho 
    y = (screen_height - window.winfo_reqheight()) // 2 # Se saca la mitad aproximada del alto
    window.geometry(f"+{x}+{y}") # Establece la posición de la ventanaCal con la resolución aproximada

#====================================================================================//
#-> La ventana principal
#====================================================================================//
ventanaMenu = tk.Tk()
ventanaMenu.title("Herramientas - Grupo 15")
ventanaMenu.config(background='black')
ventanaMenu.geometry("450x250")
ventanaMenu.resizable(0,0)

#====================================================================================//
#-> Funciones de los programas
#====================================================================================//

#------------------------------------------------------------------------------------//
#-> Funciones para llamar a la Calculadora
#------------------------------------------------------------------------------------//
def crearCalculadora():
    global calculadora
    calculadora = Calculadora()

def abrirCalculadora():
    try:
        calculadora.focus_set()
    except:
        crearCalculadora()

#------------------------------------------------------------------------------------//
#-> Funciones para llamar a la Agenda
#------------------------------------------------------------------------------------//
def crearAgenda():
    global agenda
    agenda = Agenda()

def abrirAgenda():
    try:
        agenda.focus_set()
    except:
        crearAgenda()

#------------------------------------------------------------------------------------//
#-> Funciones para llamar al Temporizador
#------------------------------------------------------------------------------------//
def crearTemporizador():
    global temporizador
    temporizador = Temporizador()

def abrirTemporizador():
    try:
        temporizador.focus_set()
    except:
        crearTemporizador()

#------------------------------------------------------------------------------------//
#-> Funciones para llamar al Cronómetro
#------------------------------------------------------------------------------------//
def crearCronometro():
    global cronometro
    cronometro = Cronometro()

def abrirCronometro():
    try:
        cronometro.focus_set()
    except:
        crearCronometro()
#------------------------------------------------------------------------------------//
#-> Función que hace funcionar al Reloj
#------------------------------------------------------------------------------------//
def actualizar_reloj():
    hora_actual = time.strftime("%H:%M:%S")
    lbl_reloj.config(text = hora_actual)
    lbl_reloj.after(1000, actualizar_reloj)

#====================================================================================//
#-> Frames para separar y ordenar los botones y Reloj
#====================================================================================//
btn_frame = tk.Frame(ventanaMenu, bg='gray85')
btn_frame.pack(side="left", fill="both")

reloj_frame = tk.Frame(ventanaMenu, bg='black')
reloj_frame.pack(anchor="center", fill="both")

#====================================================================================//
lbl_reloj = tk.Label (reloj_frame, font = ("Arial", 50),bg = "black", fg="white")
lbl_reloj.pack(anchor = "center", pady=70) 
#====================================================================================//

#====================================================================================//
#-> Botones que llaman a las funciones que abren los programas
#====================================================================================//
btn1 = tk.Button(btn_frame, text="Agenda de tareas", font=("Arial 15"), background='gray80', command=abrirAgenda)
btn1.config(width=14, height=2)
btn1.pack()

btn2 = tk.Button(btn_frame, text="Calculadora", font=("Arial 15"), background='gray80', command=abrirCalculadora)
btn2.config(width=14, height=2)
btn2.pack()

btn3 = tk.Button(btn_frame, text="Temporizador", font=("Arial 15"), background='gray80', command=abrirTemporizador)
btn3.config(width=14, height=2)
btn3.pack()

btn4 = tk.Button(btn_frame, text="Cronómetro", font=("Arial 15"), background='gray80', command=abrirCronometro)
btn4.config(width=14, height=2)
btn4.pack()
#====================================================================================//

center_window(ventanaMenu) #-> El método para centrar en la pantalla el Menú
actualizar_reloj()         #-> Método que enciende y actualiza el reloj del Menú

ventanaMenu.mainloop()