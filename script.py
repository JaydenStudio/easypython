import os
import datetime
import random
from tkinter import Tk
from tkinter import *
import turtle
import webbrowser
import logging
import math
f = False
t = True
echo = print
command = os.system
delf = os.remove
dir = os.listdir
md = os.mkdir
today = datetime.date.today() #print(today)
year = today.year #print(year)
mouth = today.month #print(mouth)
weekday2 = today.weekday() #print(weekday)
isoweekday2 = today.isoweekday() #print(isoweekday)
isoformat2 = today.isoformat() #print(isoformat)
ctime2 = today.ctime() #print(ctime)
raninteger = random.randint #print(raninteger)
ran0t1 = random.random() #print(ran0t1)
window = Tk()
tktico = window.iconbitmap
tkt = window.title
tksize = window.geometry
tkgui = window.mainloop
tkbs = window.resizable
screen = turtle.Screen
#url = "http://google.com"
openurl = webbrowser.open #openurl(url)
opennurl = webbrowser.open_new #opennurl(url)
opennewtab = webbrowser.open_new_tab #opennewtab(url)
pi = math.pi
debugmsg = logging.debug
infomsg = logging.info
warnmsg = logging.warn
errmsg = logging.error
criticalmsg = logging.critical