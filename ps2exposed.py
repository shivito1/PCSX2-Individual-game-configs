# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "johns"
__date__ = "$May 19, 2019 1:05:56 AM$"

import subprocess
import csv
import os
import sys
from tkinter import *
from tkinter import filedialog
from shutil import copyfile
import keyboard 
import time
timeout = time.time() + 5
print(timeout)
print(time.time())
class Mainisgo:
    def __init__(self,root):
        def close(event):
            root.withdraw() # if you want to bring it back
            sys.exit()
        root.bind('<Escape>', close)
        self.root = root
        root.wm_title("JSPrograms")
		
        w = 500 # width for the Tk root
        h = 250 # height for the Tk root

        # get screen width and height
        ws = root.winfo_screenwidth() # width of the screen
        hs = root.winfo_screenheight() # height of the screen

        # calculate x and y coordinates for the Tk root window
        x = (ws) / (3)
        y = (hs) / (3)

        # set the dimensions of the screen 
        # and where it is placed
        root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        root.configure(background="#4d4dff")

        # If this value is set to 1 then C:Drive will be added to backup
        self.Scanc = 0

        self.formtable()#main application GUI
        self.romdir = ''
        self.savedir = ''
        self.pcsx2location= ''
        if os.path.isdir('shivito123iniBK'): # Create ini backups folder
            print('iniBK dir exists')
        else:
            os.makedirs('shivito123iniBK')
            
        if os.path.exists('shivito123rom.txt'): # This is checking for ini filepath
            m = open('shivito123rom.txt','r')
            self.romdir = m.read()
            m.close()
            self.dir_rom() #sets ini file path globle variable 
            
        if os.path.exists('shivito123ini.txt'): # this is checking for rom dir
            m = open('shivito123ini.txt','r')
            self.savedir = m.read() 
            m.close()
        self.root.mainloop()
    def pcsx_2(self): # set pcsx2 location
        if self.pcsx2location != '':
            file_path = self.pcsx2location
            print("later")
        else:
            file_path = filedialog.askopenfilename()
            m = open('shivito123pcsx2.txt','w')
            m.write(file_path)
            m.close()
            self.pcsx2location = file_path
    def dir_rom(self): #set rom dir and creates txt file to read on next use
        if self.romdir == '':
            file_path = filedialog.askdirectory()
            m = open('shivito123rom.txt','w')
            m.write(file_path)
            m.close()
            roms = os.walk(file_path)
            for root,dir,files in roms:
                for filename in files:
                    self.listbox.insert(END,filename)
        else:
            roms = os.walk(self.romdir)
            for root,dir,files in roms:
                for filename in files:
                    self.listbox.insert(END,filename)
    def save_config(self): # Copy current ini from pcsx2ini 
        if self.savedir != '':
            file_path = self.savedir
            print("later")
        else:
            file_path = filedialog.askdirectory()
            m = open('shivito123ini.txt','w')
            m.write(file_path)
            m.close()
            self.savedir = file_path
        self.listbox.get
        roms = os.walk(file_path)
        set = self.listbox.get(ACTIVE)
        if os.path.isdir('shivito123iniBK'+'\\'+set):
            for root,dir,file in roms: #copy the files to new folder
                for filename in file:
                    if filename != "LilyPad.ini":
                        copyfile(root +'\\' +filename,'shivito123iniBK'+'\\'+set+'\\'+filename)
        else:
            os.makedirs('shivito123iniBK'+'\\'+set)
            for root,dir,file in roms: #copy the files to new folder
                for filename in file:
                    if filename != "LilyPad.ini":
                        copyfile(root +'\\' +filename,'shivito123iniBK'+'\\'+set+'\\'+filename)
        
    def dir_ini(self): #set location of ini and save location to txt file for next use
        file_path = filedialog.askdirectory()
        m = open('shivito123ini.txt','w')
        m.write(file_path)
        m.close()
        self.savedir = file_path
    def formtable(self): # GUI items
        frame = Frame(self.root)
        frame.pack(fill=BOTH)
        
        bottomframe = Frame(self.root)
        bottomframe.pack( side = BOTTOM ,fill=BOTH)
        btnpcsx2 = Button(frame,text="PCSX2.exe location?",command=self.pcsx_2)
        btnpcsx2.pack(side=LEFT,fill=BOTH)
        x = Button(frame, text="Select rom directory!",command=self.dir_rom)
        x.pack(side=LEFT,fill=BOTH)
        inidir = Button(frame, text="Select ini directory",command=self.dir_ini)
        inidir.pack(side=LEFT,fill=BOTH)
        save = Button(frame, text="Save config here",command=self.save_config)
        save.pack(side=LEFT,fill=BOTH) 
        self.listbox = Listbox(bottomframe,bg="silver")
        self.listbox.pack(fill=BOTH)
if __name__ == "__main__":
    
    try:
        print(sys.argv[1:])
        print(sys.argv[1])
    except IndexError:
        Mainisgo(Tk())
    
#    inidir = os.walk(r'C:\Users\johns\Documents\PCSX2\inis_1.4.0')
    #for root,dir,files in inidir:
   #     for filename in files:
  #          ini = open(root +'\\'+filename,"r")
 #           mp = ini.read()
#            ini.close()


    #name = input("John S shivito Profile Manger! ")
    
    #subprocess.call('pcsx21.exe "' + sys.argv[1] + '" ' + sys.argv[2] + ' ' + sys.argv[3])
    try:
        try:
            x = open('shivito123pcsx2.txt','r')
            pcsx2location = x.read()
            x.close()
            print(pcsx2location+'\\'+'pcsx2.exe "')
        except:
            print('PCSX2.exe dir not set')
        print(pcsx2location)
        x = open('shivito123ini.txt','r')
        m = x.read()
        x.close()
        print('shivito123iniBK'+'\\'+os.path.basename(sys.argv[1]))
        dir_path = os.path.dirname(os.path.realpath(__file__))
        if os.path.isdir('shivito123iniBK'+'\\'+os.path.basename(sys.argv[1])):
            moveini = os.walk('shivito123iniBK'+'\\'+os.path.basename(sys.argv[1]))
            for root,dirs,files in moveini:
                for filename in files:
                    if filename != "LilyPad.ini":
                        copyfile(root +'\\' +filename,m+'\\'+filename)
            print(os.path.basename(sys.argv[1]))
#Testing key press----------------------------------------------------------------------------------
         # using module keyboard
        while True:  # making a loop
            try:  # used try so that if user pressed other than the given key error will not be shown
                if time.time() <= timeout:
                    if keyboard.is_pressed('l'):  # if key 'q' is pressed 
                        print(pcsx2location+' "' + sys.argv[1] + '" ' + sys.argv[3])
                        subprocess.Popen(pcsx2location+' "' + sys.argv[1] + '" ' + sys.argv[3]) #play the fucking game!
                        Mainisgo(Tk())
                        break  # finishing the loop
                    elif keyboard.is_pressed('z'):
                        subprocess.Popen(pcsx2location+' "' + sys.argv[1] + '" ' + sys.argv[2] + " " + sys.argv[3])
                        break
                    else:
                        pass
                else:
                    subprocess.call(pcsx2location+' "' + sys.argv[1] + '" ' + sys.argv[2] + " " + sys.argv[3])
                    break
            except:
                break  # if user pressed a key other than the given key the loop will break
            #Testing key press----------------------------------------------------------------------------------
        

    except:
        print(Exception)
