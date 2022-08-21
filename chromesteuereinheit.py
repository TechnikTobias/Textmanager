import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, WebDriverException
import win32clipboard
import time 
import Haupt
import os
import Einstellungen
def Test01():
    print("halo welt")
    time.sleep(5)
    print("programm ist zuende")
selenium
Dateiort = os.getlogin()
ChromeDatei = open("C:\\Users\\"+Dateiort+"\\Desktop\\Lieder\\Chrome.txt", 'r', encoding='utf8')
Chromöffnen = ChromeDatei.read()
ChromeDatei.close()
try:
    if Chromöffnen == "Wahr":
        options = Options()
        options.add_argument("user-data-dir=C:\\Users\\"+Dateiort+"\\AppData\\Local\\Google\\Chrome\\User Data")
        driver = webdriver.Chrome("C:\\Users\\"+Dateiort+"\\Desktop\\Lieder\\chromedriver", chrome_options=options)
        driver.get("https://studio.youtube.com/channel/UCX5x3cxf1CitE4nfLidoxyw/livestreaming")
        VideobeschreibungDatei = open("C:\\Users\\"+Dateiort+"\\Desktop\\Lieder\\Videobeschreibung.txt", 'r',
                                    encoding='utf8')
        Videobeschreibungaktionvarable = VideobeschreibungDatei.read()
    else:
        Videobeschreibungaktionvarable = "Falsch"
except WebDriverException:
    print("Error")
    Videobeschreibungaktionvarable = "Falsch"


def Videobeschreibung():
    Streamheute = open("C:\\Users\\" + Haupt.Dateiort + "\\Desktop\\Lieder\\" + Einstellungen.Datum + ".txt", 'r',
                       encoding='utf8')
    Stream = Streamheute.read()
    try:
        if Stream == "True":
            eingabe = driver.find_element(By.XPATH,
                "/html/body/ytcp-app/ytls-live-streaming-section/ytls-core-app/div/div[2]/div/ytls-live-dashboard-page-renderer/div[1]/div[2]/ytls-broadcast-list/ytls-broadcast-list-content/div[2]/div/div/ytcp-video-row/div/div[2]/ytcp-video-list-cell-video/div[2]/div[1]/h3/a")
            eingabe.click()
            eingabe2 = driver.find_element(By.XPATH,
                "/html/body/ytcp-app/ytls-live-streaming-section/ytls-core-app/div/div[2]/div/ytls-live-dashboard-page-renderer/div[1]/div[1]/ytls-live-control-room-renderer/div[1]/div[1]/div/ytls-broadcast-metadata/div[2]/ytcp-button/div")
            eingabe2.click()
            time.sleep(2)
            eingabe3 = driver.find_element(By.XPATH,
                "/html/body/ytls-broadcast-edit-dialog/ytcp-dialog/tp-yt-paper-dialog/div[2]/ytcp-navigation/div[2]/iron-pages/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[2]/ytcp-social-suggestions-textbox/ytcp-form-input-container/div[1]/div[2]/div/ytcp-social-suggestion-input/div")
            time.sleep(1)
            eingabe3.clear()
            if len(Haupt.Eingansliedentry2.get()) >= 1:
                Texteingabe = str(
                    "Lieder \nE " + Buch + " " + Dateinen.Einganslied + " Vers " + " " + Dateinen.Eingansliedverse + "\n" + str(
                        Dateinen.Texttietel) + "\n\n\n")
                eingabe3.send_keys(Texteingabe)
            else:
                Texteingabe = str(
                    "Lieder \nE " + Buch + " " + Dateinen.Einganslied + "\n" + str(Dateinen.Texttietel) + "\n\n\n")
                eingabe3.send_keys(Texteingabe)
            if len(Haupt.Textwortliedentry2.get()) >= 1:
                Texteingabe2 = str(
                    "TW " + Buch2 + " " + Dateinen.Textwortlied + " Vers " + " " + Dateinen.Textwortliedverse + "\n" + str(
                        Dateinen.Texttietel2) + "\n\n\n")
                eingabe3.send_keys(Texteingabe2)
            else:
                Texteingabe2 = str("TW " + Buch2 + " " + Dateinen.Textwortlied + "\n" + str(
                    Dateinen.Texttietel2) + "\n\n\n")
                eingabe3.send_keys(Texteingabe2)
            if len(Haupt.Amtswechselentry2.get()) >= 1:
                Texteingabe3 = str(
                    "AW " + Buch3 + " " + Dateinen.Amtswechsel + " Vers " + " " + Dateinen.Amtswechselverse + "\n" + str(
                        Dateinen.Texttietel3) + "\n\n\n")
                eingabe3.send_keys(Texteingabe3)
            else:
                Texteingabe3 = str("AW " + Buch3 + " " + Dateinen.Amtswechsel + "\n" + str(
                    Dateinen.Texttietel3) + "\n\n\n")
                eingabe3.send_keys(Texteingabe3)
            if Haupt.Kinder == "True":
                if len(Haupt.Kinderentry2.get()) >= 1:
                    Texteingabe7 = str(
                        "Kinder " + Buch8 + " " + Dateinen.Kinder + " Vers " + " " + Dateinen.Kinderverse + "\n" + str(
                            Dateinen.Texttietel7) + "\n\n\n")
                    eingabe3.send_keys(Texteingabe7)
                else:
                    Texteingabe7 = str("AW " + Buch8 + " " + Dateinen.Kinder + "\n" + str(
                        Dateinen.Texttietel7) + "\n\n\n")
                    eingabe3.send_keys(Texteingabe7)
            if len(Haupt.Bußliedentry2.get()) >= 1:
                Texteingabe4 = str(
                    "B " + Buch4 + " " + Dateinen.Bußlied + " Vers " + " " + Dateinen.Bußliedverse + "\n" + str(
                    Dateinen.Texttietel4) + "\n\n\n")
                eingabe3.send_keys(Texteingabe4)
            else:
                Texteingabe4 = str("B " + Buch4 + " " + Dateinen.Bußlied + "\n" + str(
                    Dateinen.Texttietel4) + "\n\n\n")
                eingabe3.send_keys(Texteingabe4)
            if len(Haupt.Abendmahliedentry2.get()) >= 1:
                Texteingabe5 = str(
                    "A " + Buch5 + " " + Dateinen.Abendmahlslied + " Vers " + " " + Dateinen.Abendmahlsliedverse + "\n" + str(
                        Dateinen.Texttietel5) + "\n\n\n")
                eingabe3.send_keys(Texteingabe5)
            else:
                Texteingabe5 = str("A " + Buch5 + " " + Dateinen.Abendmahlslied + "\n" + str(
                    Dateinen.Texttietel5) + "\n\n\n")
                eingabe3.send_keys(Texteingabe5)
            if len(Haupt.Schlussliedentry2.get()) >= 1:
                Texteingabe6 = str(
                    "S " + Buch6 + " " + Dateinen.Schlusslied + " Vers " + " " + Dateinen.Schlussliedverse + "\n" + str(
                            Dateinen.Texttietel6) + "\n\n\n")
                eingabe3.send_keys(Texteingabe6)
            else:
                Texteingabe6 = str("S " + Buch6 + " " + Dateinen.Schlusslied + "\n" + str(
                    Dateinen.Texttietel6) + "\n\n\n")
                eingabe3.send_keys(Texteingabe6)
            eingabe3.send_keys(Haupt.Textwortentry.get() + "\n" + Haupt.Textwortentry2.get())
            eingabe4 = driver.find_element(By.XPATH,
                "/html/body/ytls-broadcast-edit-dialog/ytcp-dialog/tp-yt-paper-dialog/div[3]/div/ytcp-button[2]/div")
            eingabe4.click()
            time.sleep(1)
            eingabe5 = driver.find_element(By.XPATH,
                "/html/body/ytcp-app/ytls-live-streaming-section/ytls-core-app/div/div[2]/ytls-navigation/nav/div/div/li/tp-yt-paper-icon-item/div[1]/tp-yt-iron-icon")
            eingabe5.click()
    except NoSuchElementException:
        Errorbild = Toplevel(Haupt.root)
        Errorbild.geometry("560x350+500+400")
        Errorbild.config(bg="black")
        Error = Label(Errorbild, font=("Helvetica", 40),
                      text="Error", bg="black",
                      fg="green", wraplength=560)
        Error.place(x=210, y=0)
        ErrorLabel = Label(Errorbild, font=("Helvetica", 20),
                           text="Dieses Liednummer ist zu Groß oder ist noch nicht im System", bg="black",
                           fg="green", wraplength=560)
        ErrorLabel.place(x=0, y=80)


def stream_planen():
    if Chromöffnen == "Wahr":
        Streamheute = open ("C:\\Users\\"+Haupt.Dateiort+"\\Desktop\\Lieder\\"+Einstellungen.Datum+".txt", 'r',encoding='utf8')
        Stream = Streamheute.read()
        if Stream == "True":
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
            eingabe13.send_keys(Einstellungen.Datum)
            time.sleep(2)
            eingabe14 = driver.find_element(By.XPATH,"/html/body/tp-yt-iron-overlay-backdrop")
            eingabe14.click()
            time.sleep(2)
            eingabe15 = driver.find_element(By.XPATH,
                "/html/body/ytls-broadcast-create-dialog/tp-yt-paper-dialog/div/div[3]/div[2]/div[2]/div[3]/div/ytcp-form-datetime/ytcp-datetime-picker/div/form/ytcp-form-input-container/div[1]/div/tp-yt-paper-input/tp-yt-paper-input-container/div[2]/div/iron-input/input")
            eingabe15.clear()
            time.sleep(2)
            eingabe15.send_keys(Einstellungen.Uhrzeit)
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
                "/html/body/ytcp-app/ytls-live-streaming-section/ytls-core-app/div/div[2]/div/ytls-live-dashboard-page-renderer/div[1]/div[2]/ytls-broadcast-list/ytls-broadcast-list-content/div[2]/div/div/ytcp-video-row[1]/div/div[2]/ytcp-video-list-cell-video/div[2]/div[1]/div")
            eingabe19.click()
            time.sleep(1)
            eingabe20 = driver.find_element(By.XPATH,
                "/html/body/ytcp-text-menu/tp-yt-paper-dialog/tp-yt-paper-listbox/tp-yt-paper-item[2]/ytcp-ve")
            eingabe20.click()
            time.sleep(1)
            driver.get("https://rebrandly.com/links")
            time.sleep(10)
            eingabe21 = driver.find_element(By.XPATH,
                "/html/body/div[1]/div[2]/div[3]/div[2]/ul/li/div/div/div[1]/div/div[1]/div/a")
            eingabe21.click()
            time.sleep(1)
            eingabe22 = driver.find_element(By.XPATH,"/html/body/div[10]/div/div/div/header/div[3]/div[1]/div/span/p")
            eingabe22.click()
            time.sleep(1)
            win32clipboard.OpenClipboard()
            data = win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()
            eingabe23 = driver.find_element(By.XPATH,
                "/html/body/div[10]/div/div/div/header/div[3]/div[1]/div/form/label/div/div/textarea")
            eingabe23.clear()
            eingabe23.send_keys(data)
            eingabe24 = driver.find_element(By.XPATH,
                "/html/body/div[10]/div/div/div/header/div[3]/div[1]/div/form/div/button[1]")
            eingabe24.click()
            time.sleep(4)
            driver.get("https://studio.youtube.com/channel/UCX5x3cxf1CitE4nfLidoxyw/livestreaming")
            Streamheute = open("C:\\Users\\" + Haupt.Dateiort + "\\Desktop\\Lieder\\" + Einstellungen.Datum + ".txt",
                               'w', encoding='utf8')
            Streamheute.write("True")
            Streamnechst = open("C:\\Users\\" + Haupt.Dateiort + "\\Desktop\\Lieder\\" + Einstellungen.Datum2 + ".txt",
                               'w', encoding='utf8')
            Streamnechst.write("False")
            Streamnechst2 = open("C:\\Users\\" + Haupt.Dateiort + "\\Desktop\\Lieder\\" + Einstellungen.Datum3 + ".txt",
                               'w', encoding='utf8')
            Streamnechst2.write("False")
            Streamnechst3 = open("C:\\Users\\" + Haupt.Dateiort + "\\Desktop\\Lieder\\" + Einstellungen.Datum4 + ".txt",
                               'w', encoding='utf8')
            Streamnechst3.write("False")
