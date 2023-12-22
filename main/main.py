#!/usr/bin/python3

'''
   Modules/Things to add 
   X Command to update linux system
   Add functionality to add docker to system repository
   Command to install python tkinter
   Command to install Docker 
'''
import subprocess

def dependencies():
   print("********Installing dependencies*********")
   update = subprocess.run(['sudo','apt','update', '-y'], capture_output=True, text=True)
   package = subprocess.run(['grep', 'command not found'], capture_output=True,text=True, input=update.stdout)
   print(update.stdout, package.stdout)
   #Installs packages using YUM if it isn't a Debian based distro
   if(update.returncode == 1 and package.returncode == 1):
      print("I am RHEL-based, WORK IN PROGRESS ONLY PLAYABLE ON DEBIAN-BASED SYSTEMS")
      update = subprocess.run(['sudo','yum','update', '-y'], capture_output=True, text=True)

   else:
      tkinter = subprocess.run(['sudo','apt','install','python-tk','-y'], capture_output=True, text=True)
      docker = subprocess.run(['sudo', 'apt-get','install','docker-ce','docker-ce-cli','containerd.io','docker-buildx-plugin','docker-compose-plugin','-y'],
                              capture_output=True, text=True)
      print(tkinter.stdout)
      print(docker.stdout)
   



from tkinter import * 

dependencies()
#command = ['sudo','yum', 'update', '-y']
#result = subprocess.run(command, capture_output=True, text= True)
#print(result.returncode)
#print("hello world!")

