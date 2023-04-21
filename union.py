from tkinter import *
class union:
    def consulta1():
        root = Tk()
        root.title("Consulta 1")
        root.geometry("600x190")
        root.resizable(False,False)
        root.config(background="orange")
        lbc1 = Label(root, text="Consulta 1: Deseo saber cuantas casas hay en la ciudad Elk Grove con 1 o más camas, \n" 
                          "2 o más baños y de tipo Condo hay.")

        lbc1.pack()
        lbc1.place(relx=0.5,y=30,anchor="center")

        def c1():
            root.destroy()
            from consulta import Consultas
            Consultas.consulta1() 
        def regresar():
            root.destroy()
            from main import Inicio
            Inicio.mostrarindex()
        irc1=Button(root,text="Ver datos",command=c1)
        irc1.pack()
        irc1.place(relx=0.5,y=100,anchor="center")
        btnregresar=Button(root,text="Volver",command=regresar)
        btnregresar.pack()
        btnregresar.place(relx=0.5,y=160,anchor="center")
        root.mainloop()
    
    def consulta2():
        root = Tk()
        root.title("Consulta 2")
        root.geometry("600x190")
        root.resizable(False,False)
        root.config(background="yellow")
        lbc2 = Label(root, text="Consulta 2: Deseo saber cuantas casas en la ciudad de Galt con 2 o más camas, con un precio \n"
                   "entre $100000 y $200000 y de tipo Residencial hay.")

        lbc2.pack()
        lbc2.place(relx=0.5,y=30,anchor="center")

        def c2():
            root.destroy()
            from consulta import Consultas
            Consultas.consulta2() 
        def regresar():
            root.destroy()
            from main import Inicio
            Inicio.mostrarindex()
        irc2=Button(root,text="Ver datos",command=c2)
        irc2.pack()
        irc2.place(relx=0.5,y=100,anchor="center")
        btnregresar=Button(root,text="Volver",command=regresar)
        btnregresar.pack()
        btnregresar.place(relx=0.5,y=160,anchor="center")
        root.mainloop()
    
    def consulta3():
        root = Tk()
        root.title("Consulta 3")
        root.geometry("600x190")
        root.resizable(False,False)
        root.config(background="green")
        lbc3 = Label(root, text="Consulta 3: Deseo saber cuantas casas en la ciudad de Rio Linda con mas de 3 camas,\n"
                    "con un precio menor a $500000 y de tipo Residencial hay.")
        lbc3.pack()
        lbc3.place(relx=0.5,y=30,anchor="center")

        def c3():
            root.destroy()
            from consulta import Consultas
            Consultas.consulta3() 
        def regresar():
            root.destroy()
            from main import Inicio
            Inicio.mostrarindex()
        irc3=Button(root,text="Ver datos",command=c3)
        irc3.pack()
        irc3.place(relx=0.5,y=100,anchor="center")
        btnregresar=Button(root,text="Volver",command=regresar)
        btnregresar.pack()
        btnregresar.place(relx=0.5,y=160,anchor="center")
        root.mainloop()
    def consulta4():
        root = Tk()
        root.title("Consulta 4")
        root.geometry("600x190")
        root.resizable(False,False)
        root.config(background="blue")
        lbc4 = Label(root, text="Consulta 4: Deseo saber cuantas casas en la ciudad de Sacramento con mas de 1 cama, con 2 baños\n"
                "y con mas de 1000 pies cuadrados hay.")
        lbc4.pack()
        lbc4.place(relx=0.5,y=30,anchor="center")

        def c4():
            root.destroy()
            from consulta import Consultas
            Consultas.consulta4() 
        def regresar():
            root.destroy()
            from main import Inicio
            Inicio.mostrarindex()
        irc4=Button(root,text="Ver datos",command=c4)
        irc4.pack()
        irc4.place(relx=0.5,y=100,anchor="center")
        btnregresar=Button(root,text="Volver",command=regresar)
        btnregresar.pack()
        btnregresar.place(relx=0.5,y=160,anchor="center")
        root.mainloop()
    def consulta5():
        root = Tk()
        root.title("Consulta 5")
        root.geometry("600x190")
        root.resizable(False,False)
        root.config(background="#4B0082")
        lbc5 = Label(root, text="Consulta 5: Deseo saber cuantas casas en la ciudad de Nort Highlands con 4 camas, que midan entre\n"
                "1000 y 2000 pies cuadrados hay.")
        lbc5.pack()
        lbc5.place(relx=0.5,y=30,anchor="center")

        def c5():
            root.destroy()
            from consulta import Consultas
            Consultas.consulta5() 
        def regresar():
            root.destroy()
            from main import Inicio
            Inicio.mostrarindex()
        irc5=Button(root,text="Ver datos",command=c5)
        irc5.pack()
        irc5.place(relx=0.5,y=100,anchor="center")
        btnregresar=Button(root,text="Volver",command=regresar)
        btnregresar.pack()
        btnregresar.place(relx=0.5,y=160,anchor="center")
        root.mainloop()
    def consulta6():
        root = Tk()
        root.title("Consulta 6")
        root.geometry("600x190")
        root.resizable(False,False)
        root.config(background="violet")
        lbc6 = Label(root, text="Consulta 1: Deseo saber cuantas casas en la ciudad de Citrus Heights de tipo Condo, con un precio\n"
                "menor a $100000 hay.")
        lbc6.pack()
        lbc6.place(relx=0.5,y=30,anchor="center")

        def c6():
            root.destroy()
            from consulta import Consultas
            Consultas.consulta6() 
        def regresar():
            root.destroy()
            from main import Inicio
            Inicio.mostrarindex()
        irc6=Button(root,text="Ver datos",command=c6)
        irc6.pack()
        irc6.place(relx=0.5,y=100,anchor="center")
        btnregresar=Button(root,text="Volver",command=regresar)
        btnregresar.pack()
        btnregresar.place(relx=0.5,y=160,anchor="center")
        root.mainloop()
    def consulta7():
        root = Tk()
        root.title("Consulta 7")
        root.geometry("600x190")
        root.resizable(False,False)
        root.config(background="#29F3EA")
        lbc7 = Label(root, text="Consulta 1: Deseo saber cuantas casas en la ciudad de Antelope con un precio entre $100000 y $200000\n"
                "mas a parte con un tamaño mayor a 1200 pies cuadrados hay.")
        lbc7.pack()
        lbc7.place(relx=0.5,y=30,anchor="center")

        def c7():
            root.destroy()
            from consulta import Consultas
            Consultas.consulta7() 
        def regresar():
            root.destroy()
            from main import Inicio
            Inicio.mostrarindex()
        irc7=Button(root,text="Ver datos",command=c7)
        irc7.pack()
        irc7.place(relx=0.5,y=100,anchor="center")
        btnregresar=Button(root,text="Volver",command=regresar)
        btnregresar.pack()
        btnregresar.place(relx=0.5,y=160,anchor="center")
        root.mainloop()
