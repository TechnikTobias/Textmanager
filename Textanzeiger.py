import Haupt
import tkinter

Wieoft = 0
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
                if Wieoft == int(Maxzahl):
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

Wieoftlied = 1


def übergabeTextandiewand(Liedposition):

    if int(Haupt.Einganslied.Daten_fürTextanderwand[0]) == int(Liedposition):
        global Datenfürliedanderwand, Wieoft
        Datenfürliedanderwand = Haupt.Einganslied.Daten_fürTextanderwand.copy()
        Wieoft = 0
        print(Datenfürliedanderwand)




def Nächstelied():
    Wieoftlied = Wieoftlied +1
    übergabeTextandiewand(Wieoftlied)
    if Haupt.Einganslied.Daten_fürTextanderwand[0] == Wieoftlied:
        Haupt.Einganslied.Liedtextanzeige.config(bg="orange")
    if Haupt.Amtswechsellied.Daten_fürTextanderwand[0] == Wieoftlied:
        Haupt.Amtswechsellied.Liedtextanzeige.config(bg="orange")
    if Haupt.Textwortlied.Daten_fürTextanderwand[0] == Wieoftlied:
        Haupt.Textwortlied.Liedtextanzeige.config(bg="orange")

def Voeherlied():
    global Wieoftlied
    Wieoftlied = Wieoftlied - 1
    übergabeTextandiewand(Wieoftlied)

def Liedgebe():
    global Wieoft
    übergabeTextandiewand(Wieoftlied)
    print(Datenfürliedanderwand[4])
    Verinbterprätator(Datenfürliedanderwand[3], Datenfürliedanderwand[2], Datenfürliedanderwand[4])
    Aktuelllervers = len(AusganneVerse)
    if int(Wieoft) == int(Aktuelllervers):
        AkutellerText = ""
        Haupt.Text_Anzeige_Label.config(text=AkutellerText)
        Nächstelied()
        Haupt.Textmanager.update()

    elif int(Wieoft) == -1:
        AkutellerText = ""
        Haupt.Text_Anzeige_Label.config(text=AkutellerText)
    elif int(Wieoft) == -2:
        Wieoft = Wieoft - 1
    else:
        Verse(Datenfürliedanderwand[3],AusganneVerse[Wieoft],Datenfürliedanderwand[2])
        Wieoft = Wieoft + 1
        Haupt.Textmanager.update()

def Verse(Hallo123,Wieoft,WelchesBuch):
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