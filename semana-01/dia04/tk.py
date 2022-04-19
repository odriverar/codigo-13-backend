from tkinter import *
from tkinter import messagebox

def saludar():
    print("Hola mundo tk")
    messagebox.showinfo("mensaje","Hola " + txtNombre.get())

app = Tk()
app.title('Mi primera interface grafica')
app.geometry('200x200')

frame = LabelFrame(app, text='Ventana')
frame.grid(row=0, column=0, columnspan=3, pady=10)
lbNombre = Label(frame, text='Nombre: ')
lbNombre.grid(row=1, column=0)
txtNombre = Entry(frame)
txtNombre.grid(row=1, column=1)
btnSaludo = Button(frame, text='Saludar', command=saludar)
btnSaludo.grid(row=1, column=2)
app.mainloop()