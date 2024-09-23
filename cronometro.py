import tkinter as tk
from tkinter import messagebox
#CRONOMETRO INFOR 2024
#Versión = 1.0
#Desarrolladores = Equipo 15

ejecucion = False #Indica el estado en que se encuentra el tiempo.
#Variables de tiempo:
minutos = 0
segundos = 0
milisegundos = 0
click_lectura = 0
vuelta_lectura = 0

class Cronometro(tk.Toplevel):
    def __init__(self):
        super().__init__()
        #INTERFAZ GRAFICA
        self.title('Reloj // Cronometro INFOR 2024 - v.1.0')
        self.geometry('630x250')
        self.resizable(width= False, height= False)
        self.configure(bg='#0B0B3B')
        #FRAME BOTONES
        #Label Titulo CRONOMETRO
        titulo_crono = tk.Label(self, text = 'Cronómetro INFOR 2024 - v.1', font = ('Arial', 15, 'bold', 'italic'), bg = '#0B0B3B', fg = 'white')
        cronometro_label = tk.Label(self, text='00:00:000', font = ('Arial', 70), bg = 'black', fg = 'white') #Etiqueta del cronometro

        #ACTUALIZACIÓN DEL TIEMPO
        def actualizacion():
            global minutos, segundos, milisegundos, actualización_tiempo
            milisegundos += 1
            if milisegundos == 999:
                milisegundos = 0
                segundos += 1   
                if segundos == 59:
                    segundos = 0
                    minutos += 1      
            #Se adiciona formato con ceros = 00
            if minutos > 9:
                minutos_str = f'{minutos}'
            else:
                minutos_str = f'0{minutos}'
            if segundos > 9:
                segundos_str = f'{segundos}'
            else:
                segundos_str = f'0{segundos}'
            if milisegundos > 9:
                milisegundos_str = f'0{milisegundos}'
                if milisegundos > 99:
                    milisegundos_str = f'{milisegundos}'
            else:
                milisegundos_str = f'00{milisegundos}'
            cronometro_label.config(text = minutos_str + ':' + segundos_str + ':' + milisegundos_str)
            actualización_tiempo = cronometro_label.after(1, actualizacion)

        #INICIAR/PAUSAR
        def iniciar():
            global ejecucion
            if not ejecucion:
                actualizacion()
                ejecucion = True

        #PAUSAR/DETENER:
        def pausa():
            global ejecucion
            if ejecucion:
                cronometro_label.after_cancel(actualización_tiempo)
                ejecucion = False

        #VUELTAS (guardar 5 vueltas)...
        def vueltas():
            global vuelta_lectura
            vuelta_lectura = vuelta_lectura + 1 #Suma 1 cada vuelta
            lectura = f'{minutos}:{segundos}:{milisegundos}'
            if vuelta_lectura ==1:
                lista_vueltas.insert(tk.END, f'{vuelta_lectura} - {lectura}')
            elif vuelta_lectura ==2:
                lista_vueltas.insert(tk.END, f'{vuelta_lectura} - {lectura}')
            elif vuelta_lectura ==3:
                lista_vueltas.insert(tk.END, f'{vuelta_lectura} - {lectura}')
            elif vuelta_lectura ==4:
                lista_vueltas.insert(tk.END, f'{vuelta_lectura} - {lectura}')
            elif vuelta_lectura ==5:
                lista_vueltas.insert(tk.END, f'{vuelta_lectura} - {lectura}')
        #RESET (Reiniciar)
        #Parar la actualizacion del tiempo
        #Variables = 0
        #Etiquetas de inicio
        def reiniciar():
            global ejecucion, vuelta_lectura
            if ejecucion: 
                cronometro_label.after_cancel(actualización_tiempo)
                ejecucion = False    
            global minutos ,segundos, milisegundos
            minutos = 0
            segundos = 0 
            milisegundos = 0
            lista_vueltas.delete(first=0, last=5)
            vuelta_lectura = 0
            cronometro_label.config(text='00:00:000')
        

        #AYUDA - Instrucciones de como usar y soporte técnico
        def ayuda_dialogo():
            messagebox.showinfo(title= 'Más información', message='Bienvenida/o! INICIAR: Comienza a medir el tiempo que pasa. PAUSAR: Pausa la ejecución del cronometro. VUELTA: guarda los valores de unidiades de tiempo en un instante determinado. RESET: Reestablece el cronometro. ADVERTENCIA: LAS VUELTAS GUARDADAS SERAN BORRADAS.')

        #botones
        # 1.INICAR/PAUSA
        inicio_boton = tk.Button(self, text='INICIAR', height=1, width=8, font=('Arial', 18, 'bold'), command=iniciar, bg= 'green')
        # 2.PAUSA
        pausa_boton = tk.Button(self, text='PAUSAR', height=1, width=8, font=('Arial', 18, 'bold'), command=pausa, bg= 'yellow')
        # 3.VUELTAS
        vueltas_boton = tk.Button(self, text='VUELTA', height=1, width=8, font=('Arial', 18, 'bold'), command=vueltas, bg= 'blue')
        # 4.RESET
        reset_boton = tk.Button(self, text='RESET', height=1, width=8, font=('Arial', 18, 'bold'), command=reiniciar, bg= 'white')
        #5.AYUDA
        ayuda_boton = tk.Button(self, text='AYUDA', height=1, width=5, font=('Arial', 8, 'bold'), command=ayuda_dialogo, bg= 'white', fg= 'red')

        #LISTBOX LISTAS DE VUELTAS
        #5 memorias...
        lista_vueltas = tk.Listbox(self, height=5, width=12, font = ('Arial', 15))

        #GRID
        titulo_crono.grid(column=0, row=0, columnspan=3, pady=8)
        cronometro_label.grid(column=0, row=1, columnspan=3, padx=20, pady=10)
        ayuda_boton.grid(column=3, row=0)
        lista_vueltas.grid(column=3, row=1)
        inicio_boton.grid(column=0, row=2)
        pausa_boton.grid(column=1, row=2, pady=10)
        vueltas_boton.grid(column=2, row=2)
        reset_boton.grid(column=3, row=2, pady=10)
