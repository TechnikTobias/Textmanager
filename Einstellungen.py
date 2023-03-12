import Haupt
import chromesteuereinheit
from tkinter import *

def Einstellungen_erstellen():
    Haupt.Einstellungen_Laden()
    global Hintergrund_clicked, Vordergrund_clicked, Einstellungen_Textmanager, Hintergrund_opt, Vordergrund_clicked, \
        Vordergrund_opt, Hintergrundlabel, Textlabel, Buttonfarben, Kinder_Anzeigen_Grafig, Kinder_Position, Kinderbutton, Browserbutton
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
    Buttonfarben.place(x=1, y=75)
    Hintergrund_clicked = StringVar()
    Hintergrund_clicked.set(Farben_liste[Haupt.Farben_in_Zahl(Haupt.Textmanager_Hintergrund)])
    OptionMenu(Einstellungen_Textmanager, Hintergrund_clicked, *Farben_liste)
    Hintergrund_opt = OptionMenu(Einstellungen_Textmanager, Hintergrund_clicked, *Farben_liste)
    Hintergrund_opt.config(width=12, font=('Helvetica', 12), fg=Haupt.Textmanager_Textfarbe, bg=Haupt.Textmanager_Hintergrund)
    Hintergrund_opt.place(x=1, y=35)
    Vordergrund_clicked = StringVar()
    Vordergrund_clicked.set(Farben_liste[Haupt.Farben_in_Zahl(Haupt.Textmanager_Textfarbe)])
    OptionMenu(Einstellungen_Textmanager, Vordergrund_clicked, *Farben_liste)
    Vordergrund_opt = OptionMenu(Einstellungen_Textmanager, Vordergrund_clicked, *Farben_liste)
    Vordergrund_opt.config(width=12, font=('Helvetica', 12), fg=Haupt.Textmanager_Textfarbe, bg=Haupt.Textmanager_Hintergrund, activebackground="green", )
    Vordergrund_opt.place(x=150, y=35)
    Hintergrundlabel = Label(Einstellungen_Textmanager, font=('Helvetica', 12), fg=Haupt.Textmanager_Textfarbe, bg=Haupt.Textmanager_Hintergrund, text="Hintergrund")
    Hintergrundlabel.place(y=5, x=1)
    Textlabel = Label(Einstellungen_Textmanager, font=('Helvetica', 12), fg=Haupt.Textmanager_Textfarbe, bg=Haupt.Textmanager_Hintergrund, text="Textfarbe", bd=0)
    Textlabel.place(x=150, y=5)
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
    Kinderbutton.place(x=0, y=110)
    if Haupt.Browseröffnen == "Wahr":
        Browserbutton = Button(Einstellungen_Textmanager, font=('Helvetica', 12), fg="Black", bg="green", text="Browser offen", command=Browsergeschlossen)
    else:
        Browserbutton = Button(Einstellungen_Textmanager, font=('Helvetica', 12), fg="Black", bg="red", text="Kein Browser", command=Browseroffen)
    Browserbutton.place(y=150)

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
    Kinder_Anzeigen_Grafig = "False"
    Kinder_Position = 1
    Kinderladen = open("C:\\Users\\" + Haupt.Dateiort + "\\Desktop\\Lieder\\Kindereinstellung.txt", 'w', encoding='utf8')
    Kinderladen.write("Wahr")
    Kinderladen.close()
    Kinderlied = Haupt.Grafigfuer_ein_Lied(166+41 +83*Kinder_Position, "Kinderlied", "True", Textmanager_Hintergrund, Textmanager_Textfarbe,4,1)
    if Haupt.Kindeladen == True:
        Kinderlied.Eingabe_wiederherstellen("Kinderlied")
    Haupt.Aktualiesierung_Grafick()


def Kinder_Nicht_Anzeigen():
    global Kinder_Anzeigen_Grafig, Kinder_Position
    Kinderbutton.config(bg="red", text="Kein Kinderlied", command=Kinder_Anzeigen)
    Kinder_Anzeigen_Grafig = "True"
    Kinder_Position = 0
    Kinderladen = open("C:\\Users\\" + Haupt.Dateiort + "\\Desktop\\Lieder\\Kindereinstellung.txt", 'w', encoding='utf8')
    Kinderladen.write("Falsch")
    Kinderladen.close()
    Kinderlied.Zerstören()
    Haupt.Aktualiesierung_Grafick()