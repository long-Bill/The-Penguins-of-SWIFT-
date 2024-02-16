#!/usr/bin/python3

'''
   Modules/Things to add 

      X Command to update linux system
   Add functionality to add docker to system repository
      X Command to install python tkinter
      X Command to install Docker 
   Pip install Docker api
   https://stackoverflow.com/questions/61698133/docker-py-permissionerror13 --> Add user to docker group
   Test container capabilities and how python interacts with containers
   https://stackoverflow.com/questions/34051747/get-environment-variable-from-docker-container 
'''

from tkinter import *
import subprocess
import os
import re
import sys
from round import *

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
        tkinterPip = subprocess.run(
            ['sudo', 'apt', 'install', 'python-tk','python3-pip','python-dev', '-y'], capture_output=True, text=True)
        d = subprocess.run(['sudo', 'apt-get', 'install', 'docker-ce', 'docker-ce-cli', 'containerd.io', 'docker-buildx-plugin', 'docker-compose-plugin', '-y'],
                                capture_output=True, text=True)
        subprocess.run(['sudo','pip','install','docker','pexpect'],capture_output=True)

        
        roundContainer = subprocess.run(['docker','ps','--filter','name=^round','-aq'],capture_output=True,text=True)
        subprocess.run(['xargs','docker','rm','--force'],capture_output=True,text=True, input=roundContainer.stdout)

        
        client = docker.from_env()
        
        iList = client.images.list()
        for image in iList:
            name = image.tags[0]
            if (("round" in name) or ("ubuntu" in name)):
                print(image.id)
                client.images.remove(image.id,force=True)
                
        root.destroy()
        subprocess.run(['clear'])
        


############### Main ###########################
gameStatus = True


def quitGame(gui):
    gui.destroy()
    sys.exit()

def closing_menu():
        if (messagebox.askokcancel("Quit","Are you sure?")):
            quitGame(menu)


menu = Tk()
menu.protocol("WM_DELETE_WINDOW" , closing_menu)

menu.title('The Penguins of SWIFT')
w = 500
h = 500
ws = menu.winfo_screenwidth()
hs = menu.winfo_screenheight()

x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

menu.geometry('%dx%d+%d+%d' % (w, h, x, y))

start = Button(menu, text='Start!',
               command=lambda: dependencies(menu), height=2, width=10)
start.place(relx=0.5, rely=0.55, anchor='center')

quit = Button(menu,
              text='Quit',
              command=lambda: quitGame(menu),
              height=2, width=10
              )
quit.place(relx=0.5,
           rely=0.70,
           anchor='center'
           )

menu.mainloop()


if (gameStatus):
    script_directory = os.path.dirname(os.path.abspath(sys.argv[0]))
    roundDirectory = f'{script_directory}/rounds/'
    numberOfDirectory = (len(next(os.walk(roundDirectory))[1]))
    

    roundsCompleted = 0
    #Actual GAME
    # for rIndex in range(0,numberOfDirectory):
    #     subprocess.run(['echo','Creating Image, please wait.'])
    #     roundClass = globals()[f'round{rIndex}']
    #     currentRound  = roundClass(rIndex,script_directory)
        
        
    #     currentRound.createImage()
    #     subprocess.run(['clear'])
    #     currentRound.startGame()
    #     if(currentRound.quitGame == True):
    #         subprocess.run(['clear'])
    #         break

    #     if (currentRound.roundStatus == True):
    #          roundsCompleted = roundsCompleted + 1
    #     subprocess.run(['clear'])

    # For single round testing **BEGIN***
    currentRound = round10(10,script_directory)
        
        
    currentRound.createImage()
    subprocess.run(['clear'])
    currentRound.startGame()
    if(currentRound.quitGame == True):
        print("hello")
        #subprocess.run(['clear'])
        #break
    
    if (currentRound.roundStatus == True ):
            roundsCompleted = roundsCompleted + 1
    #subprocess.run(['clear'])
    #***End***
    endMenu = Tk()

    endMenu.title('End of Game')
    w = 500
    h = 250
    ws = endMenu.winfo_screenwidth()
    hs = endMenu.winfo_screenheight()

    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)

    endMenu.geometry('%dx%d+%d+%d' % (w, h, x, y))

    Progress = Label(endMenu, text=f'Completed rounds: {roundsCompleted} / {numberOfDirectory}', font=("Monospace",25))
    Progress.place(relx= 0.5, rely=0.3, anchor='center')
    quit = Button(endMenu,
                text='Quit',
                command=lambda: quitGame(endMenu),
                height=2, width=10
                )
    quit.place(relx=0.5,
            rely=0.70,
            anchor='center'
            )

    endMenu.mainloop() 
        
    


# Create a dictionary with round objects and the round number next to it.



