from threading import Thread
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, WebDriverException
import datetime
import tkinter
import pyperclip
import time 
import Haupt
import os
from Textanzeiger import Textwortübergabe
import Zeitgeber
selenium
Dateiort = os.getlogin()
Videobeschreibungaktionvarable = "Falsch"
Chromeaktuell =  False
Streamüperprüfen = False
def Chromestarten():
    global Videobeschreibungaktionvarable, Chromöffnen, driver, Streamüperprüfen, Chromeupdate, Chromeaktuell
    ChromeDatei = open("C:\\Users\\"+Dateiort+"\\Desktop\\Lieder\\Chrome.txt", 'r', encoding='utf8')
    Chromöffnen = ChromeDatei.read()
    ChromeDatei.close()
    try:
        if Chromöffnen == "Wahr":
            options = Options()
            options.add_argument("user-data-dir=C:\\Users\\"+Dateiort+"\\AppData\\Local\\Google\\Chrome\\User Data")
            driver = webdriver.Chrome("C:\\Users\\"+Dateiort+"\\Desktop\\Lieder\\chromedriver", chrome_options=options)
            driver.get("https://studio.youtube.com/channel/UCX5x3cxf1CitE4nfLidoxyw/livestreaming/manage")
            try:
                time.sleep(3)
                suche = driver.find_element(By.ID,"video-title")
                suche.click()
                endesuche = driver.find_element(By.ID,"entity-back-button")
                time.sleep(8)
                endesuche.click()
                Videobeschreibungaktionvarable = "Wahr"
            except:
                Videobeschreibungaktionvarable = "Falsch"
                print("Kein stream")
            Streamüperprüfen = True
            Chromeaktuell =  True
        else:
            Videobeschreibungaktionvarable = "Falsch"
            Chromeaktuell =  True
    except WebDriverException:
        print("Error")
        Chromeupdate = tkinter.Label(Haupt.Textmanager, font=("Helvetica", 15), text="Bitte Chromedriver aktualiesieren", bg="white", fg="green")
        Chromeupdate.place(y=760)
        Videobeschreibungaktionvarable = "Falsch"
        Chromeaktuell =  False

def Chromestarten_Thread():
    Chromestarten_thread = Thread(target=Chromestarten)
    Chromestarten_thread.start()
Chromestarten_Thread()

def Videobeschreibung_Thread():
    Videobeschreibungthread = Thread(target=Videobeschreibung)
    Videobeschreibungthread.start()
def Videobeschreibung():
    if Videobeschreibungaktionvarable == "Wahr":
        try:
                Texteingabe = ""
                try:
                    Livestreamänderung = open("C:\\Users\\" + Haupt.Dateiort + "\\Desktop\\Lieder\\Livestreamänderung.txt", 'r', encoding='utf8')
                    Livestreamänderung = Livestreamänderung.read()
                    eingabe = driver.find_element(By.XPATH,Livestreamänderung)
                    eingabe.click()
                except:
                    logdatei = open("C:\\Users\\" + Haupt.Dateiort + "\\Desktop\\Lieder\\Logdatei.txt", 'a', encoding='utf8')
                    logdatei.write("Chromedatei.Eingabe Error falsche XPATH\n"+str(datetime.datetime.now().strftime("%d.%m.%Y Datum\n%M.%H Uhr\n")))
                    logdatei.close()
                    Livestreamänderungersatz = open("C:\\Users\\" + Haupt.Dateiort + "\\Desktop\\Lieder\\Livestreamänderungersatz.txt", 'r', encoding='utf8')
                    Livestreamänderungersatz = Livestreamänderungersatz.read()
                    eingabe = driver.find_element(By.ID,Livestreamänderungersatz)
                    eingabe.click()
                try:
                    Öffnen_Einstellungenstream = open("C:\\Users\\" + Haupt.Dateiort + "\\Desktop\\Lieder\\Öffnen_Einstellungenstream.txt", 'r',    encoding='utf8')
                    Öffnen_Einstellungenstream = Öffnen_Einstellungenstream.read()
                    eingabe2 = driver.find_element(By.XPATH,Öffnen_Einstellungenstream)
                    eingabe2.click()
                except:
                    logdatei = open("C:\\Users\\" + Haupt.Dateiort + "\\Desktop\\Lieder\\Logdatei.txt", 'a', encoding='utf8')
                    logdatei.write("Chromedatei.Eingabe Error falsche XPATH\n"+str(datetime.datetime.now().strftime("%d.%m.%Y Datum\n%M.%H Uhr\n")))
                    logdatei.close()
                    Öffnen_Einstellungenstreamersatz = open("C:\\Users\\" + Haupt.Dateiort + "\\Desktop\\Lieder\\Öffnen_Einstellungenstreamersatz.txt", 'r',    encoding='utf8')
                    Öffnen_Einstellungenstreamersatz = Öffnen_Einstellungenstreamersatz.read()
                    eingabe2 = driver.find_element(By.XPATH,Öffnen_Einstellungenstreamersatz)
                    eingabe2.click()
                time.sleep(2)
                try:
                    Texteingabeclick = open("C:\\Users\\" + Haupt.Dateiort + "\\Desktop\\Lieder\\Texteingabe.txt", 'r',    encoding='utf8')
                    Texteingabeclick = Texteingabeclick.read()
                    eingabe3 = driver.find_element(By.XPATH,Texteingabeclick)
                    eingabe3.clear()
                except:
                    logdatei = open("C:\\Users\\" + Haupt.Dateiort + "\\Desktop\\Lieder\\Logdatei.txt", 'a', encoding='utf8')
                    logdatei.write("Chromedatei.Eingabe Error falsche XPATH\n"+str(datetime.datetime.now().strftime("%d.%m.%Y Datum\n%M.%H Uhr\n")))
                    logdatei.close()
                    Texteingabeclick = open("C:\\Users\\" + Haupt.Dateiort + "\\Desktop\\Lieder\\Texteingabe.txt", 'r',    encoding='utf8')
                    Texteingabeclick = Texteingabeclick.read()
                    eingabe3 = driver.find_element(By.XPATH,Texteingabeclick)
                    eingabe3.clear()
                if len(Haupt.Einganslied.Liedversefest) >= 1:
                    Texteingabe1 = str(
                        "\n\n\nLieder für den Gottesdienst \nE " + Haupt.Einganslied.Buch + " " + Haupt.Einganslied.Liednummerfest + " Vers " + " " + Haupt.Einganslied.Liedversefest + "\n" + str(
                            Haupt.Einganslied.Dateiliedtext) + "\n\n\n")
                    Texteingabe = Texteingabe + Texteingabe1
                else:
                    Texteingabe1 = str(
                        "Lieder \nE " + Haupt.Einganslied.Buch + " " + Haupt.Einganslied.Liednummerfest +"\n" + str(Haupt.Einganslied.Dateiliedtext) + "\n\n\n")
                    Texteingabe = Texteingabe + Texteingabe1
                if len(Haupt.Textwortlied.Liedversefest) >= 1:
                    Texteingabe1 = str(
                        "TW " + Haupt.Textwortlied.Buch + " " + Haupt.Textwortlied.Liednummerfest + " Vers " + " " + Haupt.Textwortlied.Liedversefest + "\n" + str(
                            Haupt.Textwortlied.Dateiliedtext) + "\n\n\n")
                    Texteingabe = Texteingabe + Texteingabe1
                else:
                    Texteingabe1 = str("TW " + Haupt.Textwortlied.Buch + " " + Haupt.Textwortlied.Liednummerfest + "\n" + str(
                        Haupt.Textwortlied.Dateiliedtext) + "\n\n\n")
                    Texteingabe = Texteingabe + Texteingabe1
                if len(Haupt.Amtswechsellied.Liedversefest) >= 1:
                    Texteingabe1 = str(
                        "AW " + Haupt.Amtswechsellied.Buch + " " + Haupt.Amtswechsellied.Liednummerfest + " Vers " + " " + Haupt.Amtswechsellied.Liedversefest + "\n" + str(Haupt.Amtswechsellied.Dateiliedtext) + "\n\n\n")
                    Texteingabe = Texteingabe + Texteingabe1
                else:
                    Texteingabe1 = str("AW " + Haupt.Amtswechsellied.Buch + " " + Haupt.Amtswechsellied.Liednummerfest + "\n" + str(
                        Haupt.Amtswechsellied.Dateiliedtext) + "\n\n\n")
                    Texteingabe = Texteingabe + Texteingabe1
                if Haupt.Kinderlied.aktualisieren_wahl == "True":
                    if len(Haupt.Kinderlied.Liedversefest) >= 1:
                        Texteingabe1 = str(
                            "Kinder " + Haupt.Kinderlied.Buch + " " + Haupt.Kinderlied.Liednummerfest + " Vers " + " " + Haupt.Kinderlied.Liedversefest + "\n" + str(
                                Haupt.Kinderlied.Dateiliedtext) + "\n\n\n")
                        Texteingabe = Texteingabe + Texteingabe1
                    else:
                        Texteingabe1 = str("Kinder " + Haupt.Kinderlied.Buch + " " + Haupt.Kinderlied.Liednummerfest + "\n" + str(
                            Haupt.Kinderlied.Dateiliedtext) + "\n\n\n")
                        Texteingabe = Texteingabe + Texteingabe1
                if len(Haupt.Bussslied.Liedversefest) >= 1:
                    Texteingabe1 = str(
                        "B " + Haupt.Bussslied.Buch + " " + Haupt.Bussslied.Liednummerfest + " Vers " + " " + Haupt.Bussslied.Liedversefest + "\n" + str(
                        Haupt.Bussslied.Dateiliedtext) + "\n\n\n")
                    Texteingabe = Texteingabe + Texteingabe1
                else:
                    Texteingabe1 = str("B " + Haupt.Bussslied.Buch + " " + Haupt.Bussslied.Liednummerfest + "\n" + str(
                        Haupt.Bussslied.Dateiliedtext) + "\n\n\n")
                    Texteingabe = Texteingabe + Texteingabe1
                if len(Haupt.Abendmahlslied.Liedversefest) >= 1:
                    Texteingabe1 = str(
                        "A " + Haupt.Abendmahlslied.Buch + " " + Haupt.Abendmahlslied.Liednummerfest + " Vers " + " " + Haupt.Abendmahlslied.Liedversefest + "\n" + str(
                            Haupt.Abendmahlslied.Dateiliedtext) + "\n\n\n")
                    Texteingabe = Texteingabe + Texteingabe1
                else:
                    Texteingabe1 = str("A " + Haupt.Abendmahlslied.Buch + " " +Haupt.Abendmahlslied.Liednummerfest + "\n" + str(
                        Haupt.Abendmahlslied.Dateiliedtext) + "\n\n\n")
                    Texteingabe = Texteingabe + Texteingabe1
                if len(Haupt.Schlusslied.Liedversefest) >= 1:
                    Texteingabe1 = str(
                        "S " + Haupt.Schlusslied.Buch + " " + Haupt.Schlusslied.Liednummerfest + " Vers " + " " + Haupt.Schlusslied.Liedversefest + "\n" + str(
                                Haupt.Schlusslied.Dateiliedtext) + "\n\n\n")
                    Texteingabe = Texteingabe + Texteingabe1
                else:
                    Texteingabe1 = str("S " + Haupt.Schlusslied.Buch + " " + Haupt.Schlusslied.Liednummerfest + "\n" + str(Haupt.Schlusslied.Dateiliedtext) + "\n\n\n")
                    Texteingabe = Texteingabe + Texteingabe1
                Textwortauslesen1 = open("C:\\Users\\" + Dateiort + "\\Desktop\\Lieder\\Textwort.txt", 'r', encoding='utf8')
                Textwortübergabe = Textwortauslesen1.read()
                Textwortauslesen1.close()
                eingabe3.send_keys(Textwortübergabe +"\n\n\n"+ Texteingabe)
                try:
                    Texteingabebestätigen = open("C:\\Users\\" + Haupt.Dateiort + "\\Desktop\\Lieder\\Texteingabebestätigen.txt", 'r',    encoding='utf8')
                    Texteingabebestätigen = Texteingabebestätigen.read()
                    eingabe4 = driver.find_element(By.XPATH,Texteingabebestätigen)
                    eingabe4.click()
                except:
                    Texteingabebestätigen = open("C:\\Users\\" + Haupt.Dateiort + "\\Desktop\\Lieder\\Texteingabebestätigenersatz.txt", 'r',    encoding='utf8')
                    Texteingabebestätigen = Texteingabebestätigen.read()
                    eingabe4 = driver.find_element(By.XPATH,Texteingabebestätigen)
                    eingabe4.click()
                time.sleep(1)
                try:
                    Texteingabeende = open("C:\\Users\\" + Haupt.Dateiort + "\\Desktop\\Lieder\\Texteingabeende.txt", 'r',    encoding='utf8')
                    Texteingabeende = Texteingabeende.read()
                    eingabe5 = driver.find_element(By.XPATH,Texteingabeende)
                    eingabe5.click()
                except:
                    Texteingabeendeersatz = open("C:\\Users\\" + Haupt.Dateiort + "\\Desktop\\Lieder\\Texteingabeendeersatz.txt", 'r',    encoding='utf8')
                    Texteingabeendeersatz = Texteingabeendeersatz.read()
                    eingabe5 = driver.find_element(By.XPATH,Texteingabeendeersatz)
                    eingabe5.click()
        except NoSuchElementException:
            Errorbild = tkinter.Toplevel(Haupt.Textmanager)
            Errorbild.geometry("560x350+500+400")
            Errorbild.config(bg="black")
            Error = tkinter.Label(Errorbild, font=("Helvetica", 40),
                          text="Error", bg="black",
                          fg="green", wraplength=560)
            Error.place(x=210, y=0)
            ErrorLabel = tkinter.Label(Errorbild, font=("Helvetica", 20),
                           text="Es gibt ein Problem mit dem Browser", bg="black",
                           fg="green", wraplength=560)
            ErrorLabel.place(x=0, y=80)

def Stream_planen_Thread():
    stream_erstellen= Thread(target=stream_planen)
    stream_erstellen.start()
def stream_planen():
    global Videobeschreibungaktionvarable
    if Chromöffnen == "Wahr":
        if Streamüperprüfen == True:
            if Videobeschreibungaktionvarable == "Wahr":
                print("stream exestiert")
            else:
                Stream_erstellen = open("C:\\Users\\" + Haupt.Dateiort + "\\Desktop\\Lieder\\Stream_erstellen.txt", 'r', encoding='utf8')
                Stream_erstellen = Stream_erstellen.read()
                eingabe8 = driver.find_element(By.XPATH,Stream_erstellen)
                eingabe8.click()
                time.sleep(2)
                Stream_erstellen_details = open("C:\\Users\\" + Haupt.Dateiort + "\\Desktop\\Lieder\\Stream_erstellen_details.txt", 'r', encoding='utf8')
                Stream_erstellen_details = Stream_erstellen_details.read()
                eingabe9 = driver.find_element(By.XPATH,Stream_erstellen_details)
                eingabe9.click()
                time.sleep(2)
                Stream_erstellen_anpassen = open("C:\\Users\\" + Haupt.Dateiort + "\\Desktop\\Lieder\\Stream_erstellen_anpassen.txt", 'r', encoding='utf8')
                Stream_erstellen_anpassen = Stream_erstellen_anpassen.read()
                eingabe10 = driver.find_element(By.XPATH,Stream_erstellen_anpassen)
                eingabe10.click()
                time.sleep(2)
                Stream_erstellen_sichtbarkeit = open("C:\\Users\\" + Haupt.Dateiort + "\\Desktop\\Lieder\\Stream_erstellen_sichtbarkeit.txt", 'r', encoding='utf8')
                Stream_erstellen_sichtbarkeit = Stream_erstellen_sichtbarkeit.read()
                eingabe11 = driver.find_element(By.XPATH,Stream_erstellen_sichtbarkeit)
                eingabe11.click()
                time.sleep(2)
                Stream_erstellen_sichtbarkeit_nicht_gelistet = open("C:\\Users\\" + Haupt.Dateiort + "\\Desktop\\Lieder\\Stream_erstellen_sichtbarkeit_nicht_gelistet.txt", 'r', encoding='utf8')
                Stream_erstellen_sichtbarkeit_nicht_gelistet = Stream_erstellen_sichtbarkeit_nicht_gelistet.read()
                eingabe111 = driver.find_element(By.XPATH,Stream_erstellen_sichtbarkeit_nicht_gelistet)
                eingabe111.click()
                time.sleep(1)
                Stream_erstellen_eingabe_datum = open("C:\\Users\\" + Haupt.Dateiort + "\\Desktop\\Lieder\\Stream_erstellen_eingabe_datum.txt", 'r', encoding='utf8')
                Stream_erstellen_eingabe_datum = Stream_erstellen_eingabe_datum.read()
                eingabe12 = driver.find_element(By.XPATH,Stream_erstellen_eingabe_datum)
                eingabe12.click()
                time.sleep(2)
                Stream_erstellen_datum = open("C:\\Users\\" + Haupt.Dateiort + "\\Desktop\\Lieder\\Stream_erstellen_datum.txt", 'r', encoding='utf8')
                Stream_erstellen_datum = Stream_erstellen_datum.read()
                eingabe13 = driver.find_element(By.XPATH,Stream_erstellen_datum)
                eingabe13.clear()
                time.sleep(2)
                eingabe13.send_keys(Zeitgeber.Datum)
                time.sleep(2)
                Stream_erstellen_hintergrund = open("C:\\Users\\" + Haupt.Dateiort + "\\Desktop\\Lieder\\Stream_erstellen_hintergrund.txt", 'r', encoding='utf8')
                Stream_erstellen_hintergrund = Stream_erstellen_hintergrund.read()
                eingabe14 = driver.find_element(By.XPATH,Stream_erstellen_hintergrund)
                eingabe14.click()
                time.sleep(2)
                Stream_erstellen_uhrzeit = open("C:\\Users\\" + Haupt.Dateiort + "\\Desktop\\Lieder\\Stream_erstellen_uhrzeit.txt", 'r', encoding='utf8')
                Stream_erstellen_uhrzeit = Stream_erstellen_uhrzeit.read()
                eingabe15 = driver.find_element(By.XPATH,Stream_erstellen_uhrzeit)
                eingabe15.clear()
                time.sleep(2)
                eingabe15.send_keys(Zeitgeber.Uhrzeit)
                time.sleep(2)
                Stream_erstellen_sichtbarkeit_fertig = open("C:\\Users\\" + Haupt.Dateiort + "\\Desktop\\Lieder\\Stream_erstellen_sichtbarkeit_fertig.txt", 'r', encoding='utf8')
                Stream_erstellen_sichtbarkeit_fertig = Stream_erstellen_sichtbarkeit_fertig.read()
                eingabe17 = driver.find_element(By.XPATH,Stream_erstellen_sichtbarkeit_fertig)
                eingabe17.click()
                time.sleep(4)
                Texteingabeende = open("C:\\Users\\" + Haupt.Dateiort + "\\Desktop\\Lieder\\Texteingabeende.txt", 'r',    encoding='utf8')
                Texteingabeende = Texteingabeende.read()
                eingabe18 = driver.find_element(By.XPATH,Texteingabeende)
                eingabe18.click()
                time.sleep(1)
                Stream_erstellen_einstellungen = open("C:\\Users\\" + Haupt.Dateiort + "\\Desktop\\Lieder\\Stream_erstellen_einstellungen.txt", 'r', encoding='utf8')
                Stream_erstellen_einstellungen = Stream_erstellen_einstellungen.read()
                eingabe19 = driver.find_element(By.XPATH,Stream_erstellen_einstellungen)
                eingabe19.click()
                time.sleep(1)
                Stream_erstellen_kopieren = open("C:\\Users\\" + Haupt.Dateiort + "\\Desktop\\Lieder\\Stream_erstellen_kopieren.txt", 'r', encoding='utf8')
                Stream_erstellen_kopieren = Stream_erstellen_kopieren.read()
                eingabe20 = driver.find_element(By.XPATH,Stream_erstellen_kopieren)
                eingabe20.click()
                time.sleep(1)
                driver.get("https://rebrandly.com/links")
                time.sleep(10)
                eingabe21 = driver.find_element(By.XPATH,
                    "/html/body/div[1]/div[2]/div[2]/div[2]/ul/li/div/div/div[1]/div/div[1]/div/a")
                eingabe21.click()
                time.sleep(1)
                eingabe22 = driver.find_element(By.XPATH,"/html/body/div[14]/div/div/div/header/div[3]/div[1]/div/span/p")
                eingabe22.click()
                time.sleep(1)
                eingabe23 = driver.find_element(By.XPATH,
                    "/html/body/div[14]/div/div/div/header/div[3]/div[1]/div/form/label/div/div/textarea")
                eingabe23.clear()
                eingabe23.send_keys(pyperclip.paste())
                eingabe24 = driver.find_element(By.XPATH,
                    "/html/body/div[14]/div/div/div/header/div[3]/div[1]/div/form/div/button[1]")
                eingabe24.click()
                time.sleep(4)
                driver.get("https://studio.youtube.com/channel/UCX5x3cxf1CitE4nfLidoxyw/livestreaming/manage")
                Videobeschreibungaktionvarable = "Wahr"
