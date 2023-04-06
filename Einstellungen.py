import Haupt
import chromesteuereinheit
from tkinter import *
import datetime

Uhrzeit_ganz = [
    "00.00",
    "00.30",
    "01.00",
    "01.30",
    "02.00",
    "02.30",
    "03.00",
    "03.30",
    "04.00",
    "04.30",
    "05.00",
    "05.30",
    "06.00",
    "06.30",
    "07.00",
    "07.30",
    "08.00",
    "08.30",
    "09.00",
    "09.30",
    "10.00",
    "10.30",
    "11.00",
    "11.30",
    "12.00",
    "12.30",
    "13.00",
    "13.30",
    "14.00",
    "14.30",
    "15.00",
    "15.30",
    "16.00",
    "16.30",
    "17.00",
    "17.30",
    "18.00",
    "18.30",
    "19.00",
    "19.30",
    "20.00",
    "20.30",
    "21.00",
    "21.30",
    "22.00",
    "22.30",
    "23.00",
    "23.30"
]

def Einstellungen_erstellen():
    Haupt.Einstellungen_Laden()
    global Hintergrund_clicked, Vordergrund_clicked, Einstellungen_Textmanager, Hintergrund_opt, Vordergrund_clicked, \
        Vordergrund_opt, Hintergrundlabel, Textlabel, Buttonfarben, Kinderbutton, Browserbutton, Uhreingabeclicked, Uhreingabe
    try:
        Einstellungen_Textmanager.destroy()
    except:
        pass
    Einstellungen_Textmanager = Toplevel(Haupt.Textmanager)
    Einstellungen_Textmanager.geometry("500x300")
    Einstellungen_Textmanager.title("Einstellungen")
    Einstellungen_Textmanager.config(bg=Haupt.Textmanager_Hintergrund)
    Farben_liste = [
        "black",
        "white",
        "green",
        "yellow",
        "pink"]
    Buttonfarben = Button(Einstellungen_Textmanager, text="Hintergrund", fg=Haupt.Textmanager_Textfarbe, bg=Haupt.Textmanager_Hintergrund, command=Hintergrund)
    Buttonfarben.place(x=5, y=75)
    Hintergrund_clicked = StringVar()
    Hintergrund_clicked.set(Farben_liste[Haupt.Farben_in_Zahl(Haupt.Textmanager_Hintergrund)])
    Hintergrund_opt = OptionMenu(Einstellungen_Textmanager, Hintergrund_clicked, *Farben_liste)
    Hintergrund_opt.config(width=12, font=('Helvetica', 12), fg=Haupt.Textmanager_Textfarbe, bg=Haupt.Textmanager_Hintergrund)
    Hintergrund_opt.place(x=5, y=35)
    Vordergrund_clicked = StringVar()
    Vordergrund_clicked.set(Farben_liste[Haupt.Farben_in_Zahl(Haupt.Textmanager_Textfarbe)])
    Vordergrund_opt = OptionMenu(Einstellungen_Textmanager, Vordergrund_clicked, *Farben_liste)
    Vordergrund_opt.config(width=12, font=('Helvetica', 12), fg=Haupt.Textmanager_Textfarbe, bg=Haupt.Textmanager_Hintergrund, activebackground="green", )
    Vordergrund_opt.place(x=155, y=35)
    Hintergrundlabel = Label(Einstellungen_Textmanager, font=('Helvetica', 12), fg=Haupt.Textmanager_Textfarbe, bg=Haupt.Textmanager_Hintergrund, text="Hintergrund")
    Hintergrundlabel.place(y=5, x=5)
    Textlabel = Label(Einstellungen_Textmanager, font=('Helvetica', 12), fg=Haupt.Textmanager_Textfarbe, bg=Haupt.Textmanager_Hintergrund, text="Textfarbe", bd=0)
    Textlabel.place(x=155, y=5)
    Textfarbe = open("C:\\Users\\" + Haupt.Dateiort + "\\Desktop\\Lieder\\Textfarbe.txt", 'w', encoding='utf8')
    Textfarbe.write(Haupt.Textmanager_Textfarbe)
    Textfarbe.close()
    Hintergrunddatei = open("C:\\Users\\" + Haupt.Dateiort + "\\Desktop\\Lieder\\Hintergrund.txt", 'w', encoding='utf8')
    Hintergrunddatei.write(Haupt.Textmanager_Hintergrund)
    Hintergrunddatei.close()
    if Haupt.Kinder_anzeigen == "Falsch":
        Kinderbutton = Button(Einstellungen_Textmanager, font=('Helvetica', 12), fg="Black", bg="red", text="Kein Kinderlied", command=Kinder_Anzeigen)
    else:
        Kinderbutton = Button(Einstellungen_Textmanager, font=('Helvetica', 12), fg="Black", bg="green", text="Kinderlied", command=Kinder_Nicht_Anzeigen)
    Kinderbutton.place(x=5, y=110)
    if Haupt.Browseröffnen == "Wahr":
        Browserbutton = Button(Einstellungen_Textmanager, font=('Helvetica', 12), fg="Black", bg="green", text="Browser offen", command=Browsergeschlossen)
    else:
        Browserbutton = Button(Einstellungen_Textmanager, font=('Helvetica', 12), fg="Black", bg="red", text="Kein Browser", command=Browseroffen)
    Browserbutton.place(x=5,y=150)
    Uhreingabeclicked = StringVar()
    Zeit()
    Uhreingabeclicked.set(Uhrzeit[3])
    Uhreingabe = OptionMenu(Einstellungen_Textmanager, Uhreingabeclicked, *Uhrzeit)
    Uhreingabe.config(font=("Helvetica", 12), bg=Haupt.Textmanager_Hintergrund, fg=Haupt.Textmanager_Textfarbe)
    Uhreingabe.place(x=5,y=190)
    Uhrzeit_speichern = Button(Einstellungen_Textmanager, font=('Helvetica', 12), fg=Haupt.Textmanager_Textfarbe, bg=Haupt.Textmanager_Hintergrund, bd=0, text="Uhrzeit bestätigeb", command=Uhrzeit_speicherndef)
    Uhrzeit_speichern.place(x=5, y=230)
    Uhrzeit_erweitern = Button(Einstellungen_Textmanager, font=('Helvetica', 12), fg=Haupt.Textmanager_Textfarbe, bg=Haupt.Textmanager_Hintergrund, bd=0, text="Erweitern", command=Erweiterndef)
    Uhrzeit_erweitern.place(x=5,y=268)

def Zeit():
    global Uhrzeit
    if 0.00 <= float(datetime.datetime.now().strftime("%H.%M")) <= 0.30:
        Uhrzeit = [
            "23.00",
            "23.30",
            "00.00",
            "00.30",
            "01.00",
            "01.30",
            "02.00",
            "02.30"
        ]
    if 0.30 <= float(datetime.datetime.now().strftime("%H.%M")) <= 1.00:
        Uhrzeit = [
            "23.30",
            "00.00",
            "00.30",
            "01.00",
            "01.30",
            "02.00",
            "02.30",
            "03.00"
        ]
    if 1.00 <= float(datetime.datetime.now().strftime("%H.%M")) <= 1.30:
        Uhrzeit = [
            "00.00",
            "00.30",
            "01.00",
            "01.30",
            "02.00",
            "02.30",
            "03.00",
            "03.30"
        ]
    if 1.30 <= float(datetime.datetime.now().strftime("%H.%M")) <= 2.00:
        Uhrzeit = [
            "00.30",
            "01.00",
            "10.30",
            "02.00",
            "02.30",
            "03.00",
            "03.30",
            "04.00"
        ]
    if 2.00 <= float(datetime.datetime.now().strftime("%H.%M")) <= 2.30:
        Uhrzeit = [
            "01.00",
            "01.30",
            "02.00",
            "02.30",
            "03.00",
            "03.30",
            "04.00",
            "04.30"
        ]
    if 2.30 <= float(datetime.datetime.now().strftime("%H.%M")) <= 3.00:
        Uhrzeit = [
            "01.30",
            "02.00",
            "02.30",
            "03.00",
            "03.30",
            "04.00",
            "04.30",
            "05.00"
        ]
    if 3.00 <= float(datetime.datetime.now().strftime("%H.%M")) <= 3.30:
        Uhrzeit = [
            "02.00",
            "02.30",
            "03.00",
            "03.30",
            "04.00",
            "04.30",
            "05.00",
            "05.30"
        ]
    if 3.30 <= float(datetime.datetime.now().strftime("%H.%M")) <= 4.00:
        Uhrzeit = [
            "02.30",
            "03.00",
            "03.30",
            "04.00",
            "04.30",
            "05.00",
            "05.30",
            "06.00"
        ]
    if 4.00 <= float(datetime.datetime.now().strftime("%H.%M")) <= 4.30:
        Uhrzeit = [
            "03.00",
            "03.30",
            "04.00",
            "04.30",
            "05.00",
            "05.30",
            "06.00",
            "06.30"
        ]
    if 4.30 <= float(datetime.datetime.now().strftime("%H.%M")) <= 5.00:
        Uhrzeit = [
            "03.30",
            "04.00",
            "04.30",
            "05.00",
            "05.30",
            "06.00",
            "06.30",
            "07.00"
        ]
    if 5.00 <= float(datetime.datetime.now().strftime("%H.%M")) <= 5.30:
        Uhrzeit = [
            "04.00",
            "04.30",
            "05.00",
            "05.30",
            "06.00",
            "06.30",
            "07.00",
            "07.30"
        ]
    if 5.30 <= float(datetime.datetime.now().strftime("%H.%M")) <= 6.00:
        Uhrzeit = [
            "04.30",
            "05.00",
            "05.30",
            "06.00",
            "06.30",
            "07.00",
            "07.30",
            "08.00"
        ]
    if 6.00 <= float(datetime.datetime.now().strftime("%H.%M")) <= 6.30:
        Uhrzeit = [
            "05.00",
            "05.30",
            "06.00",
            "06.30",
            "07.00",
            "07.30",
            "08.00",
            "08.30"
        ]
    if 6.30 <= float(datetime.datetime.now().strftime("%H.%M")) <= 7.00:
        Uhrzeit = [
            "05.30",
            "06.00",
            "06.30",
            "07.00",
            "07.30",
            "08.00",
            "08.30",
            "09.00"
        ]
    if 7.00 <= float(datetime.datetime.now().strftime("%H.%M")) <= 7.30:
        Uhrzeit = [
            "06.00",
            "06.30",
            "07.00",
            "07.30",
            "08.00",
            "08.30",
            "09.00",
            "09.30"
        ]
    if 7.30 <= float(datetime.datetime.now().strftime("%H.%M")) <= 8.00:
        Uhrzeit = [
            "06.30",
            "07.00",
            "07.30",
            "08.00",
            "08.30",
            "09.00",
            "09.30",
            "10.00"
        ]
    if 8.00 <= float(datetime.datetime.now().strftime("%H.%M")) <= 8.30:
        Uhrzeit = [
            "07.00",
            "07.30",
            "08.00",
            "08.30",
            "09.00",
            "09.30",
            "10.00",
            "10.30"
        ]
    if 8.30 <= float(datetime.datetime.now().strftime("%H.%M")) <= 9.00:
        Uhrzeit = [
            "07.30",
            "08.00",
            "08.30",
            "09.00",
            "09.30",
            "10.00",
            "10.30",
            "11.00"
        ]
    if 9.00 <= float(datetime.datetime.now().strftime("%H.%M")) <= 9.30:
        Uhrzeit = [
            "08.00",
            "08.30",
            "09.00",
            "09.30",
            "10.00",
            "10.30",
            "11.00",
            "11.30"
        ]
    if 9.30 <= float(datetime.datetime.now().strftime("%H.%M")) <= 10.00:
        Uhrzeit = [
            "08.30",
            "09.00",
            "09.30",
            "10.00",
            "10.30",
            "11.00",
            "11.30",
            "12.00"
        ]
    if 10.00 <= float(datetime.datetime.now().strftime("%H.%M")) <= 10.30:
        Uhrzeit = [
            "09.00",
            "09.30",
            "10.00",
            "10.30",
            "11.00",
            "11.30",
            "12.00",
            "12.30"
        ]
    if 10.30 <= float(datetime.datetime.now().strftime("%H.%M")) <= 11.00:
        Uhrzeit = [
            "09.30",
            "10.00",
            "10.30",
            "11.00",
            "11.30",
            "12.00",
            "12.30",
            "13.00"
        ]
    if 11.00 <= float(datetime.datetime.now().strftime("%H.%M")) <= 11.30:
        Uhrzeit = [
            "10.00",
            "10.30",
            "11.00",
            "11.30",
            "12.00",
            "12.30",
            "13.00",
            "13.30"
        ]
    if 11.30 <= float(datetime.datetime.now().strftime("%H.%M")) <= 12.00:
        Uhrzeit = [
            "10.30",
            "11.00",
            "11.30",
            "12.00",
            "12.30",
            "13.00",
            "13.30",
            "14.00"
        ]
    if 12.00 <= float(datetime.datetime.now().strftime("%H.%M")) <= 12.30:
        Uhrzeit = [
            "11.00",
            "11.30",
            "12.00",
            "12.30",
            "13.00",
            "13.30",
            "14.00",
            "14.30"
        ]
    if 12.30 <= float(datetime.datetime.now().strftime("%H.%M")) <= 13.00:
        Uhrzeit = [
            "11.30",
            "12.00",
            "12.30",
            "13.00",
            "13.30",
            "14.00",
            "14.30",
            "15.00"
        ]
    if 13.00 <= float(datetime.datetime.now().strftime("%H.%M")) <= 13.30:
        Uhrzeit = [
            "12.00",
            "12.30",
            "13.00",
            "13.30",
            "14.00",
            "14.30",
            "15.00",
            "15.30"
        ]
    if 13.30 <= float(datetime.datetime.now().strftime("%H.%M")) <= 14.00:
        Uhrzeit = [
            "12.30",
            "13.00",
            "13.30",
            "14.00",
            "14.30",
            "15.00",
            "15.30",
            "16.00"
        ]
    if 14.00 <= float(datetime.datetime.now().strftime("%H.%M")) <= 14.30:
        Uhrzeit = [
            "13.00",
            "13.30",
            "14.00",
            "14.30",
            "15.00",
            "15.30",
            "16.00",
            "16.30"
        ]
    if 14.30 <= float(datetime.datetime.now().strftime("%H.%M")) <= 15.00:
        Uhrzeit = [
            "13.30",
            "14.00",
            "14.30",
            "15.00",
            "15.30",
            "16.00",
            "16.30",
            "17.00"
        ]
    if 15.00 <= float(datetime.datetime.now().strftime("%H.%M")) <= 15.30:
        Uhrzeit = [
            "14.00",
            "14.30",
            "15.00",
            "15.30",
            "16.00",
            "16.30",
            "17.00",
            "17.30"
        ]
    if 15.30 <= float(datetime.datetime.now().strftime("%H.%M")) <= 16.00:
        Uhrzeit = [
            "14.30",
            "15.00",
            "15.30",
            "16.00",
            "16.30",
            "17.00",
            "17.30",
            "18.00"
        ]
    if 16.00 <= float(datetime.datetime.now().strftime("%H.%M")) <= 16.30:
        Uhrzeit = [
            "15.00",
            "15.30",
            "16.00",
            "16.30",
            "17.00",
            "17.30",
            "18.00",
            "18.30"
        ]
    if 16.30 <= float(datetime.datetime.now().strftime("%H.%M")) <= 17.00:
        Uhrzeit = [
            "15.30",
            "16.00",
            "16.30",
            "17.00",
            "17.30",
            "18.00",
            "18.30",
            "19.00"
        ]
    if 17.00 <= float(datetime.datetime.now().strftime("%H.%M")) <= 17.30:
        Uhrzeit = [
            "16.00",
            "16.30",
            "17.00",
            "17.30",
            "18.00",
            "18.30",
            "19.00",
            "19.30"
        ]
    if 17.30 <= float(datetime.datetime.now().strftime("%H.%M")) <= 18.00:
        Uhrzeit = [
            "16.30",
            "17.00",
            "17.30",
            "18.00",
            "18.30",
            "19.00",
            "19.30",
            "20.00"
        ]
    if 18.00 <= float(datetime.datetime.now().strftime("%H.%M")) <= 18.30:
        Uhrzeit = [
            "17.00",
            "17.30",
            "18.00",
            "18.30",
            "19.00",
            "19.30",
            "20.00",
            "20.30"
        ]
    if 18.30 <= float(datetime.datetime.now().strftime("%H.%M")) <= 19.00:
        Uhrzeit = [
            "17.30",
            "18.00",
            "18.30",
            "19.00",
            "19.30",
            "20.00",
            "20.30",
            "21.00"
        ]
    if 19.00 <= float(datetime.datetime.now().strftime("%H.%M")) <= 19.30:
        Uhrzeit = [
            "18.00",
            "18.30",
            "19.00",
            "19.30",
            "20.00",
            "20.30",
            "21.00",
            "21.30"
        ]
    if 19.30 <= float(datetime.datetime.now().strftime("%H.%M")) <= 20.00:
        Uhrzeit = [
            "18.30",
            "19.00",
            "19.30",
            "20.00",
            "20.30",
            "21.00",
            "21.30",
            "22.00"
        ]
    if 20.00 <= float(datetime.datetime.now().strftime("%H.%M")) <= 20.30:
        Uhrzeit = [
            "19.00",
            "19.30",
            "20.00",
            "20.30",
            "21.00",
            "21.30",
            "22.00",
            "22.30"
        ]
    if 20.30 <= float(datetime.datetime.now().strftime("%H.%M")) <= 21.00:
        Uhrzeit = [
            "19.30",
            "20.00",
            "20.30",
            "21.00",
            "21.30",
            "22.00",
            "22.30",
            "23.00",
        ]
    if 21.00 <= float(datetime.datetime.now().strftime("%H.%M")) <= 21.30:
        Uhrzeit = [
            "20.00",
            "20.30",
            "21.00",
            "21.30",
            "22.00",
            "22.30",
            "23.00",
            "23.30"
        ]
    if 21.30 <= float(datetime.datetime.now().strftime("%H.%M")) <= 22.00:
        Uhrzeit = [
            "20.30",
            "21.00",
            "21.30",
            "22.00",
            "22.30",
            "23.00",
            "23.30",
            "00.00"
        ]
    if 22.00 <= float(datetime.datetime.now().strftime("%H.%M")) <= 22.30:
        Uhrzeit = [
            "21.00",
            "21.30",
            "22.00",
            "22.30",
            "23.00",
            "23.30",
            "00.00",
            "00.30"
        ]
    if 22.30 <= float(datetime.datetime.now().strftime("%H.%M")) <= 23.00:
        Uhrzeit = [
            "21.30",
            "22.00",
            "22.30",
            "23.00",
            "23.30",
            "00.00",
            "00.30",
            "01.00"
        ]
    if 23.00 <= float(datetime.datetime.now().strftime("%H.%M")) <= 23.30:
        Uhrzeit = [
            "22.00",
            "22.30",
            "23.00",
            "23.30",
            "00.00",
            "00.30",
            "01.00",
            "01.30"
        ]
    if 23.30 <= float(datetime.datetime.now().strftime("%H.%M")) <= 24.00:
        Uhrzeit = [
            "22.30",
            "23.00",
            "23.30",
            "00.00",
            "00.30",
            "01.00",
            "01.30",
            "02.00"
        ]

def Erweiterndef():
    global Uhreingabeclicked1, Uhreingabe1
    Uhreingabe.destroy()
    Uhreingabeclicked1 = StringVar()
    Uhreingabeclicked1.set(Uhrzeit_ganz[0])
    Uhreingabe1 = OptionMenu(Einstellungen_Textmanager, Uhreingabeclicked1, *Uhrzeit_ganz)
    Uhreingabe1.config(font=("Helvetica", 12), bg=Haupt.Textmanager_Hintergrund, fg=Haupt.Textmanager_Textfarbe)
    Uhreingabe1.place(x=5,y=190)




def Uhrzeit_speicherndef():
    try:
        Uhreingabe1.config(fg=Haupt.Textmanager_Textfarbe, bg=Haupt.Textmanager_Hintergrund)
        Uhrzeit = Uhreingabeclicked1.get()
        print("1")
    except:
        Uhreingabe.config(fg=Haupt.Textmanager_Textfarbe, bg=Haupt.Textmanager_Hintergrund)
        Uhrzeit = Uhreingabeclicked.get()
        print("2")
    print(Uhrzeit)
    Zeit_laden = open("C:\\Users\\" + Haupt.Dateiort + "\\Desktop\\Lieder\\Zeit.txt", 'w', encoding='utf8')
    Zeit_laden2 = open("C:\\Users\\" + Haupt.Dateiort + "\\Desktop\\Lieder\\Zeit2.txt", 'w', encoding='utf8')
    Uhrzeit1 = Uhrzeit.split(".")
    if int(Uhrzeit1[1]) > 10:
        Zeit_laden.write(str(round(float(Uhreingabeclicked.get())-0.1, 2)))
        Zeit_laden2.write(str(round(float(Uhreingabeclicked.get())-0.05, 2)))
        Zeit_laden.close()
        Zeit_laden2.close()
        Haupt.Zeit = float(Uhrzeit)-0.1
        Haupt.Zeit2 = float(Uhrzeit) -0.05
    else:
        Zeit_laden.write(str(round(float(Uhreingabeclicked.get())-0.5,2)))
        Zeit_laden2.write(str(round(float(Uhreingabeclicked.get())-0.45,2)))
        Zeit_laden.close()
        Zeit_laden2.close()
        Haupt.Zeit = float(Uhrzeit)-0.8
        Haupt.Zeit2 = float(Uhrzeit) -0.75

def Hintergrund():
    global Textmanager_Hintergrund, Textmanager_Textfarbe
    Haupt.Textmanager.config(bg=Hintergrund_clicked.get())
    Haupt.Einganslied.Hintergrund(Hintergrund_clicked.get(), Vordergrund_clicked.get())
    Haupt.Textwortlied.Hintergrund(Hintergrund_clicked.get(), Vordergrund_clicked.get())
    Haupt.Amtswechsellied.Hintergrund(Hintergrund_clicked.get(), Vordergrund_clicked.get())
    Haupt.Kinderlied.Hintergrund(Hintergrund_clicked.get(), Vordergrund_clicked.get())
    Haupt.Bussslied.Hintergrund(Hintergrund_clicked.get(), Vordergrund_clicked.get())
    Haupt.Abendmahlslied.Hintergrund(Hintergrund_clicked.get(), Vordergrund_clicked.get())
    Haupt.Schlusslied.Hintergrund(Hintergrund_clicked.get(), Vordergrund_clicked.get())
    Haupt.Zusatzlied1.Hintergrund(Hintergrund_clicked.get(), Vordergrund_clicked.get())
    Haupt.Zusatzlied2.Hintergrund(Hintergrund_clicked.get(), Vordergrund_clicked.get())
    Haupt.Zusatzlied3.Hintergrund(Hintergrund_clicked.get(), Vordergrund_clicked.get())
    Haupt.Zusatzlied4.Hintergrund(Hintergrund_clicked.get(), Vordergrund_clicked.get())
    Einstellungen_Textmanager.config(bg=Hintergrund_clicked.get())
    Hintergrund_opt.config(bg=Hintergrund_clicked.get(), fg=Vordergrund_clicked.get())
    Hintergrundlabel.config(bg=Hintergrund_clicked.get(), fg=Vordergrund_clicked.get())
    Vordergrund_opt.config(bg=Hintergrund_clicked.get(), fg=Vordergrund_clicked.get())
    Textlabel.config(bg=Hintergrund_clicked.get(), fg=Vordergrund_clicked.get())
    Haupt.Textwortentry.config(bg=Hintergrund_clicked.get(), fg=Vordergrund_clicked.get())
    Haupt.Textwortlabel.config(bg=Hintergrund_clicked.get(), fg=Vordergrund_clicked.get())
    Hintergrund = open("C:\\Users\\" + Haupt.Dateiort + "\\Desktop\\Lieder\\Hintergrund.txt", 'w', encoding='utf8')
    Hintergrund.write(Hintergrund_clicked.get())
    Hintergrund.close()
    Textfarbe = open("C:\\Users\\" + Haupt.Dateiort + "\\Desktop\\Lieder\\Textfarbe.txt", 'w', encoding='utf8')
    Textfarbe.write(Vordergrund_clicked.get())
    Textfarbe.close()
    Buttonfarben.config(bg=Hintergrund_clicked.get(), fg=Vordergrund_clicked.get())
    Haupt.zusaetzliches_lied.config(bg=Hintergrund_clicked.get(), fg=Vordergrund_clicked.get())
    Textmanager_Textfarbe = Vordergrund_clicked.get()
    Textmanager_Hintergrund = Hintergrund_clicked.get()




def Browseroffen():
    Browseröffnen = open("C:\\Users\\" + Haupt.Dateiort + "\\Desktop\\Lieder\\Chrome.txt", 'w', encoding='utf8')
    Browseröffnen.write("Wahr")
    Browseröffnen.close()
    Browserbutton.config(bg="green", text="Browser offen", command=Browsergeschlossen)
    chromesteuereinheit.Chromestarten_Thread()

def Browsergeschlossen():
    Browseröffnen = open("C:\\Users\\" + Haupt.Dateiort + "\\Desktop\\Lieder\\Chrome.txt", 'w', encoding='utf8')
    Browseröffnen.write("Falsch")
    Browseröffnen.close()
    Browserbutton.config(bg="red", text="Kein Browser", command=Browseroffen)

def Kinder_Anzeigen():
    global Kinder_Anzeigen_Grafig, Kinder_Position, Kinderlied
    Kinderbutton.config(bg="green", text="Kinderlied", command=Kinder_Nicht_Anzeigen)
    Haupt.Kinder_Anzeigen_Grafig = "False"
    Haupt.Kinder_Position = 1
    Kinderladen = open("C:\\Users\\" + Haupt.Dateiort + "\\Desktop\\Lieder\\Kindereinstellung.txt", 'w', encoding='utf8')
    Kinderladen.write("Wahr")
    Kinderladen.close()
    Haupt.Kinderlied = Haupt.Grafigfuer_ein_Lied(166+41 +83*Haupt.Kinder_Position, "Kinderlied", "True", Haupt.Textmanager_Hintergrund, Haupt.Textmanager_Textfarbe,4,1)
    if Haupt.Kindeladen == True:
        Haupt.Kinderlied.Eingabe_wiederherstellen("Kinderlied", Haupt.Textmanager_Hintergrund, Haupt.Textmanager_Textfarbe,4,1, 166+41 +83*Haupt.Kinder_Position)
    Haupt.Aktualiesierung_Grafick()


def Kinder_Nicht_Anzeigen():
    global Kinder_Anzeigen_Grafig, Kinder_Position
    Kinderbutton.config(bg="red", text="Kein Kinderlied", command=Kinder_Anzeigen)
    Haupt.Kinder_Anzeigen_Grafig = "True"
    Haupt.Kinder_Position = 0
    Kinderladen = open("C:\\Users\\" + Haupt.Dateiort + "\\Desktop\\Lieder\\Kindereinstellung.txt", 'w', encoding='utf8')
    Kinderladen.write("Falsch")
    Kinderladen.close()
    Haupt.Kinderlied.Zerstören()
    Haupt.Aktualiesierung_Grafick()