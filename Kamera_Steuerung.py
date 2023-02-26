from onvif import ONVIFCamera
import onvif
import os 
from threading import *
import tkinter
import Haupt
import Textanzeiger

IP_Adresse = open("C:\\Users\\" +  os.getlogin() + "\\Desktop\\Lieder\\IP-Adresse_Kamera.txt", 'r', encoding='utf8')

IP = IP_Adresse.read()  # Camera IP address
PORT = 8080  # Port
USER = "admin"  # Username
PASS = "admin"

class ptzControl(object):
    def __init__(self):
        super(ptzControl, self).__init__()
        self.mycam = ONVIFCamera(IP,PORT,USER,PASS)
        self.media = self.mycam.create_media_service()
        self.media_profile = self.media.GetProfiles()[0]
        token = self.media_profile.token
        self.ptz = self.mycam.create_ptz_service()
        self.requestg = self.ptz.create_type('GotoPreset')
        self.requestg.ProfileToken = self.media_profile.token

    def goto_preset(self, Position):
        global Errorkamera
        self.requestg.PresetToken = Position
        self.ptz.GotoPreset(self.requestg)



def Kamera_erstellen():
    global Kamera, Ist_Kamer_aktiv, Errorkamera
    try:
        Kamera = ptzControl()
        Ist_Kamer_aktiv = True
    except onvif.exceptions.ONVIFError:
        Ist_Kamer_aktiv = False
        Errorkamera = tkinter.Toplevel(Haupt.Textmanager)
        Errorkamera.geometry("560x350+500+400")
        Errorkamera.config(bg="black")
        Error = tkinter.Button(Errorkamera, font=("Helvetica", 18),
                          text="Erneut versuchen", bg=Haupt.Textmanager_Hintergrund,
                          fg=Haupt.Textmanager_Textfarbe, command= Erneut_verbinden)
        Error.place(x=50, y=0)
        ErrorLabel = tkinter.Label(Errorkamera, font=("Helvetica", 20),
                           text="Es gibt ein problem mit der Kamera", bg=Haupt.Textmanager_Hintergrund,
                           fg=Haupt.Textmanager_Textfarbe, wraplength=560)
        ErrorLabel.place(x=0, y=80)


def Erneut_position():
    Errorkamera.destroy()
    if int(Haupt.Einganslied.Daten_fürTextanderwand[0]) == int(Textanzeiger.Wieoftlied):
        Haupt.Einganslied.Kamerapositiondef()
        Kamera.goto_preset(Haupt.Einganslied.Kameraposition)
    if int(Haupt.Textwortlied.Daten_fürTextanderwand[0]) == int(Textanzeiger.Wieoftlied):
        Haupt.Textwortlied.Kamerapositiondef()
        Kamera.goto_preset(Haupt.Textwortlied.Kameraposition)
    if int(Haupt.Amtswechsellied.Daten_fürTextanderwand[0]) == int(Textanzeiger.Wieoftlied):
        Haupt.Amtswechsellied.Kamerapositiondef()
        Kamera.goto_preset(Haupt.Amtswechsellied.Kameraposition)
    if int(Haupt.Bussslied.Daten_fürTextanderwand[0]) == int(Textanzeiger.Wieoftlied):
        Haupt.Bussslied.Kamerapositiondef()
        Kamera.goto_preset(Haupt.Bussslied.Kameraposition)
    if int(Haupt.Abendmahlslied.Daten_fürTextanderwand[0]) == int(Textanzeiger.Wieoftlied):
        Haupt.Abendmahlslied.Kamerapositiondef()
        Kamera.goto_preset(Haupt.Abendmahlslied.Kameraposition)
    if int(Haupt.Schlusslied.Daten_fürTextanderwand[0]) == int(Textanzeiger.Wieoftlied):
        Haupt.Schlusslied.Kamerapositiondef()
        Kamera.goto_preset(Haupt.Schlusslied.Kameraposition)
    if int(Haupt.Zusatzlied1.Daten_fürTextanderwand[0]) == int(Textanzeiger.Wieoftlied):
        Haupt.Zusatzlied1.Kamerapositiondef()
        Kamera.goto_preset(Haupt.Zusatzlied1.Kameraposition)
    if int(Haupt.Zusatzlied2.Daten_fürTextanderwand[0]) == int(Textanzeiger.Wieoftlied):
        Haupt.Zusatzlied2.Kamerapositiondef()
        Kamera.goto_preset(Haupt.Zusatzlied2.Kameraposition)
    if int(Haupt.Zusatzlied3.Daten_fürTextanderwand[0]) == int(Textanzeiger.Wieoftlied):
        Haupt.Zusatzlied3.Kamerapositiondef()
        Kamera.goto_preset(Haupt.Zusatzlied3.Kameraposition)
    if int(Haupt.Zusatzlied4.Daten_fürTextanderwand[0]) == int(Textanzeiger.Wieoftlied):
        Haupt.Zusatzlied4.Kamerapositiondef()
        Kamera.goto_preset(Haupt.Zusatzlied4.Kameraposition)

def Kamera_erstellen_Thread():
    Kamera_Thread = Thread(target=Kamera_erstellen)
    Kamera_Thread.start()

def Erneut_verbinden():
    Errorkamera.destroy()
    Kamera_erstellen_Thread()

