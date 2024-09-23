import tkinter as tk

class Calculadora(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Calculadora")
        self.config(background='#0B0B3B')
        self.resizable(0,0)

        operadores = ['+', '-', '/', '*', '(', ')']

        #Lógica de la Calculadora
        #->Función para insertar los caracteres a la entrada de texto
        def click_btn(valor):
            if(entrada.get() == "ERROR"):
                entrada.delete(0, 'end')
                entrada.insert(len(entrada.get()), valor)
            else:
                entrada.insert(len(entrada.get()), valor)

        #-> Función para limpiar el texto
        def borrar():
            entrada.delete(0, 'end')

        #-> Función para resolver toda la ecuación y mostrarlo
        def resolver():
            try:
                resultado = eval(entrada.get())
                entrada.delete(0, 'end')
                entrada.insert(0, resultado)
            except:
                entrada.delete(0, 'end')
                entrada.insert(0, "ERROR")

        #-> Función para negar el resultado en pantalla
        def negar():
            if len(entrada.get()) != 0:
                try:
                    texto = entrada.get()
                    if texto[0] != '-':
                        entrada.delete(0, 'end')
                        entrada.insert(0, '-'+texto)
                    else:
                        entrada.delete(0, 1)
                        texto = entrada.get()
                        entrada.delete(0, 'end')
                        entrada.insert(0, texto)
                except:
                    entrada.delete(0, 'end')
                    entrada.insert(0, "ERROR")

        # function to validate mark entry
        def only_numbers(string):
            if string in operadores or string == "ERROR":
                return True
            else:
                return string.isdigit()
            
        validation = self.register(only_numbers)

        #-> Entrada para el texto
        entrada = tk.Entry(self, font=("Arial 25"), background='white', justify="right")
        #entrada = tk.Entry(self, font=("Arial 25"), background='white', justify="right", validate="key", validatecommand=(validation, '%S'))
        entrada.grid(row = 0, column=0, columnspan=4, padx=5, pady=5)

        tk.Button(font=("Arial 25"))

        #-> Botoncitos de números
        btn1 = tk.Button(self, text="1", font=("Arial 15"), background='white', width=5, height=2, command=lambda:click_btn(1))
        btn2 = tk.Button(self, text="2", font=("Arial 15"), background='white', width=5, height=2, command=lambda:click_btn(2))
        btn3 = tk.Button(self, text="3", font=("Arial 15"), background='white', width=5, height=2, command=lambda:click_btn(3))
        btn4 = tk.Button(self, text="4", font=("Arial 15"), background='white', width=5, height=2, command=lambda:click_btn(4))
        btn5 = tk.Button(self, text="5", font=("Arial 15"), background='white', width=5, height=2, command=lambda:click_btn(5))
        btn6 = tk.Button(self, text="6", font=("Arial 15"), background='white', width=5, height=2, command=lambda:click_btn(6))
        btn7 = tk.Button(self, text="7", font=("Arial 15"), background='white', width=5, height=2, command=lambda:click_btn(7))
        btn8 = tk.Button(self, text="8", font=("Arial 15"), background='white', width=5, height=2, command=lambda:click_btn(8))
        btn9 = tk.Button(self, text="9", font=("Arial 15"), background='white', width=5, height=2, command=lambda:click_btn(9))
        btn0 = tk.Button(self, text="0", font=("Arial 15"), background='white', width=5, height=2, command=lambda:click_btn(0))

        #-> Botoncitos auxiliares
        btn_borrar = tk.Button(self, text="C", font=("Arial 15"), background='red', fg='white', width=5, height=2, command=borrar)
        btn_parentesis1 = tk.Button(self, text="(", font=("Arial 15"), background='gray80', width=5, height=2, command=lambda:click_btn("("))
        btn_parentesis2 = tk.Button(self, text=")", font=("Arial 15"), background='gray80', width=5, height=2, command=lambda:click_btn(")"))
        btn_punto = tk.Button(self, text=".", font=("Arial 15"), background='white', width=5, height=2, command=lambda:click_btn("."))
        btn_negado = tk.Button(self, text="+/-", font=("Arial 15"), background='white', width=5, height=2, command=negar)

        #-> Botoncitos de operadores
        btn_division = tk.Button(self, text="÷", font=("Arial 15"), background='gray80', width=5, height=2, command=lambda:click_btn("/"))
        btn_multiplicacion = tk.Button(self, text="x", font=("Arial 15"), background='gray80', width=5, height=2, command=lambda:click_btn("*"))
        btn_resta = tk.Button(self, text="-", font=("Arial 15"), background='gray80', width=5, height=2, command=lambda:click_btn("-"))
        btn_suma = tk.Button(self, text="+", font=("Arial 15"), background='gray80', width=5, height=2, command=lambda:click_btn("+"))
        btn_igual = tk.Button(self, text="=", font=("Arial 15"), background='cyan', width=5, height=2, command=resolver)

        #-> Insertar botones a la self
        #Primera fila
        btn_borrar.grid(row=1, column=0, padx=0, pady=1)
        btn_parentesis1.grid(row=1, column=1, padx=0, pady=1)
        btn_parentesis2.grid(row=1, column=2, padx=0, pady=1)
        btn_division.grid(row=1, column=3, padx=0, pady=1)

        #Segunda fila
        btn7.grid(row=2, column=0, padx=0, pady=1)
        btn8.grid(row=2, column=1, padx=0, pady=1)
        btn9.grid(row=2, column=2, padx=0, pady=1)
        btn_multiplicacion.grid(row=2, column=3, padx=0, pady=1)

        #Tercera fila
        btn4.grid(row=3, column=0, padx=0, pady=1)
        btn5.grid(row=3, column=1, padx=0, pady=1)
        btn6.grid(row=3, column=2, padx=0, pady=1)
        btn_resta.grid(row=3, column=3, padx=0, pady=1)

        #Cuarta fila
        btn1.grid(row=4, column=0, padx=0, pady=1)
        btn2.grid(row=4, column=1, padx=0, pady=1)
        btn3.grid(row=4, column=2, padx=0, pady=1)
        btn_suma.grid(row=4, column=3, padx=0, pady=1)

        #Quinta fila
        btn_negado.grid(row=5, column=0, padx=0, pady=1)
        btn0.grid(row=5, column=1, padx=0, pady=1)
        btn_punto.grid(row=5, column=2, padx=0, pady=1)
        btn_igual.grid(row=5, column=3, padx=0, pady=1)
