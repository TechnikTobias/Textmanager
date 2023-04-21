from tkinter import *
import Haupt

Buchclickedladen = "0"
Verseingabeladen = "0"
Liedeingabeladen = "0"
Streameinblendungladen = None
Liedverse_eingabeladen = None
Verszahlinfo = None
hi = True

def Verskontrolle():
    global Verskontroller, Liedeingabe, Verseingabe, Verszahl, Liedverse_eingabe, Buchclicked, Streameinblendung, Versbestätigen, hi
    try:
        Liedeingabe.get()
    except:
        Verskontroller = Toplevel(Haupt.Textmanager)
        Verskontroller.geometry("800x800")
        Verskontroller.title("Vers Kontrolle")
        Verskontroller.config(bg=Haupt.Textmanager_Hintergrund)
        Liedeingabe = Entry(Verskontroller, font=("Helvetica", 24), width=4)
        Liedeingabe.place(x=300,y=60)
        Verseingabe = Entry(Verskontroller, font=("Helvetica", 24), width=2)
        Verseingabe.place(x=300, y=105)
        Verszahl = Entry(Verskontroller, font=("Helvetica", 24), width=2)
        Verszahl.place(x=300, y=150)
        Liedeingabelabel = Label(Verskontroller, font=("Helvetica", 15), text="Bitte geben sie ein Lied ein", bg=Haupt.Textmanager_Hintergrund, fg=Haupt.Textmanager_Textfarbe)
        Liedeingabelabel.place(x=10, y=60)
        Verseingabelabel = Label(Verskontroller, font=("Helvetica", 15), text="Welcher Vers ist das?", bg=Haupt.Textmanager_Hintergrund, fg=Haupt.Textmanager_Textfarbe)
        Verseingabelabel.place(x=10, y=105)
        Verszahllabel = Label(Verskontroller, font=("Helvetica", 15), text="Wie viele Verse hat das Lied?", bg=Haupt.Textmanager_Hintergrund, fg=Haupt.Textmanager_Textfarbe)
        Verszahllabel.place(x=10, y=150)
        Liedverse_eingabe = Text(Verskontroller, font=("Helvetica", 20), height= 12, width=44, bg="#FFEBCD")
        Liedverse_eingabe.place(y=255, x=10)
        Buchclicked = StringVar()
        Buchclicked.set(Haupt.Buch_Listen[0])
        OptionMenu(Verskontroller, Buchclicked, *Haupt.Buch_Listen)
        Buchopt = OptionMenu(Verskontroller, Buchclicked, *Haupt.Buch_Listen)
        Buchopt.config(width=20, font=('Helvetica', 12), bg=Haupt.Textmanager_Hintergrund, fg=Haupt.Textmanager_Textfarbe)
        Buchopt.place(x=10,y=10)
        Buch_hinzufügen = Button(Verskontroller, font=("Helvetica", 24), bg=Haupt.Textmanager_Hintergrund, fg=Haupt.Textmanager_Textfarbe, text="+", command=Buch_hinzufügendef, bd=0) 
        Buch_hinzufügen.place(y=0, x=240)
        Versbestätigen = Button(Verskontroller, font=("Helvetica", 24), text="Bestätigen", command=Versbestätigendef, bd=0)
        Versbestätigen.place(x=300, y=705)
        Streameinblendung = Entry(Verskontroller, font=("Helvetica", 24), width=30, bg="#FFEBCD")
        Streameinblendung.place(x=10, y=205)
        hi = True
    Verskontrolleloop()

def Buch_hinzufügendef():
    pass

def Versbestätigendef():
    global Liedverse_eingabeladen, Streameinblendungladen, Verseingabeladen
    if len(Liedeingabe.get()) > 0:
        Text = open(f"C:\\Users\\{Haupt.Dateiort}\\Desktop\\Lieder\\Buch\\{Buchclicked.get()}\\{Liedeingabe.get()} Vers {Verse}.txt", 'w', encoding='utf8')
        Text.write(Liedverse_eingabe.get("1.0","end-1c"))
        Text.close()
        Text1 = open(f"C:\\Users\\{Haupt.Dateiort}\\Desktop\\Lieder\\Versanzahl\\{Buchclicked.get()}\\{Liedeingabe.get()}.txt", 'w', encoding='utf8')
        Text1.write(Verszahl.get())
        Text1.close()
        Text1 = open(f"C:\\Users\\{Haupt.Dateiort}\\Desktop\\Lieder\\Einbledungen\\{Buchclicked.get()}\\l{Liedeingabe.get()}.txt", 'w', encoding='utf8')
        Text1.write(Streameinblendung.get())
        Text1.close()
        Versbestätigen.config(text="Gespeichert")
        Liedverse_eingabeladen = Liedverse_eingabe.get("1.0","end-1c")
        Streameinblendungladen = Streameinblendung.get()
        Verseingabeladen = Verseingabe.get()

def Dateispeicherndef():
    global Liedverse_eingabeladen, Streameinblendungladen, Verseingabeladen, hi 
    if len(Liedeingabe.get()) > 0:
        Text = open(f"C:\\Users\\{Haupt.Dateiort}\\Desktop\\Lieder\\Buch\\{Buchclicked.get()}\\{Liedeingabe.get()} Vers {Versgespeichert}.txt", 'w', encoding='utf8')
        Text.write(Liedverse_eingabe.get("1.0","end-1c"))
        Text.close()
        Text1 = open(f"C:\\Users\\{Haupt.Dateiort}\\Desktop\\Lieder\\Versanzahl\\{Buchclicked.get()}\\{Liedeingabe.get()}.txt", 'w', encoding='utf8')
        Text1.write(Verszahl.get())
        Text1.close()
        Text1 = open(f"C:\\Users\\{Haupt.Dateiort}\\Desktop\\Lieder\\Einbledungen\\{Buchclicked.get()}\\l{Liedeingabe.get()}.txt", 'w', encoding='utf8')
        Text1.write(Streameinblendung.get())
        Text1.close()
        Versbestätigen.config(text="Gespeichert")
        Liedverse_eingabeladen = Liedverse_eingabe.get("1.0","end-1c")
        Streameinblendungladen = Streameinblendung.get()
        Verseingabeladen = Verseingabe.get()
    Liedverse_eingabeladen = Liedverse_eingabe.get("1.0","end-1c")
    Streameinblendungladen = Streameinblendung.get()
    Verseingabeladen = 100
    hi = False
    Verskontrollerdateispeichern.destroy()

def DAtennichtspeicherndef():
    global Liedverse_eingabeladen, Streameinblendungladen, Verseingabeladen, hi
    Liedverse_eingabeladen = Liedverse_eingabe.get("1.0","end-1c")
    Streameinblendungladen = Streameinblendung.get()
    hi = False
    Verseingabeladen = 100
    Verskontrollerdateispeichern.destroy()

def Abbrechendef():
    global Liedverse_eingabeladen, Streameinblendungladen, Verseingabeladen, hi
    Verseingabe.delete(0, "end")
    Verseingabe.insert(END, Verseingabeladen_abbrechen)
    hi = None
    Verskontrollerdateispeichern.destroy()

def Verskontrolleloop():
    global Buchclickedladen, Verszahlladen, Verseingabeladen, Liedeingabeladen, Verse, Verszahlinfo, Streameinblendungladen, Liedverse_eingabeladen, hi, Verskontrollerdateispeichern, Versgespeichert, Verseingabeladen_abbrechen
    Verszahl.get()
    erstart = ""
    if Verseingabe.get() == erstart:
        Verse = 1
    else:
        Verse = Verseingabe.get()
    if not Buchclicked.get() == Buchclickedladen or not Verseingabe.get() == Verseingabeladen or not Liedeingabe.get() == Liedeingabeladen:
        if not Streameinblendungladen == Streameinblendung.get() or not Liedverse_eingabeladen == Liedverse_eingabe.get("1.0","end-1c") or not Verszahlinfo == Verszahl.get():
            Versbestätigen.config(text="Bestätigen")
            if hi:
                Liedverse_eingabeladen = Liedverse_eingabe.get("1.0","end-1c")
                Streameinblendungladen = Streameinblendung.get()
                Verseingabeladen = Verseingabe.get()
                hi = False
            elif hi == None:
                hi = False
            else:
                try:
                    Verskontrollerdateispeichern.destroy()
                except:
                    pass
                Verskontrollerdateispeichern = Toplevel(Haupt.Textmanager)
                Verskontrollerdateispeichern.geometry("600x200")
                Verskontrollerdateispeichern.title("Vers Speichern")
                Verskontrollerdateispeichern.config(bg=Haupt.Textmanager_Hintergrund)
                Dateispeichern = Button(Verskontrollerdateispeichern, font=("Helvetica", 18), text="Speichern", command=Dateispeicherndef)
                Dateispeichern.place(x=50, y=80)
                Dateinichtspeichern = Button(Verskontrollerdateispeichern, font=("Helvetica", 18), text="Nicht Speichern", command=DAtennichtspeicherndef)
                Dateinichtspeichern.place(x=200, y=80)
                Abbrechen = Button(Verskontrollerdateispeichern, font=("Helvetica", 18), text="Abbrechen", command=Abbrechendef)
                Abbrechen.place(x=420, y=80)
                Infoanzeige = Label(Verskontrollerdateispeichern, font=("Helvetica", 15), text="Das Lied wurde noch nicht gespeichert", bg=Haupt.Textmanager_Hintergrund, fg=Haupt.Textmanager_Textfarbe)
                Infoanzeige.place(x=120, y=20)
        else:
            Versgespeichert = Verse
            Versbestätigen.config(text="Bestätigen")
            Streameinblendung.get()
            if len(Liedeingabe.get()) > 0:
                try:
                    Text = open(f"C:\\Users\\{Haupt.Dateiort}\\Desktop\\Lieder\\Buch\\{Buchclicked.get()}\\{Liedeingabe.get()} Vers {Verse}.txt", 'r', encoding='utf8')
                    Textfertig = Text.read()
                    Text.close()
                    Liedverse_eingabe.delete("1.0","end-1c")
                    Liedverse_eingabe.insert(END,Textfertig)
                except:
                    Liedverse_eingabe.delete("1.0","end-1c")
                try:
                    Text1 = open(f"C:\\Users\\{Haupt.Dateiort}\\Desktop\\Lieder\\Versanzahl\\{Buchclicked.get()}\\{Liedeingabe.get()}.txt", 'r', encoding='utf8')
                    text1 = Text1.read()
                    Verszahl.delete(0, "end")
                    Verszahl.insert(0, text1)
                except:
                    Verszahl.delete(0, "end")
                try:
                    Einblendung = open(f"C:\\Users\\{Haupt.Dateiort}\\Desktop\\Lieder\\Einbledungen\\{Buchclicked.get()}\\l{Liedeingabe.get()}.txt", 'r', encoding='utf8')
                    Einblendungfertig = Einblendung.read()
                    Einblendung.close()
                    Streameinblendung.delete(0, "end")
                    Streameinblendung.insert(END,Einblendungfertig)
                except:
                    Streameinblendung.delete(0, "end")
            else:
                Liedverse_eingabe.delete("1.0","end-1c")
                Verszahl.delete(0, "end")
                Streameinblendung.delete(0, "end")
            Liedverse_eingabeladen = Liedverse_eingabe.get("1.0","end-1c")
            Streameinblendungladen = Streameinblendung.get()
            Verseingabeladen_abbrechen = Verseingabe.get()
        Buchclickedladen = Buchclicked.get()
        Verseingabeladen = Verseingabe.get()
        Verszahlladen = Liedeingabe.get()
        Liedeingabeladen = Liedeingabe.get()
        Verszahlinfo= Verszahl.get()
    Liedeingabe.after(100, lambda: Verskontrolleloop())