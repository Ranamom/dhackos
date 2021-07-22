import os
import sys
import platform
import time
import random
from colorama import Fore, Style, init
import subprocess
import signal
from playsound import playsound


def clearScreen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

sr = Style.RESET_ALL
sb = Style.BRIGHT
gr = Fore.GREEN
yw = Fore.YELLOW

init()

modem = 300
offline = False

#def _green():
    #sayshort("\033[1;32;40m")

def modem_char():
    time.sleep(1.0/modem)

def send(text):
    for i in range(0,len(text)):
        sys.stdout.write(text[i])
        sys.stdout.flush()
        modem_char()

def say(text):
    if offline == True: print(text)
    else: send(text+"\n")

def sayshort(text):
    if offline == True:
        sys.stdout.write(text)
        sys.stdout.flush()
    else: send(text)

def intro_nosound():
    clearScreen()
    time.sleep(1)
    print(gr + "Sound Disabled" + sr)
    time.sleep(1)
    sayshort("\033[0;0fMemory check...")
    time.sleep(1.5)
    offline = True
    for i in range(0,31000,800):
        sayshort(str(i) + "\n")
        sayshort("\033[0;0fMemory check...")
    offline = False
    time.sleep(2)
    sayshort(sb + "\033[2;0fBoot Interface")
    time.sleep(1.5)
    cadena = "."
    offline = True
    for character in cadena:
        sayshort(str(character))
        sayshort("\033[2;15f." + "\033[2;16f." + "\033[2;17f." + "\033[2;18f." + "\033[2;19f." + "\033[2;20f." + "\033[2;21f." + "\033[2;22f." + "\033[2;23f." + "\033[2;24f." + "\033[2;25f." + "\033[2;26f." + sr + "[" + gr + "DONE" + sr + "]\n")
    offline = False
    time.sleep(2)
    sayshort(yw + "Loading configuration..." + sr + "[" + gr + "DONE" + sr + "]\n")
    time.sleep(2)


def intro():
        clearScreen()
        time.sleep(1)
        print(gr + "Sound enabled." + sr)
        time.sleep(1)
        if platform.system() == "Linux":
            p = subprocess.Popen('play-audio ' + './sounds/normalmemorycheck1.mp3', shell=True)
            time.sleep(0.3)
        elif platform.system() == "Windows":
            playsound('.\\sounds\\normalmemorycheck1.mp3', block=False)
        #time.sleep(0.3)
        sayshort("\033[0;0fMemory check...")
        time.sleep(1.5)
        offline = True
        #num = random.randint(256, 1024)
        if platform.system() == "Linux":
            p = subprocess.Popen('play-audio ' + './sounds/normalmemorycheck2.mp3', shell=True)
        elif platform.system() == "Windows":
            playsound('.\\sounds\\normalmemorycheck2.mp3', block=False)
        time.sleep(0.3)
        for i in range(0,31000,800):
            sayshort(str(i) + "\n")
            sayshort("\033[0;0fMemory check...")
        offline = False
        time.sleep(2)
        if platform.system() == "Linux":
            p = subprocess.Popen('play-audio ' + './sounds/normalbooting.mp3', shell=True)
        elif platform.system() == "Windows":
            playsound('.\\sounds\\normalbooting.mp3', block=False)
        time.sleep(0.5)
        sayshort(sb + "\033[2;0fBoot Interface")
        time.sleep(1.5)
        cadena = "."
        offline = True
        if platform.system == "Linux":
            p = subprocess.Popen('play-audio ' + './sounds/normaldone.mp3', shell=True)
        elif platform.system() == "Windows":
            playsound('.\\sounds\\normaldone.mp3', block=False)
        for caracter in cadena:
            sayshort(str(caracter))
            sayshort("\033[2;15f." + "\033[2;16f." + "\033[2;17f." + "\033[2;18f." + "\033[2;19f." + "\033[2;20f." + "\033[2;21f." + "\033[2;22f." + "\033[2;23f." + "\033[2;24f." + "\033[2;25f." + "\033[2;26f." + sr + "[" + gr + "DONE" + sr + "]\n")
        offline = False
        time.sleep(2)
        if platform.system() == "Linux":
            p = subprocess.Popen('play-audio ' + './sounds/normalloading.mp3 ./sounds/normaldone.mp3', shell=True)
        elif platform.system() == "Windows":
            playsound('.\\sounds\\normalloading.mp3', block=False)
            playsound('.\\sounds\\normaldone.mp3')
        time.sleep(0.4)
        sayshort(yw + "Loading configuration....." + sr + "[" + gr + "DONE" + sr + "]\n")
        time.sleep(2)
