import pandas as pd
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
class Consultas:
    def consulta6():
        df = pd.read_csv("Sacramentorealestatetransactions.csv")

        # Filtrar los datos por city=Sacramento, beds>1, baths>1, y type=Residential
        df = df[(df['city'] == 'CITRUS HEIGHTS') & (df['type'] =="Condo") & (df['price'] < 100000)]

        # Cambiar los nombres de las columnas a español
        df = df.rename(columns={
            'street': 'Calle',
            'city': 'Ciudad',
            'zip': 'Código postal',
            'state': 'Estado',
            'beds': 'Camas',
            'baths': 'Baños',
            'sq__ft': 'Pies cuadrados',
            'type': 'Tipo',
            'sale_date': 'Fecha de venta',
            'price': 'Precio',
            'latitude': 'Latitud',
            'longitude': 'Longitud'
        })

        # Crear una ventana de tkinter
        root = Tk()
        root.title("Consulta 1")
        root.geometry("600x320")
        root.resizable(False,False)
        root.config(background="violet")
        # Crear una tabla usando ttk.Treeview
        tree = ttk.Treeview(root, columns=list(df.columns), show='headings')

        # Configurar scrollbar x e y
        ysb = ttk.Scrollbar(root, orient=VERTICAL, command=tree.yview)
        xsb = ttk.Scrollbar(root, orient=HORIZONTAL, command=tree.xview)
        tree['yscroll'] = ysb.set
        tree['xscroll'] = xsb.set
        ysb.pack(side=RIGHT, fill=Y)
        xsb.pack(side=BOTTOM, fill=X)

        # Agregar los nombres de las columnas en español a la tabla
        for col in df.columns:
            tree.heading(col, text=df[col].name)

        # Establecer la propiedad "anchor" en "center" para centrar los datos en cada celda
        tree.tag_configure('center', anchor="center")
        for col in df.columns:
            tree.column(col, anchor='center')

        # Agregar los datos a la tabla
        for i, row in df.iterrows():
            tree.insert('', 'end', values=list(row), tags='center')

        # Empaquetar la tabla y mostrar la ventana
        tree.pack(side=LEFT, fill=BOTH, expand=1)
        tree.place(x=0,y=30,height=278,width=781)

        def regresar():
            root.destroy()
            from union import union
            union.consulta6()

        volver_btn = Button(root, text="Volver", command=regresar)
        volver_btn.pack(side='top')
        messagebox.showinfo(title="Información", message="Número de casas con sus especificaciones: {}".format(df.shape[0]))

        root.mainloop()    
    def consulta7():
        df = pd.read_csv("Sacramentorealestatetransactions.csv")

        # Filtrar los datos por city=Sacramento, beds>1, baths>1, y type=Residential
        df = df[(df['city'] == 'ANTELOPE') & (df['price'] > 100000) & (df['price'] < 200000) & (df['sq__ft'] >1200) ]

        # Cambiar los nombres de las columnas a español
        df = df.rename(columns={
            'street': 'Calle',
            'city': 'Ciudad',
            'zip': 'Código postal',
            'state': 'Estado',
            'beds': 'Camas',
            'baths': 'Baños',
            'sq__ft': 'Pies cuadrados',
            'type': 'Tipo',
            'sale_date': 'Fecha de venta',
            'price': 'Precio',
            'latitude': 'Latitud',
            'longitude': 'Longitud'
        })

        # Crear una ventana de tkinter
        root = Tk()
        root.title("Consulta 2")
        root.geometry("600x320")
        root.resizable(False,False)
        root.config(background="#29F3EA")

        # Crear una tabla usando ttk.Treeview
        tree = ttk.Treeview(root, columns=list(df.columns), show='headings')

        # Configurar scrollbar x e y
        ysb = ttk.Scrollbar(root, orient=VERTICAL, command=tree.yview)
        xsb = ttk.Scrollbar(root, orient=HORIZONTAL, command=tree.xview)
        tree['yscroll'] = ysb.set
        tree['xscroll'] = xsb.set
        ysb.pack(side=RIGHT, fill=Y)
        xsb.pack(side=BOTTOM, fill=X)

        # Agregar los nombres de las columnas en español a la tabla
        for col in df.columns:
            tree.heading(col, text=df[col].name)

        # Establecer la propiedad "anchor" en "center" para centrar los datos en cada celda
        tree.tag_configure('center', anchor="center")
        for col in df.columns:
            tree.column(col, anchor='center')

        # Agregar los datos a la tabla
        for i, row in df.iterrows():
            tree.insert('', 'end', values=list(row), tags='center')

        # Empaquetar la tabla y mostrar la ventana
        tree.pack(side=LEFT, fill=BOTH, expand=1)
        tree.place(x=0,y=30,height=278,width=781)

        def regresar():
            root.destroy()
            from union import union
            union.consulta7()

        volver_btn = Button(root, text="Volver", command=regresar)
        volver_btn.pack(side='top')
        messagebox.showinfo(title="Información", message="Número de casas con sus especificaciones: {}".format(df.shape[0]))

        root.mainloop()    

    def consulta3():
        df = pd.read_csv("Sacramentorealestatetransactions.csv")

        # Filtrar los datos por city=Sacramento, beds>1, baths>1, y type=Residential
        df = df[(df['city'] == 'RIO LINDA') & (df['beds'] >3) & (df['price'] < 500000) & (df['type'] == 'Residential')]

        # Cambiar los nombres de las columnas a español
        df = df.rename(columns={
            'street': 'Calle',
            'city': 'Ciudad',
            'zip': 'Código postal',
            'state': 'Estado',
            'beds': 'Camas',
            'baths': 'Baños',
            'sq__ft': 'Pies cuadrados',
            'type': 'Tipo',
            'sale_date': 'Fecha de venta',
            'price': 'Precio',
            'latitude': 'Latitud',
            'longitude': 'Longitud'
        })

        # Crear una ventana de tkinter
        root = Tk()
        root.title("Consulta 3")
        root.geometry("600x320")
        root.resizable(False,False)
        root.config(background="green")

        # Crear una tabla usando ttk.Treeview
        tree = ttk.Treeview(root, columns=list(df.columns), show='headings')

        # Configurar scrollbar x e y
        ysb = ttk.Scrollbar(root, orient=VERTICAL, command=tree.yview)
        xsb = ttk.Scrollbar(root, orient=HORIZONTAL, command=tree.xview)
        tree['yscroll'] = ysb.set
        tree['xscroll'] = xsb.set
        ysb.pack(side=RIGHT, fill=Y)
        xsb.pack(side=BOTTOM, fill=X)

        # Agregar los nombres de las columnas en español a la tabla
        for col in df.columns:
            tree.heading(col, text=df[col].name)

        # Establecer la propiedad "anchor" en "center" para centrar los datos en cada celda
        tree.tag_configure('center', anchor="center")
        for col in df.columns:
            tree.column(col, anchor='center')

        # Agregar los datos a la tabla
        for i, row in df.iterrows():
            tree.insert('', 'end', values=list(row), tags='center')

        # Empaquetar la tabla y mostrar la ventana
        tree.pack(side=LEFT, fill=BOTH, expand=1)
        tree.place(x=0,y=30,height=278,width=781)

        def regresar():
            root.destroy()
            from union import union
            union.consulta3()

        volver_btn = Button(root, text="Volver", command=regresar)
        volver_btn.pack(side='top')
        messagebox.showinfo(title="Información", message="Número de casas con sus especificaciones: {}".format(df.shape[0]))

        root.mainloop()
    def consulta4():
        df = pd.read_csv("Sacramentorealestatetransactions.csv")

        # Filtrar los datos por city=Sacramento, beds>1, baths>1, y type=Residential
        df = df[(df['city'] == 'SACRAMENTO') & (df['beds'] >1) & (df['sq__ft'] > 1000) & (df['baths'] == 2)]

        # Cambiar los nombres de las columnas a español
        df = df.rename(columns={
            'street': 'Calle',
            'city': 'Ciudad',
            'zip': 'Código postal',
            'state': 'Estado',
            'beds': 'Camas',
            'baths': 'Baños',
            'sq__ft': 'Pies cuadrados',
            'type': 'Tipo',
            'sale_date': 'Fecha de venta',
            'price': 'Precio',
            'latitude': 'Latitud',
            'longitude': 'Longitud'
        })

        # Crear una ventana de tkinter
        root = Tk()
        root.title("Consulta 4")
        root.geometry("600x320")
        root.resizable(False,False)
        root.config(background="blue")

        # Crear una tabla usando ttk.Treeview
        tree = ttk.Treeview(root, columns=list(df.columns), show='headings')

        # Configurar scrollbar x e y
        ysb = ttk.Scrollbar(root, orient=VERTICAL, command=tree.yview)
        xsb = ttk.Scrollbar(root, orient=HORIZONTAL, command=tree.xview)
        tree['yscroll'] = ysb.set
        tree['xscroll'] = xsb.set
        ysb.pack(side=RIGHT, fill=Y)
        xsb.pack(side=BOTTOM, fill=X)

        # Agregar los nombres de las columnas en español a la tabla
        for col in df.columns:
            tree.heading(col, text=df[col].name)

        # Establecer la propiedad "anchor" en "center" para centrar los datos en cada celda
        tree.tag_configure('center', anchor="center")
        for col in df.columns:
            tree.column(col, anchor='center')

        # Agregar los datos a la tabla
        for i, row in df.iterrows():
            tree.insert('', 'end', values=list(row), tags='center')

        # Empaquetar la tabla y mostrar la ventana
        tree.pack(side=LEFT, fill=BOTH, expand=1)
        tree.place(x=0,y=30,height=278,width=781)

        def regresar():
            root.destroy()
            from union import union
            union.consulta4()

        volver_btn = Button(root, text="Volver", command=regresar)
        volver_btn.pack(side='top')
        messagebox.showinfo(title="Información", message="Número de casas con sus especificaciones: {}".format(df.shape[0]))

        root.mainloop()
    def consulta5():
        df = pd.read_csv("Sacramentorealestatetransactions.csv")

        # Filtrar los datos por city=Sacramento, beds>1, baths>1, y type=Residential
        df = df[(df['city'] == 'NORTH HIGHLANDS') & (df['beds'] ==4) & (df['sq__ft'] > 1000) & (df['sq__ft'] < 2000)]

        # Cambiar los nombres de las columnas a español
        df = df.rename(columns={
            'street': 'Calle',
            'city': 'Ciudad',
            'zip': 'Código postal',
            'state': 'Estado',
            'beds': 'Camas',
            'baths': 'Baños',
            'sq__ft': 'Pies cuadrados',
            'type': 'Tipo',
            'sale_date': 'Fecha de venta',
            'price': 'Precio',
            'latitude': 'Latitud',
            'longitude': 'Longitud'
        })

        # Crear una ventana de tkinter
        root = Tk()
        root.title("Consulta 5")
        root.geometry("600x320")
        root.resizable(False,False)
        root.config(background="#4B0082")

        # Crear una tabla usando ttk.Treeview
        tree = ttk.Treeview(root, columns=list(df.columns), show='headings')

        # Configurar scrollbar x e y
        ysb = ttk.Scrollbar(root, orient=VERTICAL, command=tree.yview)
        xsb = ttk.Scrollbar(root, orient=HORIZONTAL, command=tree.xview)
        tree['yscroll'] = ysb.set
        tree['xscroll'] = xsb.set
        ysb.pack(side=RIGHT, fill=Y)
        xsb.pack(side=BOTTOM, fill=X)

        # Agregar los nombres de las columnas en español a la tabla
        for col in df.columns:
            tree.heading(col, text=df[col].name)

        # Establecer la propiedad "anchor" en "center" para centrar los datos en cada celda
        tree.tag_configure('center', anchor="center")
        for col in df.columns:
            tree.column(col, anchor='center')

        # Agregar los datos a la tabla
        for i, row in df.iterrows():
            tree.insert('', 'end', values=list(row), tags='center')

        # Empaquetar la tabla y mostrar la ventana
        tree.pack(side=LEFT, fill=BOTH, expand=1)
        tree.place(x=0,y=30,height=278,width=781)

        def regresar():
            root.destroy()
            from union import union
            union.consulta5()

        volver_btn = Button(root, text="Volver", command=regresar)
        volver_btn.pack(side='top')
        messagebox.showinfo(title="Información", message="Número de casas con sus especificaciones: {}".format(df.shape[0]))

        root.mainloop()    
    