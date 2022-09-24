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
            driver.get("https://studio.youtube.com/channel/UCX5x3cxf1CitE4nfLidoxyw/livestreaming")
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
        Streamheute = open("C:\\Users\\" + Haupt.Dateiort + "\\Desktop\\Lieder\\" + Zeitgeber.Datum + ".txt", 'r',
                       encoding='utf8')
        Stream = Streamheute.read()
        try:
            if Stream == "True":
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
                einagbe8 = driver.find_element(By.XPATH,
                    "/html/body/ytcp-app/ytls-live-streaming-section/ytls-core-app/div/div[2]/div/ytls-live-dashboard-page-renderer/div[1]/div[2]/ytls-broadcast-list/ytls-broadcast-list-content/div[1]/ytcp-button")
                einagbe8.click()
                time.sleep(2)
                eingabe9 = driver.find_element(By.XPATH,
                    "/html/body/ytcp-app/ytls-popup-container/tp-yt-paper-dialog/ytls-duplicate-broadcast-renderer/div[4]/ytcp-button[2]/div")
                eingabe9.click()
                time.sleep(2)
                eingabe10 = driver.find_element(By.XPATH,
                    "/html/body/ytls-broadcast-create-dialog/tp-yt-paper-dialog/div/div[4]/div/ytcp-button[2]/div")
                eingabe10.click()
                time.sleep(2)
                eingabe11 = driver.find_element(By.XPATH,
                    "/html/body/ytls-broadcast-create-dialog/tp-yt-paper-dialog/div/div[4]/div/ytcp-button[2]/div")
                eingabe11.click()
                time.sleep(2)
                eingabe111 = driver.find_element(By.XPATH,"/html/body/ytls-broadcast-create-dialog/tp-yt-paper-dialog/div/div[3]/div[2]/ytcp-video-visibility-select/div/tp-yt-paper-radio-group/tp-yt-paper-radio-button[2]/div[2]")
                eingabe111.click()
                time.sleep(1)
                eingabe12 = driver.find_element(By.XPATH,
                    "/html/body/ytls-broadcast-create-dialog/tp-yt-paper-dialog/div/div[3]/div[2]/div[2]/div[3]/div/ytcp-form-datetime/ytcp-datetime-picker/div/div/ytcp-text-dropdown-trigger/ytcp-dropdown-trigger/div/div[3]")
                eingabe12.click()
                time.sleep(2)
                eingabe13 = driver.find_element(By.XPATH,
                    "/html/body/ytcp-date-picker/tp-yt-paper-dialog/div/form/tp-yt-paper-input/tp-yt-paper-input-container/div[2]/div/iron-input/input")
                eingabe13.clear()
                time.sleep(2)
                eingabe13.send_keys(Zeitgeber.Datum)
                time.sleep(2)
                eingabe14 = driver.find_element(By.XPATH,"/html/body/tp-yt-iron-overlay-backdrop")
                eingabe14.click()
                time.sleep(2)
                eingabe15 = driver.find_element(By.XPATH,
                    "/html/body/ytls-broadcast-create-dialog/tp-yt-paper-dialog/div/div[3]/div[2]/div[2]/div[3]/div/ytcp-form-datetime/ytcp-datetime-picker/div/div[2]/form/ytcp-form-input-container/div[1]/div/tp-yt-paper-input/tp-yt-paper-input-container/div[2]/div/iron-input/input")
                eingabe15.clear()
                time.sleep(2)
                eingabe15.send_keys(Zeitgeber.Uhrzeit)
                time.sleep(2)
                eingabe17 = driver.find_element(By.XPATH,
                    "/html/body/ytls-broadcast-create-dialog/tp-yt-paper-dialog/div/div[4]/div/ytcp-button[3]/div")
                eingabe17.click()
                time.sleep(4)
                eingabe18 = driver.find_element(By.XPATH,
                    "/html/body/ytcp-app/ytls-live-streaming-section/ytls-core-app/div/div[2]/ytls-navigation/nav/div/div/li/tp-yt-paper-icon-item/div[1]/tp-yt-iron-icon")
                eingabe18.click()
                time.sleep(1)
                eingabe19 = driver.find_element(By.XPATH,
                    "/html/body/ytcp-app/ytls-live-streaming-section/ytls-core-app/div/div[2]/div/ytls-live-dashboard-page-renderer/div[1]/div[2]/ytls-broadcast-list/ytls-broadcast-list-content/div[2]/div/div/   ytcp-video-row[1]/div/div[2]/ytcp-video-list-cell-video/div[2]/div[1]/div")
                eingabe19.click()
                time.sleep(1)
                eingabe20 = driver.find_element(By.XPATH,
                    "/html/body/ytcp-text-menu/tp-yt-paper-dialog/tp-yt-paper-listbox/tp-yt-paper-item[2]/ytcp-ve")
                eingabe20.click()
                time.sleep(1)
                driver.get("https://rebrandly.com/links")
                time.sleep(10)
                eingabe21 = driver.find_element(By.XPATH,
                    "/html/body/div[1]/div[2]/div[2]/div[2]/ul/li/div/div/div[1]/div/div[1]/div/a")
                eingabe21.click()
                time.sleep(1)
                eingabe22 = driver.find_element(By.XPATH,"/html/body/div[13]/div/div/div/header/div[3]/div[1]/div/span/p")
                eingabe22.click()
                time.sleep(1)
                eingabe23 = driver.find_element(By.XPATH,
                    "/html/body/div[13]/div/div/div/header/div[3]/div[1]/div/form/label/div/div/textarea")
                eingabe23.clear()
                eingabe23.send_keys(pyperclip.paste())
                eingabe24 = driver.find_element(By.XPATH,
                    "/html/body/div[13]/div/div/div/header/div[3]/div[1]/div/form/div/button[1]")
                eingabe24.click()
                time.sleep(4)
                driver.get("https://studio.youtube.com/channel/UCX5x3cxf1CitE4nfLidoxyw/livestreaming")
                Videobeschreibungaktionvarable = "Wahr"
