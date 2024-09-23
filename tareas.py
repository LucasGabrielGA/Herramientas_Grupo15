from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkcalendar import Calendar

colorfondo = '#0B0B3B'
colorboton = "#4CAF50"
coloreliminar = "#F44336"
colorguardar = "#2196F3"
colorfuente = 'white'
colorfondo_boton_seleccionar = "#E0E0E0"
colortexto_boton_seleccionar = "#666666"
self_calendario = None

class Agenda(Toplevel):
    def __init__(self):
        super().__init__()
        self.title("AGENDA DE TAREAS")
        self.geometry("500x500")
        self.resizable(0, 0)
        self.config(background='#0B0B3B')

        titulo = StringVar()
        fecha = StringVar()
        descripcion = StringVar()

        def abrir_calendario():
            global self_calendario
            if self_calendario and self_calendario.winfo_exists():
                self_calendario.lift()
                return

            def seleccionar_fecha():
                fecha.set(calendario.get_date())
                self_calendario.destroy()

            self_calendario = Toplevel(self)
            self_calendario.title("Seleccionar Fecha")
            
            self_calendario.geometry("300x300")  
            
            calendario = Calendar(self_calendario, selectmode='day', date_pattern='dd/MM/yyyy')
            calendario.pack(padx=20, pady=20, fill=BOTH, expand=True)
            
            boton_seleccionar = Button(self_calendario, text="S e l e c i o n a r", command=seleccionar_fecha,
                                    fg="white", bg="#696969",
                                    font=('montserrat', 10, 'bold'),
                                    relief="flat", padx=10, pady=5)
            boton_seleccionar.pack(pady=10)

        def cargar():
            if titulo.get() and fecha.get() and descripcion.get():
                listbox.insert(END, titulo.get() + " - " + fecha.get() + " - " + descripcion.get())
                titulo.set("")
                fecha.set("")
                descripcion.set("")
            else:
                messagebox.showerror("Error", "Todos los campos deben ser completados.")

        def eliminar():
            if listbox.size() == 0:
                messagebox.showerror("Error", "No hay tareas para eliminar.")
                return

            if messagebox.askquestion(title="Eliminar Tarea", message="¿Está seguro que desea eliminar la tarea?") == 'yes':
                for index in reversed(listbox.curselection()):
                    listbox.delete(index)

        def guardar():
            if listbox.size() == 0:
                messagebox.showerror("Error", "No hay tareas para guardar.")
                return

            file = filedialog.asksaveasfile(defaultextension=".txt", filetypes=[("Text File", ".txt"), ("All Files", ".*")])
            if file:
                filetext = '\n'.join(listbox.get(0, END))
                file.write(filetext)
                file.close()
        
        frame_principal = Frame(self, bg=colorfondo, padx=20, pady=20)
        frame_principal.pack(fill=BOTH, expand=True)

        Label(frame_principal, text="📝AGENDA DE TAREAS 📝", bg=colorfondo, fg=colorfuente, font=('montserrat', 20, 'bold')).pack(pady=10)

        frame_formulario = Frame(frame_principal, bg=colorfondo)
        frame_formulario.pack(pady=10)

        Label(frame_formulario, text="Tarea a realizar:", bg=colorfondo, fg=colorfuente, font=('Helvetica', 12)).grid(row=0, column=0, padx=10, pady=5, sticky="w")
        Label(frame_formulario, text="Fecha:", bg=colorfondo, fg=colorfuente, font=('Helvetica', 12)).grid(row=1, column=0, padx=10, pady=5, sticky="w")
        Label(frame_formulario, text="Descripción:", bg=colorfondo, fg=colorfuente, font=('Helvetica', 12)).grid(row=2, column=0, padx=10, pady=5, sticky="w")

        Entry(frame_formulario, textvariable=titulo, borderwidth=2, relief="groove", width=30).grid(row=0, column=1, padx=10, pady=5)
        descripcion_entry = Entry(frame_formulario, textvariable=descripcion, borderwidth=2, relief="groove", width=30)
        descripcion_entry.grid(row=2, column=1, padx=10, pady=5)

        frame_fecha = Frame(frame_formulario, bg=colorfondo)
        frame_fecha.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        Entry(frame_fecha, textvariable=fecha, borderwidth=2, relief="groove", width=15).pack(side=LEFT)

        Button(frame_fecha, text="Seleccionar", command=lambda: abrir_calendario(),
            fg="#000000", bg="#E0E0E0", font=('Helvetica', 8,),
            relief="solid", borderwidth=1, width=12).pack(side=LEFT, padx=5)

        frame_botones = Frame(frame_principal, bg=colorfondo)
        frame_botones.pack(pady=15)

        Button(frame_botones, text="AGREGAR", command=cargar, bg=colorboton, fg="white", 
            font=('montserrat', 10, 'bold'), relief="flat", width=10, padx=5, pady=5).grid(row=0, column=0, padx=10)
        Button(frame_botones, text="ELIMINAR", command=eliminar, bg=coloreliminar, fg="white", 
            font=('montserrat', 10, 'bold'), relief="flat", width=10, padx=5, pady=5).grid(row=0, column=1, padx=10)
        Button(frame_botones, text="GUARDAR", command=guardar, bg=colorguardar, fg="white", 
            font=('montserrat', 10, 'bold'), relief="flat", width=10, padx=5, pady=5).grid(row=0, column=2, padx=10)

        listbox_frame = Frame(frame_principal, bg=colorfondo)
        listbox_frame.pack(pady=20, fill=BOTH, expand=True)
        label_tareas = Label(listbox_frame, text="Lista de Tareas", bg=colorfondo, fg=colorfuente, font=('Helvetica', 14, 'bold'))
        label_tareas.pack()
        listbox_and_scrollbar_frame = Frame(listbox_frame)
        listbox_and_scrollbar_frame.pack(fill=BOTH, expand=True)
        listbox = Listbox(listbox_and_scrollbar_frame, bg="white", font=('Arial', 12), width=45, height=12, selectmode=MULTIPLE, relief="groove")
        listbox.grid(row=0, column=0, sticky="nsew")

        scrollbar_vertical = Scrollbar(listbox_and_scrollbar_frame, orient=VERTICAL, command=listbox.yview)
        scrollbar_vertical.grid(row=0, column=1, sticky="ns")
        scrollbar_horizontal = Scrollbar(listbox_and_scrollbar_frame, orient=HORIZONTAL, command=listbox.xview)
        scrollbar_horizontal.grid(row=1, column=0, sticky="ew")

        listbox.config(yscrollcommand=scrollbar_vertical.set, xscrollcommand=scrollbar_horizontal.set)
        listbox_and_scrollbar_frame.grid_rowconfigure(0, weight=1)
        listbox_and_scrollbar_frame.grid_columnconfigure(0, weight=1)
