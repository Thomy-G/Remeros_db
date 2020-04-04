import matplotlib
matplotlib.use("TkAgg")

from matplotlib.backends.backend_tkagg import FigureCanvasAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

import tkinter as tk
from tkinter import ttk
import sqlite3
import datetime
#conectarse a la base de datos
conn = sqlite3.connect("Remo.db")
#crear un cursor dentro de la base
c = conn.cursor()
#determinante de fonts de toda la app
LARGE_FONT = ("Verdana", 12) #Para titulos
class Dbapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        #Agregar icono con extension .ico
        #tk.Tk.iconbitmap(self, default="Insertar icono")
        tk.Tk.wm_title(self, "Aplicacion RemoDB")

        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, Table_page,Excercises_Page_add, Athlets_page, Athlets_page_Add, Zone_page, Zone_page_Add ):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky='nsew')
        self.Show_frame(StartPage)

    def Show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Inicio", font = LARGE_FONT)
        label.pack()

        button1 = ttk.Button(self, text='Ir a la Tabla de trabajos', command=lambda: controller.Show_frame(Table_page))
        button1.pack()

        button2 = ttk.Button(self, text='Ir a la Tabla de remeros', command=lambda: controller.Show_frame(Athlets_page))
        button2.pack()

        button3 = ttk.Button(self, text='Ir a la Tabla de zonas', command=lambda: controller.Show_frame(Zone_page))
        button3.pack()


class Table_page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Tabla de trabajos", font=LARGE_FONT)
        label.grid(row=0, column=0,padx=30)

        headings = ("NOM","APEL" , "Distancia", "Tiempo", "Día", "Zona", "BPM_Promedio",'Nro Trabajo en el dia', "Anotaciones")
        tree1 = ttk.Treeview(self, height=10, columns=headings, )
        tree1.grid(row=2, column=0, columnspan=1)
        tree1.heading('#0', text="Trabajos_id", anchor='w')
        tree1.heading('NOM', text="Nombre", anchor='w')
        tree1.heading('APEL', text="Apellido", anchor='w')
        tree1.heading('Distancia', text="Distancia", anchor='w')
        tree1.heading('Tiempo', text="Tiempo", anchor='w')
        tree1.heading('Día', text="Día", anchor='w')
        tree1.heading('Zona', text="Zona", anchor='w')
        tree1.heading('BPM_Promedio', text="Pulsaciones Promedio", anchor='w')
        tree1.heading('Nro Trabajo en el dia', text="Nro Trabajo en el dia", anchor='w')
        tree1.heading("Anotaciones", text="Anotaciones", anchor='w')

        button1 = ttk.Button(self, text='Ir a la pagina de inicio', command=lambda:controller.Show_frame(StartPage))
        button1.grid(row=0, column=2,padx=30)

        button2 = ttk.Button(self, text='Agregar Trabajo', command=lambda: controller.Show_frame(Excercises_Page_add))
        button2.grid(row=3, column=0, padx=30)

class Excercises_Page_add(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="Nuevo Trabajo", font=LARGE_FONT)
        label.grid(row=0, column=0, padx=20, pady=20)

        button1 = ttk.Button(self, text='Ir a la pagina de inicio', command=lambda: controller.Show_frame(StartPage))
        button1.grid(row=0, column=1, padx=30)


        #Sql para agarrar las diferentes remeros
        lista_de_remeros = c.execute("SELECT * FROM remeros_1")
        Remerlb = []
        Remerlbdni = []
        num = 0

        for i in lista_de_remeros:

            Remerlb.append((str(num) + " " + i[2]+" "+i[3]))
            num = num+1
            Remerlbdni.append(int(i[0]))


        # Sql para agarrar las diferentes zonas
        Lista_de_zonas = c.execute("SELECT * FROM Zonas_Log")

        zonaslb = []
        for z in Lista_de_zonas:
            zonaslb.append(z[0])






        Remero_add_lbl = tk.Label(self, text="Remero", font=LARGE_FONT)
        Remero_add_lbl.grid(row=1, column=0, padx=20, pady=10)

        # Remerlb (Remeros list box son los diferentes remeros que se pueden elegir)
        Remero_add_Combobox = ttk.Combobox(self, values= Remerlb)
        Remero_add_Combobox.grid(row=1, column=1, padx=20, pady=10)

        Distancia_add_lbl = ttk.Label(self, text="Distancia", font=LARGE_FONT)
        Distancia_add_lbl.grid(row=2, column=0, padx=20, pady=10)

        Distancia_add_entry = ttk.Entry(self)
        Distancia_add_entry.grid(row=2, column=1, padx=20, pady=10)

        Tiempo_add_lbl = ttk.Label(self, text="Tiempo(mm:ss)", font=LARGE_FONT)
        Tiempo_add_lbl.grid(row=3, column=0, padx=20, pady=10)

        Tiempo_add_entry = ttk.Entry(self)
        Tiempo_add_entry.grid(row=3, column=1, padx=20, pady=10)

        Dia_add_lbl = ttk.Label(self, text="Día", font=LARGE_FONT)
        Dia_add_lbl.grid(row=4, column=0, padx=20, pady=10)

        Dia_add_entry = ttk.Entry(self)
        Dia_add_entry.grid(row=4, column=1, padx=20, pady=10)
        Dia_add_entry.insert(0, "AAAA/MM/DD")

        Zona_add_lbl = ttk.Label(self, text="Zona", font=LARGE_FONT)
        Zona_add_lbl.grid(row=5, column=0, padx=20, pady=10)

        Zona_add_Combobox= ttk.Combobox(self, values = zonaslb)
        Zona_add_Combobox.grid(row=5, column=1, padx=20, pady=10)

        BPM_Promedio_add_lbl = ttk.Label(self, text="BPM Promedio del Trabajo", font=LARGE_FONT)
        BPM_Promedio_add_lbl.grid(row=6, column=0, padx=20, pady=10)

        BPM_Promedio_add_entry = ttk.Entry(self)
        BPM_Promedio_add_entry.grid(row=6, column=1, padx=20, pady=10)

        Trabajo_del_dia_add_lbl = ttk.Label(self, text="Nro trabajo en el día", font=LARGE_FONT)
        Trabajo_del_dia_add_lbl.grid(row=1, column=2, padx=20, pady=10)

        Trabajo_del_dia_add_entry = ttk.Entry(self)
        Trabajo_del_dia_add_entry.grid(row=1, column=3, padx=20, pady=10)

        Machine_add_lbl = ttk.Label(self, text="Ejercicio", font=LARGE_FONT)
        Machine_add_lbl.grid(row=2, column=2, padx=20, pady=10)

        machlb = ["Remo", "Bici Fija", "Correr"]

        Machine_add_entry = ttk.Combobox(self, values=machlb)
        Machine_add_entry.grid(row=2, column=3, padx=20, pady=10)


        Anotaciones_add_lbl = ttk.Label(self, text="Anotaciones", font=LARGE_FONT)
        Anotaciones_add_lbl.grid(row=1, column=6)

        Anotaciones_add_entry = tk.Text(self, width=20)
        Anotaciones_add_entry.grid(row=1, column=7, rowspan = 20, sticky= "nwes")


        Bote_add_lbl = tk.Label(self, text="Bote", font=LARGE_FONT)
        Bote_add_lbl.grid(row=7, column=0, padx=20, pady=10)

        Botelb = ["1x", "2x", "2-", "2+", "4x", "4-", "4+", "8+" ]

        Bote_add_Combobox = ttk.Combobox(self, values=Botelb)
        Bote_add_Combobox.grid(row=7, column=1, padx=20, pady=10)

        def callback(event):
            if Machine_add_entry.get() != "Remo":
                Bote_add_Combobox.grid_forget()
                Bote_add_lbl.grid_forget()
            else:
                Bote_add_Combobox.grid(row=7, column=1, padx=20, pady=10)
                Bote_add_lbl.grid(row=7, column=0, padx=20, pady=10)



        Machine_add_entry.bind("<<ComboboxSelected>>", callback)





        button1 = ttk.Button(self, text='Insertar datos', command=lambda: submmit_Excersise(Remero_add_Combobox.get(),
                                                            int(Distancia_add_entry.get()), Tiempo_add_entry.get(),
                                                            Dia_add_entry.get(), Zona_add_Combobox.get(),
                                                            float(BPM_Promedio_add_entry.get()),
                                                            Trabajo_del_dia_add_entry.get(), Machine_add_entry.get(),
                                                            Anotaciones_add_entry.get("1.0","end"), Bote_add_Combobox.get() ))
        button1.grid(row=7, column=3)




        def submmit_Excersise(DNI, Distance, time, DAY, ZON, BPM, NDT, EXC, ANOT, BOTE):
            Not_working = tk.Label(self, text="No funciono")
            Not_working.grid_forget()


            dni = list(DNI)
            dni = Remerlbdni[int((dni[0]))]

            NewTime = time.replace(":", "")

            NewDate = DAY.replace("/", "")

            if EXC != "Remo":
                bote = None
            else:
                bote = BOTE


            





            try:
             c.execute("""INSERT INTO Trabajos (DNI, Distancia, Tiempo, Día, Zona, BPM_Promedio,
             N°_trabajo_del_día, Excercise, Anotaciones )
                       VALUES (?,?,?,?,?,?,?,?,?)""", (dni, Distance, NewTime, NewDate, ZON, BPM, NDT, EXC, ANOT, bote ))
             conn.commit()


            except :
                print("non valid")
                Not_working.grid(row=7, column=5)




class Athlets_page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Tabla de remeros", font=LARGE_FONT)
        label.grid(row=0, column=0, padx=30)

        button1 = ttk.Button(self, text='Ir a la pagina de inicio', command=lambda: controller.Show_frame(StartPage))
        button1.grid(row=1, column=0, padx=30, pady=20)

        headings = ('APEL',"DNI",'Nsoc', 'PES', 'ALT',"Sexo", "Fecha de nacimiento", "Mejor 2K",'Categoria(Peso)',
                    'Categoria(Edad)')


        tree2 = ttk.Treeview(self, height= 10, columns= headings, )
        tree2.grid(row=2, column=0, columnspan=1)
        tree2.heading('#0', text="Nombre", anchor='w')
        tree2.heading('APEL', text="Apellido", anchor='w')
        tree2.heading('DNI', text="DNI", anchor = 'w')
        tree2.heading('Nsoc', text="Numero de socio", anchor='w')
        tree2.heading('PES', text="Peso(Kg)", anchor='w')
        tree2.heading('ALT', text="Altura(cm)", anchor='w')
        tree2.heading('Sexo', text="Sexo", anchor='w')
        tree2.heading('Fecha de nacimiento', text="Fecha de nacimiento", anchor='w')
        tree2.heading('Mejor 2K', text="Mejor 2K", anchor='w')
        tree2.heading('Categoria(Peso)', text="Categoria(Peso)", anchor='w')
        tree2.heading('Categoria(Edad)', text="Categoria(Edad)", anchor='w')

        lista_de_remeros = c.execute("SELECT * FROM remeros_1")

        for i in lista_de_remeros:
            pro_bday= list(str(i[7]))
            altbday= [pro_bday[-2],pro_bday[-1],pro_bday[-4],pro_bday[-3],pro_bday[0],pro_bday[1],pro_bday[2],pro_bday[3]]
            altbday.insert(2, "/")

            altbday.insert(-4, "/")
            new_bday = "".join(altbday)

            pro_2k = list(str(i[8]))
            pro_2k.insert(-2, ",")
            pro_2k.insert(1,":")
            new_2k = "".join(pro_2k)

            if i[6] == "Masculino":
                if i[4] > 74:
                    CatP = "Pesado"
                else:
                    CatP = "Ligero"
            else:
                if i[4] > 60:
                    CatP = "Pesada"
                else:
                    CatP = "Ligera"

            anmd= str(i[7])
            anmd=  anmd[0:4]
            ano_nacimiento = int(anmd)

            obj_ano = datetime.datetime.now()
            ano = obj_ano.year

            if (ano-ano_nacimiento) < 15:
                CatE = "Cadete"
            elif (ano-ano_nacimiento) <17:
                CatE = "Menor"
            elif (ano-ano_nacimiento) <19:
                CatE = "Junior"
            elif (ano-ano_nacimiento) < 23:
                CatE = "Senior B"
            else:
                CatE = "S"
            #Mangling to get : Name, surname, DNI, Nsoc, Weight, height,
            tree2.insert('', 0,text= i[2], values=[i[3],i[0], i[1],i[4],i[5],i[6], new_bday, new_2k, CatP, CatE ])
            def refresh():
                for item in tree2:
                    tree2.delete(item)
                lista_de_remeros = c.execute("SELECT * FROM remeros_1")

                for i in lista_de_remeros:
                    pro_bday = list(str(i[7]))
                    altbday = [pro_bday[-2], pro_bday[-1], pro_bday[-4], pro_bday[-3], pro_bday[0], pro_bday[1],
                               pro_bday[2], pro_bday[3]]
                    altbday.insert(2, "/")

                    altbday.insert(-4, "/")
                    new_bday = "".join(altbday)

                    pro_2k = list(str(i[8]))
                    pro_2k.insert(-2, ",")
                    pro_2k.insert(1, ":")
                    new_2k = "".join(pro_2k)

                    if i[6] == "Masculino":
                        if i[4] > 74:
                            CatP = "Pesado"
                        else:
                            CatP = "Ligero"
                    else:
                        if i[4] > 60:
                            CatP = "Pesada"
                        else:
                            CatP = "Ligera"

                    anmd = str(i[7])
                    anmd = anmd[0:4]
                    ano_nacimiento = int(anmd)

                    obj_ano = datetime.datetime.now()
                    ano = obj_ano.year

                    if (ano - ano_nacimiento) < 15:
                        CatE = "Cadete"
                    elif (ano - ano_nacimiento) < 17:
                        CatE = "Menor"
                    elif (ano - ano_nacimiento) < 19:
                        CatE = "Junior"
                    elif (ano - ano_nacimiento) < 23:
                        CatE = "Senior B"
                    else:
                        CatE = "S"
                    # Mangling to get : Name, surname, DNI, Nsoc, Weight, height,
                    tree2.insert('', 0, text=i[2],
                                 values=[i[3], i[0], i[1], i[4], i[5], i[6], new_bday, new_2k, CatP, CatE])



        button2 = ttk.Button(self, text='Agregar Remero', command=lambda: controller.Show_frame(Athlets_page_Add))
        button2.grid(row=3, column=1, padx=30, pady=20)

        button3 =ttk.Button(self, text='Refresh', command=lambda: refresh())
        button3.grid(row=3, column=2, padx=30, pady=20)

class Athlets_page_Add(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)



        label = ttk.Label(self, text="Agregar remeros", font=LARGE_FONT)
        label.grid(row=0,column=0,padx=20, pady=20)

        button1 = ttk.Button(self, text='Ir a la pagina de inicio', command=lambda: controller.Show_frame(StartPage))
        button1.grid(row=0, column=1, padx=30)

        #Agregando Labels y botones en el sigiente orden: 2 lineas de Lablel, 2 o 3 de entry/Listbox
        DNI_add_lbl = tk.Label(self, text="DNI", font=LARGE_FONT)
        DNI_add_lbl.grid(row=1, column=0,padx=20, pady=10)

        DNI_add_entry = ttk.Entry(self)
        DNI_add_entry.grid(row=1, column=1,padx=20, pady=10)


        NSoc_add_lbl = ttk.Label(self, text="N° de Socio", font=LARGE_FONT)
        NSoc_add_lbl.grid(row=2, column=0,padx=20, pady=10)

        NSoc_add_entry = ttk.Entry(self)
        NSoc_add_entry.grid(row=2, column=1,padx=20, pady=10)


        Nombre_add_lbl = ttk.Label(self, text="Nombre", font=LARGE_FONT)
        Nombre_add_lbl.grid(row=3, column=0,padx=20, pady=10)

        Nombre_add_entry = ttk.Entry(self)
        Nombre_add_entry.grid(row=3, column=1,padx=20, pady=10)


        Apellido_add_lbl = ttk.Label(self, text="Apellido", font=LARGE_FONT)
        Apellido_add_lbl.grid(row=4, column=0,padx=20, pady=10)

        Apellido_add_entry = ttk.Entry(self)
        Apellido_add_entry.grid(row=4, column=1,padx=20, pady=10)


        Peso_add_lbl = ttk.Label(self, text="Peso", font=LARGE_FONT)
        Peso_add_lbl.grid(row=5, column=0,padx=20, pady=10)

        Peso_add_entry = ttk.Entry(self)
        Peso_add_entry.grid(row=5, column=1,padx=20, pady=10)

        Altura_add_lbl = ttk.Label(self, text="Altura", font=LARGE_FONT)
        Altura_add_lbl.grid(row=6, column=0, padx=20, pady=10)

        Altura_add_entry = ttk.Entry(self)
        Altura_add_entry.grid(row=6, column=1, padx=20, pady=10)

        Sexo_add_lbl = ttk.Label(self, text="Sexo", font=LARGE_FONT)
        Sexo_add_lbl.grid(row=7, column=0, padx=20, pady=10)

        Sexo_add_listbox = ttk.Combobox(self, values= ["Femenino", "Masculino"])
        Sexo_add_listbox.grid(row=7, column=1, padx=20)


        BDAY_add_lbl = ttk.Label(self, text="Fecha de Nacimiento", font=LARGE_FONT)
        BDAY_add_lbl.grid(row=8, column=0, padx=20, pady=10)

        BDAY_add_entry = ttk.Entry(self)
        BDAY_add_entry.insert(1,"AAAA/MM/DD")
        BDAY_add_entry.grid(row=8, column=1, padx=20, pady=10)

        best_2K_add_lbl = ttk.Label(self, text="Mejor 2K", font=LARGE_FONT)
        best_2K_add_lbl.grid(row=9, column=0, padx=20, pady=10)

        best_2K_add_entry = ttk.Entry(self)
        best_2K_add_entry.insert(1,"MM/SS,MS")
        best_2K_add_entry.grid(row=9, column=1, padx=20, pady=10)
        #Boton que ingresa los datos a la base
        button1 = ttk.Button(self, text='Insertar datos', command= lambda: submmit_athlete(int(DNI_add_entry.get()),
                                                                                           int(NSoc_add_entry.get()),
                                                                                           Nombre_add_entry.get(),
                                                                                           Apellido_add_entry.get(),
                                                                                           float(Peso_add_entry.get()),
                                                                                           int(Altura_add_entry.get()),
                                                                                           Sexo_add_listbox.get() ,
                                                                                           BDAY_add_entry.get(),
                                                                                           best_2K_add_entry.get()))
        button1.grid(row=10, column=1)
        #Agarra los resultados de los entry y listbox y los mete en las bases de datos
        def submmit_athlete(DNI, Nsoc, NOM, APEL, PES, ALT, SEX, BDAY, B2K):
            Not_working = tk.Label(self, text="No funciono")
            Not_working.grid_forget()



            Num_BDAY = int(BDAY.replace("/",""))

            Num_B2K = B2K.replace(":", "")
            Num_B2K = int(Num_B2K.replace(",", ""))
            try:
                c.execute('INSERT INTO Remeros_1 VALUES (?,?,?,?,?,?,?,?,?)', (DNI, Nsoc, NOM.strip(), APEL.strip(), PES, ALT, SEX,
                                                                               Num_BDAY, Num_B2K))
                conn.commit()


            except :
                print("non valid")

                Not_working.grid(row=7, column=5)










class Zone_page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Tabla de zonas", font=LARGE_FONT)
        label.grid(row=0, column=0, padx=20, pady=5)

        button1 = ttk.Button(self, text='Ir a la pagina de inicio', command=lambda: controller.Show_frame(StartPage))
        button1.grid(row=0, column=1, padx=20, pady=5)

        headings = ( "Nro_d_r", "BPM", "Lactato")
        tree3 = ttk.Treeview(self, height=10, columns=headings, )
        tree3.grid(row=2, column=0, columnspan=1)
        tree3.heading("#0", text="Nombre de la zona", anchor='w')
        tree3.heading("Nro_d_r", text="Numero de remadas", anchor='w')
        tree3.heading("BPM", text="Pulsaciones por minuto", anchor='w')
        tree3.heading("Lactato", text="Lactato (mmol/L)", anchor='w')

        Lista_de_zonas = c.execute("SELECT * FROM Zonas_Log")
        for i in Lista_de_zonas:
            ndr = list(str(i[1]))
            ndr.insert(2, "-")
            ndr = "".join(ndr)

            bpm = list(str(i[2]))
            bpm.insert(2, "-")
            bpm = "".join(bpm)

            tree3.insert('', 0, text=i[0], values=[ndr, bpm, i[3]])


        button2 = ttk.Button(self, text='Agregar zona', command=lambda: controller.Show_frame(Zone_page_Add))
        button2.grid(row=3, column=1, padx=20, pady=5)





class Zone_page_Add(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Agregar zona", font=LARGE_FONT)
        label.grid(row=0, column=0, padx=20, pady=5)

        button1 = ttk.Button(self, text='Ir a la pagina de inicio', command=lambda: controller.Show_frame(StartPage))
        button1.grid(row=0, column=1, padx=20, pady=5)

        Zname_add_lbl = tk.Label(self, text="Nombre de zona", font=LARGE_FONT)
        Zname_add_lbl.grid(row=1, column=0, padx=20, pady=5)

        Zname_add_entry = ttk.Entry(self)
        Zname_add_entry.grid(row=1, column=1, padx=20, pady=5)

        Nro_remadas_add_lbl = ttk.Label(self, text="N° de Remadas", font=LARGE_FONT)
        Nro_remadas_add_lbl.grid(row=2, column=0, padx=20, pady=5)

        Nro_remadas_add_entry = ttk.Entry(self)
        Nro_remadas_add_entry.grid(row=2, column=1, padx=20, pady=5)

        BPM_add_lbl = ttk.Label(self, text="Pulsaciones por minuto", font=LARGE_FONT)
        BPM_add_lbl.grid(row=3, column=0, padx=20, pady=5)

        BPM_add_entry = ttk.Entry(self)
        BPM_add_entry.grid(row=3, column=1, padx=20, pady=5)

        Lactato_add_lbl = ttk.Label(self, text="Lactato (mmol/L)", font=LARGE_FONT)
        Lactato_add_lbl.grid(row=4, column=0, padx=20, pady=5)

        Lactato_add_entry = ttk.Entry(self)
        Lactato_add_entry.grid(row=4, column=1, padx=20, pady=5)

        button1 = ttk.Button(self, text='Insertar datos',
                             command=lambda: submmit_Zone(Zname_add_entry.get(), Nro_remadas_add_entry.get(),
                                                          BPM_add_entry.get(), Lactato_add_entry.get() ))
        button1.grid(row=7, column=1)
        def submmit_Zone(Zname, Nro_d_r, BPM, lactato):

            Not_working = tk.Label(self, text="No funciono")
            Not_working.grid_forget()
            New_BPM = BPM.replace("-","" )
            NewNDR = Nro_d_r.replace("-", "")

            try:

                c.execute('INSERT INTO Zonas_Log VALUES (?,?,?,?)', (Zname, int(NewNDR), int(New_BPM), lactato))

                conn.commit()
            except:
                print("non valid")

                Not_working.grid(row=7, column=0)

app = Dbapp()
app.mainloop()