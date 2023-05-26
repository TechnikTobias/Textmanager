import datetime
import os
import subprocess
from re import T
import sys
from threading import Thread
import time
from tkinter import *
from PIL import Image, ImageTk
import keyboard

import chromesteuereinheit
import Textanzeiger
import Einstellungen
import Kamera_Steuerung
import Lied_kontrolle


Hintregrundaktualisierenvariable = False
Dateiort = os.getlogin()
Textmanager = Tk()
Textmanager.title("Textmanager")
Textmanager.geometry("1040x800")
Textmanager.minsize(width=1040, height=850)
Textmanager.iconbitmap(f"C:\\Users\\{Dateiort}\\Desktop\\Lieder\\picture_compress 1.ico")
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
Kindeladen= False
Textwortübergabedaten = [2, False, "Textwort", 1, ""]
Liedpositionübergabe = 0
Kinder_laden_einstellung = False
Kamera_aktiv_rechts = False
Kamera_aktiv_links = False
Kamera_aktiv_hoch = False
Kamera_aktiv_runter = False
Kamera_aktiv_zoomen_raus = False
Kamera_aktiv_zoomen_rein = False


buchladen = open(f"C:\\Users\\{Dateiort}\\Desktop\\Lieder\\Buchlisten.txt", 'r', encoding='utf8')
Buch_Listen1 = buchladen.read()
Buch_Listen = Buch_Listen1.split(sep=",")


Kameralisten = [
    "Altar",
    "Orgel",
    "Klavinova",
    "Vorlesung",
    "Chor",
    "Gemeinde",
    "Altar Schmuck",
    "Ochester",
    "Abendmahl",
    "Kelch"
]


Zeit = 9.20
Zeit1 = 19.50
Zeit2 = 9.25
Zeit3 = 19.55

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
    Kameraposition = None
    Daten_fürTextanderwand = [0]


    def __init__(self, Position, Liedname, Wahl, Hintergrund, Vordergrund, Kamera_Grund_position, Lied_standart):
        global Liedpositionübergabe
        if Wahl == "True":
            self.clicked = StringVar()
            self.clicked.set(Buch_Listen[Lied_standart])
            self.opt = OptionMenu(Textmanager, self.clicked, *Buch_Listen)
            self.opt.config(font=('Helvetica', 12), bg=Hintergrund, fg=Vordergrund)
            self.Kameraclicked = StringVar()
            self.Kameraclicked.set(Kameralisten[Kamera_Grund_position])
            self.Kameraopt = OptionMenu(Textmanager, self.Kameraclicked, *Kameralisten)
            self.Lied = Label(Textmanager, font=("Helvetica", 15), pady=5, text=Liedname, bg=Hintergrund, fg=Vordergrund)
            self.Verse = Label(Textmanager, font=("Helvetica", 15), text="Verse", bg=Hintergrund, fg=Vordergrund)
            self.Liednummer = Entry(Textmanager, font=("Helvetica", 24), width=10, border=0)
            self.Liedverse = Entry(Textmanager, font=("Helvetica", 24), width=10, border=0)
            self.Liedtextanzeige = Button(Textmanager, font=12, pady=5, bg=Hintergrund, border=0, fg=Vordergrund)
            self.Liedtextanzeige["justify"] = "left"
            self.Kameraopt.config(font=('Helvetica', 12), bg=Hintergrund, fg=Vordergrund)
            self.Kameraopt.place(x=80, y=40 + Position)
            self.opt.place(x=410, y=25 + Position)
            self.Liedtextanzeige.place(x=585, y=15 + Position)
            self.Lied.place(x=0, y=0 + Position)
            self.Verse.place(y=40 + Position)
            self.Liednummer.place(x=210, y=0 + Position)
            self.Liedverse.place(x=210, y=39 + Position)
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
        global Errorbild
        try:
            with open(f"C:\\Users\\{Dateiort}\\Desktop\\Lieder\\Einbledungen\\{self.clicked.get()}\\l{self.Liednummer.get()}.txt", 'r', encoding='utf8') as self.Dateiliedtext1:
                self.Dateiliedtext = self.Dateiliedtext1.read()
            try:
                Errorbild.destroy()
            except:
                pass
        except FileNotFoundError:
            try:
                Errorbild.destroy()
            except:
                pass
            Errorbild = Toplevel(Textmanager)
            Errorbild.geometry("560x350+500+400")
            Errorbild.config(bg=Textmanager_Hintergrund)
            Error = Label(Errorbild, font=("Helvetica", 40), text="Error", bg=Textmanager_Hintergrund, fg=Textmanager_Textfarbe, wraplength=560)
            Error.place(x=210, y=0)
            ErrorLabel = Label(Errorbild, font=("Helvetica", 20), text=f"Dieses Liednummer {self.Liednummer.get()} im {self.clicked.get()} ist zu Groß oder ist noch nicht im System", bg=Textmanager_Hintergrund, fg=Textmanager_Textfarbe, wraplength=560)
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
        self.Kameraopt.destroy()
        self.Kameraopt = None
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
    def Buchabkuerzen(self, welches_buch):
        if welches_buch == "Gesangbuch":
            self.Buch = "GB"
            self.Buchzahl_clicked = 0
        elif welches_buch == "Chorbuch":
            self.Buch = "CB"
            self.Buchzahl_clicked = 1
        elif welches_buch == "Jugendliederbuch":
            self.Buch = "JLB"
            self.Buchzahl_clicked = 2
        elif welches_buch == "Argentinisches Chorbuch":
            self.Buch = "AC"
            self.Buchzahl_clicked = 7
        elif welches_buch == "Kinderliederbuch":
            self.Buch = "KLB"
            self.Buchzahl_clicked = 3
        elif welches_buch == "Sonderheft":
            self.Buch = "SH"
            self.Buchzahl_clicked = 9
        elif welches_buch == "Spanisches Chorbuch":
            self.Buch = "SpC"
            self.Buchzahl_clicked = 8
        elif welches_buch == "Band 1 Singt dem Herrn":
            self.Buch = "SdH Band 1"
            self.Buchzahl_clicked = 4
        elif welches_buch == "Band 2 Singt dem Herrn":
            self.Buch = "SdH Band 2"
            self.Buchzahl_clicked = 5
        elif welches_buch == "Band 3 Singt dem Herrn":
            self.Buch = "SdH Band 3"
            self.Buchzahl_clicked = 6


    def Kamerapositiondef(self):
        global Kameraposition
        if self.Kameraclicked.get() == "Altar":
            self.Kameraposition = 1
        elif self.Kameraclicked.get() == "Orgel":
            self.Kameraposition = 2
        elif self.Kameraclicked.get() == "Klavinova":
            self.Kameraposition = 3
        elif self.Kameraclicked.get() == "Vorlesung":
            self.Kameraposition = 4
        elif self.Kameraclicked.get() == "Chor":
            self.Kameraposition = 5
        elif self.Kameraclicked.get() == "Gemeinde":
            self.Kameraposition = 6
        elif self.Kameraclicked.get() == "Altar Schmuck":
            self.Kameraposition = 7
        elif self.Kameraclicked.get() == "Ochester":
            self.Kameraposition = 8
        elif self.Kameraclicked.get() == "Abendmahl":
            self.Kameraposition = 9
        elif self.Kameraclicked.get() == "Kelch":
            self.Kameraposition = 10

    # Zeig im programm, welches Lied ausgewählt ist.
    def Livestream_Vorchau(self):
        if len(self.Liedverse.get()) >= 1:
            self.Liedtextanzeige.config(text=f"{self.Buch} {self.Liednummer.get()} Vers {self.Liedverse.get()}\n{self.Dateiliedtext}")
        else:
            self.Liedtextanzeige.config(text=f"{self.Buch} {self.Liednummer.get()}\n{self.Dateiliedtext}")


    def Datein_lesen_spontan(self):
        try:
            self.Dateiliedtext1 = open(f"C:\\Users\\{Dateiort}\\Desktop\\Lieder\\Einbledungen\\({Textanzeiger.clicked.get()}\\l{Textanzeiger.Texteingabe.get()}.txt", 'r', encoding='utf8')
            self.Dateiliedtext = self.Dateiliedtext1.read()
        except:
            if len(Textanzeiger.Texteingabe.get()) > 3:
                Hi = Textanzeiger.Texteingabe.get()
                Hi2 = Hi[:-1]
                Textanzeiger.Texteingabe.delete(0, "end")
                Textanzeiger.Texteingabe.insert(0, Hi2)


    def Livestream_Vorchau_spontan(self, Liedname):
        try:
            if len(Textanzeiger.Verseingabe.get()) >= 1:
                self.Liedtextanzeige.config(text=f"{self.Buch} {Textanzeiger.Texteingabe.get()} Vers {Textanzeiger.Verseingabe.get()}\n{self.Dateiliedtext}")
            else:
                self.Liedtextanzeige.config(text=f"{self.Buch} {Textanzeiger.Texteingabe.get()}\n{self.Dateiliedtext}")
            Lied_Textueberabe = open(f"C:\\Users\\{Dateiort}\\Desktop\\Lieder\\Einbledungen\\{Textanzeiger.clicked.get()}\\l{Textanzeiger.Texteingabe.get()}.txt", 'r', encoding='utf8')
            Lied_Text = Lied_Textueberabe.read()
            Livestream_Text = open(f"C:\\Users\\{Dateiort}\\Desktop\\Lieder\\{Liedname}.txt", 'w', encoding='utf8')
            Lied_nummer_uebergabe = open(f"C:\\Users\\{Dateiort}\\Desktop\\Lieder\\Nummer{Liedname}.txt", 'w', encoding='utf8')
            Lied_nummer_uebergabe.write(Textanzeiger.Texteingabe.get())
            Lied_nummer_uebergabe.close()
            Lied_Vers_uebergabe = open(f"C:\\Users\\{Dateiort}\\Desktop\\Lieder\\Verse{Liedname}.txt", 'w', encoding='utf8')
            Lied_Vers_uebergabe.write(Textanzeiger.Verseingabe.get())
            Lied_Vers_uebergabe.close()
            Lied_Buch_Uebergabe = open(f"C:\\Users\\{Dateiort}\\Desktop\\Lieder\\Buch{Liedname}.txt", 'w', encoding='utf8')
            Lied_Buch_Uebergabe.write(str(self.Buchzahl_clicked))
            Lied_Buch_Uebergabe.close()
            if len(Textanzeiger.Verseingabe.get()) >= 1:
                Livestream_Text.write(f"{self.Buch} {Textanzeiger.Texteingabe.get()} Vers {Textanzeiger.Verseingabe.get()}\n{Lied_Text}")
            else:
                Livestream_Text.write(f"{self.Buch} {Textanzeiger.Texteingabe.get()}\n{Lied_Text}")
            Livestream_Text.close()
        except:
            pass

    def Spontaneingabe_Hintergrund_aktualisierung(self, Welcheslied, Liedposition, Liedname):
        global Hintregrundaktualisierenvariable
        if Welcheslied:
            Verseüber = Textanzeiger.Verseingabe.get()
            if Textanzeiger.Versüperprüfen(Textanzeiger.clicked.get() ,Textanzeiger.Texteingabe.get(), Verseüber,Verseüber):
                Hi = Textanzeiger.Verseingabe.get()
                Hi2 = Hi[:-1]
                Textanzeiger.Verseingabe.delete(0, "end")
                Textanzeiger.Verseingabe.insert(0, Hi2)
            else:
                Textanzeiger.Verseingabe.delete(0, "end")
                Textanzeiger.Verseingabe.insert(END, Textanzeiger.Versüperprüfen(Textanzeiger.clicked.get() ,Textanzeiger.Texteingabe.get(), Verseüber,Verseüber))
            Grafigfuer_ein_Lied.Buchabkuerzen(self,Textanzeiger.clicked.get())
            Grafigfuer_ein_Lied.Datein_lesen_spontan(self)
            Grafigfuer_ein_Lied.Livestream_Vorchau_spontan(self, Liedname)
            self.Daten_fürTextanderwand = [Liedposition, False, Textanzeiger.clicked.get(), Textanzeiger.Texteingabe.get(), Textanzeiger.Verseingabe.get()]



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
                Grafigfuer_ein_Lied.Buchabkuerzen(self, self.clicked.get())
                Grafigfuer_ein_Lied.Datein_lesen(self)
                Grafigfuer_ein_Lied.Livestream_Vorchau(self)
                AktuellerText1 = open(f"C:\\Users\\{Dateiort}\\Desktop\\Lieder\\{Liedname}.txt", 'r', encoding='utf8')
                AktuellerText = AktuellerText1.read()
                if len(self.Liedverse.get()) >= 1:
                    if AktuellerText == (f"{self.Buch} {self.Liednummer.get()} Vers {self.Liedverse.get()}\n{self.Dateiliedtext}"):
                        self.Liednummer.config(bg="green")
                        self.Liedverse.config(bg="green")
                    else:
                        self.Liednummer.config(bg="red")
                        self.Liedverse.config(bg="red")
                else:
                    if AktuellerText == (f"{self.Buch} {self.Liednummer.get()}\n{self.Dateiliedtext}"):
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
                Lied_Textueberabe = open(f"C:\\Users\\{Dateiort}\\Desktop\\Lieder\\Einbledungen\\{self.clicked.get()}\\l{self.Liednummer.get()}.txt", 'r', encoding='utf8')
                Lied_Text = Lied_Textueberabe.read()
                Livestream_Text = open(f"C:\\Users\\{Dateiort}\\Desktop\\Lieder\\{Liedname}.txt", 'w', encoding='utf8')
                Lied_nummer_uebergabe = open(f"C:\\Users\\{Dateiort}\\Desktop\\Lieder\\Nummer{Liedname}.txt", 'w', encoding='utf8')
                Lied_nummer_uebergabe.write(self.Liednummer.get())
                Lied_nummer_uebergabe.close()
                Lied_Vers_uebergabe = open(f"C:\\Users\\{Dateiort}\\Desktop\\Lieder\\Verse{Liedname}.txt", 'w', encoding='utf8')
                Lied_Vers_uebergabe.write(self.Liedverse.get())
                Lied_Vers_uebergabe.close()
                Lied_Buch_Uebergabe = open(f"C:\\Users\\{Dateiort}\\Desktop\\Lieder\\Buch{Liedname}.txt", 'w', encoding='utf8')
                Lied_Buch_Uebergabe.write(str(self.Buchzahl_clicked))
                Lied_Buch_Uebergabe.close()
                Lied_optTrue = open(f"C:\\Users\\{Dateiort}\\Desktop\\Lieder\\Buch{Liedname}_fexisten.txt", 'w', encoding='utf8')
                Lied_optTrue.write("True")
                Lied_optTrue.close()
                Kamera_opt = open(f"C:\\Users\\{Dateiort}\\Desktop\\Lieder\\Buch{Liedname}Kamera_position.txt", 'w', encoding='utf8')
                self.Kamerapositiondef()
                Kamera_opt.write(str(self.Kameraposition-1))
                Kamera_opt.close()
                if len(self.Liedverse.get()) >= 1:
                    Livestream_Text.write(f"{self.Buch} {self.Liednummer.get()} Vers {self.Liedverse.get()}\n{Lied_Text}")
                else:
                    Livestream_Text.write(f"{self.Buch} {self.Liednummer.get()}\n{Lied_Text}")
                Livestream_Text.close()
                self.Daten_fürTextanderwand = [Liedposition, False, self.clicked.get(), self.Liednummer.get(), self.Liedverse.get()]
                self.Liednummerfest = self.Liednummer.get()
                self.Liedversefest = self.Liedverse.get()
                Hintregrundaktualisierenvariable = True
                Datei_Kontrolle(self.clicked.get() , self.Liednummer.get())
            else:
                Lied_optTrue = open(f"C:\\Users\\{Dateiort}\\Desktop\\Lieder\\Buch{Liedname}_fexisten.txt", 'w', encoding='utf8')
                Lied_optTrue.write("False")
                Lied_optTrue.close()
        except:
            self.Liedversefest = 0
            self.Liednummerfest = 0

    # Löscht alle Eingaben für ein Lied
    def Eingabe_loeschen(self, Kamera_position, Lied_buch):
        global Kindeladen
        if self.aktualisieren_wahl == "True":
            self.Liedverse.delete(0, "end")
            self.Liednummer.delete(0, "end")
            self.clicked.set(Buch_Listen[Lied_buch])
            self.Kameraclicked.set(Kameralisten[Kamera_position])
        Kindeladen= False

    # Wiederherstellt, die Alten eingaben
    def Eingabe_wiederherstellen(self, Liedname, Hintergrund, Vordergrund , Kamera_Grund_position, Lied_standart, Position, Kinderlied_posiozion):
        global Kindeladen, Liedpositionübergabe, Wie_viele_zusatzlieder, Kinder_Position, Kinder_anzeigen, Kinder_laden_einstellung
        Lied_optTrue = open(f"C:\\Users\\{Dateiort}\\Desktop\\Lieder\\Buch{Liedname}_fexisten.txt", 'r', encoding='utf8')
        if Lied_optTrue.read() == "True":
            self.aktualisieren_wahl = "True"
        if self.aktualisieren_wahl == "True":
            try:
                self.Liedverse.get()
            except:
                if Kinderlied_posiozion:
                    Kinder_Position = 1
                    Kinder_laden_einstellung = True
                else:
                    Wie_viele_zusatzlieder = Wie_viele_zusatzlieder + 1
                self.clicked = StringVar()
                self.clicked.set(Buch_Listen[Lied_standart])
                self.opt = OptionMenu(Textmanager, self.clicked, *Buch_Listen)
                self.opt.config(font=('Helvetica', 12), bg=Hintergrund, fg=Vordergrund)
                self.Kameraclicked = StringVar()
                self.Kameraclicked.set(Kameralisten[Kamera_Grund_position])
                self.Kameraopt = OptionMenu(Textmanager, self.Kameraclicked, *Kameralisten)
                self.Lied = Label(Textmanager, font=("Helvetica", 15), pady=5, text=Liedname, bg=Hintergrund, fg=Vordergrund)
                self.Verse = Label(Textmanager, font=("Helvetica", 15), text="Verse", bg=Hintergrund, fg=Vordergrund)
                self.Liednummer = Entry(Textmanager, font=("Helvetica", 24), width=10, border=0)
                self.Liedverse = Entry(Textmanager, font=("Helvetica", 24), width=10, border=0)
                self.Liedtextanzeige = Button(Textmanager, font=12, pady=5, bg=Hintergrund, border=0, fg=Vordergrund)
                self.Liedtextanzeige["justify"] = "left"
                self.Kameraopt.config(font=('Helvetica', 12), bg=Hintergrund, fg=Vordergrund)
                self.Kameraopt.place(x=80, y=40 + Position)
                self.opt.place(x=410, y=25 + Position)
                self.Liedtextanzeige.place(x=555, y=15 + Position)
                self.Lied.place(x=0, y=0 + Position)
                self.Verse.place(y=40 + Position)
                self.Liednummer.place(x=210, y=0 + Position)
                self.Liedverse.place(x=210, y=39 + Position)
                self.aktualisieren_wahl = "True"
                Liedpositionübergabe = Liedpositionübergabe + 1
                self.gespeichertestlied = 100
                self.gespeichertestBuch = 100
                self.gespeichertestvers = 100
                Aktualiesierung_Grafick()
                Textmanager.update()
            self.Liedverse.delete(0, "end")
            self.Liednummer.delete(0, "end")
            Lied_nummer_uebergabe = open(f"C:\\Users\\{Dateiort}\\Desktop\\Lieder\\Nummer" + str(Liedname) + ".txt", 'r', encoding='utf8')
            Lied_Vers_uebergabe = open(f"C:\\Users\\{Dateiort}\\Desktop\\Lieder\\Verse" + str(Liedname) + ".txt", 'r', encoding='utf8')
            Lied_Buch_Uebergabe = open(f"C:\\Users\\{Dateiort}\\Desktop\\Lieder\\Buch" + str(Liedname) + ".txt", 'r', encoding='utf8')
            Kamera_option = open(f"C:\\Users\\{Dateiort}\\Desktop\\Lieder\\Buch{Liedname}Kamera_position.txt", 'r', encoding='utf8')
            Lied_vers = Lied_Vers_uebergabe.read()
            Lied_Nummer = Lied_nummer_uebergabe.read()
            Lied_Buch = Lied_Buch_Uebergabe.read()
            Lied_Vers_uebergabe.close()
            Lied_Buch_Uebergabe.close()
            Lied_nummer_uebergabe.close()
            self.Liedverse.insert(0, Lied_vers)
            self.Liednummer.insert(0, Lied_Nummer)
            self.clicked.set(Buch_Listen[int(Lied_Buch)])
            self.Kameraclicked.set(Kameralisten[int(Kamera_option.read())])
            Kindeladen= True


    def Hintergrund(self, Hintergrund, Vordergrund):
        if self.aktualisieren_wahl == "True":
            self.opt.config(bg=Hintergrund, fg=Vordergrund)
            self.Lied.config(bg=Hintergrund, fg=Vordergrund)
            self.Verse.config(bg=Hintergrund, fg=Vordergrund)
            self.Liedtextanzeige.config(bg=Hintergrund, fg=Vordergrund)
            self.Kameraopt.config(bg=Hintergrund,fg=Vordergrund)

    def Aktualiesieren(self, Position):
        if self.aktualisieren_wahl == "True":
            self.Liednummer.place(x=210, y=Position)
            self.Lied.place(x=0, y=Position)
            self.opt.place(x=410, y=25 + Position)
            self.Liedtextanzeige.place(x=585, y=15 + Position)
            self.Liedverse.place(x=210, y=40 + Position)
            self.Kameraopt.place(x=80, y=40+ Position)
            self.Verse.place(y=40 + Position)
    
    def Grafikresetten(self):
        if self.aktualisieren_wahl == "True":
            self.Liedtextanzeige.config(bg=Textmanager_Hintergrund)

    def Grafick_präsentation(self, Liedcommand):
        if self.aktualisieren_wahl == "True":
            self.Liednummer.destroy()
            self.Liedverse.destroy()
            self.Liedtextanzeige.place(x=210)
            self.opt.destroy()
            self.Liedtextanzeige.config(command=Liedcommand)

    
    def Grafick_Eingabe(self, Position, Liedname, Hintergrund, Vordergrund , Kamera_Grund_position, Lied_standart):
        if self.aktualisieren_wahl == "True":
            self.clicked = StringVar()
            self.clicked.set(Buch_Listen[0])
            OptionMenu(Textmanager, self.clicked, *Buch_Listen)
            self.opt = OptionMenu(Textmanager, self.clicked, *Buch_Listen)
            self.opt.config(width=12, font=('Helvetica', 12), bg=Textmanager_Hintergrund, fg=Textmanager_Textfarbe, bd=0)
            self.Liednummer = Entry(Textmanager, font=("Helvetica", 24), width=10, bd=0)
            self.Liedverse = Entry(Textmanager, font=("Helvetica", 24), width=10, bd=0)
            self.opt.place(x=400, y=25 + Position)
            self.Liedtextanzeige.place(x=445, y=15 + Position)
            self.Lied.place(x=0, y=0 + Position)
            self.Verse.place(y=40 + Position)
            self.Liednummer.place(x=210, y=0 + Position)
            self.Liedverse.place(x=210, y=39 + Position)
            self.Eingabe_wiederherstellen(Liedname, Hintergrund, Vordergrund , Kamera_Grund_position, Lied_standart, Position, False)
            Hauptbildschirmbutton.place(x=800)
            self.Liedtextanzeige.config(command="")
            self.gespeichertestBuch = 0
            self.gespeichertestlied = 0
            self.gespeichertestvers = 0



def Einstellungen_Laden(Kinder_laden_einstellung):
    global Textmanager_Textfarbe, Textmanager_Hintergrund, Kinder_anzeigen, Kinder_Anzeigen_Grafig, Kinder_Position, Zusatzlied1_obwahr, Zusatzlied2_obwahr, Zusatzlied3_obwahr, Zusatzlied4_obwahr, Wie_viele_zusatzlieder, Browseröffnen, Zeit, Zeit1, Zeit2, Zeit3, Kinder_anzeigen_einstellung
    Textfarbe = open(f"C:\\Users\\{Dateiort}\\Desktop\\Lieder\\Textfarbe.txt", 'r', encoding='utf8')
    Textmanager_Textfarbe = Textfarbe.read()
    Textfarbe.close()
    Hintergrund = open(f"C:\\Users\\{Dateiort}\\Desktop\\Lieder\\Hintergrund.txt", 'r', encoding='utf8')
    Textmanager_Hintergrund = Hintergrund.read()
    Hintergrund.close()
    Kinderladen = open(f"C:\\Users\\{Dateiort}\\Desktop\\Lieder\\Kindereinstellung.txt", 'r', encoding='utf8')
    Kinder_anzeigen = Kinderladen.read()
    Kinderladen.close()
    Browseröffnen = open(f"C:\\Users\\{Dateiort}\\Desktop\\Lieder\\Chrome.txt", 'r', encoding='utf8')
    Browseröffnen = Browseröffnen.read()
    if Kinder_laden_einstellung:
        if Kinder_anzeigen == "Wahr":
            Kinder_Anzeigen_Grafig = "True"
            Kinder_Position = 1
            Kinder_anzeigen_einstellung = True
        else:
            Kinder_Anzeigen_Grafig = "False"
            Kinder_Position = 0
            Kinder_anzeigen_einstellung = False



# Erstellt die Grundstruktur des Programms
def Textmamager_erstellen():
    Einstellungen_Laden(True)
    global Einganslied, Textwortlied, Amtswechsellied, Kinderlied, Bussslied, Abendmahlslied, Schlusslied, Zusatzlied1, Zusatzlied2, Zusatzlied3, Zusatzlied4, zusaetzliches_lied, Button_bestaetigen, Wie_viele_zusatzlieder, loeschenbutton, Einstellungen_button, Textwortentry, Textwortlabel, wiederherstellen, Stream_erstell_button, Hauptbildschirmbutton, zusaetzliches_liedzerstörer, Verskontroll_Button, Stream_plan_button, Kamera_steuerung_button, Info_button
    Einganslied = Grafigfuer_ein_Lied(0, "Eingangslied", "True", Textmanager_Hintergrund, Textmanager_Textfarbe,5,0)
    Textwortlied = Grafigfuer_ein_Lied(83+41, "Textwortlied", "True", Textmanager_Hintergrund, Textmanager_Textfarbe,4,1)
    Amtswechsellied = Grafigfuer_ein_Lied(166+41, "Amtswechsellied", "True", Textmanager_Hintergrund, Textmanager_Textfarbe,4,1)
    Kinderlied = Grafigfuer_ein_Lied(166+41 +83*Kinder_Position, "Kinderlied", Kinder_Anzeigen_Grafig, Textmanager_Hintergrund, Textmanager_Textfarbe,4,1)
    Bussslied = Grafigfuer_ein_Lied(249+41+83*Kinder_Position, "Bußlied", "True", Textmanager_Hintergrund, Textmanager_Textfarbe,5,0)
    Abendmahlslied = Grafigfuer_ein_Lied(332+41+83*Kinder_Position, "Abendmahlslied", "True", Textmanager_Hintergrund, Textmanager_Textfarbe,5,0)
    Schlusslied = Grafigfuer_ein_Lied(415+41+83*Kinder_Position, "Schlusslied", "True", Textmanager_Hintergrund, Textmanager_Textfarbe,4,1)
    Zusatzlied1 = Grafigfuer_ein_Lied(1000+83*Kinder_Position, "Zusatzlied", Zusatzlied1_obwahr, Textmanager_Hintergrund, Textmanager_Textfarbe,4,1)
    Zusatzlied2 = Grafigfuer_ein_Lied(1000+83*Kinder_Position, "Zusatzlied1", Zusatzlied2_obwahr, Textmanager_Hintergrund, Textmanager_Textfarbe,4,1)
    Zusatzlied3 = Grafigfuer_ein_Lied(1000+83*Kinder_Position, "Zusatzlied2", Zusatzlied3_obwahr, Textmanager_Hintergrund, Textmanager_Textfarbe,4,1)
    Zusatzlied4 = Grafigfuer_ein_Lied(1000+83*Kinder_Position, "Zusatzlied3", Zusatzlied4_obwahr, Textmanager_Hintergrund, Textmanager_Textfarbe,4,1)
    Textmanager.config(bg=Textmanager_Hintergrund)
    zusaetzliches_lied = Button(Textmanager, font=("Helvetica", 12), fg=Textmanager_Textfarbe, bg=Textmanager_Hintergrund, text="Weiters Lied", command=zusaetzlicheslied, border=0)
    zusaetzliches_lied.place(x=300, y=500+41+83*Kinder_Position)
    zusaetzliches_liedzerstörer = Button(Textmanager, font=("Helvetica", 12), bg=Textmanager_Hintergrund, fg=Textmanager_Textfarbe, text="Zusatzlied Löschen", command=zusaetzlichesliedzerstörer, border=0)
    Button_bestaetigen = Button(Textmanager, font=("Helvetica", 24), text="Bestätigen", command=Button_command, border=0)
    Button_bestaetigen.place(x=800, y=200)
    loeschenbutton = Button(Textmanager, font=("Helvetica", 20), fg="#98FB98", bg="#B22222", text="Löschen", command=Eingabe_loeschen, border=0)
    loeschenbutton.place(x=800, y=396)
    wiederherstellen = Button(Textmanager, font=("Helvetica", 20), fg="#98FB98", bg="#B22222", text="Wiederherstellen", command=Eingabe_wiederherstellen, border=0)
    wiederherstellen.place(x=800, y=333)
    Einstellungen_button = Button(Textmanager, font=("Helvetica", 20), fg="#98FB98", bg="#B22222", text="Einstellung", command=Einstellungen.Einstellungen_erstellen, border=0)
    Einstellungen_button.place(x=800, y=270)
    Textwortlabel = Label(Textmanager, font=("Halvetica", 15), bg=Textmanager_Hintergrund, fg=Textmanager_Textfarbe, text="Textwort")
    Textwortlabel.place(y=83)
    Textwortentry = Button(Textmanager, font=("Helvetica", 15), text="Bitte hier das Textwort eingeben", bg=Textmanager_Hintergrund, fg=Textmanager_Textfarbe, command=Textwortcommand, border=0)
    Textwortentry.place(x=210,y=83)
    Stream_erstell_button = Button(Textmanager, font=("Helvetica", 20), fg="#98FB98", bg="#B22222", text="Stream Erstellen", command = chromesteuereinheit.Stream_planen_Thread, border=0)
    Stream_erstell_button.place(x=800, y=480)
    Stream_plan_button = Button(Textmanager, font=("Helvetica", 20), fg="#98FB98", bg="#B22222", text="Stream starten", command=Streamstarten, border=0)
    Hauptbildschirmbutton = Button(Textmanager, font=("Helvetica", 20), fg="#98FB98", bg="#B22222", text="Präsentation", command=Grifuckfürpräsantatiom, border=0)
    Hauptbildschirmbutton.place(x=800, y=680)
    Verskontroll_Button = Button(Textmanager, font=("Helvetica", 15), fg="#98FB98", bg="#B22222", text="Liedkontrolle", command=Lied_kontrolle.Verskontrolle, border=0)
    Verskontroll_Button.place(x=800, y=110)
    Info_button = Button(Textmanager, font=("Helvetica", 15), fg="#98FB98", bg="#B22222", text="Info", command=info, border=0)
    Info_button.place(x=800,y=800)
    Kamera_steuerung_button = Button(Textmanager, font=("Helvetica", 15), fg="#98FB98", bg="#B22222", text="Kamera", command=Kamera, border=0)
    Kamera_steuerung_button.place(x=800, y=750)

def Kamera_grund_steuerung():
    global Kamera_aktiv_zoomen_raus, Kamera_aktiv_zoomen_rein, Kamera_aktiv_runter, Kamera_aktiv_hoch, Kamera_aktiv_links, Kamera_aktiv_rechts
    Kamera_aktiv_rechts = False
    Kamera_aktiv_links = False
    Kamera_aktiv_hoch = False
    Kamera_aktiv_runter = False
    Kamera_aktiv_zoomen_raus = False
    Kamera_aktiv_zoomen_rein = False


def Kamera_rechtsdef():
    global Kamera_aktiv_rechts
    Kamera_grund_steuerung()
    Kamera_aktiv_rechts = True

def Kamera_linksdef():
    global Kamera_aktiv_links
    Kamera_grund_steuerung()
    Kamera_aktiv_links = True

def Kamera_hochdef():
    global Kamera_aktiv_hoch
    Kamera_grund_steuerung()
    Kamera_aktiv_hoch = True

def Kamera_runterdef():
    global Kamera_aktiv_runter
    Kamera_grund_steuerung()
    Kamera_aktiv_runter = True

def Kamera_hereinzoomdef():
    global Kamera_aktiv_zoomen_rein
    Kamera_grund_steuerung()
    Kamera_aktiv_zoomen_rein = True

def Kamera_herauszoondef():
    global Kamera_aktiv_zoomen_raus
    Kamera_grund_steuerung()
    Kamera_aktiv_zoomen_raus = True



def Kamera():
    global Kamera_steuerung_anzeige, Kameraclicked_aktuell, Kamera_rechts
    try: 
        Kamera_steuerung_anzeige.destroy()
    except:
        pass
    Kamera_steuerung_anzeige = Toplevel(Textmanager)
    Kamera_steuerung_anzeige.geometry("320x280")
    Kamera_steuerung_anzeige.config(bg=Textmanager_Hintergrund)
    Kameraclicked_aktuell = StringVar()
    Kameraclicked_aktuell.set(Kameralisten[0])
    Kameraopt = OptionMenu(Kamera_steuerung_anzeige, Kameraclicked_aktuell, *Kameralisten)
    Kameraopt.place(y=0)
    Kamera_bewegen = Button(Kamera_steuerung_anzeige, font=("Helvetica", 15), fg="#98FB98", bg="#B22222", text="Steuern", command=Steuern, border=0)
    Kamera_bewegen.place(y=40)
    Kamera_rechts = Button(Kamera_steuerung_anzeige, font=("Helvetica", 15), fg="#98FB98", bg="#B22222", text="Rechts", border=0, command = Kamera_rechtsdef)
    Kamera_rechts.place(x=200, y=100)
    Kamera_links = Button(Kamera_steuerung_anzeige, font=("Helvetica", 15), fg="#98FB98", bg="#B22222", text="Links", border=0, command = Kamera_linksdef)
    Kamera_links.place(x=10, y=100)
    Kamera_hoch = Button(Kamera_steuerung_anzeige, font=("Helvetica", 15), fg="#98FB98", bg="#B22222", text="Hoch", border=0, command = Kamera_hochdef)
    Kamera_hoch.place(x=105, y=50)
    Kamera_runter = Button(Kamera_steuerung_anzeige, font=("Helvetica", 15), fg="#98FB98", bg="#B22222", text="runter", border=0, command = Kamera_runterdef)
    Kamera_runter.place(x=105, y=150)   
    Kamera_herauszoomen = Button(Kamera_steuerung_anzeige, font=("Helvetica", 15), fg="#98FB98", bg="#B22222", text="hereinzoomen", border=0, command = Kamera_hereinzoomdef)
    Kamera_herauszoomen.place(x=10, y=195)
    Kamera_hereinzoomen = Button(Kamera_steuerung_anzeige, font=("Helvetica", 15), fg="#98FB98", bg="#B22222", text="herauszoomen", border=0, command = Kamera_herauszoondef)
    Kamera_hereinzoomen.place(x=10, y=235)

def Kamera_position():
        if Kameraclicked_aktuell.get() == "Altar":
            return 1
        elif Kameraclicked_aktuell.get() == "Orgel":
            return 2
        elif Kameraclicked_aktuell.get() == "Klavinova":
            return 3
        elif Kameraclicked_aktuell.get() == "Vorlesung":
            return 4
        elif Kameraclicked_aktuell.get() == "Chor":
            return 5
        elif Kameraclicked_aktuell.get() == "Gemeinde":
            return 6
        elif Kameraclicked_aktuell.get() == "Altar Schmuck":
            return 7
        elif Kameraclicked_aktuell.get() == "Ochester":
            return 8
        elif Kameraclicked_aktuell.get() == "Abendmahl":
            return 9
        elif Kameraclicked_aktuell.get() == "Kelch":
            return 10

def Steuern():
    Kamera_grund_steuerung()
    Kamera_Steuerung.Kamera.goto_preset(Kamera_position())

def info():
    global Info_manager
    try:
        Info_manager.destroy()
    except:
        pass
    Info_manager = Toplevel(Textmanager)
    Info_manager.geometry("800x600")
    Info_manager.config(bg=Textmanager_Hintergrund)
    Text_für_Info = "Entwickler/ Uhrheber: Tobias Giebelhaus\nIn gedenken an meinen Geliebten Opa der bis zum Schluss Geistig fit war und sorgen kurz vor dem Tod im Internet war. Er war ein sehr lieber Opa"
    Info_zum_programm = Label(Info_manager, font=("Halvetica", 15), bg=Textmanager_Hintergrund, fg=Textmanager_Textfarbe, text=Text_für_Info, wraplength=800)
    Info_zum_programm["justify"] = "left"
    Info_zum_programm.place(x=0,y=0)
    Bild_für_opa1 = Image.open(f"C:\\Users\\{Dateiort}\\Desktop\\Lieder\\Sterbe Anzeige Opa.jpg")
    Bild_für_opa = ImageTk.PhotoImage(image=Bild_für_opa1.resize((472,341))) 
    Bild_für_opa_Label = Label(Info_manager,image=Bild_für_opa)
    Bild_für_opa_Label.place(x=0,y=100)
    Bild_für_opa_Label.draw()

def Textwortcommand():
    global Textworteingabe, Textwort_manager, Textworteingabeübergabe, Textwort_manager
    Textworteingabeübergabe = True
    try:
        Textworteingabe.get("1.0","1.end")
    except:
        Textwort_manager = Toplevel(Textmanager)
        Textwort_manager.geometry("800x600")
        Textworteingabe = Text(Textwort_manager, font=("Helvetica", 15), height= 20, width=60, bg="#FFEBCD")
        if Textwortwiederherstellen:
            Textwortauslesen = open(f"C:\\Users\\{Dateiort}\\Desktop\\Lieder\\Textwort.txt", 'r', encoding='utf8')
            Textwortvariabel = Textwortauslesen.read()
            Textworteingabe.insert(END, Textwortvariabel)
            Textwortauslesen.close()
        Textworteingabe.pack()
        Textwortbestätigen = Button(Textwort_manager, font=("Helvetica", 15), text="Textwort bestätigen", bg="#FFEBCD", command=Textwortbestätigenbefehl, border=0)
        Textwortbestätigen.place(x=270, y=520)


def Textwortbestätigenbefehl():
    global Textwortübergabe, Textworteingabeübergabe
    Textwortentry.config(text=Textworteingabe.get("1.0","1.end"))
    Textwortübergabe = Textworteingabe.get("1.0","1.end")
    Textwortübergabeganz = Textworteingabe.get("1.0","end-1c")
    Textwortauslesen = open(f"C:\\Users\\{Dateiort}\\Desktop\\Lieder\\Textwort.txt", 'w', encoding='utf8')
    Textwortauslesen.write(Textwortübergabeganz)
    Textwortauslesen.close()
    Textwortauslesen1 = open(f"C:\\Users\\{Dateiort}\\Desktop\\Lieder\\Textwortbutton.txt", 'w', encoding='utf8')
    Textwortauslesen1.write(Textwortübergabe)
    Textwortauslesen1.close()
    Textwortauslesen2 = open(f"C:\\Users\\{Dateiort}\\Desktop\\Lieder\\Buch\\Textwort\\1 Vers 1.txt", 'w', encoding='utf8')
    Textwortauslesen2.write(Textwortübergabeganz)
    Textwortauslesen2.close()
    Textwort_manager.destroy()
    Textworteingabeübergabe = False

def Grifuckfürpräsantatiom():
    if Buttonebestätigengedrückt:
        global Hintregrundaktualisieren, klick, zurueck, AnfangHaupt, Stream_beenden_button, Tastensperren
        Eingabe_wiederherstellen()
        Textmanager.update()
        Button_command()
        Hintergrund_aktualisieren()
        Hintregrundaktualisieren = False
        zurueck = Button(Textmanager, font=("Helvetica", 20), fg="#98FB98", bg="#B22222", text="zurück", command=Textanzeiger.Versvorher, border=0)
        zurueck.place(x=430, y=600)
        klick = Button(Textmanager, font=("Helvetica", 20), fg="#98FB98", bg="#B22222", text="weiter", command=Textanzeiger.Liedgebe, border=0)
        klick.place(x=430,y=500)
        AnfangHaupt = Button(Textmanager, font=("Helvetica", 20), fg="#98FB98", bg="#B22222", text="Anfang", command = Textanzeiger.Anfang, border=0)
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
        Textanzeiger.Eingasliedübergabefirst()
        Textwortentry.config(command=Textanzeiger.Textwortübergabe, bg=Textmanager_Hintergrund, fg=Textmanager_Textfarbe)
        Textwortentry.place(x=210)
        Textanzeiger.Datenfürliedanderwand = Einganslied.Daten_fürTextanderwand.copy()
        Textanzeiger.Wieoft = 0
        Stream_erstell_button.destroy()
        Stream_beenden_button = Button(Textmanager, font=("Helvetica", 15), fg="#98FB98", bg="#B22222", text="Stream\nBeenden", command=Streambeenden, border=0)
        Stream_beenden_button.place(x=430, y=300)
        Tastensperren = Button(Textmanager, font=("Helvetica", 15), fg="#98FB98", bg="green", text="Tastatur", command=Tastaturaus, border=0)
        Tastensperren.place(x=430, y=230)
        Kamera_steuerung_button.place(y=750, x=430)
        Textmanager.minsize(width=400, height=800)
        Textmanager.geometry("600x"+str(Textmanager.winfo_height())+"")
        Info_button.place(x=430,y=800)
        Verskontroll_Button.destroy()
        Stream_plan_button.destroy()
        Textmanager.update()

def Grifickeingabe():
    global Hintregrundaktualisieren, zusaetzliches_lied, Button_bestaetigen, loeschenbutton, wiederherstellen, Einstellungen_button, Stream_erstell_button, zusaetzliches_liedzerstörer, Textwortentry
    klick.destroy()
    zurueck.destroy()
    AnfangHaupt.destroy()
    Hauptbildschirmbutton.config(command=Grifuckfürpräsantatiom, text="Präsentation")
    Textmanager.minsize(width=1040, height=800)
    Textmanager.geometry("1040x"+str(Textmanager.winfo_height())+"")
    Einganslied.Grafick_Eingabe(0,"Einganslied", Textmanager_Hintergrund, Textmanager_Textfarbe, 5,0)
    Textwortlied.Grafick_Eingabe(83+41, "Textwortlied", Textmanager_Hintergrund, Textmanager_Textfarbe, 4,1)
    Amtswechsellied.Grafick_Eingabe(166+41, "Amtswechsellied", Textmanager_Hintergrund, Textmanager_Textfarbe,4,1,)
    Kinderlied.Grafick_Eingabe(249+41, "Kinderlied", Textmanager_Hintergrund, Textmanager_Textfarbe,4,1)
    Bussslied.Grafick_Eingabe(249+41+83*Kinder_Position, "Bußlied", Textmanager_Hintergrund, Textmanager_Textfarbe, 5,0)
    Abendmahlslied.Grafick_Eingabe(332+41+83*Kinder_Position, "Abendmahlslied", Textmanager_Hintergrund, Textmanager_Textfarbe, 5,0)
    Schlusslied.Grafick_Eingabe(415+41+83*Kinder_Position, "Schlusslied", Textmanager_Hintergrund, Textmanager_Textfarbe, 5,0)
    Zusatzlied1.Grafick_Eingabe(498+41+83*Kinder_Position, "Zusatzlied1", Textmanager_Hintergrund, Textmanager_Textfarbe,4,1)
    Zusatzlied2.Grafick_Eingabe(581+41+83*Kinder_Position, "Zusatzlied2", Textmanager_Hintergrund, Textmanager_Textfarbe,4,1)
    Zusatzlied3.Grafick_Eingabe(664+41+83*Kinder_Position, "Zusatzlied3", Textmanager_Hintergrund, Textmanager_Textfarbe,4,1)
    Zusatzlied4.Grafick_Eingabe(747+41+83*Kinder_Position, "Zusatzlied4", Textmanager_Hintergrund, Textmanager_Textfarbe,4,1)
    zusaetzliches_lied = Button(Textmanager, font=("Helvetica", 12), bg=Textmanager_Hintergrund, fg=Textmanager_Textfarbe, text="Weiters Lied", border=0)
    zusaetzliches_lied.place(x=300, y=500+83*Kinder_Position+Wie_viele_zusatzlieder+83)
    if Zusatzlied1_obwahr:
        zusaetzliches_lied.config(command=zusaetzlicheslied1)
        zusaetzliches_liedzerstörer = Button(Textmanager, font=("Helvetica", 12), bg=Textmanager_Hintergrund, fg=Textmanager_Textfarbe, text="Zusatzlied Löschen", command=zusaetzlichesliedzerstörer, border=0)
    elif Zusatzlied2_obwahr:
        zusaetzliches_lied.config(command=zusaetzlicheslied2)
        zusaetzliches_liedzerstörer = Button(Textmanager, font=("Helvetica", 12), bg=Textmanager_Hintergrund, fg=Textmanager_Textfarbe, text="Zusatzlied Löschen", command=zusaetzlichesliedzerstörer1, border=0)
    elif Zusatzlied3_obwahr:
        zusaetzliches_lied.config(command=zusaetzlicheslied3)
        zusaetzliches_liedzerstörer = Button(Textmanager, font=("Helvetica", 12), bg=Textmanager_Hintergrund, fg=Textmanager_Textfarbe, text="Zusatzlied Löschen", command=zusaetzlichesliedzerstörer2, border=0)
    elif Zusatzlied4_obwahr:
        zusaetzliches_liedzerstörer = Button(Textmanager, font=("Helvetica", 12), bg=Textmanager_Hintergrund, fg=Textmanager_Textfarbe, text="Zusatzlied Löschen", command=zusaetzlichesliedzerstörer3, border=0)
        zusaetzliches_lied.destroy()
    else:
        zusaetzliches_lied.config(command=zusaetzlicheslied)
    Button_bestaetigen = Button(Textmanager, font=("Helvetica", 24), text="Bestätigen", command=Button_command, border=0)
    Button_bestaetigen.place(x=800, y=200)
    loeschenbutton = Button(Textmanager, font=("Helvetica", 20), fg="#98FB98", bg="#B22222", text="Löschen", command=Eingabe_loeschen, border=0)
    loeschenbutton.place(x=800, y=396)
    wiederherstellen = Button(Textmanager, font=("Helvetica", 20), fg="#98FB98", bg="#B22222", text="Wiederherstellen", command=Eingabe_wiederherstellen, border=0)
    wiederherstellen.place(x=800, y=333)
    Einstellungen_button = Button(Textmanager, font=("Helvetica", 20), fg="#98FB98", bg="#B22222", text="Einstellung", command=Einstellungen.Einstellungen_erstellen, border=0)
    Einstellungen_button.place(x=800, y=270)
    Stream_erstell_button = Button(Textmanager, font=("Helvetica", 20), fg="#98FB98", bg="#B22222", text="Stream Erstellen", command = chromesteuereinheit.Stream_planen_Thread, border=0)
    Stream_erstell_button.place(x=800, y=480)
    Textwortentry.config(command=Textwortcommand, bg=Textmanager_Hintergrund, fg=Textmanager_Textfarbe)
    Aktualiesierung_Grafick()
    Stream_beenden_button.destroy()
    Verskontroll_Button = Button(Textmanager, font=("Helvetica", 15), fg="#98FB98", bg="#B22222", text="Liedkontrolle", command=Lied_kontrolle.Verskontrolle, border=0)
    Verskontroll_Button.place(x=800, y=110)
    Stream_plan_button = Button(Textmanager, font=("Helvetica", 20), fg="#98FB98", bg="#B22222", text="Stream starten", command=Streamstarten, border=0)
    Kamera_steuerung_button.place(x=800, y=750)
    Info_button.place(x=800,y=800)
    Tastensperren.destroy()
    Textanzeiger.Wieoft = 0
    Textanzeiger.Wieoftlied = 1
    Hintregrundaktualisieren = True
    Textanzeiger.Grundstellung(False, False)



def Datei_Kontrolle(Buch, Lied):
    try:
        wieoft = 0
        Text1 = open(f"C:\\Users\\{Dateiort}\\Desktop\\Lieder\\Versanzahl\\{Buch}\\{Lied}.txt", 'r', encoding='utf8')
        Hi = Text1.read()
        while not wieoft == int(Hi):
            Text = open(f"C:\\Users\\{Dateiort}\\Desktop\\Lieder\\Buch\\{Buch}\\{Lied} Vers {wieoft+1}.txt", 'r', encoding='utf8')
            wieoft = wieoft + 1
    except:
            try:
                Errorbild.destroy()
            except:
                pass
            Errorbild = Toplevel(Textmanager)
            Errorbild.geometry("560x350+500+400")
            Errorbild.config(bg=Textmanager_Hintergrund)
            Error = Label(Errorbild, font=("Helvetica", 40), text="Error", bg=Textmanager_Hintergrund, fg=Textmanager_Textfarbe, wraplength=560)
            Error.place(x=210, y=0)
            ErrorLabel = Label(Errorbild, font=("Helvetica", 20), text=f"Die Liednummer {Lied} im {Buch} ist noch nicht im System", bg=Textmanager_Hintergrund, fg=Textmanager_Textfarbe, wraplength=560)
            ErrorLabel.place(x=0, y=80)


def zusaetzlicheslied3():
    global Wie_viele_zusatzlieder, Zusatzlied4, Zusatzlied4_obwahr, Zusatzlied3_obwahr
    Zusatzlied4 = Grafigfuer_ein_Lied(498 + 83 * Wie_viele_zusatzlieder+83*Kinder_Position, "Zusatzlied" + str(Wie_viele_zusatzlieder + 1), "True", Textmanager_Hintergrund, Textmanager_Textfarbe,4,1)
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
    zusaetzliches_lied = Button(Textmanager, font=("Helvetica", 12), fg=Textmanager_Textfarbe, bg=Textmanager_Hintergrund, text="Weiters Lied",
    command=zusaetzlicheslied3)
    Aktualiesierung_Grafick()
    zusaetzliches_liedzerstörer.config(command=zusaetzlichesliedzerstörer2)

def zusaetzlicheslied2():
    global Wie_viele_zusatzlieder, Zusatzlied3, Zusatzlied3_obwahr, Zusatzlied2_obwahr
    Zusatzlied3 = Grafigfuer_ein_Lied(498 + 83 * Wie_viele_zusatzlieder+83*Kinder_Position, "Zusatzlied" + str(Wie_viele_zusatzlieder + 1), "True", Textmanager_Hintergrund, Textmanager_Textfarbe,4,1)
    Wie_viele_zusatzlieder = Wie_viele_zusatzlieder + 1
    Zusatzlied3_obwahr = True
    Zusatzlied2_obwahr = False
    Textmanager.geometry("1040x990")
    if not chromesteuereinheit.Chromeaktuell:
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
    if not chromesteuereinheit.Chromeaktuell:
        chromesteuereinheit.Chromeupdate.place(y=760)
    Textmanager.geometry("1040x800")
    Textmanager.minsize(width=1040, height=850)

def zusaetzlicheslied1():
    global Wie_viele_zusatzlieder, Zusatzlied2, Zusatzlied2_obwahr, Zusatzlied1_obwahr
    Zusatzlied2 = Grafigfuer_ein_Lied(498 + 83 * Wie_viele_zusatzlieder+83*Kinder_Position, "Zusatzlied" + str(Wie_viele_zusatzlieder + 1), "True", Textmanager_Hintergrund, Textmanager_Textfarbe,4,1)
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
    Zusatzlied1 = Grafigfuer_ein_Lied(498 + 83 * Wie_viele_zusatzlieder+83*Kinder_Position, "Zusatzlied" + str(Wie_viele_zusatzlieder + 1), "True", Textmanager_Hintergrund, Textmanager_Textfarbe,4,1)
    Wie_viele_zusatzlieder = Wie_viele_zusatzlieder + 1
    Zusatzlied1_obwahr = True
    zusaetzliches_liedzerstörer = Button(Textmanager, font=("Helvetica", 12), fg=Textmanager_Textfarbe, bg=Textmanager_Hintergrund, text="Zusatzlied Löschen", command=zusaetzlichesliedzerstörer, border=0)
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

    if Hintregrundaktualisieren:
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
        try:
            Lied_kontrolle.Buchhinzufügen.config(bg=Textmanager_Hintergrund)
        except:
            try:
                Kamera_steuerung_anzeige.config(bg=Textmanager_Hintergrund)
                while keyboard.is_pressed(" "):
                    if Kamera_aktiv_hoch:
                        Kamera_Steuerung.Kamera.move_tilt(1)
                    elif Kamera_aktiv_runter:
                        Kamera_Steuerung.Kamera.move_tilt(-1)
                    elif Kamera_aktiv_rechts:
                        Kamera_Steuerung.Kamera.move_pan(1)
                    elif Kamera_aktiv_links:
                        Kamera_Steuerung.Kamera.move_pan(-1)
                    elif Kamera_aktiv_zoomen_rein:
                        Kamera_Steuerung.Kamera.zoom(1)
                    elif Kamera_aktiv_zoomen_raus:
                        Kamera_Steuerung.Kamera.zoom(-1)
                if Kamera_aktiv_hoch or Kamera_aktiv_runter or Kamera_aktiv_links or Kamera_aktiv_rechts or Kamera_aktiv_zoomen_rein or Kamera_aktiv_zoomen_raus:
                    Kamera_Steuerung.Kamera.stop()
            except:
                if Testeneingeben:
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
                    elif keyboard.is_pressed("."):
                        while keyboard.is_pressed("."):
                            pass
                        if Textanzeiger.Anzeige:
                            Hi = ""
                            Text_Anzeige_Label.config(text=Hi)
                            Textmanager.update()
                            Textanzeiger.Anzeige = False
                            keyboard.press("0")
                            time.sleep(0.5)
                            keyboard.release("0")
                            time.sleep(0.5)
                            keyboard.press("1")
                            time.sleep(0.5)
                            keyboard.release("1")
                        else:
                            Textanzeiger.Wieoft = Textanzeiger.Wieoft -1
                            Textanzeiger.Liedgebe()
                            Textanzeiger.Anzeige = True
                if keyboard.is_pressed("strg"):
                    if keyboard.is_pressed("y"):
                        while keyboard.is_pressed("y"):
                            pass
                        if not Testeneingeben: 
                            Tastaturan()
                        else:
                            Tastaturaus()

    if float(datetime.datetime.now().strftime("%H.%M")) == float(Zeit) or float(datetime.datetime.now().strftime("%H.%M")) == float(Zeit1):
        Textanzeiger.Grundstellung(True, False)
        Einganslied.Liedtextanzeige.config(bg="orange")
        Zeit1 = 100
        Zeit = 100
    if float(datetime.datetime.now().strftime("%H.%M")) == float(Zeit2) or float(datetime.datetime.now().strftime("%H.%M")) == float(Zeit3):
        keyboard.press("F24")
        time.sleep(0.5)
        keyboard.release("F24")
        time.sleep(0.5)
        keyboard.press("1")
        time.sleep(0.5)
        keyboard.release("1")
        Zeit2 = 100
        Zeit3 = 100
    Einganslied.Spontaneingabe_Hintergrund_aktualisierung(Textanzeiger.Darf_ich_Einganslied, 1,"Einganslied")
    Textwortlied.Spontaneingabe_Hintergrund_aktualisierung(Textanzeiger.Darf_ich_Textwortlied, 3, "Textwortlied")
    Amtswechsellied.Spontaneingabe_Hintergrund_aktualisierung(Textanzeiger.Darf_ich_Amtswechsel, 4, "Amtswechsellied")
    Kinderlied.Spontaneingabe_Hintergrund_aktualisierung(Textanzeiger.Darf_ich_Kinderlied, 5, "Kinderlied")
    Bussslied.Spontaneingabe_Hintergrund_aktualisierung(Textanzeiger.Darf_ich_Busslied, 5 + Kinder_Position, "Bußlied")
    Abendmahlslied.Spontaneingabe_Hintergrund_aktualisierung(Textanzeiger.Darf_ich_Abendmahlslied, 6 + Kinder_Position, "Abendmahlslied")
    Schlusslied.Spontaneingabe_Hintergrund_aktualisierung(Textanzeiger.Darf_ich_Schlusslied, 7  + Kinder_Position, "Schlusslied")
    Zusatzlied1.Spontaneingabe_Hintergrund_aktualisierung(Textanzeiger.Darf_ich_Zusatzlied1, 8  + Kinder_Position, "Zusatzlied1")
    Zusatzlied2.Spontaneingabe_Hintergrund_aktualisierung(Textanzeiger.Darf_ich_Zusatzlied2, 9  + Kinder_Position, "Zusatzlied2")
    Zusatzlied3.Spontaneingabe_Hintergrund_aktualisierung(Textanzeiger.Darf_ich_Zusatzlied3, 10  + Kinder_Position, "Zusatzlied3")
    Zusatzlied4.Spontaneingabe_Hintergrund_aktualisierung(Textanzeiger.Darf_ich_Zusatzlied4, 11 + Kinder_Position, "Zusatzlied4")
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
    Text_Anzeige_Label.config(text="")
    Textmanager.update()
    keyboard.press("9")
    time.sleep(0.5)
    keyboard.release("9")
    time.sleep(0.5)
    keyboard.press("1")
    time.sleep(0.5)
    keyboard.release("1")
    time.sleep(116)
    keyboard.press("strg")
    time.sleep(0.1)
    keyboard.press("q")
    time.sleep(1.5)
    keyboard.release("strg")
    keyboard.release("q")
    time.sleep(5)
    Textanzeiger.Grundstellung(True, True)
    keyboard.press("strg")
    keyboard.press("x")
    time.sleep(0.5)
    keyboard.release("strg")
    keyboard.release("x")
    time.sleep(0.5)
    keyboard.press("1")
    time.sleep(0.5)
    keyboard.release("1")
    subprocess.call("taskkill /IM chrome.exe /F")
    subprocess.call("shutdown /s /t 5")
    sys.exit()

def Eingabe_loeschen():
    global Textworteingabeübergabe, Textwortwiederherstellen, Wie_viele_zusatzlieder
    Einganslied.Eingabe_loeschen(5,0)
    Textwortlied.Eingabe_loeschen(4,1)
    Amtswechsellied.Eingabe_loeschen(4,1)
    Bussslied.Eingabe_loeschen(5,0)
    Abendmahlslied.Eingabe_loeschen(5,0)
    Schlusslied.Eingabe_loeschen(4,1)
    Kinderlied.Eingabe_loeschen(4,1)
    try:
        Zusatzlied1.Zerstören(4,1)
    except:
        pass
    try:
        Zusatzlied2.Zerstören(4,1)
    except:
        pass
    try:
        Zusatzlied3.Zerstören(4,1)
    except:
        pass
    try:    
        Zusatzlied4.Zerstören(4,1)
    except:
        pass
    try:
        zusaetzliches_lied.config(command=zusaetzlicheslied)
    except:
        pass
    try:
        zusaetzliches_liedzerstörer.destroy()
    except:
        pass
    Wie_viele_zusatzlieder = 0
    Textwortwiederherstellen = False
    Textworteingabeübergabe = False
    Textwortübergabe = "Bitte hier das Textwort eingeben"
    Textwortentry.config(text=Textwortübergabe)
    Aktualiesierung_Grafick()


def Eingabe_wiederherstellen():
    global Textwortwiederherstellen, Zeit, Zeit1, Zeit2, Zeit3
    Zeit_laden = open(f"C:\\Users\\{Dateiort}\\Desktop\\Lieder\\Zeit.txt", 'r', encoding='utf8')
    Zeit = Zeit_laden.read()
    Zeit_laden.close()
    Zeit_laden = open(f"C:\\Users\\{Dateiort}\\Desktop\\Lieder\\Zeit1.txt", 'r', encoding='utf8')
    Zeit1 = Zeit_laden.read()
    Zeit_laden.close()
    Zeit_laden = open(f"C:\\Users\\{Dateiort}\\Desktop\\Lieder\\Zeit2.txt", 'r', encoding='utf8')
    Zeit2 = Zeit_laden.read()
    Zeit_laden.close()
    Zeit_laden = open(f"C:\\Users\\{Dateiort}\\Desktop\\Lieder\\Zeit3.txt", 'r', encoding='utf8')
    Zeit3 = Zeit_laden.read()
    Zeit_laden.close()
    Einganslied.Eingabe_wiederherstellen("Einganslied", Textmanager_Hintergrund, Textmanager_Textfarbe, 5,0,0, False)
    Textwortlied.Eingabe_wiederherstellen("Textwortlied", Textmanager_Hintergrund, Textmanager_Textfarbe, 4,1, 83+41, False)
    Amtswechsellied.Eingabe_wiederherstellen("Amtswechsellied", Textmanager_Hintergrund, Textmanager_Textfarbe,4,1, 166+41, False)
    Bussslied.Eingabe_wiederherstellen("Bußlied", Textmanager_Hintergrund, Textmanager_Textfarbe, 5,0, 332+41+83*Kinder_Position, False)
    Abendmahlslied.Eingabe_wiederherstellen("Abendmahlslied", Textmanager_Hintergrund, Textmanager_Textfarbe, 5,0, 332+41+83*Kinder_Position, False)
    Schlusslied.Eingabe_wiederherstellen( "Schlusslied", Textmanager_Hintergrund, Textmanager_Textfarbe, 5,0, 415+41+83*Kinder_Position, False)
    Kinderlied.Eingabe_wiederherstellen("Kinderlied", Textmanager_Hintergrund, Textmanager_Textfarbe,4,1, 249+41+83*Kinder_Position, True)
    Zusatzlied1.Eingabe_wiederherstellen("Zusatzlied1", Textmanager_Hintergrund, Textmanager_Textfarbe,4,1, 498 + 83 * 1 +83*Kinder_Position, False)
    Zusatzlied2.Eingabe_wiederherstellen("Zusatzlied2", Textmanager_Hintergrund, Textmanager_Textfarbe,4,1, 498 + 83 * 2 +83*Kinder_Position, False)
    Zusatzlied3.Eingabe_wiederherstellen("Zusatzlied3", Textmanager_Hintergrund, Textmanager_Textfarbe,4,1, 498 + 83 * 3 +83*Kinder_Position, False)
    Zusatzlied4.Eingabe_wiederherstellen("Zusatzlied4", Textmanager_Hintergrund, Textmanager_Textfarbe,4,1, 498 + 83 * 4 +83*Kinder_Position, False)
    Textwortauslesen1 = open(f"C:\\Users\\{Dateiort}\\Desktop\\Lieder\\Textwortbutton.txt", 'r', encoding='utf8')
    Textwortübergabe = Textwortauslesen1.read()
    Textwortauslesen1.close()
    Textwortentry.config(text=Textwortübergabe)
    Textwortwiederherstellen = True
    if Textworteingabeübergabe:
        try:
            Textwortauslesen = open(f"C:\\Users\\{Dateiort}\\Desktop\\Lieder\\Textwort.txt", 'r', encoding='utf8')
            Textwortvariabel = Textwortauslesen.read()
            Textworteingabe.delete("1.0", END)
            Textworteingabe.insert(END, Textwortvariabel)
            Textwortauslesen.close()
        except:
            pass

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
        try:
            zusaetzliches_liedzerstörer.place(x=30, y=500+41 + Wie_viele_zusatzlieder * 83+83*Kinder_Position)
        except:
            pass
    if Wie_viele_zusatzlieder < 4:
        try:
            zusaetzliches_lied.place(x=300, y=(500+41 + Wie_viele_zusatzlieder * 83+83*Kinder_Position))
        except:
            pass
    Textwortentry.place(x=210,y=83)
    if Wie_viele_zusatzlieder == 0:
        zusaetzliches_lied.config(command=zusaetzlicheslied)
    elif Wie_viele_zusatzlieder == 1:
        zusaetzliches_lied.config(command=zusaetzlicheslied1)
        try:
            zusaetzliches_liedzerstörer.config(command=zusaetzlichesliedzerstörer)
        except:
            pass
    elif Wie_viele_zusatzlieder == 2:
        try:
            zusaetzliches_lied.config(command=zusaetzlicheslied2)
            zusaetzliches_liedzerstörer.config(command=zusaetzlichesliedzerstörer1)
        except:
            pass
    elif Wie_viele_zusatzlieder == 3:
        try:
            zusaetzliches_lied.config(command=zusaetzlicheslied3)
            zusaetzliches_liedzerstörer.config(command=zusaetzlichesliedzerstörer2)
        except:
            pass
    elif Wie_viele_zusatzlieder == 4:
        zusaetzliches_liedzerstörer.config(command=zusaetzlichesliedzerstörer3)


Textmamager_erstellen()
Hintergrund_aktualisieren()
