import pandas as pd
from tkinter import *
import tkinter as tk

class Inicio:
    def mostrarindex():
        root = tk.Tk()
        root.title("Menú")
        root.geometry("400x350")
        root.config(background="black")

        def c3():
            root.destroy()
            from union import union
            union.consulta3()

        def c4():
            root.destroy()
            from union import union
            union.consulta4()

        def c5():
            root.destroy()
            from union import union
            union.consulta5()

        def c6():
            root.destroy()
            from union import union
            union.consulta6()

        def c7():
            root.destroy()
            from union import union
            union.consulta7()

        b1 = tk.Button(root, text="consulta 3", command=c3)
        b1.pack()
        b1.place(relx=0.5, y=120, anchor="center")

        b2 = tk.Button(root, text="consulta 4", command=c4)
        b2.pack()
        b2.place(relx=0.5, y=160, anchor="center")

                #nooooooooooooooooooooooooooooooooooooooooo
                 

        b4 = tk.Button(root, text="consulta 1", command=c6)
        b4.pack()
        b4.place(relx=0.5, y=40, anchor="center")

        b5 = tk.Button(root, text="consulta 2", command=c7)
        b5.pack()
        b5.place(relx=0.5, y=80, anchor="center")

        b3 = tk.Button(root, text="consulta 5", command=c5)
        b3.pack()
        b3.place(relx=0.5, y=200, anchor="center")

        root.mainloop()

    mostrarindex()
