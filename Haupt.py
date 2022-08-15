import os
from tkinter import *
import tkinter
from tkinter import scrolledtext
from tkinter.scrolledtext import ScrolledText
Dateiort = os.getlogin()
Textmanager = Tk()
Textmanager.title("Textmanager")
Textmanager.geometry("1040x800")
Textmanager.iconbitmap("C:\\Users\\" + Dateiort + "\\Desktop\\Lieder\\picture_compress 1.ico")
AnzeigeText = Toplevel(Textmanager)
AnzeigeText.geometry("1920x1080+1920+0")
AnzeigeText.overrideredirect(True)
Text_Anzeige_Label = Label(AnzeigeText, font=("Helvetica", 60), fg="white", bg="black", wraplength=1920)
Aktueller_Text = ""
Text_Anzeige_Label.config(text=Aktueller_Text)
Text_Anzeige_Label["justify"] = "left"
Text_Anzeige_Label.place(x=0, y=0)
Wie_viele_zusatzlieder = 0
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




Stream_erstell_button = Button(Textmanager, font=("Helvetica", 20), fg="#98FB98", bg="#B22222", text="Stream Erstellen")
klick = Button(Textmanager, font=("Helvetica", 20), fg="#98FB98", bg="#B22222", text="weiter")
zurueck = Button(Textmanager, font=("Helvetica", 20), fg="#98FB98", bg="#B22222", text="zurück")
Hauptbildschirmbutton = Button(Textmanager, font=("Helvetica", 20), fg="#98FB98", bg="#B22222", text="Präsentation")
AnfangHaupt = Button(Textmanager, font=("Helvetica", 20), fg="#98FB98", bg="#B22222", text="Anfang")


class Grafigfuer_ein_Lied:
    # erstellt Grafik(Eingabe und Ausgabe des Liedes) für ein Lied
    opt = None
    Lied = None
    Verse = None
    Liednummer = None
    Liedverse = None
    Liedtextanzeige = None
    Buch = None
    ErrorLabel = None
    Dateiliedtext1 = None
    Dateiliedtext = None
    aktualisieren_wahl = "False"
    Buchzahl_clicked = None

    def __init__(self, Position, Liedname, Wahl, Hintergrund, Vordergrund):
        if Wahl == "True":
            self.clicked = StringVar()
            self.clicked.set(Buch_Listen[0])
            OptionMenu(Textmanager, self.clicked, *Buch_Listen)
            self.opt = OptionMenu(Textmanager, self.clicked, *Buch_Listen)
            self.opt.config(width=12, font=('Helvetica', 12), bg=Hintergrund, fg=Vordergrund)
            self.Lied = Label(Textmanager, font=("Helvetica", 15), pady=5, text=Liedname, bg=Hintergrund,
                              fg=Vordergrund)
            self.Verse = Label(Textmanager, font=("Helvetica", 15), text="Verse", bg=Hintergrund, fg=Vordergrund)
            self.Liednummer = Entry(Textmanager, font=("Helvetica", 24), width=10,xscrollcommand=False)
            self.Liedverse = Entry(Textmanager, font=("Helvetica", 24), width=10)
            self.Liedtextanzeige = Button(Textmanager, font=12, pady=5, bg=Hintergrund, border=0, fg=Vordergrund)
            self.Liedtextanzeige["justify"] = "left"
            self.opt.place(x=340, y=25 + Position)
            self.Liedtextanzeige.place(x=495, y=15 + Position)
            self.Lied.place(x=0, y=0 + Position)
            self.Verse.place(y=40 + Position)
            self.Liednummer.place(x=150, y=0 + Position)
            self.Liedverse.place(x=150, y=40 + Position)
            self.Buch = None
            self.ErrorLabel = None
            self.aktualisieren_wahl = "True"
        else:
            self.opt = None
            self.Lied = None
            self.Verse = None
            self.Liednummer = None
            self.Liedverse = None
            self.Liedtextanzeige = None
            self.Buch = None
            self.ErrorLabel = None
            self.Dateiliedtext1 = None
            self.Dateiliedtext = None
            self.aktualisieren_wahl = "False"
            self.Buchzahl_clicked = None
        Textmanager.update()

    # Lädt den Namen des Liedes für den Livestream und Livestream vorschau
    def Datein_lesen(self):
        try:
            self.Dateiliedtext1 = open("C:\\Users\\" + Dateiort + "\\Desktop\\Lieder\\Einbledungen\\" + str(
                self.clicked.get()) + "\\l" + str(self.Liednummer.get()) + ".txt", 'r', encoding='utf8')
            self.Dateiliedtext = self.Dateiliedtext1.read()
        except FileNotFoundError:
            Errorbild = Toplevel(Textmanager)
            Errorbild.geometry("560x350+500+400")
            Errorbild.config(bg="black")
            Error = Label(Errorbild, font=("Helvetica", 40), text="Error", bg="black", fg="green", wraplength=560)
            Error.place(x=210, y=0)
            ErrorLabel = Label(Errorbild, font=("Helvetica", 20),
                               text="Dieses Liednummer ist zu Groß oder ist noch nicht im System", bg="black",
                               fg="green", wraplength=560)
            ErrorLabel.place(x=0, y=80)
            Hi = self.Liednummer.get()
            Hi2 = Hi[:-1]
            self.Liednummer.delete(0, "end")
            self.Liednummer.insert(0, Hi2)

    def Zerstören(self):
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
        self.ErrorLabel = None
        self.Dateiliedtext1 = None
        self.Dateiliedtext = None
        self.aktualisieren_wahl = "False"
        self.Buchzahl_clicked = None
        Textmanager.update()


    def Erstellen(self, Position, Liedname, Hintergrund, Vordergrund):
        self.clicked = StringVar()
        self.clicked.set(Buch_Listen[0])
        OptionMenu(Textmanager, self.clicked, *Buch_Listen)
        self.opt = OptionMenu(Textmanager, self.clicked, *Buch_Listen)
        self.opt.config(width=12, font=('Helvetica', 12), bg=Hintergrund, fg=Vordergrund)
        self.Lied = Label(Textmanager, font=("Helvetica", 15), pady=5, text=Liedname, bg=Hintergrund,
                              fg=Vordergrund)
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
        self.Buch = None
        self.ErrorLabel = None
        self.aktualisieren_wahl = "True"


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
            self.Buchzahl_clicked = 3
        elif self.clicked.get() == "Kinderliederbuch":
            self.Buch = "KLB"
            self.Buchzahl_clicked = 4
        elif self.clicked.get() == "Sonderheft":
            self.Buch = "SH"
            self.Buchzahl_clicked = 5
        elif self.clicked.get() == "Spanisches Chorbuch":
            self.Buch = "SpC"
            self.Buchzahl_clicked = 6
        elif self.clicked.get() == "Band 1 Singt dem Herrn":
            self.Buch = "SdH Band 1"
            self.Buchzahl_clicked = 7
        elif self.clicked.get() == "Band 2 Singt dem Herrn":
            self.Buch = "SdH Band 2"
            self.Buchzahl_clicked = 8
        elif self.clicked.get() == "Band 3 Singt dem Herrn":
            self.Buch = "SdH Band 3"
            self.Buchzahl_clicked = 9

    # Zeig im programm, welches Lied ausgewählt ist.
    def Livestream_Vorchau(self):
        if len(self.Liedverse.get()) >= 1:
            self.Liedtextanzeige.config(text=str(self.Buch + " " + self.Liednummer.get() + " Vers " +
                                                 str(self.Liedverse.get()) + "\n" + self.Dateiliedtext))
        else:
            self.Liedtextanzeige.config(text=str(self.Buch + " " + self.Liednummer.get()+"\n" + self.Dateiliedtext))

    # sorgt dafür, dass alles aktualisiert wird
    def Hintergrund_aktualisierung(self, Liedname):
        if self.aktualisieren_wahl == "True":
            Grafigfuer_ein_Lied.Buchabkuerzen(self)
            Grafigfuer_ein_Lied.Datein_lesen(self)
            Grafigfuer_ein_Lied.Livestream_Vorchau(self)
            AktuellerText1 = open("C:\\Users\\" + Dateiort + "\\Desktop\\Lieder\\" + str(Liedname) +
                                  ".txt", 'r', encoding='utf8')
            AktuellerText = AktuellerText1.read()
            if len(self.Liedverse.get()) >= 1:
                if AktuellerText == (
                        self.Buch + " " + self.Liednummer.get() + " Vers " + str(self.Liedverse.get()) + "\n"
                        + self.Dateiliedtext):
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
        else:
            pass

    # Speichert alle relevanten Daten egal ob Livestream oder zum Wiederherstellen
    def Knopf_Druecken(self, Liedname):
        if self.aktualisieren_wahl == "True":
            Lied_Textueberabe = open(
                "C:\\Users\\" + Dateiort + "\\Desktop\\Lieder\\Einbledungen\\" + self.clicked.get() + "\\l" +
                str(self.Liednummer.get()) + ".txt", 'r', encoding='utf8')
            Lied_Text = Lied_Textueberabe.read()
            Livestream_Text = open("C:\\Users\\" + Dateiort + "\\Desktop\\Lieder\\" + Liedname + ".txt", 'w',
                                   encoding='utf8')
            Lied_nummer_uebergabe = open("C:\\Users\\" + Dateiort + "\\Desktop\\Lieder\\Nummer"+Liedname +
                                         ".txt", 'w', encoding='utf8')
            Lied_nummer_uebergabe.write(self.Liednummer.get())
            Lied_nummer_uebergabe.close()
            Lied_Vers_uebergabe = open("C:\\Users\\" + Dateiort + "\\Desktop\\Lieder\\Verse"+Liedname +
                                       ".txt", 'w', encoding='utf8')
            Lied_Vers_uebergabe.write(self.Liedverse.get())
            Lied_Vers_uebergabe.close()
            Lied_Buch_Uebergabe = open("C:\\Users\\" + Dateiort + "\\Desktop\\Lieder\\Buch"+Liedname +
                                       ".txt", 'w', encoding='utf8')
            Lied_Buch_Uebergabe.write(str(self.Buchzahl_clicked))
            Lied_Buch_Uebergabe.close()
            if len(self.Liedverse.get()) >= 1:
                Livestream_Text.write(self.Buch + " " + str(self.Liednummer.get()) + " Vers " + str(
                    self.Liedverse.get()) + "\n" + Lied_Text)
            else:
                Livestream_Text.write(self.Buch + " " + str(self.Liednummer.get()) + "\n" + Lied_Text)
            Livestream_Text.close()

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
            Lied_nummer_uebergabe = open("C:\\Users\\" + Dateiort + "\\Desktop\\Lieder\\Nummer" + Liedname +
                                         ".txt", 'r', encoding='utf8')
            Lied_Vers_uebergabe = open("C:\\Users\\" + Dateiort + "\\Desktop\\Lieder\\Verse" + Liedname +
                                       ".txt", 'r', encoding='utf8')
            Lied_Buch_Uebergabe = open("C:\\Users\\" + Dateiort + "\\Desktop\\Lieder\\Buch" + Liedname +
                                       ".txt", 'r', encoding='utf8')
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


def Einstellungen_Laden():
    global Textmanager_Textfarbe, Textmanager_Hintergrund, Kinder_anzeigen, Kinder_Anzeigen_Grafig, Kinder_Position, \
        Zusatzlied1_obwahr, Zusatzlied2_obwahr, Zusatzlied3_obwahr, Zusatzlied4_obwahr, Wie_viele_zusatzlieder
    Textfarbe = open("C:\\Users\\" + Dateiort + "\\Desktop\\Lieder\\Textfarbe.txt", 'r', encoding='utf8')
    Textmanager_Textfarbe = Textfarbe.read()
    Textfarbe.close()
    Hintergrund = open("C:\\Users\\" + Dateiort + "\\Desktop\\Lieder\\Hintergrund.txt", 'r', encoding='utf8')
    Textmanager_Hintergrund = Hintergrund.read()
    Hintergrund.close()
    Kinderladen = open("C:\\Users\\" + Dateiort + "\\Desktop\\Lieder\\Kindereinstellung.txt", 'r', encoding='utf8')
    Kinder_anzeigen = Kinderladen.read()
    Kinderladen.close()
    if Kinder_anzeigen == "Wahr":
        Kinder_Anzeigen_Grafig = "True"
        Kinder_Position = 1
    else:
        Kinder_Anzeigen_Grafig = "False"
        Kinder_Position = 0
    Zusatzlied1_obwahr = "False"
    Zusatzlied2_obwahr = "False"
    Zusatzlied3_obwahr = "False"
    Zusatzlied4_obwahr = "False"


# Erstellt die Grundstruktur des Programms
def Textmamager_erstellen():
    Einstellungen_Laden()
    global Einganslied, Textwortlied, Amtswechsellied, Kinderlied, Bussslied, Abendmahlslied, Schlusslied, Zusatzlied1,\
        Zusatzlied2, Zusatzlied3, Zusatzlied4, zusaetzliches_lied, Button_bestaetigen, Wie_viele_zusatzlieder, \
        loeschenbutton, Einstellungen_button, Textwortentry, Textwortlabel
    Einganslied = Grafigfuer_ein_Lied(0, "Einganslied", "True", Textmanager_Hintergrund, Textmanager_Textfarbe)
    Textwortlied = Grafigfuer_ein_Lied(83, "Textwortlied", "True", Textmanager_Hintergrund, Textmanager_Textfarbe)
    Amtswechsellied = Grafigfuer_ein_Lied(166, "Amtswechsellied", "True", Textmanager_Hintergrund, Textmanager_Textfarbe)
    Kinderlied = Grafigfuer_ein_Lied(166 +83*Kinder_Position, "Kinderlied", Kinder_Anzeigen_Grafig, Textmanager_Hintergrund, Textmanager_Textfarbe)
    Bussslied = Grafigfuer_ein_Lied(249+83*Kinder_Position, "Bußlied", "True", Textmanager_Hintergrund, Textmanager_Textfarbe)
    Abendmahlslied = Grafigfuer_ein_Lied(332+83*Kinder_Position, "Abendmahlslied", "True", Textmanager_Hintergrund, Textmanager_Textfarbe)
    Schlusslied = Grafigfuer_ein_Lied(415+83*Kinder_Position, "Schlusslied", "True", Textmanager_Hintergrund, Textmanager_Textfarbe)
    Zusatzlied1 = Grafigfuer_ein_Lied(1000+83*Kinder_Position, "Zusatzlied", Zusatzlied1_obwahr, Textmanager_Hintergrund, Textmanager_Textfarbe)
    Zusatzlied2 = Grafigfuer_ein_Lied(1000+83*Kinder_Position, "Zusatzlied1", Zusatzlied2_obwahr, Textmanager_Hintergrund, Textmanager_Textfarbe)
    Zusatzlied3 = Grafigfuer_ein_Lied(1000+83*Kinder_Position, "Zusatzlied2", Zusatzlied3_obwahr, Textmanager_Hintergrund, Textmanager_Textfarbe)
    Zusatzlied4 = Grafigfuer_ein_Lied(1000+83*Kinder_Position, "Zusatzlied3", Zusatzlied4_obwahr, Textmanager_Hintergrund, Textmanager_Textfarbe)
    Textmanager.config(bg=Textmanager_Hintergrund)
    zusaetzliches_lied = Button(Textmanager, font=("Helvetica", 12), fg=Textmanager_Hintergrund,
                                bg=Textmanager_Textfarbe, text="Weiters Lied",
                                command=zusaetzlicheslied)
    zusaetzliches_lied.place(x=300, y=500+83*Kinder_Position)
    Button_bestaetigen = Button(Textmanager, font=("Helvetica", 24), text="Bestätigen", command=Button_command)
    Button_bestaetigen.place(x=800, y=200)
    loeschenbutton = Button(Textmanager, font=("Helvetica", 20), fg="#98FB98", bg="#B22222", text="Löschen",
                            command=Eingabe_loeschen)
    loeschenbutton.place(x=800, y=396)
    wiederherstellen = Button(Textmanager, font=("Helvetica", 20), fg="#98FB98", bg="#B22222", text="Wiederherstellen",
                              command=Eingabe_wiederherstellen)
    wiederherstellen.place(x=800, y=333)
    Einstellungen_button = Button(Textmanager, font=("Helvetica", 20), fg="#98FB98", bg="#B22222", text="Einstellung",
                                  command=Einstellungen)
    Einstellungen_button.place(x=800, y=270)
    Textwortlabel = Label(Textmanager, font=("Halvetica", 15), bg="#FFEBCD", text="Kapitel")
    Textwortentry = Text(Textmanager, font=("Helvetica", 15), width=40,height=5, bg="#FFEBCD")
    Textwortentry.place(x=0,y=620)



def zusaetzlicheslied3():
    global Wie_viele_zusatzlieder, Zusatzlied4, Zusatzlied4_obwahr
    Zusatzlied4 = Grafigfuer_ein_Lied(498 + 83 * Wie_viele_zusatzlieder+83*Kinder_Position, "Zusatzlied" + str(Wie_viele_zusatzlieder + 1),
                                      "True", Textmanager_Hintergrund, Textmanager_Textfarbe)
    Wieoft1 = Wie_viele_zusatzlieder + 1
    Wie_viele_zusatzlieder = Wieoft1
    Zusatzlied4_obwahr = True
    zusaetzliches_lied.destroy()

    zusaetzliches_liedzerstörer.config(command=zusaetzlichesliedzerstörer3)

def zusaetzlichesliedzerstörer3():
    global Wie_viele_zusatzlieder, zusaetzliches_lied
    Zusatzlied4.Zerstören()
    Wie_viele_zusatzlieder = Wie_viele_zusatzlieder - 1
    zusaetzliches_lied = Button(Textmanager, font=("Helvetica", 12), fg=Textmanager_Hintergrund,
            bg=Textmanager_Textfarbe, text="Weiters Lied",
    command=zusaetzlicheslied3)
    Aktualiesierung_Grafick()
    zusaetzliches_liedzerstörer.config(command=zusaetzlichesliedzerstörer2)

def zusaetzlicheslied2():
    global Wie_viele_zusatzlieder, Zusatzlied3, Zusatzlied3_obwahr
    Zusatzlied3 = Grafigfuer_ein_Lied(498 + 83 * Wie_viele_zusatzlieder+83*Kinder_Position, "Zusatzlied" + str(Wie_viele_zusatzlieder + 1),
                                      "True", Textmanager_Hintergrund, Textmanager_Textfarbe)
    Wie_viele_zusatzlieder1 = Wie_viele_zusatzlieder + 1
    Wie_viele_zusatzlieder = Wie_viele_zusatzlieder1
    Zusatzlied3_obwahr = True
    Textmanager.geometry("1040x990")
    zusaetzliches_lied.config(command=zusaetzlicheslied3)
    Aktualiesierung_Grafick()
    zusaetzliches_liedzerstörer.config(command=zusaetzlichesliedzerstörer2)

def zusaetzlichesliedzerstörer2():
    global Wie_viele_zusatzlieder
    Zusatzlied3.Zerstören()
    Wie_viele_zusatzlieder = Wie_viele_zusatzlieder - 1
    zusaetzliches_lied.config(command=zusaetzlicheslied2)
    Aktualiesierung_Grafick()
    zusaetzliches_liedzerstörer.config(command=zusaetzlichesliedzerstörer1)
    Textmanager.geometry("1040x800")

def zusaetzlicheslied1():
    global Wie_viele_zusatzlieder, Zusatzlied2, Zusatzlied2_obwahr
    Zusatzlied2 = Grafigfuer_ein_Lied(498 + 83 * Wie_viele_zusatzlieder+83*Kinder_Position, "Zusatzlied" + str(Wie_viele_zusatzlieder + 1),
                                      "True", Textmanager_Hintergrund, Textmanager_Textfarbe)
    Wieoft1 = Wie_viele_zusatzlieder + 1
    Wie_viele_zusatzlieder = Wieoft1
    Zusatzlied2_obwahr = True
    Aktualiesierung_Grafick()
    zusaetzliches_lied.config(command=zusaetzlicheslied2)
    zusaetzliches_liedzerstörer.config(command=zusaetzlichesliedzerstörer1)

def zusaetzlichesliedzerstörer1():
    global Wie_viele_zusatzlieder
    Zusatzlied2.Zerstören()
    Wie_viele_zusatzlieder = Wie_viele_zusatzlieder - 1
    zusaetzliches_lied.config(command=zusaetzlicheslied1)
    Aktualiesierung_Grafick()
    zusaetzliches_liedzerstörer.config(command=zusaetzlichesliedzerstörer)

def zusaetzlicheslied():
    global Wie_viele_zusatzlieder, Zusatzlied1, Zusatzlied1_obwahr, zusaetzliches_liedzerstörer
    Zusatzlied1 = Grafigfuer_ein_Lied(498 + 83 * Wie_viele_zusatzlieder+83*Kinder_Position, "Zusatzlied" + str(Wie_viele_zusatzlieder + 1),
                                      "True", Textmanager_Hintergrund, Textmanager_Textfarbe)
    Wieoft1 = Wie_viele_zusatzlieder + 1
    Wie_viele_zusatzlieder = Wieoft1
    Zusatzlied1_obwahr = True
    zusaetzliches_liedzerstörer = Button(Textmanager, font=("Helvetica", 12), fg=Textmanager_Hintergrund,
                                bg=Textmanager_Textfarbe, text="Zusatzlied Löschen",
                                command=zusaetzlichesliedzerstörer)
    zusaetzliches_lied.config(command=zusaetzlicheslied1)
    Aktualiesierung_Grafick()


def zusaetzlichesliedzerstörer():
    global Wie_viele_zusatzlieder
    Zusatzlied1.Zerstören()
    Wie_viele_zusatzlieder = Wie_viele_zusatzlieder - 1
    zusaetzliches_lied.config(command=zusaetzlicheslied)
    Aktualiesierung_Grafick()
    zusaetzliches_liedzerstörer.destroy()


def Button_command():
    Einganslied.Knopf_Druecken("Einganslied")
    Textwortlied.Knopf_Druecken("Textwortlied")
    Amtswechsellied.Knopf_Druecken("Amtswechsellied")
    Kinderlied.Knopf_Druecken("Kinderlied")
    Bussslied.Knopf_Druecken("Bußlied")
    Abendmahlslied.Knopf_Druecken("Abendmahlslied")
    Schlusslied.Knopf_Druecken("Schlusslied")
    Zusatzlied1.Knopf_Druecken("Zusatzlied1")
    Zusatzlied2.Knopf_Druecken("Zusatzlied2")
    Zusatzlied3.Knopf_Druecken("Zusatzlied3")
    Zusatzlied4.Knopf_Druecken("Zusatzlied4")
    Textwortreinschreiben = open("C:\\Users\\" + Dateiort + "\\Desktop\\Lieder\\Textwort.txt", 'w', encoding='utf8')
    Textwortreinschreiben.write(Textwortentry.get("1.0","end-1c"))


def Hintergrund_aktualisieren():
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
    Textwortauslesen= open("C:\\Users\\" + Dateiort + "\\Desktop\\Lieder\\Textwort.txt", 'r', encoding='utf8')
    if Textwortentry.get("1.0","end-1c") == Textwortauslesen.read():
        Textwortentry.config(bg="green")
    else:
        Textwortentry.config(bg="red")
    Einganslied.Lied.after(50, lambda: Hintergrund_aktualisieren())


def Eingabe_loeschen():
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


def Eingabe_wiederherstellen():
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
        Vordergrund_opt, Hintergrundlabel, Textlabel, Buttonfarben, Kinder_Anzeigen_Grafig, Kinder_Position, Kinderbutton
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
    Einstellungen_Laden()
    if Kinder_anzeigen == "Falsch":
        Kinderbutton = Button(Einstellungen_Textmanager, font=('Helvetica', 12), fg="Black", bg="red", text="Kein Kinderlied", command=Kinder_Anzeigen)
    else:
        Kinderbutton = Button(Einstellungen_Textmanager, font=('Helvetica', 12), fg="Black", bg="green", text="Kinderlied", command=Kinder_Nicht_Anzeigen)
    Kinderbutton.place(x=0, y=110)


def Kinder_Anzeigen():
    global Kinder_Anzeigen_Grafig, Kinder_Position
    Kinderbutton.config(bg="green", text="Kinderlied", command=Kinder_Nicht_Anzeigen)
    Kinder_Anzeigen_Grafig = "False"
    Kinder_Position = 1
    Kinderladen = open("C:\\Users\\" + Dateiort + "\\Desktop\\Lieder\\Kindereinstellung.txt", 'w', encoding='utf8')
    Kinderladen.write("Wahr")
    Kinderladen.close()
    Kinderlied.Erstellen(166 +83*Kinder_Position, "Kinderlied", Textmanager_Hintergrund, Textmanager_Textfarbe)
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
    Textwortlied.Aktualiesieren(83)
    Amtswechsellied.Aktualiesieren(166)
    Kinderlied.Aktualiesieren(249)
    Bussslied.Aktualiesieren(249+83*Kinder_Position)
    Abendmahlslied.Aktualiesieren(332+83*Kinder_Position)
    Schlusslied.Aktualiesieren(415+83*Kinder_Position)
    Zusatzlied1.Aktualiesieren(498+83*Kinder_Position)
    Zusatzlied2.Aktualiesieren(581+83*Kinder_Position)
    Zusatzlied3.Aktualiesieren(664+83*Kinder_Position)
    Zusatzlied4.Aktualiesieren(747+83*Kinder_Position)
    if Wie_viele_zusatzlieder > 0:
            zusaetzliches_liedzerstörer.place(x=30, y=500 + Wie_viele_zusatzlieder * 83+83*Kinder_Position)
    if Wie_viele_zusatzlieder < 4:
        zusaetzliches_lied.place(x=300, y=(500 + Wie_viele_zusatzlieder * 83+83*Kinder_Position))
    Textwortentry.place(x=0,y=(537 + Wie_viele_zusatzlieder * 83+83*Kinder_Position))
    


Einstellungen_Laden()
Textmamager_erstellen()
Hintergrund_aktualisieren()