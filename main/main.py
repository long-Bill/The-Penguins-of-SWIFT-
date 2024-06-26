#!/usr/bin/python3


import subprocess
import os
import sys
import distro

############### Main ###########################
gameStatus = True
script_directory = os.path.dirname(os.path.abspath(sys.argv[0]))
systemDistro = distro.name(pretty=True)


'''
For binary mode
#script_directory = sys.executable

#script_directory = os.path.split(script_directory)[0]
'''
inputLoop = True
subprocess.run(['clear'])
while(inputLoop):
    print("**************************************************************")
    print("*       Dependencies need to be installed to start game      *")
    print("*                         Continue?                          *")
    print("**************************************************************")
    install = input("Please select Yes (y) or No (n): ")
    if (install == 'y' or install == 'Y' or install == 'yes' or install == 'Yes'):
        subprocess.run(['clear'])
        inputLoop = False
        ####Install dependencies
        print("HE SAID YES")
    elif (install == 'n' or install == 'N' or install == 'no' or install == 'No'):
        subprocess.run(['clear'])
        print("Exiting...")
        sys.exit()
    else:
        subprocess.run(['clear'])
        print("Input error: incorrect input, please try again")
tkinterPip = subprocess.run(
            ['sudo', 'apt', 'install', 'python3-tk','python3-pip','python3-dev', '-y'], capture_output=True, text=True)

p = subprocess.run(['sudo','pip','install','docker','pexpect','paramiko','pillow'],capture_output=True)
if "Kali" in systemDistro:
    d = subprocess.run(['sudo', 'apt-get', 'install', 'docker.io', '-y'],
                                capture_output=True, text=True)
    print(d.stdout)
else:
    d = subprocess.run(['sudo', 'apt-get', 'install', 'docker-ce', 'docker-ce-cli', 'containerd.io', 'docker-buildx-plugin', 'docker-compose-plugin', '-y'],
                                capture_output=True, text=True)

from tkinter import *
import docker
from PIL import ImageTk, Image
#Change to clean up function, dependencies will be installed in the beginning
def dependencies(root):
    print("********Installing dependencies*********")
    update = subprocess.run(
        ['sudo', 'apt', 'update', '-y'], capture_output=True, text=True)
    package = subprocess.run(['grep', 'command not found'],
                             capture_output=True, text=True, input=update.stdout)

    # Installs packages using YUM if it isn't a Debian based distro
    if (update.returncode == 1 and package.returncode == 1):
        print("I am RHEL-based, WORK IN PROGRESS ONLY PLAYABLE ON DEBIAN-BASED SYSTEMS")
        update = subprocess.run(
            ['sudo', 'yum', 'update', '-y'], capture_output=True, text=True)
        root.destroy()

    else:
        username = os.environ['USER']
        addDocker = subprocess.run(['sudo','usermod','-aG','docker',f'{username}'],capture_output=True,text=True)
        #changeShell = subprocess.run(['newgrp','docker'],capture_output=True,text=True)
        roundContainer = subprocess.run(['sudo','docker','ps','--filter','name=^round','-aq'],capture_output=True,text=True)
        subprocess.run(['xargs','sudo','docker','rm','--force'],capture_output=True,text=True, input=roundContainer.stdout)

        
        client = docker.from_env()
        
        iList = client.images.list()
        for image in iList:
            name = image.tags[0]
            if (("round" in name) or ("ubuntu" in name)):
                print(image.id)
                client.images.remove(image.id,force=True)
                
        root.destroy()
        subprocess.run(['clear'])
def quitGame(gui):
    gui.destroy()
    sys.exit()

def closing_menu():
        if (messagebox.askokcancel("Quit","Are you sure?")):
            quitGame(menu)


menu = Tk()
menu.protocol("WM_DELETE_WINDOW" , closing_menu)

menu.title('The Penguins of SWIFT')

img = PhotoImage(file=f"{script_directory}/assets/penguinStart.png")
img = img.subsample(5)

menu.config(background="#303030")
w = 600
h = 600
ws = menu.winfo_screenwidth()
hs = menu.winfo_screenheight()

x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

menu.geometry('%dx%d+%d+%d' % (w, h, x, y))
title = Label(menu, text="The Penguins Of SWIFT", font=("Monospace",25),bg="#303030",fg="white")
picture = Label(menu, image= img,bg="#303030")
title.place(relx=0.5, rely=0.55, anchor='center')
picture.place(relx=0.5, rely=0.25, anchor='center')
start = Button(menu, text='Start!',
               command=lambda: dependencies(menu), height=2, width=10,bg="#ffab40",foreground="white")
start.place(relx=0.30, rely=0.75, anchor='center')

quit = Button(menu,
              text='Quit',
              command=lambda: quitGame(menu),
              height=2, width=10,bg="#ffab40",foreground="white"
              )
quit.place(relx=0.70,
           rely=0.75,
           anchor='center'
           )

menu.mainloop()
from round import *

if (gameStatus):
    
    roundDirectory = f'{script_directory}/rounds/'
    numberOfDirectory = (len(next(os.walk(roundDirectory))[1]))
    

    roundsCompleted = 0
    #Actual GAME
    for rIndex in range(0,numberOfDirectory):
        subprocess.run(['echo','Creating Image, please wait.'])
        roundClass = globals()[f'round{rIndex}']
        currentRound  = roundClass(rIndex,script_directory)
        
        
        currentRound.createImage()
        subprocess.run(['clear'])
        currentRound.startGame()
        if(currentRound.quitGame == True):
            subprocess.run(['clear'])
            break

        if (currentRound.roundStatus == True):
             roundsCompleted = roundsCompleted + 1
        subprocess.run(['clear'])

    # For single round testing **BEGIN***
    # currentRound = round13(13,script_directory)
        
        
    # currentRound.createImage()
    # subprocess.run(['clear'])
    # currentRound.startGame()
    # if(currentRound.quitGame == True):
    #     print("hello")
    #     subprocess.run(['clear'])
    #     #break
    
    # if (currentRound.roundStatus == True ):
    #         roundsCompleted = roundsCompleted + 1
    # subprocess.run(['clear'])
    #***End***
    endMenu = Tk()
    endMenu.title('Thank you!')
    w = 550
    h = 500
    ws = endMenu.winfo_screenwidth()
    hs = endMenu.winfo_screenheight()

    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)

    endMenu.geometry('%dx%d+%d+%d' % (w, h, x, y))
    endMenu.configure(bg="#303030")
    img = PhotoImage(file=f"{script_directory}/assets/private.png")
    img = img.subsample(6)
    picture = Label(endMenu, image= img,bg="#303030")
    picture.place(relx=0.5, rely=0.25, anchor='center')
    Progress = Label(endMenu, text=f'Completed rounds: {roundsCompleted} / {numberOfDirectory}', font=("Monospace",25),bg="#303030",fg="green")
    Progress.place(relx= 0.5, rely=0.55, anchor='center')
    thank = Label(endMenu, text="Thank you for playing!", font=("Monospace",20),bg="#303030",fg="white")
    thank.place(relx= 0.5, rely=0.65, anchor='center')
    quit = Button(endMenu,
            text='Quit',
            command=lambda: quitGame(endMenu),
            height=2, width=10,
            bg="#ffab40",foreground="white"
            )
    quit.place(relx=0.5,
            rely=0.80,
            anchor='center'
            )

    endMenu.mainloop() 
        



