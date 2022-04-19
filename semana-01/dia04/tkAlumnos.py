from tkinter import *
from tkinter.ttk import Treeview

class Alumno:
    def registrarAlumno(self):
        self.TrvAlumnos.insert('', 0, text=self.nombre.get(), values=self.email.get())
        
    def __init__(self,window):
        self.wind = window
        self.wind.title('CRUD DE ALUMNOS')
        self.wind.geometry('420x390')
        self.wind.configure(bg='#49A')
        
        frame = LabelFrame(self.wind, text='Registro de nuevo Alumno')
        frame.grid(row=0, column=0, columnspan=3, pady=10)
        
        ############ CAMPO NOMBRE ############
        # LABEL NOMBRE
        lblNombre = Label(frame, text='Nombre: ')
        lblNombre.grid(row=1,column=0)
        # TEXT NOMBRE
        self.nombre = Entry(frame) 
        self.nombre.grid(row=1, column=1)
        
        ############ CAMPO EMAIL ############
        # LABEL EMAIL
        lblEmail = Label(frame, text='Email: ')
        lblEmail.grid(row=2,column=0)
        # TEXT EMAIL
        self.email = Entry(frame) 
        self.email.grid(row=2, column=1)
        
        ############ CAMPO EMAIL ############
        btnNuevoAlumno = Button(frame, text='Registrar', command=self.registrarAlumno)
        btnNuevoAlumno.grid(row=4, columnspan=2, sticky=W +E)

        ############ BOTON NUEVO ALUMNO ############
        self.TrvAlumnos = Treeview(height=10, columns=2)
        self.TrvAlumnos.grid(row=5, column=0, columnspan=2, padx=10)
        self.TrvAlumnos.heading('#0', text='Nombre', anchor=CENTER)
        self.TrvAlumnos.heading('#1', text='Email', anchor=CENTER)
        
window = Tk()
app = Alumno(window)
window.mainloop()