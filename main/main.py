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
    print(update.stdout, package.stdout)

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
        pip = subprocess.run(['sudo','pip','install','docker'])
        print(tkinterPip.stdout)
        print(d.stdout)

        
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

############### Main ###########################
gameStatus = True


def quitGame(gui):
    gui.destroy()
    sys.exit()


menu = Tk()
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
    print(roundDirectory)
    numberOfDirectory = (len(next(os.walk(roundDirectory))[1]))
    rounds = [numberOfDirectory]
    for rIndex in range(0,len(rounds)):

        roundClass = globals()[f'round{rIndex}']
        rounds[rIndex]= roundClass(rIndex,script_directory)
        currentRound = rounds[rIndex]
        
        currentRound.createImage()
        currentRound.startGame()
        
    


# Create a dictionary with round objects and the round number next to it.



