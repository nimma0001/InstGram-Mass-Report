from time import sleep
from webbot import *
import pyautogui
import random

listofoption = {
    "Suicide, self-injury or eating disorders": '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div[3]/button[3]',
    "Nudity or sexual activity":'/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div[3]/button[5]',
    "Hate speech or symbols":'/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div[3]/button[6]',
    "Bullying or harassment":'/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div[3]/button[8]',
    "Scam or fraud":'/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div[3]/button[10]'
    }

listofoptionnum = {
    "1": '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div[3]/button[3]',
    "2":'/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div[3]/button[5]',
    "3":'/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div[3]/button[6]',
    "4":'/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div[3]/button[8]',
    "5":'/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div[3]/button[10]'
    }

Nudity = ["Nudity or pornography", "Sexual exploitation or solicitation", "Sharing private images", "Involves a child"]
bull = ['Me', "Someone I know", "Someone else"]
def runreport(upfile, typeof, reprtn, rest):
    typereport = listofoptionnum[typeof[0]]
    if typeof[0] == "Nudity or sexual activity":
        typeof[1] == Nudity[typeof[1]]
    if typeof[0] == "Bullying or harassment":
        typeof[1] == bull[typeof[1]]
    for l in upfile:
        print(l['ac'])
        username=l['ac']        
        password=l['ps']
        app = Browser()
        app.go_to("instagram.com/accounts/login/")
        sleep(2)
        app.type(username, into='Phone number, username, or email')
        sleep(0.5)
        app.press(app.Key.TAB)
        sleep(0.3)
        app.type(password, into='Password')
        app.press(app.Key.ENTER)
        sleep(int(rest))
        app.go_to("https://www.instagram.com/%s/" % reprtn)
        sleep(10)
        #/html/body/div/div/div/div/div/div/div/div/div/div[2]/div[2]/section/main/div/header/section/div/div[2]
        #app.click(xpath='//*[@id="react-root"]/section/main/div/header/section/div[1]/div/button')
        app.click(xpath='//button[@class="_abl-"]')#oprn asetting
        sleep(1)
        app.click(text='Report')
        # app.click(xpath='//*[@id="mount_0_0_s9"]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div/button[3]')
        sleep(1)
        #app.click(xpath='//*[@id="mount_0_0_Zd"]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div[3]/button[2]/div')
        app.click(text='Report Account')
        sleep(1)
        app.click(xpath='/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div[3]/button[1]')
        # # app.click(xpath='//div[@class="_ab8w  _ab94 _ab99 _ab9f _ab9m _ab9o _abcm"]')
        sleep(1)
        app.click(xpath=typereport)
        sleep(2)
        if (typeof[0] == "1" or typeof[0] == "3"):
            app.click(text='submit report')
            sleep(1)
            app.click(text='Close')
        elif typeof[0] == "5":
            app.click(text='Close')
        elif typeof[0] == "2":
            app.click(text=typeof[1])
            sleep(1)
            app.click(text='submit report')
            sleep(1)
            app.click(text='Close')
        elif typeof[0] == "4":
            sleep(2)
            if typeof[1] == 'Me':
                app.click(xpath='/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div[3]/button[1]')
            elif typeof == 'Someone I know':
                app.click(xpath='/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div[3]/button[2]')
            else:
                app.click(xpath='/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div[3]/button[3]')
            sleep(10)
            app.click(text='submit report')
            sleep(1)
            
            app.click(text='Close')
        sleep(1)
        app.click(xpath='/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[2]/div[1]/div/div/div/div[5]')
        sleep(1)
        app.click(xpath='/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[2]/div[2]/section/main/div/header/section/div[1]/div[2]/button')
        sleep(1)
        app.click(xpath='/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div/button[11]')
        sleep(1)
        pyautogui.keyDown('ctrl')
        sleep(0.25)
        pyautogui.keyDown('w')
        sleep(0.5)
        pyautogui.keyUp('ctrl')
        pyautogui.keyUp('w')
        print('reported from account :', username)