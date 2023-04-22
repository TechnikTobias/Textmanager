import re
import time
import Haupt
import tkinter
import keyboard
from threading import *
import Kamera_Steuerung
Anzeige = False
Wieoft = 0
Wieoftlied = 1
voherliedzwischensehne = False
lesteslied = False
Darf_ich_Einganslied = False
Darf_ich_Textwortlied = False
Darf_ich_Amtswechsel = False
Darf_ich_Busslied = False
Darf_ich_Abendmahlslied = False
Darf_ich_Schlusslied = False
Darf_ich_Kinderlied = False
Darf_ich_Zusatzlied1 = False
Darf_ich_Zusatzlied2 = False
Darf_ich_Zusatzlied3 = False
Darf_ich_Zusatzlied4 = False
Verseingabe = None

def Versüperprüfen(Buch, Liednummer, Verseübergabe, Verse):
    global Verzanzahl1
    try:
        Verzanzahl1 = open(f"C:\\Users\\{Haupt.Dateiort}\\Desktop\\Lieder\\Versanzahl\\{Buch}\\{Liednummer}.txt", "r", encoding="utf-8")
    except:
        pass
    Verzanzahl = Verzanzahl1.read()
    Verse1 = Verse.split(",")
    Hallo = []
    try:
        while True:
            Hallo = Hallo + Verse1.pop().split("-")
            if len(Verse1) == 0:
                break
        while True:
            if Hallo == [""]:
                break
            if int(Hallo.pop()) > int(Verzanzahl):
                return True
            if len(Hallo) == 0:
                break
    except:
        pass
    p = re.compile(("[0-9,-]"))
    j = p.findall(Verseübergabe)
    charakter = "[]´"
    Verserückgabe = "".join(x for x in j if x not in charakter)
    return Verserückgabe

def Verinbterprätator(Welcheart,WelchesBuch,WelcherVers):
    try:
        global AusganneVerse
        datenteil1 = []
        AusganneVerse = []
        if len(WelcherVers) == 1:
            p = re.compile(("[0-9]"))
            j =p.findall(WelcherVers)
            charakter = "[],"
            WelcherVers = "".join(x for x in j if x not in charakter)
        einzeldaten = WelcherVers
        if einzeldaten == "":
            Sooft = 0
            AusganneVerse = []
            Wieoft = 1
            while True:
                Verzanzahl = open(f"C:\\Users\\{Haupt.Dateiort}\\Desktop\\Lieder\\Versanzahl\\{WelchesBuch}\\{Welcheart}.txt", "r", encoding="utf-8")
                Maxzahl = Verzanzahl.read()
                if Sooft == int(Maxzahl) + 1:
                    break
                AusganneVerse = AusganneVerse + [Wieoft]
                Wieoft = int(Wieoft) + 1
                Sooft = Sooft + 1
        else:
            daten = einzeldaten.split(",")
            # teilt alles bei den kommas
            Wieoft = 0
            ob1oder2odermehr = len(daten)
            while True:
                if Wieoft == ob1oder2odermehr:
                    break
                teilvers = daten.pop(0)
                # teil nach und nach vom letzten
                if len(teilvers) == 3:
                    datenteil1 = datenteil1 + [teilvers]
                elif len(teilvers) == 1:
                    AusganneVerse = AusganneVerse + [int(teilvers)]
                    # Alles mit länge 1
                elif len(teilvers) == 2:
                    AusganneVerse = AusganneVerse + [1]
                Wieoft = Wieoft + 1

            Vonbis = list(filter(lambda x: x[1].count("-"), datenteil1))
            # Lässt nur lange sachen mit - durch
            ob1oder2 = -(len(Vonbis))

            if ob1oder2 < 0:
                wieoft = 0
                teil1 = []
                teil2 = []
                while True:
                    if wieoft == ob1oder2:
                        break
                    if wieoft == ob1oder2 + 1:
                        teil1 = Vonbis[0]
                        # trennt 1 mit - vom anderem
                    if wieoft == ob1oder2 + 2:
                        teil2 = Vonbis[-1]
                        # trennt 1 mit - vom anderem
                    wieoft = wieoft - 1
                wievileverse = (int(teil1[-1]) - int(teil1[0]))
                # AusganneVerse ist teil des endergebnis
                Startvers = teil1[0]
                wieoft = 0
                while True:
                    if wieoft == wievileverse + 1:
                        break
                    AusganneVerse = AusganneVerse + [int(Startvers)]
                    Startvers = int(Startvers) + 1
                    wieoft = wieoft + 1
                    # fügt ersten paar verse dazu
                if len(teil2) > 1:
                    wievileverse = (int(teil2[-1]) - int(teil2[0]))
                    Versanfang = teil2[0]
                    wieoft = 0
                    while True:
                        if wieoft == wievileverse + 1:
                            break
                        AusganneVerse = AusganneVerse + [int(Versanfang)]
                        Versanfang = int(Versanfang) + 1
                        wieoft = wieoft + 1
                        # fügt zweite teil verse dazu
        Verzanzahl = open(f"C:\\Users\\{Haupt.Dateiort}\\Desktop\\Lieder\\Versanzahl\\{WelchesBuch}\\{Welcheart}.txt", "r", encoding="utf-8")
        Maxzahl = Verzanzahl.read()
        AusganneVerse.sort()
        global Hai
        Hai = "False"
        if len(AusganneVerse) == 0:
            Sooft = 0
            Wieoft = 1
            while True:
                Verzanzahl = open(f"C:\\Users\\{Haupt.Dateiort}\\Desktop\\Lieder\\Versanzahl\\{WelchesBuch}\\{Welcheart}.txt", "r", encoding="utf-8")
                Maxzahl = Verzanzahl.read()
                if Sooft == int(Maxzahl) + 1:
                    break
                AusganneVerse = AusganneVerse + [Wieoft]
                Wieoft = int(Wieoft) + 1
                Sooft = Sooft + 1
        if len(AusganneVerse) == 1:
            if int(AusganneVerse[0]) > int(Maxzahl):
                AusganneVerse = Maxzahl
                return True
        if int(AusganneVerse[-1]) > int(Maxzahl):
            AusganneVerse.pop()
            return True
        if int(AusganneVerse[-1]) > int(Maxzahl):
            AusganneVerse.pop()
        if int(AusganneVerse[-1]) > int(Maxzahl):
            AusganneVerse.pop()
        if int(AusganneVerse[-1]) > int(Maxzahl):
            AusganneVerse.pop()
        if int(AusganneVerse[-1]) > int(Maxzahl):
            AusganneVerse.pop()
        if int(AusganneVerse[-1]) > int(Maxzahl):
            AusganneVerse.pop()
        if int(AusganneVerse[-1]) > int(Maxzahl):
            AusganneVerse.pop()
        # Filter, das niht mehr als es Verse gibt
    except:
        Errorbild = tkinter.Toplevel(Haupt.Textmanager)
        Errorbild.geometry("560x350+500+400")
        Errorbild.config(bg=Haupt.Textmanager_Hintergrund)
        Error = tkinter.Label(Errorbild, font=("Helvetica", 40),
                      text="Error", bg=Haupt.Textmanager_Hintergrund,
                      fg=Haupt.Textmanager_Textfarbe, wraplength=560)
        Error.place(x=210, y=0)
        ErrorLabel = tkinter.Label(Errorbild, font=("Helvetica", 20),
                           text="In 0rdner Lieder im Odner Versanzahl fehlt die Datei für das Lied "+Welcheart, bg=Haupt.Textmanager_Hintergrund,
                           fg=Haupt.Textmanager_Textfarbe, wraplength=560)
        ErrorLabel.place(x=0, y=80)

def Grundstellung(Livestreamaktualisierung, Kamera_stellung):
    global Darf_ich_Kinderlied, Darf_ich_Busslied, Darf_ich_Abendmahlslied, Darf_ich_Busslied, Darf_ich_Einganslied, Darf_ich_Textwortlied, Darf_ich_Amtswechsel, Darf_ich_Schlusslied, Darf_ich_Zusatzlied1, Darf_ich_Zusatzlied2, Darf_ich_Zusatzlied3, Darf_ich_Zusatzlied4, Anzeige
    Anzeige = False
    Darf_ich_Einganslied = False
    Darf_ich_Textwortlied = False
    Darf_ich_Amtswechsel = False
    Darf_ich_Kinderlied = False
    Darf_ich_Busslied = False
    Darf_ich_Abendmahlslied = False
    Darf_ich_Schlusslied = False
    Darf_ich_Zusatzlied1 =False
    Darf_ich_Zusatzlied2 = False
    Darf_ich_Zusatzlied3 = False
    Darf_ich_Zusatzlied4 = False
    try:
        Texteingabe.destroy()
    except:
        pass
    try:
        Verseingabe.destroy()
    except:
        pass
    try:
        opt.destroy()
    except:
        pass
    Haupt.Einganslied.Grafikresetten()
    Haupt.Textwortlied.Grafikresetten()
    Haupt.Amtswechsellied.Grafikresetten()
    Haupt.Bussslied.Grafikresetten()
    Haupt.Abendmahlslied.Grafikresetten()
    Haupt.Schlusslied.Grafikresetten()
    Haupt.Kinderlied.Grafikresetten()
    Haupt.Zusatzlied1.Grafikresetten()
    Haupt.Zusatzlied2.Grafikresetten()
    Haupt.Zusatzlied3.Grafikresetten()
    Haupt.Zusatzlied4.Grafikresetten()
    Haupt.Textwortentry.config(bg=Haupt.Textmanager_Hintergrund, fg=Haupt.Textmanager_Textfarbe)
    Haupt.Text_Anzeige_Label.config(text="")
    Haupt.Textmanager.update()

    if Livestreamaktualisierung:
        keyboard.press("0")
        time.sleep(0.5)
        keyboard.release("0")
        time.sleep(0.5)
        keyboard.press("1")
        time.sleep(0.5)
        keyboard.release("1")
    if Kamera_stellung:
        if Kamera_Steuerung.Ist_Kamer_aktiv:
            Kamera_Steuerung.Kamera.goto_preset(1)



def vorherübergabeTextandiewand():
    global Datenfürliedanderwand, Wieoft, voherliedzwischensehne, lesteslied, Wieoftlied
    Datenfürliedanderwand = []
    Grundstellung(False, False)
    if Wieoftlied == 0:
        Wieoftlied = 1
    Nächstelied()

def Anfang():
    global Datenfürliedanderwand, Wieoft, voherliedzwischensehne, lesteslied, Wieoftlied
    Datenfürliedanderwand = []
    Wieoft = 0
    Wieoftlied = 1
    Haupt.Text_Anzeige_Label.config(text="")
    Datenfürliedanderwand = Haupt.Einganslied.Daten_fürTextanderwand.copy()
    Haupt.Einganslied.Liedtextanzeige.config(bg="orange")
    Haupt.Textmanager.update()
    Grundstellung(True, True)

def Eingasliedübergabefirst():
    global Datenfürliedanderwand, Wieoft, Wieoftlied, lesteslied, Darf_ich_Einganslied
    Datenfürliedanderwand = Haupt.Einganslied.Daten_fürTextanderwand.copy()
    Wieoftlied = int(Haupt.Einganslied.Daten_fürTextanderwand[0])
    Wieoft = 0
    Grundstellung(False, False)
    Haupt.Einganslied.Liedtextanzeige.config(bg="orange")
    lesteslied = False
    if len(Datenfürliedanderwand[3]) == 0:
        Eingabe()
        Darf_ich_Einganslied = True

def Eingasliedübergabe():
    global Datenfürliedanderwand, Wieoft, Wieoftlied, lesteslied, Darf_ich_Einganslied
    Datenfürliedanderwand = Haupt.Einganslied.Daten_fürTextanderwand.copy()
    Wieoftlied = int(Haupt.Einganslied.Daten_fürTextanderwand[0])
    Wieoft = 0
    Grundstellung(True, True)
    Haupt.Einganslied.Liedtextanzeige.config(bg="orange")
    lesteslied = False
    if len(Datenfürliedanderwand[3]) == 0:
        Eingabe()
        Darf_ich_Einganslied = True

def Textwortliedübergabe():
    global Datenfürliedanderwand, Wieoft, Wieoftlied, lesteslied, Darf_ich_Textwortlied
    Datenfürliedanderwand = Haupt.Textwortlied.Daten_fürTextanderwand.copy()
    Wieoftlied = int(Haupt.Textwortlied.Daten_fürTextanderwand[0])
    Wieoft = 0
    Grundstellung(True, True)
    Haupt.Textwortlied.Liedtextanzeige.config(bg="orange")
    lesteslied = False
    if len(Datenfürliedanderwand[3]) == 0:
        Eingabe()
        Darf_ich_Textwortlied = True


def Amtswechseliedübergabe():
    global Datenfürliedanderwand, Wieoft, Wieoftlied, lesteslied, Darf_ich_Amtswechsel
    Datenfürliedanderwand = Haupt.Amtswechsellied.Daten_fürTextanderwand.copy()
    Wieoftlied = int(Haupt.Amtswechsellied.Daten_fürTextanderwand[0])
    Wieoft = 0
    Grundstellung(True, True)
    Haupt.Amtswechsellied.Liedtextanzeige.config(bg="orange")
    lesteslied = False
    if len(Datenfürliedanderwand[3]) == 0:
        Eingabe()
        Darf_ich_Amtswechsel = True

def Bußliedübergabe():
    global Datenfürliedanderwand, Wieoft, Wieoftlied, lesteslied, Darf_ich_Busslied
    Datenfürliedanderwand = Haupt.Bussslied.Daten_fürTextanderwand.copy()
    Wieoftlied = int(Haupt.Bussslied.Daten_fürTextanderwand[0])
    Wieoft = 0
    Grundstellung(True, True)
    Haupt.Bussslied.Liedtextanzeige.config(bg="orange")
    lesteslied = False
    if len(Datenfürliedanderwand[3]) == 0:
        Eingabe()
        Darf_ich_Busslied = True

def Abendmahlsliedübergabe():
    global Datenfürliedanderwand, Wieoft, Wieoftlied, lesteslied, Darf_ich_Abendmahlslied
    Datenfürliedanderwand = Haupt.Abendmahlslied.Daten_fürTextanderwand.copy()
    Wieoftlied = int(Haupt.Abendmahlslied.Daten_fürTextanderwand[0])
    Wieoft = 0
    Grundstellung(True, True)
    Haupt.Abendmahlslied.Liedtextanzeige.config(bg="orange")
    lesteslied = False
    if len(Datenfürliedanderwand[3]) == 0:
        Eingabe()
        Darf_ich_Abendmahlslied = True
    

def Schlussliedübergabe():
    global Datenfürliedanderwand, Wieoftlied, Wieoft, lesteslied, Darf_ich_Schlusslied
    Datenfürliedanderwand = Haupt.Schlusslied.Daten_fürTextanderwand.copy()
    Wieoftlied = int(Haupt.Schlusslied.Daten_fürTextanderwand[0])
    Wieoft = 0
    Grundstellung(True, True)
    Haupt.Schlusslied.Liedtextanzeige.config(bg="orange")
    lesteslied = False
    if len(Datenfürliedanderwand[3]) == 0:
        Eingabe()
        Darf_ich_Schlusslied = True


def Kinderliedübergabe():
    global Datenfürliedanderwand, Wieoftlied, Wieoft, lesteslied, Darf_ich_Kinderlied
    Datenfürliedanderwand = Haupt.Kinderlied.Daten_fürTextanderwand.copy()
    Wieoftlied = int(Haupt.Kinderlied.Daten_fürTextanderwand[0])
    Wieoft = 0
    Grundstellung(True, True)
    Haupt.Kinderlied.Liedtextanzeige.config(bg="orange")
    lesteslied = False
    if len(Datenfürliedanderwand[3]) == 0:
        Eingabe()
        Darf_ich_Kinderlied = True


def Zusatzlied1übergabe():
    global Datenfürliedanderwand, Wieoftlied, Wieoft, lesteslied, Darf_ich_Zusatzlied1
    Datenfürliedanderwand = Haupt.Zusatzlied1.Daten_fürTextanderwand.copy()
    Wieoftlied = int(Haupt.Zusatzlied1.Daten_fürTextanderwand[0])
    Wieoft = 0
    Grundstellung(True, True)
    Haupt.Zusatzlied1.Liedtextanzeige.config(bg="orange")
    lesteslied = False
    if len(Datenfürliedanderwand[3]) == 0:
        Eingabe()
        Darf_ich_Zusatzlied1 = True

def Zusatzlied2übergabe():
    global Datenfürliedanderwand, Wieoftlied, Wieoft, lesteslied, Darf_ich_Zusatzlied2
    Datenfürliedanderwand = Haupt.Zusatzlied2.Daten_fürTextanderwand.copy()
    Wieoftlied = int(Haupt.Zusatzlied2.Daten_fürTextanderwand[0])
    Wieoft = 0
    Grundstellung(True, True)
    Haupt.Zusatzlied2.Liedtextanzeige.config(bg="orange")
    lesteslied = False
    if len(Datenfürliedanderwand[3]) == 0:
        Eingabe()
        Darf_ich_Zusatzlied2 = True

def Zusatzlied3übergabe():
    global Datenfürliedanderwand, Wieoftlied, Wieoft, lesteslied, Darf_ich_Zusatzlied3
    Datenfürliedanderwand = Haupt.Zusatzlied3.Daten_fürTextanderwand.copy()
    Wieoftlied = int(Haupt.Zusatzlied3.Daten_fürTextanderwand[0])
    Wieoft = 0
    Grundstellung(True, True)
    Haupt.Zusatzlied3.Liedtextanzeige.config(bg="orange")
    lesteslied = False
    if len(Datenfürliedanderwand[3]) == 0:
        Eingabe()
        Darf_ich_Zusatzlied3 = True

def Zusatzlied4übergabe():
    global Datenfürliedanderwand, Wieoftlied, Wieoft, lesteslied, Darf_ich_Zusatzlied4
    Datenfürliedanderwand = Haupt.Zusatzlied4.Daten_fürTextanderwand.copy()
    Wieoftlied = int(Haupt.Zusatzlied4.Daten_fürTextanderwand[0])
    Wieoft = 0
    Grundstellung(True, True)
    Haupt.Zusatzlied4.Liedtextanzeige.config(bg="orange")
    lesteslied = False
    if len(Datenfürliedanderwand[3]) == 0:
        Eingabe()
        Darf_ich_Zusatzlied4 = True

def Textwortübergabe():
    global Datenfürliedanderwand, Wieoftlied, Wieoft, lesteslied
    Datenfürliedanderwand = Haupt.Textwortübergabedaten.copy()
    Wieoftlied = int(Haupt.Textwortübergabedaten[0])
    Wieoft = 0
    Grundstellung(True, True)
    Haupt.Textwortentry.config(bg="orange")
    lesteslied = False

def Eingabe():
    global Texteingabe, Verseingabe, clicked, opt
    Texteingabe = tkinter.Entry(Haupt.Textmanager, font=("Helvetica", 24), width=4)
    Texteingabe.place(x=30, y=600)
    Verseingabe = tkinter.Entry(Haupt.Textmanager, font=("Helvetica", 24), width=7)
    Verseingabe.place(x=30, y=645)
    clicked = Haupt.StringVar()
    clicked.set(Haupt.Buch_Listen[0])
    opt = Haupt.OptionMenu(Haupt.Textmanager, clicked, *Haupt.Buch_Listen)
    opt.config(width=12, font=('Helvetica', 12), bg=Haupt.Textmanager_Hintergrund, fg=Haupt.Textmanager_Textfarbe)
    opt.place(x=170, y=630)

def Nächstelied():
    global Wieoftlied, Datenfürliedanderwand, Wieoft, lesteslied, Darf_ich_Amtswechsel, Darf_ich_Einganslied, Darf_ich_Textwortlied, Darf_ich_Abendmahlslied, Darf_ich_Schlusslied, Darf_ich_Zusatzlied1, Darf_ich_Zusatzlied2, Darf_ich_Zusatzlied3, Darf_ich_Zusatzlied4, Darf_ich_Busslied, Darf_ich_Kinderlied
    Wieoft = 0
    Grundstellung(True, True)
    Datenfürliedanderwand = []
    if int(Haupt.Einganslied.Daten_fürTextanderwand[0]) == int(Wieoftlied):
        Haupt.Einganslied.Liedtextanzeige.config(bg="orange")
        Datenfürliedanderwand = Haupt.Einganslied.Daten_fürTextanderwand.copy()
        if len(Datenfürliedanderwand[3]) == 0:
            Eingabe()
            Darf_ich_Einganslied = True
    elif int(Haupt.Textwortübergabedaten[0]) == int(Wieoftlied):
        Haupt.Textwortentry.config(bg="orange")
        Datenfürliedanderwand = Haupt.Textwortübergabedaten.copy()
    elif int(Haupt.Textwortlied.Daten_fürTextanderwand[0]) == int(Wieoftlied):
        Haupt.Textwortlied.Liedtextanzeige.config(bg="orange")
        Datenfürliedanderwand = Haupt.Textwortlied.Daten_fürTextanderwand.copy()
        if len(Datenfürliedanderwand[3]) == 0:
            Eingabe()
            Darf_ich_Textwortlied = True
    elif int(Haupt.Amtswechsellied.Daten_fürTextanderwand[0]) == int(Wieoftlied):
        Haupt.Amtswechsellied.Liedtextanzeige.config(bg="orange")
        Datenfürliedanderwand = Haupt.Amtswechsellied.Daten_fürTextanderwand.copy()
        if len(Datenfürliedanderwand[3]) == 0:
            Eingabe()
            Darf_ich_Amtswechsel = True
    elif int(Haupt.Bussslied.Daten_fürTextanderwand[0]) == int(Wieoftlied):
        Haupt.Bussslied.Liedtextanzeige.config(bg="orange")
        Datenfürliedanderwand = Haupt.Bussslied.Daten_fürTextanderwand.copy()
        if len(Datenfürliedanderwand[3]) == 0:
            Eingabe()
            Darf_ich_Busslied = True
    elif int(Haupt.Abendmahlslied.Daten_fürTextanderwand[0]) == int(Wieoftlied):
        Haupt.Abendmahlslied.Liedtextanzeige.config(bg="orange")
        Datenfürliedanderwand = Haupt.Abendmahlslied.Daten_fürTextanderwand.copy()
        if len(Datenfürliedanderwand[3]) == 0:
            Eingabe()
            Darf_ich_Abendmahlslied = True
    elif int(Haupt.Schlusslied.Daten_fürTextanderwand[0]) == int(Wieoftlied):
        Haupt.Schlusslied.Liedtextanzeige.config(bg="orange")
        Datenfürliedanderwand = Haupt.Schlusslied.Daten_fürTextanderwand.copy()
        if len(Datenfürliedanderwand[3]) == 0:
            Eingabe()
            Darf_ich_Schlusslied = True
    elif int(Haupt.Kinderlied.Daten_fürTextanderwand[0]) == int(Wieoftlied):
        Haupt.Kinderlied.Liedtextanzeige.config(bg="orange")
        Datenfürliedanderwand = Haupt.Kinderlied.Daten_fürTextanderwand.copy()
        if len(Datenfürliedanderwand[3]) == 0:
            Eingabe()
            Darf_ich_Kinderlied = True
    elif int(Haupt.Zusatzlied1.Daten_fürTextanderwand[0]) == int(Wieoftlied):
        Haupt.Zusatzlied1.Liedtextanzeige.config(bg="orange")
        Datenfürliedanderwand = Haupt.Zusatzlied1.Daten_fürTextanderwand.copy()
        if len(Datenfürliedanderwand[3]) == 0:
            Eingabe()
            Darf_ich_Zusatzlied1 = True
    elif int(Haupt.Zusatzlied2.Daten_fürTextanderwand[0]) == int(Wieoftlied):
        Haupt.Zusatzlied2.Liedtextanzeige.config(bg="orange")
        Datenfürliedanderwand = Haupt.Zusatzlied2.Daten_fürTextanderwand.copy()
        if len(Datenfürliedanderwand[3]) == 0:
            Eingabe()
            Darf_ich_Zusatzlied2 = True
    elif int(Haupt.Zusatzlied3.Daten_fürTextanderwand[0]) == int(Wieoftlied):
        Haupt.Zusatzlied3.Liedtextanzeige.config(bg="orange")
        Datenfürliedanderwand = Haupt.Zusatzlied3.Daten_fürTextanderwand.copy()
        if len(Datenfürliedanderwand[3]) == 0:
            Eingabe()
            Darf_ich_Zusatzlied3 = True
    elif int(Haupt.Zusatzlied4.Daten_fürTextanderwand[0]) == int(Wieoftlied):
        Haupt.Zusatzlied4.Liedtextanzeige.config(bg="orange")
        Datenfürliedanderwand = Haupt.Zusatzlied4.Daten_fürTextanderwand.copy()
        if len(Datenfürliedanderwand[3]) == 0:
            Eingabe()
            Darf_ich_Zusatzlied4 = True
    else:
        Haupt.Text_Anzeige_Label.config(text="")
        lesteslied = True
    Haupt.Textmanager.update()


def Voeherlied():
    global Wieoftlied, Wieoft, voherliedzwischensehne, AusganneVerse, Datenfürliedanderwand
    try:
        if Wieoftlied > 1:
            Wieoftlied = Wieoftlied - 1
            vorherübergabeTextandiewand()
            Verinbterprätator(Datenfürliedanderwand[3], Datenfürliedanderwand[2], Datenfürliedanderwand[4])
            Wieoft = len(AusganneVerse) + 1
            Wieoft = Wieoft - 2
            Verse(Datenfürliedanderwand[3],AusganneVerse[Wieoft],Datenfürliedanderwand[2])
            Wieoft = Wieoft + 1
        else:
            Nächstelied()
    except:
        pass

def Versvorher():
    global Wieoft, voherliedzwischensehne, lesteslied, Wieoftlied
    Grundstellung(False, True)
    if lesteslied:
        lesteslied = False
        Wieoftlied = Wieoftlied - 1
        vorherübergabeTextandiewand()
        Verinbterprätator(Datenfürliedanderwand[3], Datenfürliedanderwand[2], Datenfürliedanderwand[4])
        Wieoft = len(AusganneVerse) + 1
    if not voherliedzwischensehne:
        Wieoft = Wieoft - 2
        Liedgebe()
    voherliedzwischensehne = False

def Liedgebe():
    global Wieoft, Wieoftlied, Datenfürliedanderwand, voherliedzwischensehne, lesteslied
    if not lesteslied:
        if Wieoftlied == 0:
            Wieoft = 0
            Datenfürliedanderwand = Haupt.Einganslied.Daten_fürTextanderwand.copy()
            Wieoftlied = 1
            Haupt.Textmanager.update()
        spontandaten(Wieoftlied)
        Verinbterprätator(Datenfürliedanderwand[3], Datenfürliedanderwand[2], Datenfürliedanderwand[4])
        Aktuelllervers = len(AusganneVerse)
        if int(Wieoft) == int(Aktuelllervers):
            Wieoftlied = Wieoftlied + 1
            AkutellerText = ""
            Haupt.Text_Anzeige_Label.config(text=AkutellerText)
            Nächstelied()
            Haupt.Textmanager.update()
        elif int(Wieoft) == - 1:
            AkutellerText = ""
            Haupt.Text_Anzeige_Label.config(text=AkutellerText)
            Wieoft = 0
            Nächstelied()
            Haupt.Textmanager.update()
            if Wieoftlied == 1:
                Voeherlied()
                Haupt.Textmanager.update()
        elif int(Wieoft) == - 2:
            Wieoft = 0
            Voeherlied()
            Haupt.Textmanager.update()
        else:
            Verse(Datenfürliedanderwand[3],AusganneVerse[Wieoft],Datenfürliedanderwand[2])
            Wieoft = Wieoft + 1
            Haupt.Textmanager.update()

def spontandaten(Liedposition):
    global Datenfürliedanderwand
    if int(Haupt.Einganslied.Daten_fürTextanderwand[0]) == int(Liedposition):
        Datenfürliedanderwand = Haupt.Einganslied.Daten_fürTextanderwand.copy()
    elif int(Haupt.Textwortlied.Daten_fürTextanderwand[0]) == int(Liedposition):
        Datenfürliedanderwand = Haupt.Textwortlied.Daten_fürTextanderwand.copy()
    elif int(Haupt.Amtswechsellied.Daten_fürTextanderwand[0]) == int(Liedposition):
        Datenfürliedanderwand = Haupt.Amtswechsellied.Daten_fürTextanderwand.copy()
    elif int(Haupt.Kinderlied.Daten_fürTextanderwand[0]) == int(Liedposition):
        Datenfürliedanderwand = Haupt.Kinderlied.Daten_fürTextanderwand.copy()
    elif int(Haupt.Bussslied.Daten_fürTextanderwand[0]) == int(Liedposition):
        Datenfürliedanderwand = Haupt.Bussslied.Daten_fürTextanderwand.copy()
    elif int(Haupt.Abendmahlslied.Daten_fürTextanderwand[0]) == int(Liedposition):
        Datenfürliedanderwand = Haupt.Abendmahlslied.Daten_fürTextanderwand.copy()
    elif int(Haupt.Schlusslied.Daten_fürTextanderwand[0]) == int(Liedposition):
        Datenfürliedanderwand = Haupt.Schlusslied.Daten_fürTextanderwand.copy()
    elif int(Haupt.Zusatzlied1.Daten_fürTextanderwand[0]) == int(Liedposition):
        Datenfürliedanderwand = Haupt.Zusatzlied1.Daten_fürTextanderwand.copy()
    elif int(Haupt.Zusatzlied2.Daten_fürTextanderwand[0]) == int(Liedposition):
        Datenfürliedanderwand = Haupt.Zusatzlied2.Daten_fürTextanderwand.copy()
    elif int(Haupt.Zusatzlied3.Daten_fürTextanderwand[0]) == int(Liedposition):
        Datenfürliedanderwand = Haupt.Zusatzlied3.Daten_fürTextanderwand.copy()
    elif int(Haupt.Zusatzlied4.Daten_fürTextanderwand[0]) == int(Liedposition):
        Datenfürliedanderwand = Haupt.Zusatzlied4.Daten_fürTextanderwand.copy()


def Eingabelöschen():
        global Darf_ich_Kinderlied, Darf_ich_Busslied, Darf_ich_Abendmahlslied, Darf_ich_Busslied, Darf_ich_Einganslied, Darf_ich_Textwortlied, Darf_ich_Amtswechsel, Darf_ich_Schlusslied, Darf_ich_Zusatzlied1, Darf_ich_Zusatzlied2, Darf_ich_Zusatzlied3, Darf_ich_Zusatzlied4
        Darf_ich_Einganslied = False
        Darf_ich_Textwortlied = False
        Darf_ich_Amtswechsel = False
        Darf_ich_Kinderlied = False
        Darf_ich_Busslied = False
        Darf_ich_Abendmahlslied = False
        Darf_ich_Schlusslied = False
        Darf_ich_Zusatzlied1 =False
        Darf_ich_Zusatzlied2 = False
        Darf_ich_Zusatzlied3 = False
        Darf_ich_Zusatzlied4 = False
        try:
            Texteingabe.destroy()
        except:
            pass
        try:
            Verseingabe.destroy()
        except:
            pass
        try:
            opt.destroy()
        except:
            pass


def optisches_fedback(Liedposition):
    if int(Haupt.Einganslied.Daten_fürTextanderwand[0]) == int(Liedposition):
        Eingabelöschen()
        Haupt.Einganslied.Liedtextanzeige.config(bg="green")
        Haupt.Textmanager.update()
        if len(Haupt.Einganslied.Daten_fürTextanderwand[3]) > 0:
            keyboard.press("F24")
            time.sleep(0.5)
            keyboard.release("F24")
            time.sleep(0.5)
            keyboard.press("1")
            time.sleep(0.5)
            keyboard.release("1")
        if Kamera_Steuerung.Ist_Kamer_aktiv:
                Haupt.Einganslied.Kamerapositiondef()
                Kamera_Steuerung.Kamera.goto_preset(Haupt.Einganslied.Kameraposition)
                



    elif int(Haupt.Textwortübergabedaten[0]) == int(Liedposition):
        Eingabelöschen()
        Haupt.Textwortentry.config(bg="green")
        Haupt.Textmanager.update()
        keyboard.press("F13")
        time.sleep(0.5)
        keyboard.release("F13")
        time.sleep(0.5)
        keyboard.press("1")
        time.sleep(0.5)
        keyboard.release("1")
    
    elif int(Haupt.Amtswechsellied.Daten_fürTextanderwand[0]) == int(Liedposition):
        Eingabelöschen()
        Haupt.Amtswechsellied.Liedtextanzeige.config(bg="green")
        Haupt.Textmanager.update()
        if len(Haupt.Amtswechsellied.Daten_fürTextanderwand[3]) > 0:
            keyboard.press("F23")
            time.sleep(0.5)
            keyboard.release("F23")
            time.sleep(0.5)
            keyboard.press("1")
            time.sleep(0.5)
            keyboard.release("1")
        if Kamera_Steuerung.Ist_Kamer_aktiv:
            try:
                Haupt.Amtswechsellied.Kamerapositiondef()
                Kamera_Steuerung.Kamera.goto_preset(Haupt.Amtswechsellied.Kameraposition)
            except:
                print("error kei1ne Kamera")
    
    elif int(Haupt.Textwortlied.Daten_fürTextanderwand[0]) == int(Liedposition):
        Eingabelöschen()
        Haupt.Textwortlied.Liedtextanzeige.config(bg="green")
        Haupt.Textmanager.update()
        if len(Haupt.Textwortlied.Daten_fürTextanderwand[3]) > 0:
            keyboard.press("F22")
            time.sleep(0.5)
            keyboard.release("F22")
            time.sleep(0.5)
            keyboard.press("1")
            time.sleep(0.5)
            keyboard.release("1")
        if Kamera_Steuerung.Ist_Kamer_aktiv:
            try:
                Haupt.Textwortlied.Kamerapositiondef()
                Kamera_Steuerung.Kamera.goto_preset(Haupt.Textwortlied.Kameraposition)
            except:
                print("error kei1ne Kamera")

    elif int(Haupt.Bussslied.Daten_fürTextanderwand[0]) == int(Liedposition):
        Eingabelöschen()
        Haupt.Bussslied.Liedtextanzeige.config(bg="green")
        Haupt.Textmanager.update()
        if len(Haupt.Bussslied.Daten_fürTextanderwand[3]) > 0:
            keyboard.press("F21")
            time.sleep(0.5)
            keyboard.release("F21")
            time.sleep(0.5)
            keyboard.press("1")
            time.sleep(0.5)
            keyboard.release("1")
        if Kamera_Steuerung.Ist_Kamer_aktiv:
            try:
                Haupt.Bussslied.Kamerapositiondef()
                Kamera_Steuerung.Kamera.goto_preset(Haupt.Bussslied.Kameraposition)
            except:
                print("error kei1ne Kamera")

    elif int(Haupt.Abendmahlslied.Daten_fürTextanderwand[0]) == int(Liedposition):
        Eingabelöschen()
        Haupt.Abendmahlslied.Liedtextanzeige.config(bg="green")
        Haupt.Textmanager.update()
        if len(Haupt.Abendmahlslied.Daten_fürTextanderwand[3]) > 0:
            keyboard.press("F20")
            time.sleep(0.5)
            keyboard.release("F20")
            time.sleep(0.5)
            keyboard.press("1")
            time.sleep(0.5)
            keyboard.release("1")
        if Kamera_Steuerung.Ist_Kamer_aktiv:
            try:
                Haupt.Abendmahlslied.Kamerapositiondef()
                Kamera_Steuerung.Kamera.goto_preset(Haupt.Abendmahlslied.Kameraposition)
            except:
                print("error kei1ne Kamera")

    elif int(Haupt.Schlusslied.Daten_fürTextanderwand[0]) == int(Liedposition):
        Eingabelöschen()
        Haupt.Schlusslied.Liedtextanzeige.config(bg="green")
        Haupt.Textmanager.update()
        if len(Haupt.Schlusslied.Daten_fürTextanderwand[3]) > 0:
            keyboard.press("F19")
            time.sleep(0.5)
            keyboard.release("F19")
            time.sleep(0.5)
            keyboard.press("1")
            time.sleep(0.5)
            keyboard.release("1")
        if Kamera_Steuerung.Ist_Kamer_aktiv:
            try:
                Haupt.Schlusslied.Kamerapositiondef()
                Kamera_Steuerung.Kamera.goto_preset(Haupt.Schlusslied.Kameraposition)
            except:
                print("error kei1ne Kamera")

    elif int(Haupt.Kinderlied.Daten_fürTextanderwand[0]) == int(Liedposition):
        Eingabelöschen()
        Haupt.Kinderlied.Liedtextanzeige.config(bg="green")
        Haupt.Textmanager.update()
        if len(Haupt.Kinderlied.Daten_fürTextanderwand[3]) > 0:
            keyboard.press("F18")
            time.sleep(0.5)
            keyboard.release("F18")
            time.sleep(0.5)
            keyboard.press("1")
            time.sleep(0.5)
            keyboard.release("1")
        if Kamera_Steuerung.Ist_Kamer_aktiv:
            try:
                Haupt.Kinderlied.Kamerapositiondef()
                Kamera_Steuerung.Kamera.goto_preset(Haupt.Kinderlied.Kameraposition)
            except:
                print("error kei1ne Kamera")

    elif int(Haupt.Zusatzlied1.Daten_fürTextanderwand[0]) == int(Liedposition):
        Eingabelöschen()
        Haupt.Zusatzlied1.Liedtextanzeige.config(bg="green")
        Haupt.Textmanager.update()
        if len(Haupt.Zusatzlied1.Daten_fürTextanderwand[3]) > 0:
            keyboard.press("F17")
            time.sleep(0.5)
            keyboard.release("F17")
            time.sleep(0.5)
            keyboard.press("1")
            time.sleep(0.5)
            keyboard.release("1")
        if Kamera_Steuerung.Ist_Kamer_aktiv:
            try:
                Haupt.Zusatzlied1.Kamerapositiondef()
                Kamera_Steuerung.Kamera.goto_preset(Haupt.Zusatzlied1.Kameraposition)
            except:
                print("error kei1ne Kamera")

    elif int(Haupt.Zusatzlied2.Daten_fürTextanderwand[0]) == int(Liedposition):
        Eingabelöschen()
        Haupt.Zusatzlied2.Liedtextanzeige.config(bg="green")
        Haupt.Textmanager.update()
        if len(Haupt.Zusatzlied2.Daten_fürTextanderwand[3]) > 0:
            keyboard.press("F16")
            time.sleep(0.5)
            keyboard.release("F16")
            time.sleep(0.5)
            keyboard.press("1")
            time.sleep(0.5)
            keyboard.release("1")
        if Kamera_Steuerung.Ist_Kamer_aktiv:
            try:
                Haupt.Zusatzlied2.Kamerapositiondef()
                Kamera_Steuerung.Kamera.goto_preset(Haupt.Zusatzlied2.Kameraposition)
            except:
                print("error kei1ne Kamera")

    elif int(Haupt.Zusatzlied3.Daten_fürTextanderwand[0]) == int(Liedposition):
        Eingabelöschen()
        Haupt.Zusatzlied3.Liedtextanzeige.config(bg="green")
        Haupt.Textmanager.update()
        if len(Haupt.Zusatzlied3.Daten_fürTextanderwand[3]) > 0:
            keyboard.press("F15")
            time.sleep(0.5)
            keyboard.release("F15")
            time.sleep(0.5)
            keyboard.press("1")
            time.sleep(0.5)
            keyboard.release("1")
        if Kamera_Steuerung.Ist_Kamer_aktiv:
            try:
                Haupt.Zusatzlied3.Kamerapositiondef()
                Kamera_Steuerung.Kamera.goto_preset(Haupt.Zusatzlied3.Kameraposition)
            except:
                print("error kei1ne Kamera")

    elif int(Haupt.Zusatzlied4.Daten_fürTextanderwand[0]) == int(Liedposition):
        Eingabelöschen()
        Haupt.Zusatzlied4.Liedtextanzeige.config(bg="green")
        Haupt.Textmanager.update()
        if len(Haupt.Zusatzlied4.Daten_fürTextanderwand[3]) > 0:
            keyboard.press("F14")
            time.sleep(0.5)
            keyboard.release("F14")
            time.sleep(0.5)
            keyboard.press("1")
            time.sleep(0.5)
            keyboard.release("1")
        if Kamera_Steuerung.Ist_Kamer_aktiv:
            try:
                Haupt.Zusatzlied4.Kamerapositiondef()
                Kamera_Steuerung.Kamera.goto_preset(Haupt.Zusatzlied4.Kameraposition)
            except:
                print("error kei1ne Kamera")


def Verse(Hallo123,Wieoft,WelchesBuch):
    global Anzeige
    Anzeige = True
    try:
        Texttest = open(f"C:\\Users\\{Haupt.Dateiort}\\Desktop\\Lieder\\Buch\\{WelchesBuch}\\{Hallo123} Vers {Wieoft}.txt", "r", encoding="utf-8")
        Aktuellertext = Texttest.read()
        Haupt.Text_Anzeige_Label.config(text=Aktuellertext)
        Haupt.Textmanager.update()
    except FileNotFoundError:
        Errorbild = tkinter.Toplevel(Haupt.Textmanager)
        Errorbild.geometry("560x350+500+400")
        Errorbild.config(bg=Haupt.Textmanager_Hintergrund)
        Error = tkinter.Label(Errorbild, font=("Helvetica", 40),
                      text="Error", bg=Haupt.Textmanager_Hintergrund,
                      fg=Haupt.Textmanager_Textfarbe, wraplength=560)
        Error.place(x=210, y=0)
        ErrorLabel = tkinter.Label(Errorbild, font=("Helvetica", 20),
                           text=f"Das Lied {Hallo123} im Buch {WelchesBuch} Vers {Wieoft} Exesitert nicht", bg=Haupt.Textmanager_Hintergrund,
                           fg=Haupt.Textmanager_Textfarbe, wraplength=560)
        ErrorLabel.place(x=0, y=80)
    optisches_fedback(Wieoftlied)
