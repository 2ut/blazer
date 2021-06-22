import os
import string
import random
import time
import datetime
import sys
import keyboard
import os.path
def send():
    time.sleep(0.5)
    print("|", end = "\r")
    time.sleep(0.1)
    print("/", end = "\r")
    time.sleep(0.1)
    print("-", end = "\r")
    time.sleep(0.1)
    print("|", end = "\r")
    time.sleep(0.1)
    print("/", end = "\r")
    time.sleep(0.1)
    print("-", end = "\r")
    time.sleep(0.1)
    print("|", end = "\r")
    time.sleep(0.1)
    print("/", end = "\r")
    time.sleep(0.1)
    print("-", end = "\r")
    time.sleep(0.1)
    print("|", end = "\r")
    time.sleep(0.1)
    print("/", end = "\r")
    time.sleep(0.1)
    print("-", end = "\r")
    time.sleep(0.1)
    print("|", end = "\r")
    time.sleep(0.1)
    print("/", end = "\r")
    time.sleep(0.1)
    print("-", end = "\r")
    time.sleep(0.1)
    print("|", end = "\r")
    time.sleep(0.1)
    print("/", end = "\r")
    time.sleep(0.1)
    print("-", end = "\r")
    time.sleep(0.1)
    print("|", end = "\r")
    time.sleep(0.1)
    print("/", end = "\r")
    time.sleep(0.1)
    print("-", end = "\r")
    time.sleep(0.1)
    print("|", end = "\r")
    time.sleep(0.1)
    print("/", end = "\r")
    time.sleep(0.1)
    print("\u001b[38;5;202mAttack \u001b[38;5;166mSent Succes\u001b[38;5;166msfu\u001b[38;5;130mlly.")
    choices()
def methods():
    print("\u001b[38;5;253m1 - tcp")
    print("\u001b[38;5;253m2 - http")
    choices()
def choices() : 
    choice = input("\u001b[38;5;202mBLA\u001b[38;5;166mZE\u001b[38;5;130mR \u001b[38;5;202m$ \u001b[38;5;202m")
    if choice.startswith((".tcp")):
        send()
        choices()                     
    elif choice.startswith((".http")):
        send()
        choices() 
    elif choice.startswith((".methods")):
        methods()
        choices()   
    elif choice.startswith((".cls")):
        blazer()
        choices()           
    else:
        print("\u001b[38;5;202m" + choice + " \u001b[38;5;166mIs Not\u001b[38;5;202m A Va\u001b[38;5;166mlid \u001b[38;5;130mCommand.\u001b[38;5;202m")
        choices()
        
def blazer() :
    os.system("cls")
    print("")
    print("                                                 \u001b[38;5;130m╔╗ ╦  ╔═╗╔═╗╔═╗╦═╗")
    print("                                                 \u001b[38;5;166m╠╩╗║  ╠═╣╔═╝║╣ ╠╦╝")
    print("                                                 \u001b[38;5;202m╚═╝╩═╝╩ ╩╚═╝╚═╝╩╚═")
    print("                                     \u001b[38;5;202m╔═════════\u001b[38;5;166m═══\u001b[38;5;130m══════════════════════\u001b[38;5;166m══════\u001b[38;5;202m╗")
    print("                                     \u001b[38;5;202m║          \u001b[38;5;130mWELC\u001b[38;5;166mO\u001b[38;5;202mME TO \u001b[38;5;202mBL\u001b[38;5;166mAZ\u001b[38;5;130mER             \u001b[38;5;202m║")
    print("                                     \u001b[38;5;202m╚═════════\u001b[38;5;166m═══\u001b[38;5;130m══════════════════════\u001b[38;5;166m══════\u001b[38;5;202m╝") 
    print("                                     ╚════\u001b[38;5;166m═══════════════\u001b[38;5;202m══════════\u001b[38;5;166m═══════════╝") 
    print("")
blazer()
choices()
