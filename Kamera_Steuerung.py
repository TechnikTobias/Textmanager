from onvif import ONVIFCamera
import os 
from threading import *
import tkinter
import Haupt
import Textanzeiger

IP_Adresse = open("C:\\Users\\" +  os.getlogin() + "\\Desktop\\Lieder\\IP-Adresse_Kamera.txt", 'r', encoding='utf8')

IP = IP_Adresse.read()  # Camera IP address
PORT = 8080  # Port
USER = "admin"  # Username
PASS = "4Hasen+Voegel"  # Password

class ptzControl(object):
    def __init__(self):
        super(ptzControl, self).__init__()
        self.mycam = ONVIFCamera(IP,PORT,USER,PASS)
        # create media service object
        self.media = self.mycam.create_media_service()
        # Get target profile
        self.media_profile = self.media.GetProfiles()[0]
        # Use the first profile and Profiles have at least one
        token = self.media_profile.token
        # PTZ controls  -------------------------------------------------------------
        self.ptz = self.mycam.create_ptz_service()
        # Get available PTZ services
        request = self.ptz.create_type('GetServiceCapabilities')
        Service_Capabilities = self.ptz.GetServiceCapabilities(request)
        # Get PTZ status
        status = self.ptz.GetStatus({'ProfileToken': token})

        # Get PTZ configuration options for getting option ranges
        request = self.ptz.create_type('GetConfigurationOptions')
        request.ConfigurationToken = self.media_profile.PTZConfiguration.token
        ptz_configuration_options = self.ptz.GetConfigurationOptions(request)

        # get continuousMove request -- requestc
        self.requestc = self.ptz.create_type('ContinuousMove')
        self.requestc.ProfileToken = self.media_profile.token
        if self.requestc.Velocity is None:
            self.requestc.Velocity = self.ptz.GetStatus({'ProfileToken': self.media_profile.token}).Position
            self.requestc.Velocity.PanTilt.space = ptz_configuration_options.Spaces.ContinuousPanTiltVelocitySpace[0].URI
            self.requestc.Velocity.Zoom.space = ptz_configuration_options.Spaces.ContinuousZoomVelocitySpace[0].URI

        # get absoluteMove request -- requesta
        self.requesta = self.ptz.create_type('AbsoluteMove')
        self.requesta.ProfileToken = self.media_profile.token
        if self.requesta.Position is None:
            self.requesta.Position = self.ptz.GetStatus(
                {'ProfileToken': self.media_profile.token}).Position
        if self.requesta.Speed is None:
            self.requesta.Speed = self.ptz.GetStatus(
                {'ProfileToken': self.media_profile.token}).Position

        # get relativeMove request -- requestr
        self.requestr = self.ptz.create_type('RelativeMove')
        self.requestr.ProfileToken = self.media_profile.token
        if self.requestr.Translation is None:
            self.requestr.Translation = self.ptz.GetStatus(
                {'ProfileToken': self.media_profile.token}).Position
            self.requestr.Translation.PanTilt.space = ptz_configuration_options.Spaces.RelativePanTiltTranslationSpace[0].URI
            self.requestr.Translation.Zoom.space = ptz_configuration_options.Spaces.RelativeZoomTranslationSpace[0].URI
        if self.requestr.Speed is None:
            self.requestr.Speed = self.ptz.GetStatus(
                {'ProfileToken': self.media_profile.token}).Position

        self.requests = self.ptz.create_type('Stop')
        self.requests.ProfileToken = self.media_profile.token
        self.requestp = self.ptz.create_type('SetPreset')
        self.requestp.ProfileToken = self.media_profile.token
        self.requestg = self.ptz.create_type('GotoPreset')
        self.requestg.ProfileToken = self.media_profile.token
        self.stop()

    # Stop pan, tilt and zoom
    def stop(self):
        self.requests.PanTilt = True
        self.requests.Zoom = True
        print(f"self.request:{self.requests}")
        self.ptz.Stop(self.requests)

    # Continuous move functions
    def perform_move(self, requestc):
        # Start continuous move
        ret = self.ptz.ContinuousMove(requestc)

    def move_tilt(self, velocity):
        self.requestc.Velocity.PanTilt.x = 0.0
        self.requestc.Velocity.PanTilt.y = velocity
        self.perform_move(self.requestc)

    def move_pan(self, velocity):
        self.requestc.Velocity.PanTilt.x = velocity
        self.requestc.Velocity.PanTilt.y = 0.0
        self.perform_move(self.requestc)

    def move_continuous(self, pan, tilt):
        self.requestc.Velocity.PanTilt.x = pan
        self.requestc.Velocity.PanTilt.y = tilt
        self.perform_move(self.requestc)

    def zoom(self, velocity):
        self.requestc.Velocity.Zoom.x = velocity
        self.perform_move(self.requestc)


    # Absolute move functions --NO ERRORS BUT CAMERA DOES NOT MOVE
    def move_abspantilt(self, pan, tilt, velocity):
        self.requesta.Position.PanTilt.x = pan
        self.requesta.Position.PanTilt.y = tilt
        self.requesta.Speed.PanTilt.x = velocity
        self.requesta.Speed.PanTilt.y = velocity
        ret = self.ptz.AbsoluteMove(self.requesta)

    # Relative move functions --NO ERRORS BUT CAMERA DOES NOT MOVE
    def move_relative(self, pan, tilt, velocity):
        self.requestr.Translation.PanTilt.x = pan
        self.requestr.Translation.PanTilt.y = tilt
        self.requestr.Speed.PanTilt = [velocity,velocity]
        # self.requestr.Speed.PanTilt.x = velocity
        # self.requestr.Speed.PanTilt.y = velocity
        self.requestr.Speed.Zoom = 0
        ret = self.ptz.RelativeMove(self.requestr)

    def zoom_relative(self, zoom, velocity):
        self.requestr.Translation.PanTilt.x = 0
        self.requestr.Translation.PanTilt.y = 0
        self.requestr.Translation.Zoom.x = zoom
        self.requestr.Speed.PanTilt.x = 0
        self.requestr.Speed.PanTilt.y = 0
        self.requestr.Speed.Zoom.x = velocity
        ret = self.ptz.RelativeMove(self.requestr)

        # Sets preset set, query and and go to

    def set_preset(self, name):
        self.requestp.PresetName = name
        self.requestp.PresetToken = '100'
        self.preset = self.ptz.SetPreset(self.requestp)  # returns the PresetToken

    def get_preset(self):
        self.ptzPresetsList = self.ptz.GetPresets(self.requestc)

    def goto_preset(self, Position):
        try:
            self.requestg.PresetToken = Position
            self.ptz.GotoPreset(self.requestg)
        except:
            Errorkamera = tkinter.Toplevel(Haupt.Textmanager)
            Errorkamera.geometry("560x350+500+400")
            Errorkamera.config(bg="black")
            Error = tkinter.Button(Errorkamera, font=("Helvetica", 18),
                            text="Erneut versuchen", bg="black",
                            fg="green", command= Erneut_position)
            Error.place(x=50, y=0)
            ErrorLabel = tkinter.Label(Errorkamera, font=("Helvetica", 20),
                            text="Die Kamera kann aktuell sich nicht bewegen\nBitte versuchen sie es öfters und geben sie dem Etwickler bescheid", bg="black",
                            fg="green", wraplength=560)
            ErrorLabel.place(x=0, y=80)

def Kamera_erstellen():
    global Kamera, Ist_Kamer_aktiv, Errorkamera
    try:
        Kamera = ptzControl()
        Ist_Kamer_aktiv = True
    except:
        Ist_Kamer_aktiv = False
        Errorkamera = tkinter.Toplevel(Haupt.Textmanager)
        Errorkamera.geometry("560x350+500+400")
        Errorkamera.config(bg="black")
        Error = tkinter.Button(Errorkamera, font=("Helvetica", 18),
                          text="Erneut versuchen", bg="black",
                          fg="green", command= Erneut_verbinden)
        Error.place(x=50, y=0)
        ErrorLabel = tkinter.Label(Errorkamera, font=("Helvetica", 20),
                           text="Es gibt ein problem mit der Kamera", bg="black",
                           fg="green", wraplength=560)
        ErrorLabel.place(x=0, y=80)


def Erneut_position():
    if int(Haupt.Einganslied.Daten_fürTextanderwand[0]) == int(Textanzeiger.Liedposition):
        Haupt.Einganslied.Kamerapositiondef()
        Kamera.goto_preset(Haupt.Einganslied.Kameraposition)
    if int(Haupt.Textwortlied.Daten_fürTextanderwand[0]) == int(Textanzeiger.Liedposition):
        Haupt.Textwortlied.Kamerapositiondef()
        Kamera.goto_preset(Haupt.Textwortlied.Kameraposition)
    if int(Haupt.Amtswechsellied.Daten_fürTextanderwand[0]) == int(Textanzeiger.Liedposition):
        Haupt.Amtswechsellied.Kamerapositiondef()
        Kamera.goto_preset(Haupt.Amtswechsellied.Kameraposition)
    if int(Haupt.Bussslied.Daten_fürTextanderwand[0]) == int(Textanzeiger.Liedposition):
        Haupt.Bussslied.Kamerapositiondef()
        Kamera.goto_preset(Haupt.Bussslied.Kameraposition)
    if int(Haupt.Abendmahlslied.Daten_fürTextanderwand[0]) == int(Textanzeiger.Liedposition):
        Haupt.Abendmahlslied.Kamerapositiondef()
        Kamera.goto_preset(Haupt.Abendmahlslied.Kameraposition)
    if int(Haupt.Schlusslied.Daten_fürTextanderwand[0]) == int(Textanzeiger.Liedposition):
        Haupt.Schlusslied.Kamerapositiondef()
        Kamera.goto_preset(Haupt.Schlusslied.Kameraposition)
    if int(Haupt.Zusatzlied1.Daten_fürTextanderwand[0]) == int(Textanzeiger.Liedposition):
        Haupt.Zusatzlied1.Kamerapositiondef()
        Kamera.goto_preset(Haupt.Zusatzlied1.Kameraposition)
    if int(Haupt.Zusatzlied2.Daten_fürTextanderwand[0]) == int(Textanzeiger.Liedposition):
        Haupt.Zusatzlied2.Kamerapositiondef()
        Kamera.goto_preset(Haupt.Zusatzlied2.Kameraposition)
    if int(Haupt.Zusatzlied3.Daten_fürTextanderwand[0]) == int(Textanzeiger.Liedposition):
        Haupt.Zusatzlied3.Kamerapositiondef()
        Kamera.goto_preset(Haupt.Zusatzlied3.Kameraposition)
    if int(Haupt.Zusatzlied4.Daten_fürTextanderwand[0]) == int(Textanzeiger.Liedposition):
        Haupt.Zusatzlied4.Kamerapositiondef()
        Kamera.goto_preset(Haupt.Zusatzlied4.Kameraposition)

def Kamera_erstellen_Thread():
    Kamera_Thread = Thread(target=Kamera_erstellen)
    Kamera_Thread.start()

def Erneut_verbinden():
    Errorkamera.destroy()
    Kamera_erstellen()