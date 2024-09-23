import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import time


counting = False

class Temporizador(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title('Temporizador')
        self.resizable(0,0)
        self.config(bg='#0B0B3B')
        self.geometry("400x200")


        wanted_hora= tk.IntVar()
        wanted_minutos= tk.IntVar()
        wanted_segundos= tk.IntVar()



        hora_var = tk.StringVar(value= '00')
        minutos_var = tk. StringVar(value = '00')
        segundos_var = tk. StringVar(value = '00')


        def count_down ():
            total_seconds = 0
            counting = True
            counting_stop = False

            hour, minuet, second = wanted_hora.get(), wanted_minutos.get(), wanted_segundos.get()
            total_seconds = hour*3600 + minuet*60 + second

            #inicio_btn.config(text= 'Detener', command=count_stop)

            if total_seconds != 0:
                wanted_hora.set(0)
                wanted_minutos.set(0)
                wanted_segundos.set(0)
                while total_seconds > -1 and counting:
                    if counting_stop == True:
                        break
                    elif second >= 0:
                        if second > 9:
                            segundos_var.set(f'{second}')
                            second -= 1
                            total_seconds -= 1
                            self.update()
                            time.sleep(1)

                        else:
                            segundos_var.set(f'0{second}')
                            second -= 1
                            self.update()
                            time.sleep(1)

                    elif minuet > 0:
                        if minuet > 9:
                            minuet -= 1
                            minutos_var.set(f'{minuet}')
                            second = 59

                        else:
                            minuet -= 1
                            minutos_var.set(f'0{minuet}')
                            second = 60

                    elif hour > 0:
                        if hour > 9:
                            hour -= 1
                            hora_var.set(f'{hour}')
                            minuet = 60
                        else:
                            hour -= 1
                            hora_var.set(f'0{hour}')
                            minuet = 60
                    else:
                        messagebox.showinfo('Temporizador', '¡Se acabó el tiempo!')
                        break
        def edit ():
            win = tk.Toplevel()
            win.title('Tiempo')
            win.config (padx=40, pady= 20)
            win.resizable(0,0)
            win.config(bg='light sky blue')
            


            h_lbl = tk.Label(win, font= ('Times New Roman', 20), text = 'Hora :', bg='light sky blue')
            m_lbl = tk.Label(win, font= ('Times New Roman', 20), text = 'Minutos :', bg='light sky blue')
            s_lbl = tk.Label(win, font= ('Times New Roman', 20), text = 'Segundos :', bg='light sky blue')

            h_lbl.grid(column=0 , row= 0, ipadx= 10)
            m_lbl.grid(column=0 , row= 1, ipadx= 10)
            s_lbl.grid(column=0 , row= 2, ipadx= 10)

            h_ent = tk.Entry(win)
            m_ent = tk.Entry(win)
            s_ent = tk.Entry(win)

            h_ent.grid (column=1, row= 0)
            m_ent.grid (column=1, row= 1)
            s_ent.grid (column=1, row= 2)

            submit_btn = ttk.Button(win, text='Asignar', 
                                    command=lambda:submit(h_ent.get(),
                                                m_ent.get(),
                                                s_ent.get(), 
                                                win) 
        )
            submit_btn.grid(columnspan=2, row = 3, pady=10)

        def submit(h, m, s, w):

            global counting
            counting = False

            try:
                hour = int (h)
            except:
                hour = 0
            try:
                minuet = int (m)
            except:
                minuet = 0

            try:
                second = int (s)
            except:
                second = 0

            if 25 > hour > 9:
                hora_var.set(f'{hour}')
            elif hour < 10:
                hora_var.set(f'0{hour}')
            else:
                hour = 24
                hora_var.set(f'{hour}')

            if 25 > minuet > 9:
                minutos_var.set(f'{minuet}')
            elif minuet < 10:
                minutos_var.set(f'0{minuet}')
            else:
                minuet = 59
                minutos_var.set(f'{minuet}')

            if 25 > second > 9:
                segundos_var.set(f'{second}')
            elif second < 10:
                segundos_var.set(f'0{second}')
            else:
                second = 59
                segundos_var.set(f'{second}')

            wanted_hora.set(hour)
            wanted_minutos.set(minuet)
            wanted_segundos.set(second)

            w.destroy ()

        # count_down = tk.Label(ventana, text='00:00:00', font = ('Arial', 70), bg = 'black', fg = 'white')

        lbl_marco = tk.Frame(self, background='black', padx=30, pady=20)
        lbl_marco.grid(column = 2, row = 4, padx=35, pady=10)

        hora_lab = tk.Label(lbl_marco, font = ('Times New Roman', 50), textvariable=hora_var, bg='black', fg='white')
        colon1_lab = tk.Label (lbl_marco, font = ('Times New Roman', 50), text= ':', bg='black', fg= 'white')
        minutos_lab = tk.Label(lbl_marco, font = ('Times New Roman', 50), textvariable= minutos_var, bg='black', fg= 'white')
        colon2_lab = tk.Label(lbl_marco, font = ('Times New Roman', 50), text = ':', bg='black', fg= 'white')
        segundos_lab = tk.Label(lbl_marco, font = ('Times New Roman', 50), textvariable= segundos_var, bg='black', fg= 'white')

        hora_lab.grid (column=0, row=0)
        colon1_lab.grid (column=1, row=0)
        minutos_lab.grid (column=2, row=0)
        colon2_lab.grid (column=3, row=0)
        segundos_lab.grid(column=4, row=0)

        btn_marco = tk.Frame(self, background='#0B0B3B', padx=30, pady=20)
        btn_marco.grid(column = 2, row = 5, padx=35)

        inicio_btn =tk.Button(btn_marco, text='Iniciar', height=1, width=8, font=('Arial', 10, 'bold'), command=count_down, bg='cyan')
        edit_btn = tk.Button(btn_marco, text='Tiempo', height=1, width=8, font=('Arial', 10, 'bold'), command=edit, bg= 'red')


        edit_btn.grid(column=0, row=0)
        inicio_btn.grid(column=1, row=0)