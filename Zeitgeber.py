import datetime
Heute = datetime.date.today()

if Heute.weekday() <= 2:
    if Heute.weekday() == 2:
        Jetzt= datetime.datetime.now().strftime("%H")
        if int(Jetzt) < 20:
            Mittwoch = 2
            Uhrzeit = "20:00"
            Sonntag = 6
        else:
            Mittwoch = 6
            Uhrzeit = "9:30"
            Sonntag = 9
    else:
        Mittwoch = 2
        Uhrzeit = "20:00"
        Sonntag =6
elif Heute.weekday() == 6:
    Jetzt = datetime.datetime.now().strftime("%H")
    if int(Jetzt) > 9:
        Mittwoch = 9
        Uhrzeit = "20:00"
        Sonntag =13
    else:
        Mittwoch = 6
        Uhrzeit = "9:30"
        Sonntag = 9
elif Heute.weekday() > 2:
    Mittwoch = 6
    Uhrzeit= "9:30"
    Sonntag = 9
Nächstergotesdienst=Mittwoch - Heute.weekday()
Übernächstergottesdienst=Sonntag - Heute.weekday()
jl = datetime.timedelta(Nächstergotesdienst)
jl4 = datetime.timedelta(Übernächstergottesdienst)
jl5 = datetime.timedelta(7)
Aktuell=datetime.datetime.now()
jn=(Aktuell +jl)
jn2 =(Aktuell+jl4)
jn3 = (jn + jl5)
jn4 = (jn2 + jl5)
Datum = (jn.strftime("%d.%m.%Y"))

