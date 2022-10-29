from ast import Str
import datetime
import os
import subprocess
from re import T
import sys
from threading import Thread
import threading
import time
from tkinter import *
from turtle import goto
import chromesteuereinheit
import Textanzeiger
import keyboard
Zeit = 9.20
Zeit1 = 19.50
Zeit2 = 9.25
Zeit3 = 19.55
Hintregrundaktualisierenvariable = False
Dateiort = os.getlogin()
Textmanager = Tk()
Textmanager.title("Textmanager")
Textmanager.geometry("1040x800")
Textmanager.minsize(width=1040, height=850)
Textmanager.iconbitmap("C:\\Users\\" + Dateiort + "\\Desktop\\Lieder\\picture_compress 1.ico")
AnzeigeText = Toplevel(Textmanager)
AnzeigeText.config(bg="black")
AnzeigeText.geometry("1920x1080+1920+0")
AnzeigeText.overrideredirect(True)
Text_Anzeige_Label = Label(AnzeigeText, font=("Helvetica", 60), fg="white", bg="black", wraplength=1920)
Aktueller_Text = ""
Text_Anzeige_Label.config(text=Aktueller_Text)
Text_Anzeige_Label["justify"] = "left"
Text_Anzeige_Label.place(x=0, y=0)
Wie_viele_zusatzlieder = 0
Zusatzlied1_obwahr = "False"
Zusatzlied2_obwahr = "False"
Zusatzlied3_obwahr = "False"
Zusatzlied4_obwahr = "False"
Hintregrundaktualisieren = True
Buttonebestätigengedrückt = False
Testeneingeben = True
Textwortwiederherstellen = False
Textworteingabeübergabe = False
Textwortübergabe = None
Buchclickedladen = None
Verseingabeladen = None
Liedeingabeladen = None
Textwortübergabedaten = [2, False, "Textwort", 1, ""]
Liedpositionübergabe = 0
Buch_Listen = [
    "Gesangbuch",
    "Chorbuch",
    "Jugendliederbuch",
    "Kinderliederbuch",
    "Band 1 Singt dem Herrn",
    "Band 2 Singt dem Herrn",
    "Band 3 Singt dem Herrn",
    "Argentinisches Chorbuch",
    "Spanisches Chorbuch",
    "Sonderheft"]





class Grafigfuer_ein_Lied:
    # erstellt Grafik(Eingabe und Ausgabe des Liedes) für ein Lied
    global Liedpositionübergabe
    opt = None
    Lied = None
    Verse = None
    Liednummer = None
    Liedverse = None
    Liedtextanzeige = None
    Buch = "GB"
    Dateiliedtext1 = None
    Dateiliedtext = None
    aktualisieren_wahl = "False"
    Buchzahl_clicked = None
    Liednummerfest = None
    Liedversefest = None
    gespeichertestlied = None
    gespeichertestvers = None
    gespeichertestBuch = None
    Daten_fürTextanderwand = [0]


    def __init__(self, Position, Liedname, Wahl, Hintergrund, Vordergrund):
        global Liedpositionübergabe
        if Wahl == "True":
            self.clicked = StringVar()
            self.clicked.set(Buch_Listen[0])
            OptionMenu(Textmanager, self.clicked, *Buch_Listen)
            self.opt = OptionMenu(Textmanager, self.clicked, *Buch_Listen)
            self.opt.config(width=12, font=('Helvetica', 12), bg=Hintergrund, fg=Vordergrund)
            self.Lied = Label(Textmanager, font=("Helvetica", 15), pady=5, text=Liedname, bg=Hintergrund, fg=Vordergrund)
            self.Verse = Label(Textmanager, font=("Helvetica", 15), text="Verse", bg=Hintergrund, fg=Vordergrund)
            self.Liednummer = Entry(Textmanager, font=("Helvetica", 24), width=10)
            self.Liedverse = Entry(Textmanager, font=("Helvetica", 24), width=10)
            self.Liedtextanzeige = Button(Textmanager, font=12, pady=5, bg=Hintergrund, border=0, fg=Vordergrund)
            self.Liedtextanzeige["justify"] = "left"
            self.opt.place(x=340, y=25 + Position)
            self.Liedtextanzeige.place(x=495, y=15 + Position)
            self.Lied.place(x=0, y=0 + Position)
            self.Verse.place(y=40 + Position)
            self.Liednummer.place(x=150, y=0 + Position)
            self.Liedverse.place(x=150, y=40 + Position)
            self.aktualisieren_wahl = "True"
            Liedpositionübergabe = Liedpositionübergabe + 1
        else:
            self.opt = None
            self.Lied = None
            self.Verse = None
            self.Liednummer = None
            self.Liedverse = None
            self.Liedtextanzeige = None
            self.Dateiliedtext1 = None
            self.Dateiliedtext = None
            self.aktualisieren_wahl = "False"
            self.Buchzahl_clicked = None
            self.Daten_fürTextanderwand = [0]
        Textmanager.update()

    # Lädt den Namen des Liedes für den Livestream und Livestream vorschau
    def Datein_lesen(self):
        try:
            self.Dateiliedtext1 = open("C:\\Users\\" + Dateiort + "\\Desktop\\Lieder\\Einbledungen\\" + str(self.clicked.get()) + "\\l" + str(self.Liednummer.get()) + ".txt", 'r', encoding='utf8')
            self.Dateiliedtext = self.Dateiliedtext1.read()
        except FileNotFoundError:
            Errorbild = Toplevel(Textmanager)
            Errorbild.geometry("560x350+500+400")
            Errorbild.config(bg="black")
            Error = Label(Errorbild, font=("Helvetica", 40), text="Error", bg="black", fg="green", wraplength=560)
            Error.place(x=210, y=0)
            ErrorLabel = Label(Errorbild, font=("Helvetica", 20), text="Dieses Liednummer ist zu Groß oder ist noch nicht im System", bg="black", fg="green", wraplength=560)
            ErrorLabel.place(x=0, y=80)
            if len(self.Liednummer.get()) > 3:
                Hi = self.Liednummer.get()
                Hi2 = Hi[:-1]
                self.Liednummer.delete(0, "end")
                self.Liednummer.insert(0, Hi2)

    def Zerstören(self):
        global Liedpositionübergabe
        self.opt.destroy()
        self.Lied.destroy()
        self.Verse.destroy()
        self.Liednummer.destroy()
        self.Liedverse.destroy()
        self.Liedtextanzeige.destroy()
        self.opt = None
        self.Lied = None
        self.Verse = None
        self.Liednummer = None
        self.Liedverse = None
        self.Liedtextanzeige = None
        self.Buch = None
        self.Dateiliedtext1 = None
        self.Dateiliedtext = None
        self.aktualisieren_wahl = "False"
        self.Buchzahl_clicked = None
        Liedpositionübergabe = Liedpositionübergabe - 1
        Textmanager.update()


    # Erstellt die Buchabkürzung für den Livestream und NBuchzahl für das Wiederherstellen
    def Buchabkuerzen(self):
        if self.clicked.get() == "Gesangbuch":
            self.Buch = "GB"
            self.Buchzahl_clicked = 0
        elif self.clicked.get() == "Chorbuch":
            self.Buch = "CB"
            self.Buchzahl_clicked = 1
        elif self.clicked.get() == "Jugendliederbuch":
            self.Buch = "JLB"
            self.Buchzahl_clicked = 2
        elif self.clicked.get() == "Argentinisches Chorbuch":
            self.Buch = "AC"
            self.Buchzahl_clicked = 7
        elif self.clicked.get() == "Kinderliederbuch":
            self.Buch = "KLB"
            self.Buchzahl_clicked = 3
        elif self.clicked.get() == "Sonderheft":
            self.Buch = "SH"
            self.Buchzahl_clicked = 9
        elif self.clicked.get() == "Spanisches Chorbuch":
            self.Buch = "SpC"
            self.Buchzahl_clicked = 8
        elif self.clicked.get() == "Band 1 Singt dem Herrn":
            self.Buch = "SdH Band 1"
            self.Buchzahl_clicked = 4
        elif self.clicked.get() == "Band 2 Singt dem Herrn":
            self.Buch = "SdH Band 2"
            self.Buchzahl_clicked = 5
        elif self.clicked.get() == "Band 3 Singt dem Herrn":
            self.Buch = "SdH Band 3"
            self.Buchzahl_clicked = 6

    # Zeig im programm, welches Lied ausgewählt ist.
    def Livestream_Vorchau(self):
        if len(self.Liedverse.get()) >= 1:
            self.Liedtextanzeige.config(text=str(self.Buch + " " + self.Liednummer.get() + " Vers " + str(self.Liedverse.get()) + "\n" + self.Dateiliedtext))
        else:
            self.Liedtextanzeige.config(text=str(self.Buch + " " + self.Liednummer.get()+"\n" + self.Dateiliedtext))


    def Datein_lesen_spontan(self):
        try:
            self.Dateiliedtext1 = open("C:\\Users\\" + Dateiort + "\\Desktop\\Lieder\\Einbledungen\\" + str(Textanzeiger.clicked.get()) + "\\l" + str(Textanzeiger.Texteingabe.get()) + ".txt", 'r', encoding='utf8')
            self.Dateiliedtext = self.Dateiliedtext1.read()
        except:
            pass


    def Livestream_Vorchau_spontan(self):
        if len(Textanzeiger.Verseingabe.get()) >= 1:
            self.Liedtextanzeige.config(text=str(self.Buch + " " + Textanzeiger.Texteingabe.get() + " Vers " + str(Textanzeiger.Verseingabe.get()) + "\n" + self.Dateiliedtext))
        else:
            self.Liedtextanzeige.config(text=str(self.Buch + " " + Textanzeiger.Texteingabe.get()+"\n" + self.Dateiliedtext))

    def Spontaneingabe_Hintergrund_aktualisierung(self, Welcheslied):
        global Hintregrundaktualisierenvariable
        if Welcheslied:
            Verseüber = Textanzeiger.Verseingabe.get()
            if Textanzeiger.Versüperprüfen(Textanzeiger.clicked.get() ,Textanzeiger.Texteingabe.get(), Verseüber,Verseüber) == True:
                Hi = Textanzeiger.Verseingabe.get()
                Hi2 = Hi[:-1]
                Textanzeiger.Verseingabe.delete(0, "end")
                Textanzeiger.Verseingabe.insert(0, Hi2)
            else:
                Textanzeiger.Verseingabe.delete(0, "end")
                Textanzeiger.Verseingabe.insert(END, Textanzeiger.Versüperprüfen(Textanzeiger.clicked.get() ,Textanzeiger.Texteingabe.get(), Verseüber,Verseüber))
            Grafigfuer_ein_Lied.Buchabkuerzen(self)
            Grafigfuer_ein_Lied.Datein_lesen_spontan(self)
            Grafigfuer_ein_Lied.Livestream_Vorchau_spontan(self)


    # sorgt dafür, dass alles aktualisiert wird
    def Hintergrund_aktualisierung(self, Liedname):
        global Hintregrundaktualisierenvariable
        if self.aktualisieren_wahl == "True":
            if not self.gespeichertestlied == self.Liednummer.get() or not self.gespeichertestvers == self.Liedverse.get() or not self.gespeichertestBuch == self.clicked.get() or Hintregrundaktualisierenvariable:
                Verseüber = self.Liedverse.get()
                if Textanzeiger.Versüperprüfen(self.clicked.get() ,self.Liednummer.get(), Verseüber,Verseüber) == True:
                    Hi = self.Liedverse.get()
                    Hi2 = Hi[:-1]
                    self.Liedverse.delete(0, "end")
                    self.Liedverse.insert(0, Hi2)
                else:
                    self.Liedverse.delete(0, "end")
                    self.Liedverse.insert(END, Textanzeiger.Versüperprüfen(self.clicked.get() ,self.Liednummer.get(), Verseüber,Verseüber))
                Grafigfuer_ein_Lied.Buchabkuerzen(self)
                Grafigfuer_ein_Lied.Datein_lesen(self)
                Grafigfuer_ein_Lied.Livestream_Vorchau(self)
                AktuellerText1 = open("C:\\Users\\" + Dateiort + "\\Desktop\\Lieder\\" + str(Liedname) + ".txt", 'r', encoding='utf8')
                AktuellerText = AktuellerText1.read()
                if len(self.Liedverse.get()) >= 1:
                    if AktuellerText == (self.Buch + " " + self.Liednummer.get() + " Vers " + str(self.Liedverse.get()) + "\n" + self.Dateiliedtext):
                        self.Liednummer.config(bg="green")
                        self.Liedverse.config(bg="green")
                    else:
                        self.Liednummer.config(bg="red")
                        self.Liedverse.config(bg="red")
                else:
                    if AktuellerText == (self.Buch + " " + self.Liednummer.get() + "\n" + self.Dateiliedtext):
                        self.Liednummer.config(bg="green")
                        self.Liedverse.config(bg="green")
                    else:
                        self.Liednummer.config(bg="red")
                        self.Liedverse.config(bg="red")
            self.gespeichertestlied = self.Liednummer.get()
            self.gespeichertestvers = self.Liedverse.get()
            self.gespeichertestBuch = self.clicked.get()
            
    # Speichert alle relevanten Daten egal ob Livestream oder zum Wiederherstellen
    def Knopf_Druecken(self, Liedname, Liedposition):
        global Hintregrundaktualisierenvariable 
        try:
            if self.aktualisieren_wahl == "True":
                Lied_Textueberabe = open(
                    "C:\\Users\\" + Dateiort + "\\Desktop\\Lieder\\Einbledungen\\" + self.clicked.get() + "\\l" +
                    str(self.Liednummer.get()) + ".txt", 'r', encoding='utf8')
                Lied_Text = Lied_Textueberabe.read()
                Livestream_Text = open("C:\\Users\\" + Dateiort + "\\Desktop\\Lieder\\" + Liedname + ".txt", 'w', encoding='utf8')
                Lied_nummer_uebergabe = open("C:\\Users\\" + Dateiort + "\\Desktop\\Lieder\\Nummer"+Liedname + ".txt", 'w', encoding='utf8')
                Lied_nummer_uebergabe.write(self.Liednummer.get())
                Lied_nummer_uebergabe.close()
                Lied_Vers_uebergabe = open("C:\\Users\\" + Dateiort + "\\Desktop\\Lieder\\Verse"+Liedname + ".txt", 'w', encoding='utf8')
                Lied_Vers_uebergabe.write(self.Liedverse.get())
                Lied_Vers_uebergabe.close()
                Lied_Buch_Uebergabe = open("C:\\Users\\" + Dateiort + "\\Desktop\\Lieder\\Buch"+Liedname + ".txt", 'w', encoding='utf8')
                Lied_Buch_Uebergabe.write(str(self.Buchzahl_clicked))
                Lied_Buch_Uebergabe.close()
                if len(self.Liedverse.get()) >= 1:
                    Livestream_Text.write(self.Buch + " " + str(self.Liednummer.get()) + " Vers " + str(self.Liedverse.get()) + "\n" + Lied_Text)
                else:
                    Livestream_Text.write(self.Buch + " " + str(self.Liednummer.get()) + "\n" + Lied_Text)
                Livestream_Text.close()
                self.Daten_fürTextanderwand = [Liedposition, False, self.clicked.get(), self.Liednummer.get(), self.Liedverse.get()]
                self.Liednummerfest = self.Liednummer.get()
                self.Liedversefest = self.Liedverse.get()
                Hintregrundaktualisierenvariable = True
        except:
            self.Liedversefest = 0
            self.Liednummerfest = 0

    # Löscht alle Eingaben für ein Lied
    def Eingabe_loeschen(self):
        if self.aktualisieren_wahl == "True":
            self.Liedverse.delete(0, "end")
            self.Liednummer.delete(0, "end")
            self.clicked.set(Buch_Listen[0])

    # Wiederherstellt, die Alten eingaben
    def Eingabe_wiederherstellen(self, Liedname):
        if self.aktualisieren_wahl == "True":
            self.Liedverse.delete(0, "end")
            self.Liednummer.delete(0, "end")
            Lied_nummer_uebergabe = open("C:\\Users\\" + Dateiort + "\\Desktop\\Lieder\\Nummer" + Liedname + ".txt", 'r', encoding='utf8')
            Lied_Vers_uebergabe = open("C:\\Users\\" + Dateiort + "\\Desktop\\Lieder\\Verse" + Liedname + ".txt", 'r', encoding='utf8')
            Lied_Buch_Uebergabe = open("C:\\Users\\" + Dateiort + "\\Desktop\\Lieder\\Buch" + Liedname + ".txt", 'r', encoding='utf8')
            Lied_vers = Lied_Vers_uebergabe.read()
            Lied_Nummer = Lied_nummer_uebergabe.read()
            Lied_Buch = Lied_Buch_Uebergabe.read()
            self.Liedverse.insert(0, Lied_vers)
            self.Liednummer.insert(0, Lied_Nummer)
            self.clicked.set(Buch_Listen[int(Lied_Buch)])

    def Hintergrund(self, Hintergrund, Vordergrund):
        if self.aktualisieren_wahl == "True":
            self.opt.config(bg=Hintergrund, fg=Vordergrund)
            self.Liednummer.config(bg=Hintergrund, fg=Vordergrund)
            self.Liedverse.config(bg=Hintergrund, fg=Vordergrund)
            self.Lied.config(bg=Hintergrund, fg=Vordergrund)
            self.Verse.config(bg=Hintergrund, fg=Vordergrund)
            self.Liedtextanzeige.config(bg=Hintergrund, fg=Vordergrund)

    def Aktualiesieren(self, Position):
        if self.aktualisieren_wahl == "True":
            self.Liednummer.place(x=150, y=Position)
            self.Lied.place(x=0, y=Position)
            self.opt.place(x=340, y=25 + Position)
            self.Liedtextanzeige.place(x=495, y=15 + Position)
            self.Liedverse.place(x=150, y=40 + Position)
            self.Verse.place(y=40 + Position)
    
    def Grafikresetten(self):
        if self.aktualisieren_wahl == "True":
            self.Liedtextanzeige.config(bg=Textmanager_Hintergrund)

    def Grafick_präsentation(self, Liedcommand):
        if self.aktualisieren_wahl == "True":
            self.Liednummer.destroy()
            self.Liedverse.destroy()
            self.Liedtextanzeige.place(x=180)
            self.opt.destroy()
            self.Liedtextanzeige.config(command=Liedcommand)

    
    def Grafick_Eingabe(self, Position, Liedname):
        if self.aktualisieren_wahl == "True":
            self.clicked = StringVar()
            self.clicked.set(Buch_Listen[0])
            OptionMenu(Textmanager, self.clicked, *Buch_Listen)
            self.opt = OptionMenu(Textmanager, self.clicked, *Buch_Listen)
            self.opt.config(width=12, font=('Helvetica', 12), bg=Textmanager_Hintergrund, fg=Textmanager_Textfarbe)
            self.Liednummer = Entry(Textmanager, font=("Helvetica", 24), width=10)
            self.Liedverse = Entry(Textmanager, font=("Helvetica", 24), width=10)
            self.opt.place(x=340, y=25 + Position)
            self.Liedtextanzeige.place(x=495, y=15 + Position)
            self.Lied.place(x=0, y=0 + Position)
            self.Verse.place(y=40 + Position)
            self.Liednummer.place(x=150, y=0 + Position)
            self.Liedverse.place(x=150, y=40 + Position)
            self.Eingabe_wiederherstellen(Liedname)
            Hauptbildschirmbutton.place(x=800)
            self.Liedtextanzeige.config(command="")
            self.gespeichertestBuch = 0
            self.gespeichertestlied = 0
            self.gespeichertestvers = 0



def Einstellungen_Laden():
    global Textmanager_Textfarbe, Textmanager_Hintergrund, Kinder_anzeigen, Kinder_Anzeigen_Grafig, Kinder_Position, Zusatzlied1_obwahr, Zusatzlied2_obwahr, Zusatzlied3_obwahr, Zusatzlied4_obwahr, Wie_viele_zusatzlieder, Browseröffnen
    Textfarbe = open("C:\\Users\\" + Dateiort + "\\Desktop\\Lieder\\Textfarbe.txt", 'r', encoding='utf8')
    Textmanager_Textfarbe = Textfarbe.read()
    Textfarbe.close()
    Hintergrund = open("C:\\Users\\" + Dateiort + "\\Desktop\\Lieder\\Hintergrund.txt", 'r', encoding='utf8')
    Textmanager_Hintergrund = Hintergrund.read()
    Hintergrund.close()
    Kinderladen = open("C:\\Users\\" + Dateiort + "\\Desktop\\Lieder\\Kindereinstellung.txt", 'r', encoding='utf8')
    Kinder_anzeigen = Kinderladen.read()
    Kinderladen.close()
    Browseröffnen = open("C:\\Users\\" + Dateiort + "\\Desktop\\Lieder\\Chrome.txt", 'r', encoding='utf8')
    Browseröffnen = Browseröffnen.read()
    if Kinder_anzeigen == "Wahr":
        Kinder_Anzeigen_Grafig = "True"
        Kinder_Position = 1
    else:
        Kinder_Anzeigen_Grafig = "False"
        Kinder_Position = 0



# Erstellt die Grundstruktur des Programms
def Textmamager_erstellen():
    Einstellungen_Laden()
    global Einganslied, Textwortlied, Amtswechsellied, Kinderlied, Bussslied, Abendmahlslied, Schlusslied, Zusatzlied1, Zusatzlied2, Zusatzlied3, Zusatzlied4, zusaetzliches_lied, Button_bestaetigen, Wie_viele_zusatzlieder, loeschenbutton, Einstellungen_button, Textwortentry, Textwortlabel, wiederherstellen, Stream_erstell_button, Hauptbildschirmbutton, zusaetzliches_liedzerstörer, Verskontroll_Button, Stream_plan_button
    Einganslied = Grafigfuer_ein_Lied(0, "Eingangslied", "True", Textmanager_Hintergrund, Textmanager_Textfarbe)
    Textwortlied = Grafigfuer_ein_Lied(83+41, "Textwortlied", "True", Textmanager_Hintergrund, Textmanager_Textfarbe)
    Amtswechsellied = Grafigfuer_ein_Lied(166+41, "Amtswechsellied", "True", Textmanager_Hintergrund, Textmanager_Textfarbe)
    Kinderlied = Grafigfuer_ein_Lied(166+41 +83*Kinder_Position, "Kinderlied", Kinder_Anzeigen_Grafig, Textmanager_Hintergrund, Textmanager_Textfarbe)
    Bussslied = Grafigfuer_ein_Lied(249+41+83*Kinder_Position, "Bußlied", "True", Textmanager_Hintergrund, Textmanager_Textfarbe)
    Abendmahlslied = Grafigfuer_ein_Lied(332+41+83*Kinder_Position, "Abendmahlslied", "True", Textmanager_Hintergrund, Textmanager_Textfarbe)
    Schlusslied = Grafigfuer_ein_Lied(415+41+83*Kinder_Position, "Schlusslied", "True", Textmanager_Hintergrund, Textmanager_Textfarbe)
    Zusatzlied1 = Grafigfuer_ein_Lied(1000+83*Kinder_Position, "Zusatzlied", Zusatzlied1_obwahr, Textmanager_Hintergrund, Textmanager_Textfarbe)
    Zusatzlied2 = Grafigfuer_ein_Lied(1000+83*Kinder_Position, "Zusatzlied1", Zusatzlied2_obwahr, Textmanager_Hintergrund, Textmanager_Textfarbe)
    Zusatzlied3 = Grafigfuer_ein_Lied(1000+83*Kinder_Position, "Zusatzlied2", Zusatzlied3_obwahr, Textmanager_Hintergrund, Textmanager_Textfarbe)
    Zusatzlied4 = Grafigfuer_ein_Lied(1000+83*Kinder_Position, "Zusatzlied3", Zusatzlied4_obwahr, Textmanager_Hintergrund, Textmanager_Textfarbe)
    Textmanager.config(bg=Textmanager_Hintergrund)
    zusaetzliches_lied = Button(Textmanager, font=("Helvetica", 12), fg=Textmanager_Hintergrund, bg=Textmanager_Textfarbe, text="Weiters Lied", command=zusaetzlicheslied)
    zusaetzliches_liedzerstörer = Button(Textmanager, font=("Helvetica", 12), fg=Textmanager_Hintergrund, bg=Textmanager_Textfarbe, text="Zusatzlied Löschen", command=zusaetzlichesliedzerstörer)    
    zusaetzliches_lied.place(x=300, y=500+41+83*Kinder_Position)
    Button_bestaetigen = Button(Textmanager, font=("Helvetica", 24), text="Bestätigen", command=Button_command)
    Button_bestaetigen.place(x=800, y=200)
    loeschenbutton = Button(Textmanager, font=("Helvetica", 20), fg="#98FB98", bg="#B22222", text="Löschen", command=Eingabe_loeschen)
    loeschenbutton.place(x=800, y=396)
    wiederherstellen = Button(Textmanager, font=("Helvetica", 20), fg="#98FB98", bg="#B22222", text="Wiederherstellen", command=Eingabe_wiederherstellen)
    wiederherstellen.place(x=800, y=333)
    Einstellungen_button = Button(Textmanager, font=("Helvetica", 20), fg="#98FB98", bg="#B22222", text="Einstellung", command=Einstellungen)
    Einstellungen_button.place(x=800, y=270)
    Textwortlabel = Label(Textmanager, font=("Halvetica", 15), bg=Textmanager_Hintergrund, fg=Textmanager_Textfarbe, text="Textwort")
    Textwortlabel.place(y=83)
    Textwortentry = Button(Textmanager, font=("Helvetica", 15), text="Bitte hier das Textwort eingeben", bg=Textmanager_Hintergrund, fg=Textmanager_Textfarbe, command=Textwortcommand, border=0)
    Textwortentry.place(x=150,y=83)
    Stream_erstell_button = Button(Textmanager, font=("Helvetica", 20), fg="#98FB98", bg="#B22222", text="Stream Erstellen", command = chromesteuereinheit.Stream_planen_Thread)
    Stream_plan_button = Button(Textmanager, font=("Helvetica", 20), fg="#98FB98", bg="#B22222", text="Stream starten", command=Streamstarten)
    Stream_plan_button.place(x=800, y=20)
    Hauptbildschirmbutton = Button(Textmanager, font=("Helvetica", 20), fg="#98FB98", bg="#B22222", text="Präsentation", command=Grifuckfürpräsantatiom)
    Hauptbildschirmbutton.place(x=800, y=720)
    Verskontroll_Button = Button(Textmanager, font=("Helvetica", 15), fg="#98FB98", bg="#B22222", text="Liedkontrolle", command=Verskontrolle)
    Verskontroll_Button.place(x=800, y=110)

def Textwortcommand():
    global Textworteingabe, Textwort_manager, Textworteingabeübergabe
    Textworteingabeübergabe = True
    Textwort_manager = Toplevel(Textmanager)
    Textwort_manager.geometry("800x600")
    Textworteingabe = Text(Textwort_manager, font=("Helvetica", 15), height= 20, width=60, bg="#FFEBCD")
    if Textwortwiederherstellen == True:
        Textwortauslesen = open("C:\\Users\\" + Dateiort + "\\Desktop\\Lieder\\Textwort.txt", 'r', encoding='utf8')
        Textwortvariabel = Textwortauslesen.read()
        Textworteingabe.insert(END, Textwortvariabel)
        Textwortauslesen.close()
    Textworteingabe.pack()
    Textwortbestätigen = Button(Textwort_manager, font=("Helvetica", 15), text="Textwort bestätigen", bg="#FFEBCD", command=Textwortbestätigenbefehl)
    Textwortbestätigen.place(x=270, y=520)


def Textwortbestätigenbefehl():
    global Textwortübergabe, Textworteingabeübergabe
    Textwortentry.config(text=Textworteingabe.get("1.0","1.end"))
    Textwortübergabe = Textworteingabe.get("1.0","1.end")
    Textwortübergabeganz = Textworteingabe.get("1.0","end-1c")
    Textwortauslesen = open("C:\\Users\\" + Dateiort + "\\Desktop\\Lieder\\Textwort.txt", 'w', encoding='utf8')
    Textwortauslesen.write(Textwortübergabeganz)
    Textwortauslesen.close()
    Textwortauslesen1 = open("C:\\Users\\" + Dateiort + "\\Desktop\\Lieder\\Textwortbutton.txt", 'w', encoding='utf8')
    Textwortauslesen1.write(Textwortübergabe)
    Textwortauslesen1.close()
    Textwortauslesen2 = open("C:\\Users\\" + Dateiort + "\\Desktop\\Lieder\\Buch\\Textwort\\1 Vers 1.txt", 'w', encoding='utf8')
    Textwortauslesen2.write(Textwortübergabeganz)
    Textwortauslesen2.close()
    Textwort_manager.destroy()
    Textworteingabeübergabe = False

def Grifuckfürpräsantatiom():
    if Buttonebestätigengedrückt == True:
        global Hintregrundaktualisieren, klick, zurueck, AnfangHaupt, Stream_beenden_button, Tastensperren
        Hintregrundaktualisieren = False
        zurueck = Button(Textmanager, font=("Helvetica", 20), fg="#98FB98", bg="#B22222", text="zurück", command=Textanzeiger.Versvorher)
        zurueck.place(x=430, y=630)
        klick = Button(Textmanager, font=("Helvetica", 20), fg="#98FB98", bg="#B22222", text="weiter", command=Textanzeiger.Liedgebe)
        klick.place(x=430,y=500)
        AnfangHaupt = Button(Textmanager, font=("Helvetica", 20), fg="#98FB98", bg="#B22222", text="Anfang", command = Textanzeiger.Anfang)
        AnfangHaupt.place(x=430, y=20)
        Einganslied.Grafick_präsentation(Textanzeiger.Eingasliedübergabe)
        Textwortlied.Grafick_präsentation(Textanzeiger.Textwortliedübergabe)
        Amtswechsellied.Grafick_präsentation(Textanzeiger.Amtswechseliedübergabe)
        Kinderlied.Grafick_präsentation(Textanzeiger.Kinderliedübergabe)
        Bussslied.Grafick_präsentation(Textanzeiger.Bußliedübergabe)
        Abendmahlslied.Grafick_präsentation(Textanzeiger.Abendmahlsliedübergabe)
        Schlusslied.Grafick_präsentation(Textanzeiger.Schlussliedübergabe)
        Zusatzlied1.Grafick_präsentation(Textanzeiger.Zusatzlied1übergabe)
        Zusatzlied2.Grafick_präsentation(Textanzeiger.Zusatzlied2übergabe)
        Zusatzlied3.Grafick_präsentation(Textanzeiger.Zusatzlied3übergabe)
        Zusatzlied4.Grafick_präsentation(Textanzeiger.Zusatzlied4übergabe)
        Button_bestaetigen.destroy()
        Einstellungen_button.destroy()
        wiederherstellen.destroy()
        loeschenbutton.destroy()
        Stream_erstell_button.destroy()
        Hauptbildschirmbutton.place(x=430)
        Hauptbildschirmbutton.config(command=Grifickeingabe, text="Eingabe")
        zusaetzliches_lied.destroy()
        zusaetzliches_liedzerstörer.destroy()
        Einganslied.Liedtextanzeige.config(bg="orange")
        Textwortentry.config(command=Textanzeiger.Textwortübergabe, bg=Textmanager_Hintergrund, fg=Textmanager_Textfarbe)
        Textwortentry.place(x=180)
        Textanzeiger.Datenfürliedanderwand = Einganslied.Daten_fürTextanderwand.copy()
        Textanzeiger.Wieoft = 0
        Stream_erstell_button.destroy()
        Stream_beenden_button = Button(Textmanager, font=("Helvetica", 15), fg="#98FB98", bg="#B22222", text="Stream\nBeenden", command=Streambeenden)
        Stream_beenden_button.place(x=430, y=300)
        Tastensperren = Button(Textmanager, font=("Helvetica", 15), fg="#98FB98", bg="green", text="Tastatur", command=Tastaturaus)
        Tastensperren.place(x=430, y=230)
        Textmanager.minsize(width=400, height=800)
        Textmanager.geometry("600x"+str(Textmanager.winfo_height())+"")
        Verskontroll_Button.destroy()
        Stream_plan_button.destroy()
        Textmanager.update()

def Grifickeingabe():
    global Hintregrundaktualisieren, zusaetzliches_lied, Button_bestaetigen, loeschenbutton, wiederherstellen, Einstellungen_button, Stream_erstell_button, zusaetzliches_liedzerstörer, Textwortentry
    Hintregrundaktualisieren = True
    klick.destroy()
    zurueck.destroy()
    AnfangHaupt.destroy()
    Hauptbildschirmbutton.config(command=Grifuckfürpräsantatiom, text="Präsentation")
    Textmanager.minsize(width=1040, height=800)
    Textmanager.geometry("1040x"+str(Textmanager.winfo_height())+"")
    Einganslied.Grafick_Eingabe(0,"Einganslied")
    Textwortlied.Grafick_Eingabe(83+41, "Textwortlied")
    Amtswechsellied.Grafick_Eingabe(166+41, "Amtswechsellied")
    Kinderlied.Grafick_Eingabe(249+41, "Kinderlied")
    Bussslied.Grafick_Eingabe(249+41+83*Kinder_Position, "Bußlied")
    Abendmahlslied.Grafick_Eingabe(332+41+83*Kinder_Position, "Abendmahlslied")
    Schlusslied.Grafick_Eingabe(415+41+83*Kinder_Position, "Schlusslied")
    Zusatzlied1.Grafick_Eingabe(498+41+83*Kinder_Position, "Zusatzlied1")
    Zusatzlied2.Grafick_Eingabe(581+41+83*Kinder_Position, "Zusatzlied2")
    Zusatzlied3.Grafick_Eingabe(664+41+83*Kinder_Position, "Zusatzlied3")
    Zusatzlied4.Grafick_Eingabe(747+41+83*Kinder_Position, "Zusatzlied4")
    zusaetzliches_lied = Button(Textmanager, font=("Helvetica", 12), bg=Textmanager_Hintergrund, fg=Textmanager_Textfarbe, text="Weiters Lied", )
    zusaetzliches_lied.place(x=300, y=500+83*Kinder_Position+Wie_viele_zusatzlieder+83)
    if Zusatzlied1_obwahr == True:
        zusaetzliches_lied.config(command=zusaetzlicheslied1)
        zusaetzliches_liedzerstörer = Button(Textmanager, font=("Helvetica", 12), bg=Textmanager_Hintergrund, fg=Textmanager_Textfarbe, text="Zusatzlied Löschen", command=zusaetzlichesliedzerstörer)
    elif Zusatzlied2_obwahr == True:
        zusaetzliches_lied.config(command=zusaetzlicheslied2)
        zusaetzliches_liedzerstörer = Button(Textmanager, font=("Helvetica", 12), bg=Textmanager_Hintergrund, fg=Textmanager_Textfarbe, text="Zusatzlied Löschen", command=zusaetzlichesliedzerstörer1)
    elif Zusatzlied3_obwahr == True:
        zusaetzliches_lied.config(command=zusaetzlicheslied3)
        zusaetzliches_liedzerstörer = Button(Textmanager, font=("Helvetica", 12), bg=Textmanager_Hintergrund, fg=Textmanager_Textfarbe, text="Zusatzlied Löschen", command=zusaetzlichesliedzerstörer2)
    elif Zusatzlied4_obwahr == True:
        zusaetzliches_liedzerstörer = Button(Textmanager, font=("Helvetica", 12), bg=Textmanager_Hintergrund, fg=Textmanager_Textfarbe, text="Zusatzlied Löschen", command=zusaetzlichesliedzerstörer3)
        zusaetzliches_lied.destroy()
    else:
        zusaetzliches_lied.config(command=zusaetzlicheslied)
    Button_bestaetigen = Button(Textmanager, font=("Helvetica", 24), text="Bestätigen", command=Button_command)
    Button_bestaetigen.place(x=800, y=200)
    loeschenbutton = Button(Textmanager, font=("Helvetica", 20), fg="#98FB98", bg="#B22222", text="Löschen", command=Eingabe_loeschen)
    loeschenbutton.place(x=800, y=396)
    wiederherstellen = Button(Textmanager, font=("Helvetica", 20), fg="#98FB98", bg="#B22222", text="Wiederherstellen", command=Eingabe_wiederherstellen)
    wiederherstellen.place(x=800, y=333)
    Einstellungen_button = Button(Textmanager, font=("Helvetica", 20), fg="#98FB98", bg="#B22222", text="Einstellung", command=Einstellungen)
    Einstellungen_button.place(x=800, y=270)
    Stream_erstell_button = Button(Textmanager, font=("Helvetica", 20), fg="#98FB98", bg="#B22222", text="Stream Erstellen", command = chromesteuereinheit.Stream_planen_Thread)
    Stream_erstell_button.place(x=800, y=480)
    Textwortentry.config(command=Textwortcommand, bg=Textmanager_Hintergrund, fg=Textmanager_Textfarbe)
    Aktualiesierung_Grafick()
    Stream_beenden_button.destroy()
    Verskontroll_Button = Button(Textmanager, font=("Helvetica", 15), fg="#98FB98", bg="#B22222", text="Liedkontrolle", command=Verskontrolle)
    Verskontroll_Button.place(x=800, y=110)
    Stream_plan_button = Button(Textmanager, font=("Helvetica", 20), fg="#98FB98", bg="#B22222", text="Stream starten", command=Streamstarten)
    Stream_plan_button.place(x=800, y=20)
    Tastensperren.destroy()
    Textanzeiger.Wieoft = 0
    Textanzeiger.Wieoftlied = 1
    Textanzeiger.Grundstellung(True)

def Verskontrolle():
    global Verskontroller, Liedeingabe, Verseingabe, Verszahl, Liedverse_eingabe, Buchclicked, Streameinblendung 
    Verskontroller = Toplevel(Textmanager)
    Verskontroller.geometry("800x800")
    Verskontroller.title("Vers Kontrolle")
    Verskontroller.config(bg=Textmanager_Hintergrund)
    Liedeingabe = Entry(Verskontroller, font=("Helvetica", 24), width=4)
    Liedeingabe.place(x=300,y=60)
    Verseingabe = Entry(Verskontroller, font=("Helvetica", 24), width=2)
    Verseingabe.place(x=300, y=105)
    Verszahl = Entry(Verskontroller, font=("Helvetica", 24), width=2)
    Verszahl.place(x=300, y=150)
    Liedeingabelabel = Label(Verskontroller, font=("Helvetica", 15), text="Bitte geben sie ein Lied ein", bg=Textmanager_Hintergrund, fg=Textmanager_Textfarbe)
    Liedeingabelabel.place(x=10, y=60)
    Verseingabelabel = Label(Verskontroller, font=("Helvetica", 15), text="Welcher Vers ist das?", bg=Textmanager_Hintergrund, fg=Textmanager_Textfarbe)
    Verseingabelabel.place(x=10, y=105)
    Verszahllabel = Label(Verskontroller, font=("Helvetica", 15), text="Wie viele Verse hat das Lied?", bg=Textmanager_Hintergrund, fg=Textmanager_Textfarbe)
    Verszahllabel.place(x=10, y=150)
    Liedverse_eingabe = Text(Verskontroller, font=("Helvetica", 20), height= 15, width=40, bg="#FFEBCD")
    Liedverse_eingabe.place(y=255, x=10)
    Buchclicked = StringVar()
    Buchclicked.set(Buch_Listen[0])
    OptionMenu(Verskontroller, Buchclicked, *Buch_Listen)
    Buchopt = OptionMenu(Verskontroller, Buchclicked, *Buch_Listen)
    Buchopt.config(width=20, font=('Helvetica', 12), bg=Textmanager_Hintergrund, fg=Textmanager_Textfarbe)
    Buchopt.place(x=10,y=10)
    Versbestätigen = Button(Verskontroller, font=("Helvetica", 24), text="Bestätigen", command=Versbestätigendef)
    Versbestätigen.place(x=300, y=755)
    Streameinblendung = Entry(Verskontroller, font=("Helvetica", 24), width=30, bg="#FFEBCD")
    Streameinblendung.place(x=10, y=205)
    Verskontrolleloop()

def Versbestätigendef():
    Text = open("C:\\Users\\" + Dateiort + "\\Desktop\\Lieder\\Buch\\"+Buchclicked.get()+"\\"+Liedeingabe.get()+" Vers "+str(Verse)+".txt", 'w', encoding='utf8')
    Text.write(Liedverse_eingabe.get("1.0","end-1c"))
    Text.close()
    Text1 = open("C:\\Users\\" + Dateiort + "\\Desktop\\Lieder\\Versanzahl\\"+Buchclicked.get()+"\\"+Liedeingabe.get()+".txt", 'w', encoding='utf8')
    Text1.write(Verszahl.get())
    Text1.close()

def Verskontrolleloop():
    global Buchclickedladen, Verszahlladen, Verseingabeladen, Liedeingabeladen, Verse
    Verszahl.get()
    erstart = ""
    if Verseingabe.get() == erstart:
        Verse = 1
    else:
        Verse = Verseingabe.get()
    Liedverse_eingabe.get("1.0","end-1c")
    if not Buchclicked.get() == Buchclickedladen or not Verseingabe.get() == Verseingabeladen or not Liedeingabe.get() == Liedeingabeladen:
        if len(Liedeingabe.get()) > 0:
            try:
                Text = open("C:\\Users\\" + Dateiort + "\\Desktop\\Lieder\\Buch\\"+Buchclicked.get()+"\\"+Liedeingabe.get()+" Vers "+str(Verse)+".txt", 'r', encoding='utf8')
                Textfertig = Text.read()
                Text.close()
                Liedverse_eingabe.delete("1.0","end-1c")
                Liedverse_eingabe.insert(END,Textfertig)
            except:
                Liedverse_eingabe.delete("1.0","end-1c")
            try:
                Text1 = open("C:\\Users\\" + Dateiort + "\\Desktop\\Lieder\\Versanzahl\\"+Buchclicked.get()+"\\"+Liedeingabe.get()+".txt", 'r', encoding='utf8')
                text1 = Text1.read()
                Verszahl.delete(0, "end")
                Verszahl.insert(0, text1)
            except:
                Verszahl.delete(0, "end")
            try:
                Einblendung = open("C:\\Users\\" + Dateiort + "\\Desktop\\Lieder\\Einbledungen\\"+Buchclicked.get()+"\\l"+Liedeingabe.get()+".txt", 'r', encoding='utf8')
                Einblendungfertig = Einblendung.read()
                Einblendung.close()
                Streameinblendung.delete(0, "end")
                Streameinblendung.insert(END,Einblendungfertig)
            except:
                Streameinblendung.delete(0, "end")
                print("error")
                print("C:\\Users\\" + Dateiort + "\\Desktop\\Lieder\\Buch\\"+Buchclicked.get()+"\\"+Liedeingabe.get()+" Vers "+str(Verse)+".txt")
                print(Verse)
    Buchclickedladen = Buchclicked.get()
    Verseingabeladen = Verseingabe.get()
    Verszahlladen = Liedeingabe.get()
    Liedeingabeladen= Liedeingabe.get()
    Liedeingabe.after(100, lambda: Verskontrolleloop())


def zusaetzlicheslied3():
    global Wie_viele_zusatzlieder, Zusatzlied4, Zusatzlied4_obwahr, Zusatzlied3_obwahr
    Zusatzlied4 = Grafigfuer_ein_Lied(498 + 83 * Wie_viele_zusatzlieder+83*Kinder_Position, "Zusatzlied" + str(Wie_viele_zusatzlieder + 1), "True", Textmanager_Hintergrund, Textmanager_Textfarbe)
    Wie_viele_zusatzlieder = Wie_viele_zusatzlieder + 1
    Zusatzlied4_obwahr = True
    Zusatzlied3_obwahr = False
    Aktualiesierung_Grafick()
    zusaetzliches_lied.destroy()
    zusaetzliches_liedzerstörer.config(command=zusaetzlichesliedzerstörer3)

def zusaetzlichesliedzerstörer3():
    global Wie_viele_zusatzlieder, zusaetzliches_lied, Zusatzlied4_obwahr, Zusatzlied3_obwahr
    Zusatzlied4.Zerstören()
    Zusatzlied4_obwahr = False
    Zusatzlied3_obwahr = True
    Wie_viele_zusatzlieder = Wie_viele_zusatzlieder - 1
    zusaetzliches_lied = Button(Textmanager, font=("Helvetica", 12), fg=Textmanager_Hintergrund,
            bg=Textmanager_Textfarbe, text="Weiters Lied",
    command=zusaetzlicheslied3)
    Aktualiesierung_Grafick()
    zusaetzliches_liedzerstörer.config(command=zusaetzlichesliedzerstörer2)

def zusaetzlicheslied2():
    global Wie_viele_zusatzlieder, Zusatzlied3, Zusatzlied3_obwahr, Zusatzlied2_obwahr
    Zusatzlied3 = Grafigfuer_ein_Lied(498 + 83 * Wie_viele_zusatzlieder+83*Kinder_Position, "Zusatzlied" + str(Wie_viele_zusatzlieder + 1), "True", Textmanager_Hintergrund, Textmanager_Textfarbe)
    Wie_viele_zusatzlieder = Wie_viele_zusatzlieder + 1
    Zusatzlied3_obwahr = True
    Zusatzlied2_obwahr = False
    Textmanager.geometry("1040x990")
    if chromesteuereinheit.Chromeaktuell == False:
        chromesteuereinheit.Chromeupdate.place(y=940)
    Textmanager.minsize(width=1040, height=990)
    zusaetzliches_lied.config(command=zusaetzlicheslied3)
    Aktualiesierung_Grafick()
    zusaetzliches_liedzerstörer.config(command=zusaetzlichesliedzerstörer2)

def zusaetzlichesliedzerstörer2():
    global Wie_viele_zusatzlieder, Zusatzlied3_obwahr, Zusatzlied2_obwahr
    Zusatzlied3.Zerstören()
    Zusatzlied3_obwahr = False
    Zusatzlied2_obwahr = True
    Wie_viele_zusatzlieder = Wie_viele_zusatzlieder - 1
    zusaetzliches_lied.config(command=zusaetzlicheslied2)
    Aktualiesierung_Grafick()
    zusaetzliches_liedzerstörer.config(command=zusaetzlichesliedzerstörer1)
    if chromesteuereinheit.Chromeaktuell == False:
        chromesteuereinheit.Chromeupdate.place(y=760)
    Textmanager.geometry("1040x800")
    Textmanager.minsize(width=1040, height=850)

def zusaetzlicheslied1():
    global Wie_viele_zusatzlieder, Zusatzlied2, Zusatzlied2_obwahr, Zusatzlied1_obwahr
    Zusatzlied2 = Grafigfuer_ein_Lied(498 + 83 * Wie_viele_zusatzlieder+83*Kinder_Position, "Zusatzlied" + str(Wie_viele_zusatzlieder + 1),
                                      "True", Textmanager_Hintergrund, Textmanager_Textfarbe)
    Wie_viele_zusatzlieder = Wie_viele_zusatzlieder + 1
    Zusatzlied2_obwahr = True
    Zusatzlied1_obwahr = False
    Aktualiesierung_Grafick()
    zusaetzliches_lied.config(command=zusaetzlicheslied2)
    zusaetzliches_liedzerstörer.config(command=zusaetzlichesliedzerstörer1)

def zusaetzlichesliedzerstörer1():
    global Wie_viele_zusatzlieder, Zusatzlied2_obwahr, Zusatzlied1_obwahr
    Zusatzlied2.Zerstören()
    Zusatzlied2_obwahr = False
    Zusatzlied1_obwahr = True
    Wie_viele_zusatzlieder = Wie_viele_zusatzlieder - 1
    zusaetzliches_lied.config(command=zusaetzlicheslied1)
    Aktualiesierung_Grafick()
    zusaetzliches_liedzerstörer.config(command=zusaetzlichesliedzerstörer)

def zusaetzlicheslied():
    global Wie_viele_zusatzlieder, Zusatzlied1, Zusatzlied1_obwahr, zusaetzliches_liedzerstörer
    Zusatzlied1 = Grafigfuer_ein_Lied(498 + 83 * Wie_viele_zusatzlieder+83*Kinder_Position, "Zusatzlied" + str(Wie_viele_zusatzlieder + 1),
                                      "True", Textmanager_Hintergrund, Textmanager_Textfarbe)
    Wie_viele_zusatzlieder = Wie_viele_zusatzlieder + 1
    Zusatzlied1_obwahr = True
    zusaetzliches_liedzerstörer = Button(Textmanager, font=("Helvetica", 12), fg=Textmanager_Hintergrund, bg=Textmanager_Textfarbe, text="Zusatzlied Löschen", command=zusaetzlichesliedzerstörer)
    zusaetzliches_lied.config(command=zusaetzlicheslied1)
    Aktualiesierung_Grafick()


def zusaetzlichesliedzerstörer():
    global Wie_viele_zusatzlieder, Zusatzlied1_obwahr
    Zusatzlied1.Zerstören()
    Zusatzlied1_obwahr = False
    Wie_viele_zusatzlieder = Wie_viele_zusatzlieder - 1
    zusaetzliches_lied.config(command=zusaetzlicheslied)
    Aktualiesierung_Grafick()
    zusaetzliches_liedzerstörer.destroy()


def Button_command():
    global Buttonebestätigengedrückt
    Einganslied.Knopf_Druecken("Einganslied", 1)
    Textwortlied.Knopf_Druecken("Textwortlied", 3)
    Amtswechsellied.Knopf_Druecken("Amtswechsellied", 4)
    Kinderlied.Knopf_Druecken("Kinderlied", 5)
    Bussslied.Knopf_Druecken("Bußlied", 5+Kinder_Position)
    Abendmahlslied.Knopf_Druecken("Abendmahlslied", 6+Kinder_Position)
    Schlusslied.Knopf_Druecken("Schlusslied", 7+Kinder_Position)
    Zusatzlied1.Knopf_Druecken("Zusatzlied1", 8+Kinder_Position)
    Zusatzlied2.Knopf_Druecken("Zusatzlied2", 9+Kinder_Position)
    Zusatzlied3.Knopf_Druecken("Zusatzlied3", 10+Kinder_Position)
    Zusatzlied4.Knopf_Druecken("Zusatzlied4", 11+Kinder_Position)
    chromesteuereinheit.Videobeschreibung_Thread()
    Buttonebestätigengedrückt = True


def Hintergrund_aktualisieren():
    global Testeneingeben, Zeit, Zeit1, Zeit2, Zeit3, Hintregrundaktualisierenvariable
    if Hintregrundaktualisieren == True:
        Einganslied.Hintergrund_aktualisierung("Einganslied")
        Textwortlied.Hintergrund_aktualisierung("Textwortlied")
        Amtswechsellied.Hintergrund_aktualisierung("Amtswechsellied")
        Kinderlied.Hintergrund_aktualisierung("Kinderlied")
        Bussslied.Hintergrund_aktualisierung("Bußlied")
        Abendmahlslied.Hintergrund_aktualisierung("Abendmahlslied")
        Schlusslied.Hintergrund_aktualisierung("Schlusslied")
        Zusatzlied1.Hintergrund_aktualisierung("Zusatzlied1")
        Zusatzlied2.Hintergrund_aktualisierung("Zusatzlied2")
        Zusatzlied3.Hintergrund_aktualisierung("Zusatzlied3")
        Zusatzlied4.Hintergrund_aktualisierung("Zusatzlied4")
        Hintregrundaktualisierenvariable = False
    else:
        if Testeneingeben == True:
            if keyboard.get_hotkey_name()== str(1):
                while keyboard.get_hotkey_name()==str(1):
                    pass
            elif keyboard.get_hotkey_name() == str(2):
                while keyboard.get_hotkey_name() == str(2):
                    pass
            elif keyboard.get_hotkey_name() == str(3):
                while keyboard.get_hotkey_name() == str(3):
                    pass
            elif keyboard.get_hotkey_name() == str(4):
                while keyboard.get_hotkey_name() == str(4):
                    pass
            elif keyboard.get_hotkey_name()== str(5):
                while keyboard.get_hotkey_name()== str(5):
                    pass
            elif keyboard.get_hotkey_name() == str(6):
                while keyboard.get_hotkey_name() == str(6):
                    pass
            elif keyboard.get_hotkey_name()== str(7):
                while keyboard.get_hotkey_name() == str(7):
                    pass
            elif keyboard.get_hotkey_name() == str(8):
                while keyboard.get_hotkey_name() == str(8):
                    pass
            elif keyboard.get_hotkey_name()== str(9):
                while keyboard.get_hotkey_name() == str(9):
                    pass
            elif keyboard.get_hotkey_name() == str(0):
                while keyboard.get_hotkey_name() == str(0):
                    pass
            elif keyboard.is_pressed("page_down"):
                while keyboard.is_pressed("page_down"):
                    pass
                Textanzeiger.Liedgebe()
            elif keyboard.is_pressed("page_up"):
                while keyboard.is_pressed("page_up"):
                    pass
                Textanzeiger.Versvorher()
            elif keyboard.is_pressed("space"):
                while keyboard.is_pressed("space"):
                    pass
                Textanzeiger.Liedgebe()
            elif keyboard.is_pressed("left"):
                while keyboard.is_pressed("left"):
                    pass
                Textanzeiger.Versvorher()
            elif keyboard.is_pressed("right"):
                while keyboard.is_pressed("right"):
                    pass
                Textanzeiger.Liedgebe()
            elif keyboard.is_pressed("up"):
                while keyboard.is_pressed("up"):
                    pass
                Textanzeiger.Wieoft = 0
                Textanzeiger.Wieoftlied = Textanzeiger.Wieoftlied - 1
                Textanzeiger.vorherübergabeTextandiewand()
            elif keyboard.is_pressed("down"):
                while keyboard.is_pressed("down"):
                    pass
                Textanzeiger.Wieoftlied = Textanzeiger.Wieoftlied + 1
                Textanzeiger.Nächstelied()
        if keyboard.is_pressed("strg"):
            if keyboard.is_pressed("y"):
                while keyboard.is_pressed("y"):
                    pass
                if Testeneingeben == False:  
                    Testeneingeben = True
                else:
                    Testeneingeben = False
    if float(datetime.datetime.now().strftime("%H.%M")) == Zeit or float(datetime.datetime.now().strftime("%H.%M")) == Zeit1:
        Textanzeiger.Grundstellung(True)
        Zeit1 = 100
        Zeit = 100
    if float(datetime.datetime.now().strftime("%H.%M")) == Zeit2 or float(datetime.datetime.now().strftime("%H.%M")) == Zeit3:
        keyboard.press("F24")
        time.sleep(0.5)
        keyboard.release("F24")
        time.sleep(0.5)
        keyboard.press("1")
        time.sleep(0.5)
        keyboard.release("1")
        Zeit2 = 100
        Zeit3 = 100
    Amtswechsellied.Spontaneingabe_Hintergrund_aktualisierung(Textanzeiger.Darf_ich_Amtswechsel)
    Einganslied.Lied.after(100, lambda: Hintergrund_aktualisieren())


def Tastaturaus():
    global Testeneingeben
    Testeneingeben = False
    Tastensperren.config(bg="red", command=Tastaturan)

def Tastaturan():
    global Testeneingeben
    Testeneingeben = True
    Tastensperren.config(bg="green", command=Tastaturaus)

def Streamstarten1():
    pass
    keyboard.press("")
    time.sleep()
    keyboard.release("")
    time.sleep(5)
    keyboard.press("")
    keyboard.press("")
    time.sleep()
    keyboard.release("")
    keyboard.release("")

def Streamstarten():
    Streamstarten_Thread = Thread(target=Streamstarten1)
    Streamstarten_Thread.start()

def Streambeenden_Thread():
    Streambeenden_thread = Thread(target=Streambeenden)
    Streambeenden_thread.start()

def Streambeenden():
    keyboard.press("9")
    time.sleep(0.5)
    keyboard.release("9")
    time.sleep(0.5)
    keyboard.press("1")
    time.sleep(0.5)
    keyboard.release("1")
    time.sleep(116)
    keyboard.press("strg")
    keyboard.press("q")
    time.sleep(1.5)
    keyboard.release("strg")
    keyboard.release("q")
    time.sleep(5)
    Textanzeiger.Grundstellung(True)
    subprocess.call("taskkill /IM chrome.exe /F")
    subprocess.call("shutdown /s /t 60")
    sys.exit()

def Eingabe_loeschen():
    global Textworteingabeübergabe, Textwortwiederherstellen
    Einganslied.Eingabe_loeschen()
    Textwortlied.Eingabe_loeschen()
    Amtswechsellied.Eingabe_loeschen()
    Bussslied.Eingabe_loeschen()
    Abendmahlslied.Eingabe_loeschen()
    Schlusslied.Eingabe_loeschen()
    Kinderlied.Eingabe_loeschen()
    Zusatzlied1.Eingabe_loeschen()
    Zusatzlied2.Eingabe_loeschen()
    Zusatzlied3.Eingabe_loeschen()
    Zusatzlied4.Eingabe_loeschen()
    Textwortwiederherstellen = False
    Textworteingabeübergabe = False
    Textwortübergabe = "Bitte hier das Textwort eingeben"
    Textwortentry.config(text=Textwortübergabe)


def Eingabe_wiederherstellen():
    global Textwortwiederherstellen
    Einganslied.Eingabe_wiederherstellen("Einganslied")
    Textwortlied.Eingabe_wiederherstellen("Textwortlied")
    Amtswechsellied.Eingabe_wiederherstellen("Amtswechsellied")
    Bussslied.Eingabe_wiederherstellen("Bußlied")
    Abendmahlslied.Eingabe_wiederherstellen("Abendmahlslied")
    Schlusslied.Eingabe_wiederherstellen("Schlusslied")
    Kinderlied.Eingabe_wiederherstellen("Kinderlied")
    Zusatzlied1.Eingabe_wiederherstellen("Zusatzlied1")
    Zusatzlied2.Eingabe_wiederherstellen("Zusatzlied2")
    Zusatzlied3.Eingabe_wiederherstellen("Zusatzlied3")
    Zusatzlied4.Eingabe_wiederherstellen("Zusatzlied4")
    Textwortauslesen1 = open("C:\\Users\\" + Dateiort + "\\Desktop\\Lieder\\Textwortbutton.txt", 'r', encoding='utf8')
    Textwortübergabe = Textwortauslesen1.read()
    Textwortauslesen1.close()
    Textwortentry.config(text=Textwortübergabe)
    Textwortwiederherstellen = True
    if Textworteingabeübergabe == True:
        Textwortauslesen = open("C:\\Users\\" + Dateiort + "\\Desktop\\Lieder\\Textwort.txt", 'r', encoding='utf8')
        Textwortvariabel = Textwortauslesen.read()
        Textworteingabe.delete("1.0", END)
        Textworteingabe.insert(END, Textwortvariabel)
        Textwortauslesen.close()


def Farben_in_Zahl(uebergabe):
    if uebergabe == "black":
        return 0
    elif uebergabe == "white":
        return 1
    elif uebergabe == "green":
        return 2
    elif uebergabe == "yellow":
        return 3
    elif uebergabe == "pink":
        return 4


def Hintergrund():
    Textmanager.config(bg=Hintergrund_clicked.get())
    Einganslied.Hintergrund(Hintergrund_clicked.get(), Vordergrund_clicked.get())
    Textwortlied.Hintergrund(Hintergrund_clicked.get(), Vordergrund_clicked.get())
    Amtswechsellied.Hintergrund(Hintergrund_clicked.get(), Vordergrund_clicked.get())
    Kinderlied.Hintergrund(Hintergrund_clicked.get(), Vordergrund_clicked.get())
    Bussslied.Hintergrund(Hintergrund_clicked.get(), Vordergrund_clicked.get())
    Abendmahlslied.Hintergrund(Hintergrund_clicked.get(), Vordergrund_clicked.get())
    Schlusslied.Hintergrund(Hintergrund_clicked.get(), Vordergrund_clicked.get())
    Zusatzlied1.Hintergrund(Hintergrund_clicked.get(), Vordergrund_clicked.get())
    Zusatzlied2.Hintergrund(Hintergrund_clicked.get(), Vordergrund_clicked.get())
    Zusatzlied3.Hintergrund(Hintergrund_clicked.get(), Vordergrund_clicked.get())
    Zusatzlied4.Hintergrund(Hintergrund_clicked.get(), Vordergrund_clicked.get())
    Einstellungen_Textmanager.config(bg=Hintergrund_clicked.get())
    Hintergrund_opt.config(bg=Hintergrund_clicked.get(), fg=Vordergrund_clicked.get())
    Hintergrundlabel.config(bg=Hintergrund_clicked.get(), fg=Vordergrund_clicked.get())
    Vordergrund_opt.config(bg=Hintergrund_clicked.get(), fg=Vordergrund_clicked.get())
    Textlabel.config(bg=Hintergrund_clicked.get(), fg=Vordergrund_clicked.get())
    Hintergrund = open("C:\\Users\\" + Dateiort + "\\Desktop\\Lieder\\Hintergrund.txt", 'w', encoding='utf8')
    Hintergrund.write(Hintergrund_clicked.get())
    Hintergrund.close()
    Textfarbe = open("C:\\Users\\" + Dateiort + "\\Desktop\\Lieder\\Textfarbe.txt", 'w', encoding='utf8')
    Textfarbe.write(Vordergrund_clicked.get())
    Textfarbe.close()
    Buttonfarben.config(bg=Hintergrund_clicked.get(), fg=Vordergrund_clicked.get())
    zusaetzliches_lied.config(bg=Vordergrund_clicked.get(), fg=Hintergrund_clicked.get())


def Einstellungen():
    Einstellungen_Laden()
    global Hintergrund_clicked, Vordergrund_clicked, Einstellungen_Textmanager, Hintergrund_opt, Vordergrund_clicked, \
        Vordergrund_opt, Hintergrundlabel, Textlabel, Buttonfarben, Kinder_Anzeigen_Grafig, Kinder_Position, Kinderbutton, Browserbutton
    Einstellungen_Textmanager = Toplevel(Textmanager)
    Einstellungen_Textmanager.geometry("500x300")
    Einstellungen_Textmanager.title("Einstellungen")
    Einstellungen_Textmanager.config(bg=Textmanager_Hintergrund)
    Farben_liste = [
        "black",
        "white",
        "green",
        "yellow",
        "pink"]
    Buttonfarben = Button(Einstellungen_Textmanager, text="Hintergrund", fg=Textmanager_Textfarbe,
                          bg=Textmanager_Hintergrund, command=Hintergrund)
    Buttonfarben.place(x=1, y=75)
    Hintergrund_clicked = StringVar()
    Hintergrund_clicked.set(Farben_liste[Farben_in_Zahl(Textmanager_Hintergrund)])
    OptionMenu(Einstellungen_Textmanager, Hintergrund_clicked, *Farben_liste)
    Hintergrund_opt = OptionMenu(Einstellungen_Textmanager, Hintergrund_clicked, *Farben_liste)
    Hintergrund_opt.config(width=12, font=('Helvetica', 12), fg=Textmanager_Textfarbe, bg=Textmanager_Hintergrund)
    Hintergrund_opt.place(x=1, y=35)
    Vordergrund_clicked = StringVar()
    Vordergrund_clicked.set(Farben_liste[Farben_in_Zahl(Textmanager_Textfarbe)])
    OptionMenu(Einstellungen_Textmanager, Vordergrund_clicked, *Farben_liste)
    Vordergrund_opt = OptionMenu(Einstellungen_Textmanager, Vordergrund_clicked, *Farben_liste)
    Vordergrund_opt.config(width=12, font=('Helvetica', 12), fg=Textmanager_Textfarbe, bg=Textmanager_Hintergrund)
    Vordergrund_opt.place(x=150, y=35)
    Hintergrundlabel = Label(Einstellungen_Textmanager, font=('Helvetica', 12), fg=Textmanager_Textfarbe,
                             bg=Textmanager_Hintergrund, text="Hintergrund")
    Hintergrundlabel.place(y=5, x=1)
    Textlabel = Label(Einstellungen_Textmanager, font=('Helvetica', 12), fg=Textmanager_Textfarbe,
                      bg=Textmanager_Hintergrund, text="Textfarbe")
    Textlabel.place(x=150, y=5)
    Textfarbe = open("C:\\Users\\" + Dateiort + "\\Desktop\\Lieder\\Textfarbe.txt", 'w', encoding='utf8')
    Textfarbe.write(Textmanager_Textfarbe)
    Textfarbe.close()
    Hintergrunddatei = open("C:\\Users\\" + Dateiort + "\\Desktop\\Lieder\\Hintergrund.txt", 'w', encoding='utf8')
    Hintergrunddatei.write(Textmanager_Hintergrund)
    Hintergrunddatei.close()
    if Kinder_anzeigen == "Falsch":
        Kinderbutton = Button(Einstellungen_Textmanager, font=('Helvetica', 12), fg="Black", bg="red", text="Kein Kinderlied", command=Kinder_Anzeigen)
    else:
        Kinderbutton = Button(Einstellungen_Textmanager, font=('Helvetica', 12), fg="Black", bg="green", text="Kinderlied", command=Kinder_Nicht_Anzeigen)
    Kinderbutton.place(x=0, y=110)
    if Browseröffnen == "Wahr":
        Browserbutton = Button(Einstellungen_Textmanager, font=('Helvetica', 12), fg="Black", bg="green", text="Browser offen", command=Browsergeschlossen)
    else:
        Browserbutton = Button(Einstellungen_Textmanager, font=('Helvetica', 12), fg="Black", bg="red", text="Kein Browser", command=Browseroffen)
    Browserbutton.place(y=150)

def Browseroffen():
    Browseröffnen = open("C:\\Users\\" + Dateiort + "\\Desktop\\Lieder\\Chrome.txt", 'w', encoding='utf8')
    Browseröffnen.write("Wahr")
    Browseröffnen.close()
    Browserbutton.config(bg="green", text="Browser offen", command=Browsergeschlossen)
    chromesteuereinheit.Chromestarten_Thread()

def Browsergeschlossen():
    Browseröffnen = open("C:\\Users\\" + Dateiort + "\\Desktop\\Lieder\\Chrome.txt", 'w', encoding='utf8')
    Browseröffnen.write("Falsch")
    Browseröffnen.close()
    Browserbutton.config(bg="red", text="Kein Browser", command=Browseroffen)

def Kinder_Anzeigen():
    global Kinder_Anzeigen_Grafig, Kinder_Position, Kinderlied
    Kinderbutton.config(bg="green", text="Kinderlied", command=Kinder_Nicht_Anzeigen)
    Kinder_Anzeigen_Grafig = "False"
    Kinder_Position = 1
    Kinderladen = open("C:\\Users\\" + Dateiort + "\\Desktop\\Lieder\\Kindereinstellung.txt", 'w', encoding='utf8')
    Kinderladen.write("Wahr")
    Kinderladen.close()
    Kinderlied = Grafigfuer_ein_Lied(166+41 +83*Kinder_Position, "Kinderlied", "True", Textmanager_Hintergrund, Textmanager_Textfarbe)
    Aktualiesierung_Grafick()


def Kinder_Nicht_Anzeigen():
    global Kinder_Anzeigen_Grafig, Kinder_Position
    Kinderbutton.config(bg="red", text="Kein Kinderlied", command=Kinder_Anzeigen)
    Kinder_Anzeigen_Grafig = "True"
    Kinder_Position = 0
    Kinderladen = open("C:\\Users\\" + Dateiort + "\\Desktop\\Lieder\\Kindereinstellung.txt", 'w', encoding='utf8')
    Kinderladen.write("Falsch")
    Kinderladen.close()
    Kinderlied.Zerstören()
    Aktualiesierung_Grafick()


def Aktualiesierung_Grafick():
    global Wie_viele_zusatzlieder
    Einganslied.Aktualiesieren(0)
    Textwortlied.Aktualiesieren(83+41)
    Amtswechsellied.Aktualiesieren(166+41)
    Kinderlied.Aktualiesieren(249+41)
    Bussslied.Aktualiesieren(249+41+83*Kinder_Position)
    Abendmahlslied.Aktualiesieren(332+41+83*Kinder_Position)
    Schlusslied.Aktualiesieren(415+41+83*Kinder_Position)
    Zusatzlied1.Aktualiesieren(498+41+83*Kinder_Position)
    Zusatzlied2.Aktualiesieren(581+41+83*Kinder_Position)
    Zusatzlied3.Aktualiesieren(664+41+83*Kinder_Position)
    Zusatzlied4.Aktualiesieren(747+41+83*Kinder_Position)
    if Wie_viele_zusatzlieder > 0:
            zusaetzliches_liedzerstörer.place(x=30, y=500+41 + Wie_viele_zusatzlieder * 83+83*Kinder_Position)
    if Wie_viele_zusatzlieder < 4:
        zusaetzliches_lied.place(x=300, y=(500+41 + Wie_viele_zusatzlieder * 83+83*Kinder_Position))
    Textwortentry.place(x=150,y=83)
    


Einstellungen_Laden()
Textmamager_erstellen()
Hintergrund_aktualisieren()
