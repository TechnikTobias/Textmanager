import Haupt
import tkinter

Wieoft = 0
Wieoftlied = 1
voherliedzwischensehne = False
lesteslied = False

def Verinbterprätator(Welcheart,WelchesBuch,WelcherVers):
    try:
        global AusganneVerse
        datenteil1 = []
        AusganneVerse = []
        if WelcherVers == "":
            AusganneVerse = []
            Wieoft = 1
            while True:
                Verzanzahl = open(
                    "C:\\Users\\" + Haupt.Dateiort + "\\Desktop\\Lieder\\Versanzahl\\" + WelchesBuch + "\\" + Welcheart + ".txt",
                    "r",
                    encoding="utf-8")
                Maxzahl = Verzanzahl.read()
                if Wieoft == int(Maxzahl) + 1:
                    break
                AusganneVerse = AusganneVerse + [Wieoft]
                Wieoft = int(Wieoft) + 1
        else:
            daten = WelcherVers.split(",")
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
        Verzanzahl = open(
            "C:\\Users\\" + Haupt.Dateiort + "\\Desktop\\Lieder\\Versanzahl\\" + WelchesBuch + "\\" + Welcheart + ".txt",
            "r",
            encoding="utf-8")
        Maxzahl = Verzanzahl.read()
        AusganneVerse.sort()
        if len(AusganneVerse) == 0:
            Sooft = 0
            Wieoft = 1
            while True:
                Verzanzahl = open(
                    "C:\\Users\\" + Haupt.Dateiort + "\\Desktop\\Lieder\\Versanzahl\\" + WelchesBuch + "\\" + Welcheart + ".txt",
                    "r",
                    encoding="utf-8")
                Maxzahl = Verzanzahl.read()
                if Sooft == int(Maxzahl) + 1:
                    break
                AusganneVerse = AusganneVerse + [Wieoft]
                Wieoft = int(Wieoft) + 1
                Sooft = Sooft + 1
        if len(AusganneVerse) == 1:
            if int(AusganneVerse[0]) > int(Maxzahl):
                AusganneVerse = Maxzahl
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
        if int(AusganneVerse[-1]) > int(Maxzahl):
            AusganneVerse.pop()
        # Filter, das niht mehr als es Verse gibt
    except FileNotFoundError:
        Errorbild = tkinter.Toplevel(Haupt.Textmanager)
        Errorbild.geometry("560x350+500+400")
        Errorbild.config(bg="black")
        Error = tkinter.Label(Errorbild, font=("Helvetica", 40),
                      text="Error", bg="black",
                      fg="green", wraplength=560)
        Error.place(x=210, y=0)
        ErrorLabel = tkinter.Label(Errorbild, font=("Helvetica", 20),
                           text="In 0rdner Lieder im Odner Versanzahl fehlt die Datei für das Lied "+Welcheart, bg="black",
                           fg="green", wraplength=560)
        ErrorLabel.place(x=0, y=80)

def Grundstellung():
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
    Haupt.Text_Anzeige_Label.config(text="")

def positionfeedback(Liedposition):
    if int(Haupt.Einganslied.Daten_fürTextanderwand[0]) == int(Liedposition):
        Haupt.Einganslied.Liedtextanzeige.config(bg="orange")
    elif int(Haupt.Amtswechsellied.Daten_fürTextanderwand[0]) == int(Liedposition):
        Haupt.Amtswechsellied.Liedtextanzeige.config(bg="orange")
    elif int(Haupt.Textwortlied.Daten_fürTextanderwand[0]) == int(Liedposition):
        Haupt.Textwortlied.Liedtextanzeige.config(bg="orange")
    elif int(Haupt.Bussslied.Daten_fürTextanderwand[0]) == int(Liedposition):
        Haupt.Bussslied.Liedtextanzeige.config(bg="orange")
    elif int(Haupt.Abendmahlslied.Daten_fürTextanderwand[0]) == int(Liedposition):
        Haupt.Abendmahlslied.Liedtextanzeige.config(bg="orange")
    elif int(Haupt.Schlusslied.Daten_fürTextanderwand[0]) == int(Liedposition):
        Haupt.Schlusslied.Liedtextanzeige.config(bg="orange")
    elif int(Haupt.Kinderlied.Daten_fürTextanderwand[0]) == int(Liedposition):
        Haupt.Kinderlied.Liedtextanzeige.config(bg="orange")
    elif int(Haupt.Zusatzlied1.Daten_fürTextanderwand[0]) == int(Liedposition):
        Haupt.Zusatzlied1.Liedtextanzeige.config(bg="orange")
    elif int(Haupt.Zusatzlied2.Daten_fürTextanderwand[0]) == int(Liedposition):
        Haupt.Zusatzlied2.Liedtextanzeige.config(bg="orange")
    elif int(Haupt.Zusatzlied3.Daten_fürTextanderwand[0]) == int(Liedposition):
        Haupt.Zusatzlied3.Liedtextanzeige.config(bg="orange")
    elif int(Haupt.Zusatzlied4.Daten_fürTextanderwand[0]) == int(Liedposition):
        Haupt.Zusatzlied4.Liedtextanzeige.config(bg="orange")

def vorherübergabeTextandiewand(Liedposition):
    global Datenfürliedanderwand, Wieoft, voherliedzwischensehne, lesteslied
    Datenfürliedanderwand = []
    Grundstellung()
    if int(Haupt.Einganslied.Daten_fürTextanderwand[0]) == int(Liedposition):
        Datenfürliedanderwand = Haupt.Einganslied.Daten_fürTextanderwand.copy()
        Haupt.Einganslied.Liedtextanzeige.config(bg="orange")
    elif int(Haupt.Amtswechsellied.Daten_fürTextanderwand[0]) == int(Liedposition):
        Haupt.Amtswechsellied.Liedtextanzeige.config(bg="orange")
        Datenfürliedanderwand = Haupt.Amtswechsellied.Daten_fürTextanderwand.copy()
    elif int(Haupt.Textwortlied.Daten_fürTextanderwand[0]) == int(Liedposition):
        Haupt.Textwortlied.Liedtextanzeige.config(bg="orange")
        Datenfürliedanderwand = Haupt.Textwortlied.Daten_fürTextanderwand.copy()
    elif int(Haupt.Bussslied.Daten_fürTextanderwand[0]) == int(Liedposition):
        Haupt.Bussslied.Liedtextanzeige.config(bg="orange")
        Datenfürliedanderwand = Haupt.Bussslied.Daten_fürTextanderwand.copy()
    elif int(Haupt.Abendmahlslied.Daten_fürTextanderwand[0]) == int(Liedposition):
        Haupt.Abendmahlslied.Liedtextanzeige.config(bg="orange")
        Datenfürliedanderwand = Haupt.Abendmahlslied.Daten_fürTextanderwand.copy()
    elif int(Haupt.Schlusslied.Daten_fürTextanderwand[0]) == int(Liedposition):
        Haupt.Schlusslied.Liedtextanzeige.config(bg="orange")
        Datenfürliedanderwand = Haupt.Schlusslied.Daten_fürTextanderwand.copy()
    elif int(Haupt.Kinderlied.Daten_fürTextanderwand[0]) == int(Liedposition):
        Haupt.Kinderlied.Liedtextanzeige.config(bg="orange")
        Datenfürliedanderwand = Haupt.Kinderlied.Daten_fürTextanderwand.copy()
    elif int(Haupt.Zusatzlied1.Daten_fürTextanderwand[0]) == int(Liedposition):
        Haupt.Zusatzlied1.Liedtextanzeige.config(bg="orange")
        Datenfürliedanderwand = Haupt.Zusatzlied1.Daten_fürTextanderwand.copy()
    elif int(Haupt.Zusatzlied2.Daten_fürTextanderwand[0]) == int(Liedposition):
        Haupt.Zusatzlied2.Liedtextanzeige.config(bg="orange")
        Datenfürliedanderwand = Haupt.Zusatzlied2.Daten_fürTextanderwand.copy()
    elif int(Haupt.Zusatzlied3.Daten_fürTextanderwand[0]) == int(Liedposition):
        Haupt.Zusatzlied3.Liedtextanzeige.config(bg="orange")
        Datenfürliedanderwand = Haupt.Zusatzlied3.Daten_fürTextanderwand.copy()
    elif int(Haupt.Zusatzlied4.Daten_fürTextanderwand[0]) == int(Liedposition):
        Haupt.Zusatzlied4.Liedtextanzeige.config(bg="orange")
        Datenfürliedanderwand = Haupt.Zusatzlied4.Daten_fürTextanderwand.copy()
    else:
        Haupt.Text_Anzeige_Label.config(text="")
        lesteslied = True

def Anfang():
    global Datenfürliedanderwand, Wieoft, voherliedzwischensehne, lesteslied, Wieoftlied
    Datenfürliedanderwand = []
    Grundstellung()
    Wieoft = 0
    Wieoftlied = 1
    Haupt.Text_Anzeige_Label.config(text="")
    if int(Haupt.Einganslied.Daten_fürTextanderwand[0]) == int(1):
        Datenfürliedanderwand = Haupt.Einganslied.Daten_fürTextanderwand.copy()
        Haupt.Einganslied.Liedtextanzeige.config(bg="orange")
    elif int(Haupt.Amtswechsellied.Daten_fürTextanderwand[0]) == int(1):
        Haupt.Amtswechsellied.Liedtextanzeige.config(bg="orange")
        Datenfürliedanderwand = Haupt.Amtswechsellied.Daten_fürTextanderwand.copy()
    elif int(Haupt.Textwortlied.Daten_fürTextanderwand[0]) == int(1):
        Haupt.Textwortlied.Liedtextanzeige.config(bg="orange")
        Datenfürliedanderwand = Haupt.Textwortlied.Daten_fürTextanderwand.copy()
    elif int(Haupt.Bussslied.Daten_fürTextanderwand[0]) == int(1):
        Haupt.Bussslied.Liedtextanzeige.config(bg="orange")
        Datenfürliedanderwand = Haupt.Bussslied.Daten_fürTextanderwand.copy()
    elif int(Haupt.Abendmahlslied.Daten_fürTextanderwand[0]) == int(1):
        Haupt.Abendmahlslied.Liedtextanzeige.config(bg="orange")
        Datenfürliedanderwand = Haupt.Abendmahlslied.Daten_fürTextanderwand.copy()
    elif int(Haupt.Schlusslied.Daten_fürTextanderwand[0]) == int(1):
        Haupt.Schlusslied.Liedtextanzeige.config(bg="orange")
        Datenfürliedanderwand = Haupt.Schlusslied.Daten_fürTextanderwand.copy()
    elif int(Haupt.Kinderlied.Daten_fürTextanderwand[0]) == int(1):
        Haupt.Kinderlied.Liedtextanzeige.config(bg="orange")
        Datenfürliedanderwand = Haupt.Kinderlied.Daten_fürTextanderwand.copy()
    elif int(Haupt.Zusatzlied1.Daten_fürTextanderwand[0]) == int(1):
        Haupt.Zusatzlied1.Liedtextanzeige.config(bg="orange")
        Datenfürliedanderwand = Haupt.Zusatzlied1.Daten_fürTextanderwand.copy()
    elif int(Haupt.Zusatzlied2.Daten_fürTextanderwand[0]) == int(1):
        Haupt.Zusatzlied2.Liedtextanzeige.config(bg="orange")
        Datenfürliedanderwand = Haupt.Zusatzlied2.Daten_fürTextanderwand.copy()
    elif int(Haupt.Zusatzlied3.Daten_fürTextanderwand[0]) == int(1):
        Haupt.Zusatzlied3.Liedtextanzeige.config(bg="orange")
        Datenfürliedanderwand = Haupt.Zusatzlied3.Daten_fürTextanderwand.copy()
    elif int(Haupt.Zusatzlied4.Daten_fürTextanderwand[0]) == int(1):
        Haupt.Zusatzlied4.Liedtextanzeige.config(bg="orange")
        Datenfürliedanderwand = Haupt.Zusatzlied4.Daten_fürTextanderwand.copy()


def Eingasliedübergabe():
    global Datenfürliedanderwand, Wieoft, Wieoftlied
    Datenfürliedanderwand = Haupt.Einganslied.Daten_fürTextanderwand.copy()
    Wieoftlied = int(Haupt.Einganslied.Daten_fürTextanderwand[0])
    Wieoft = 0
    Grundstellung()
    Haupt.Einganslied.Liedtextanzeige.config(bg="orange")


def Textwortliedübergabe():
    global Datenfürliedanderwand, Wieoft, Wieoftlied
    Datenfürliedanderwand = Haupt.Textwortlied.Daten_fürTextanderwand.copy()
    Wieoftlied = int(Haupt.Textwortlied.Daten_fürTextanderwand[0])
    Wieoft = 0
    Grundstellung()
    Haupt.Textwortlied.Liedtextanzeige.config(bg="orange")


def Amtswechseliedübergabe():
    global Datenfürliedanderwand, Wieoft, Wieoftlied
    Datenfürliedanderwand = Haupt.Amtswechsellied.Daten_fürTextanderwand.copy()
    Wieoftlied = int(Haupt.Amtswechsellied.Daten_fürTextanderwand[0])
    Wieoft = 0
    Grundstellung()
    Haupt.Amtswechsellied.Liedtextanzeige.config(bg="orange")

def Bußliedübergabe():
    global Datenfürliedanderwand, Wieoft, Wieoftlied
    Datenfürliedanderwand = Haupt.Bussslied.Daten_fürTextanderwand.copy()
    Wieoftlied = int(Haupt.Bussslied.Daten_fürTextanderwand[0])
    Wieoft = 0
    Grundstellung()
    Haupt.Bussslied.Liedtextanzeige.config(bg="orange")

def Abendmahlsliedübergabe():
    global Datenfürliedanderwand, Wieoft, Wieoftlied
    Datenfürliedanderwand = Haupt.Abendmahlslied.Daten_fürTextanderwand.copy()
    Wieoftlied = int(Haupt.Abendmahlslied.Daten_fürTextanderwand[0])
    Wieoft = 0
    Grundstellung()
    Haupt.Abendmahlslied.Liedtextanzeige.config(bg="orange")

def Schlussliedübergabe():
    global Datenfürliedanderwand, Wieoftlied, Wieoft
    Datenfürliedanderwand = Haupt.Schlusslied.Daten_fürTextanderwand.copy()
    Wieoftlied = int(Haupt.Schlusslied.Daten_fürTextanderwand[0])
    Wieoft = 0
    Grundstellung()
    Haupt.Schlusslied.Liedtextanzeige.config(bg="orange")

def Kinderliedübergabe():
    global Datenfürliedanderwand, Wieoftlied, Wieoft
    Datenfürliedanderwand = Haupt.Kinderlied.Daten_fürTextanderwand.copy()
    Wieoftlied = int(Haupt.Kinderlied.Daten_fürTextanderwand[0])
    Wieoft = 0
    Grundstellung()
    Haupt.Kinderlied.Liedtextanzeige.config(bg="orange")

def Zusatzlied1übergabe():
    global Datenfürliedanderwand, Wieoftlied, Wieoft
    Datenfürliedanderwand = Haupt.Zusatzlied1.Daten_fürTextanderwand.copy()
    Wieoftlied = int(Haupt.Zusatzlied1.Daten_fürTextanderwand[0])
    Wieoft = 0
    Grundstellung()
    Haupt.Zusatzlied1.Liedtextanzeige.config(bg="orange")

def Zusatzlied2übergabe():
    global Datenfürliedanderwand, Wieoftlied, Wieoft
    Datenfürliedanderwand = Haupt.Zusatzlied2.Daten_fürTextanderwand.copy()
    Wieoftlied = int(Haupt.Zusatzlied2.Daten_fürTextanderwand[0])
    Wieoft = 0
    Grundstellung()
    Haupt.Zusatzlied2.Liedtextanzeige.config(bg="orange")

def Zusatzlied3übergabe():
    global Datenfürliedanderwand, Wieoftlied, Wieoft
    Datenfürliedanderwand = Haupt.Zusatzlied3.Daten_fürTextanderwand.copy()
    Wieoftlied = int(Haupt.Zusatzlied3.Daten_fürTextanderwand[0])
    Wieoft = 0
    Grundstellung()
    Haupt.Zusatzlied3.Liedtextanzeige.config(bg="orange")

def Zusatzlied4übergabe():
    global Datenfürliedanderwand, Wieoftlied, Wieoft
    Datenfürliedanderwand = Haupt.Zusatzlied4.Daten_fürTextanderwand.copy()
    Wieoftlied = int(Haupt.Zusatzlied4.Daten_fürTextanderwand[0])
    Wieoft = 0
    Grundstellung()
    Haupt.Zusatzlied4.Liedtextanzeige.config(bg="orange")


def Nächstelied():
    global Wieoftlied, Datenfürliedanderwand, Wieoft, lesteslied
    Wieoft = 0
    Datenfürliedanderwand = []
    Grundstellung()
    if int(Haupt.Einganslied.Daten_fürTextanderwand[0]) == int(Wieoftlied):
        Haupt.Einganslied.Liedtextanzeige.config(bg="orange")
        Datenfürliedanderwand = Haupt.Einganslied.Daten_fürTextanderwand.copy()
    elif int(Haupt.Amtswechsellied.Daten_fürTextanderwand[0]) == int(Wieoftlied):
        Haupt.Amtswechsellied.Liedtextanzeige.config(bg="orange")
        Datenfürliedanderwand = Haupt.Amtswechsellied.Daten_fürTextanderwand.copy()
    elif int(Haupt.Textwortlied.Daten_fürTextanderwand[0]) == int(Wieoftlied):
        Haupt.Textwortlied.Liedtextanzeige.config(bg="orange")
        Datenfürliedanderwand = Haupt.Textwortlied.Daten_fürTextanderwand.copy()
    elif int(Haupt.Amtswechsellied.Daten_fürTextanderwand[0]) == int(Wieoftlied):
        Haupt.Amtswechsellied.Liedtextanzeige.config(bg="orange")
        Datenfürliedanderwand = Haupt.Amtswechsellied.Daten_fürTextanderwand.copy()
    elif int(Haupt.Bussslied.Daten_fürTextanderwand[0]) == int(Wieoftlied):
        Haupt.Bussslied.Liedtextanzeige.config(bg="orange")
        Datenfürliedanderwand = Haupt.Bussslied.Daten_fürTextanderwand.copy()
    elif int(Haupt.Abendmahlslied.Daten_fürTextanderwand[0]) == int(Wieoftlied):
        Haupt.Abendmahlslied.Liedtextanzeige.config(bg="orange")
        Datenfürliedanderwand = Haupt.Abendmahlslied.Daten_fürTextanderwand.copy()
    elif int(Haupt.Schlusslied.Daten_fürTextanderwand[0]) == int(Wieoftlied):
        Haupt.Schlusslied.Liedtextanzeige.config(bg="orange")
        Datenfürliedanderwand = Haupt.Schlusslied.Daten_fürTextanderwand.copy()
    elif int(Haupt.Kinderlied.Daten_fürTextanderwand[0]) == int(Wieoftlied):
        Haupt.Kinderlied.Liedtextanzeige.config(bg="orange")
        Datenfürliedanderwand = Haupt.Kinderlied.Daten_fürTextanderwand.copy()
    elif int(Haupt.Zusatzlied1.Daten_fürTextanderwand[0]) == int(Wieoftlied):
        Haupt.Zusatzlied1.Liedtextanzeige.config(bg="orange")
        Datenfürliedanderwand = Haupt.Zusatzlied1.Daten_fürTextanderwand.copy()
    elif int(Haupt.Zusatzlied2.Daten_fürTextanderwand[0]) == int(Wieoftlied):
        Haupt.Zusatzlied2.Liedtextanzeige.config(bg="orange")
        Datenfürliedanderwand = Haupt.Zusatzlied2.Daten_fürTextanderwand.copy()
    elif int(Haupt.Zusatzlied3.Daten_fürTextanderwand[0]) == int(Wieoftlied):
        Haupt.Zusatzlied3.Liedtextanzeige.config(bg="orange")
        Datenfürliedanderwand = Haupt.Zusatzlied3.Daten_fürTextanderwand.copy()
    elif int(Haupt.Zusatzlied4.Daten_fürTextanderwand[0]) == int(Wieoftlied):
        Haupt.Zusatzlied4.Liedtextanzeige.config(bg="orange")
        Datenfürliedanderwand = Haupt.Zusatzlied4.Daten_fürTextanderwand.copy()
    else:
        Haupt.Text_Anzeige_Label.config(text="")
        lesteslied = True


def Voeherlied():
    global Wieoftlied, Wieoft, voherliedzwischensehne, AusganneVerse, Datenfürliedanderwand
    if Wieoftlied > 1:
        Wieoftlied = Wieoftlied - 1
        vorherübergabeTextandiewand(Wieoftlied)
        Verinbterprätator(Datenfürliedanderwand[3], Datenfürliedanderwand[2], Datenfürliedanderwand[4])
        Wieoft = len(AusganneVerse) + 1
        Wieoft = Wieoft - 2
        Verse(Datenfürliedanderwand[3],AusganneVerse[Wieoft],Datenfürliedanderwand[2])
        Wieoft = Wieoft + 1
    

def Versvorher():
    global Wieoft, voherliedzwischensehne, lesteslied, Wieoftlied
    if lesteslied == True:
        lesteslied = False
        Wieoftlied = Wieoftlied - 1
        vorherübergabeTextandiewand(Wieoftlied)
        Verinbterprätator(Datenfürliedanderwand[3], Datenfürliedanderwand[2], Datenfürliedanderwand[4])
        Wieoft = len(AusganneVerse) + 1
    if voherliedzwischensehne == False:
        Wieoft = Wieoft - 2
        positionfeedback(Wieoftlied)
        Liedgebe()
    voherliedzwischensehne = False

def Liedgebe():
    global Wieoft, Wieoftlied, Datenfürliedanderwand, voherliedzwischensehne, lesteslied
    if lesteslied == False:
        if voherliedzwischensehne == True:
            Wieoftlied = Wieoftlied + 1
            Nächstelied()
        if Wieoftlied == 0:
            Wieoft = 0
            Datenfürliedanderwand = Haupt.Einganslied.Daten_fürTextanderwand.copy()
            Wieoftlied = 1
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
        elif int(Wieoft) == - 2:
            Wieoft = 0
            Voeherlied()
        else:
            Verse(Datenfürliedanderwand[3],AusganneVerse[Wieoft],Datenfürliedanderwand[2])
            Wieoft = Wieoft + 1
            Haupt.Textmanager.update()


def optisches_fedback(Liedposition):
    if int(Haupt.Einganslied.Daten_fürTextanderwand[0]) == int(Liedposition):
        Haupt.Einganslied.Liedtextanzeige.config(bg="green")
    elif int(Haupt.Amtswechsellied.Daten_fürTextanderwand[0]) == int(Liedposition):
        Haupt.Amtswechsellied.Liedtextanzeige.config(bg="green")
    elif int(Haupt.Textwortlied.Daten_fürTextanderwand[0]) == int(Liedposition):
        Haupt.Textwortlied.Liedtextanzeige.config(bg="green")
    elif int(Haupt.Bussslied.Daten_fürTextanderwand[0]) == int(Liedposition):
        Haupt.Bussslied.Liedtextanzeige.config(bg="green")
    elif int(Haupt.Abendmahlslied.Daten_fürTextanderwand[0]) == int(Liedposition):
        Haupt.Abendmahlslied.Liedtextanzeige.config(bg="green")
    elif int(Haupt.Schlusslied.Daten_fürTextanderwand[0]) == int(Liedposition):
        Haupt.Schlusslied.Liedtextanzeige.config(bg="green")
    elif int(Haupt.Kinderlied.Daten_fürTextanderwand[0]) == int(Liedposition):
        Haupt.Kinderlied.Liedtextanzeige.config(bg="green")
    elif int(Haupt.Zusatzlied1.Daten_fürTextanderwand[0]) == int(Liedposition):
        Haupt.Zusatzlied1.Liedtextanzeige.config(bg="green")
    elif int(Haupt.Zusatzlied2.Daten_fürTextanderwand[0]) == int(Liedposition):
        Haupt.Zusatzlied2.Liedtextanzeige.config(bg="green")
    elif int(Haupt.Zusatzlied3.Daten_fürTextanderwand[0]) == int(Liedposition):
        Haupt.Zusatzlied3.Liedtextanzeige.config(bg="green")
    elif int(Haupt.Zusatzlied4.Daten_fürTextanderwand[0]) == int(Liedposition):
        Haupt.Zusatzlied4.Liedtextanzeige.config(bg="green")


def Verse(Hallo123,Wieoft,WelchesBuch):
    optisches_fedback(Wieoftlied)
    try:
        Texttest = open("C:\\Users\\"+Haupt.Dateiort+"\\Desktop\\Lieder\\Buch\\"+str(WelchesBuch)+"\\"+str(Hallo123)+" Vers " + str(Wieoft) + ".txt",
                    "r", encoding="utf-8")
        Aktuellertext = Texttest.read()
        Haupt.Text_Anzeige_Label.config(text=Aktuellertext)
    except FileNotFoundError:
        Errorbild = tkinter.Toplevel(Haupt.Textmanager)
        Errorbild.geometry("560x350+500+400")
        Errorbild.config(bg="black")
        Error = tkinter.Label(Errorbild, font=("Helvetica", 40),
                      text="Error", bg="black",
                      fg="green", wraplength=560)
        Error.place(x=210, y=0)
        ErrorLabel = tkinter.Label(Errorbild, font=("Helvetica", 20),
                           text="Das Lied "+str(Hallo123)+" im Buch "+str(WelchesBuch)+" Vers "+str(Wieoft)+" Exesitert nicht", bg="black",
                           fg="green", wraplength=560)
        ErrorLabel.place(x=0, y=80)