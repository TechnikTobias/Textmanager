from onvif import ONVIFCamera

IP = "192.168.178.58"  # Camera IP address
PORT = 8080  # Port
USER = "admin"  # Username
PASS = "4Hasen+Voegel"  # Password

class ptzControl(object):
    def __init__(self):
        super(ptzControl, self).__init__()
        self.mycam = ONVIFCamera(IP,PORT,USER,PASS)
        self.media = self.mycam.create_media_service()
        self.media_profile = self.media.GetProfiles()[0]
        self.ptz = self.mycam.create_ptz_service()
        self.requestg = self.ptz.create_type('GotoPreset')
        self.requestg.ProfileToken = self.media_profile.token

    def goto_preset(self, Position):
        self.requestg.PresetToken = Position
        self.ptz.GotoPreset(self.requestg)

Kamera = ptzControl()
