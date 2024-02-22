
import docker
import subprocess
from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
import base64

class round0:
    flg = "UEBydHlUaW1lIQ==" # --> Change for each class
    title = "The First Time" # --> Change for each class
    description = "Private just became an intern for SWIFT and barely knows how to use Linux. He is given a text string from King Julien and needs to be placed in the \"MyMessage.txt\" file. The text string is: \n\"Maurice where are my party flags!\" " # --> Change for each class
    
    # static --> constant for all rounds
    def __str__(self) -> str:
        return self.directory + " " + self.name
    
    #Class method for roundStatus
    
    def trueRoundStatus(self):
        self.roundStatus = True


    # static --> constant for all rounds
    def __init__(self, roundNumber, scriptD):
        self.roundNumber = roundNumber
        self.name = "round{}".format(self.roundNumber)
        self.roundStatus = False
        self.quitGame = False
        self.directory = "{}/rounds/round{}".format(scriptD, self.roundNumber)
        
    

    # static --> constant for all rounds

    def startGame(self):
        def closing_menu():
            if (messagebox.askokcancel("Quit","Are you sure?")):
                subprocess.run(['docker', 'exec', '-it','-u','root', self.name, '/var/backups/chattr','-i','/etc/bash.bashrc'])
                menu.destroy()
                client = docker.from_env()
                client.containers.get(self.name).remove(force=True)
                client.images.remove(self.name)
                client.images.remove("ubuntu:22.04")
                self.quitGame = True
        menu = Tk()
        menu.protocol("WM_DELETE_WINDOW" , closing_menu)
        menu.title(self.name)
        w = 500
        h = 500
        ws = menu.winfo_screenwidth()
        hs = menu.winfo_screenheight()

        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)

        menu.geometry('%dx%d+%d+%d' % (w, h, x, y))
        menu.configure(bg="#303030")
        title = Label(menu, text=f'{self.title}', font=("Monospace",20),bg="#303030",fg="white")
        title.place(relx=0.5,rely=0.05, anchor='center')
        scenario = Label(menu, text="Scenario", font=("Monospace",13),bg="#303030",fg="white")
        scenario.place(relx=0.05,rely=0.20)
        text = scrolledtext.ScrolledText(menu, width= 55, height= 10,wrap=WORD)
        text.insert(END, self.description)
        text.configure(state ='disabled')      
        text.place(relx=0.05, rely=0.25)
        start = Button(menu, text='Check', 
               command=lambda: self.checkSolution(menu), height=2, width=10,bg="#ffab40",foreground="white")
        start.place(relx=0.5, rely=0.70, anchor='center')
        
        
        menu.after(2000, self.enterImage())
        
        menu.mainloop()
      
    def createImage(self):
        client = docker.from_env()
        client.images.build(path=self.directory, tag=self.name, rm=True)
        client.containers.run(
            detach=True,
            image=self.name,
            cap_add = "LINUX_IMMUTABLE",
            command="sleep infinity",
            name=self.name,
            tty=True,
            stdin_open=True,
            hostname=self.name
        )
        
    def enterImage(self):
        #chattr is in /var/backups
        subprocess.run(['docker', 'exec', '-it','-u','root', self.name, 'chattr','+i','/etc/bash.bashrc'])
        subprocess.run(['docker', 'exec', '-it','-u','root', self.name, 'mv','/usr/bin/chattr','/var/backups/chattr'])
        subprocess.Popen(['docker', 'exec', '-it', self.name, '/bin/bash'])
        

    def wrongAnswer(self,error):
        root = Tk()
        root.config(bg="coral1")
        root.title("INCORRECT ANSWER")
        w = 525
        h = 175
        ws = root.winfo_screenwidth()
        hs = root.winfo_screenheight()

        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)

        root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        frame = Frame(root,bg="coral1")
        frame.pack()
        
        
        check = Label(frame, text=u'\u2716',font=("Monospace",55),fg="Red",padx=20,pady=5,bg="coral1")

        check.pack(side= LEFT)
        text = Label(frame, text=f'{error}',font=("Monospace",12),bg="coral1",fg="Black")
        text.pack(side= RIGHT)
        
        okay = Button(root,
                text='Ok',
                command=lambda: root.destroy(),
                height=1, width=10
                ) 
        okay.place(relx=0.5,
                rely=0.80,
                anchor='w'
                )
        
        root.mainloop()

      
    def correctAnswer(self,roundMenu):
        self.trueRoundStatus()
        root = Tk()
        root.config(bg="light green")
        root.title("CORRECT ANSWER")
        w = 500
        h = 150
        ws = root.winfo_screenwidth()
        hs = root.winfo_screenheight()

        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        
        root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        frame = Frame(root,bg="light green")
        frame.pack()
        def close():
            subprocess.run(['docker', 'exec', '-it','-u','root', self.name, '/var/backups/chattr','-i','/etc/bash.bashrc'])
            root.destroy()
            roundMenu.destroy()
            client = docker.from_env()
            client.containers.get(self.name).remove(force=True)
            client.images.remove(self.name)
            client.images.remove("ubuntu:22.04")
        
        check = Label(frame, text=u'\u2713',font=("Monospace",55),fg="Green",padx=20,pady=5,bg="light green")

        check.pack(side= LEFT)
        bin = base64.b64decode(self.flg)
        text = Text(frame, font=("Monospace",15),bg="light green",width=25, height= 5, borderwidth=0, highlightthickness = 0, wrap=WORD)
        
        text.insert(END, "Correct! Here is your flag:\n" f"pen{{{bin.decode('utf-8')}}}")
        text.pack(side= RIGHT)
        text.configure(state ='disabled')
        next = Button(root,
                text='Next round',
                command=lambda: close(),
                height=1, width=10
                ) 
        next.place(relx=0.5,
                rely=0.80,
                anchor='w'
                )
        
        root.mainloop()


    # Will be dynamic for each round
    def checkSolution(self,mainMenu):
        ls = subprocess.run(
            ['docker', 'exec', '-it', self.name, 'cat', 'MyMessage.txt'], capture_output=True, text=True)
        check = subprocess.run(
            ['grep', 'Maurice where are my party flags!'], capture_output=True, text=True, input=ls.stdout)
        if(check.returncode == 0 ):
            
            self.correctAnswer(mainMenu)
        else:
            self.wrongAnswer("Incorrect answer, check file again")
            
class round1(round0):
    flg = "QWZyMWNAX2hhc19QZW5ndTFucz8=" # --> Change for each class
    title = "Search and Retrieve" # --> Change for each class
    description = "Skipper has asked Private to search for a file entitled  \"Route-To-Madagascar.txt\"  hidden somewhere in the system. \n\n-Retrieve the file while keeping its content and place it at Skipper's home directory as a hidden file. \n-Rename the file to \"Skipper_Plan\".\n\nPassword for private is \"private\"" # --> Change for each class

    def checkSolution(self,mainMenu):
        fileName = subprocess.run(
            ['docker','exec','-it',self.name,'ls','/home/skipper/.Skipper_Plan'], capture_output=True, text=True
        )
        if(fileName.returncode == 0):
            sum = subprocess.run(
                ['docker','exec','-it',self.name,'sha256sum','/home/skipper/.Skipper_Plan'],capture_output=True, text=True
            )
            if("05b4de00eca348f04d2e9272fd2fc8838e172512e04010a4d388d1d47a9b9dea" in sum.stdout):
                self.correctAnswer(mainMenu)
            else:
                self.wrongAnswer("Content mismatch")
        else:
            self.wrongAnswer("File: Skipper_Plan not found")
            
class round2(round0):
    
    flg = "S0BuZ2Fyb28=" # --> Change for each class
    title = "New Personnel" # --> Change for each class
    description = "Skipper tasks Private to create an account on the machine for every penguin.\n\n-Create users for \"kowalski\", \"rico\", and \"private\".\n-Set their passwords to \"$butterb@11\".\n-Create a home directory for each user.\n-Set the shell to /bin/bash.\n-Assign them to groups respective to their names.\n\nPassword for Private is \"private\""  # --> Change for each class

    def checkSolution(self,mainMenu):
        import pexpect
        userList = ["kowalski", "rico","skipper"]
        errorUser = []
        
        passwd = subprocess.run(['docker','exec','-it',self.name,'cat','/etc/passwd'],capture_output=True,text=True)
        for user in userList: 
            userFound = False
            id = subprocess.run(['docker','exec','-it',self.name,'id',f'{user}'],capture_output=True,text=True)
            
            if("no such user" in id.stdout ):
                userFound = False
            else:
                #Finds the group name
                group = subprocess.run(['awk','-F ','{{print $3}}'],capture_output=True,text=True,input=id.stdout)
                if(user in group.stdout):
                    for line in passwd.stdout.split('\n'):
                        
                        if ((user in line) and (f'/home/{user}' in line) and ("/bin/bash" in line)):
                            userFound = True
                            
            if(userFound == False):
                errorUser.append(user)

        if(errorUser):
            userErrors = ""
            for string in errorUser:
                userErrors += string + " "
            self.wrongAnswer(f'{userErrors} - Incorrect! \ncheck username, home directory, \nor default shell')
        else:
            for user in userList:
                child = pexpect.spawn(f'docker exec -it {self.name} su - {user} ')
                child.expect("Password:")
                child.sendline("$butterb@11")
                try:
                    child.expect('\$')
                except:
                    errorUser.append(user)
                
            if(not errorUser):
                self.correctAnswer(mainMenu)
            elif(errorUser):
                userErrors = ""
                for string in errorUser:
                    userErrors += string + " "
                    self.wrongAnswer(f'Incorrect! \nUsers: {userErrors} - password is incorrect')

class round3(round0):
    
    flg = "bWFuaEB0dGFuIQ==" # --> Change for each class
    title = "Demoted" # --> Change for each class
    description = "King Julien is angered by Mort's incompetence and demands Private to have his sudo privileges revoked. Remove Mort's sudo privileges.\n\nPassword for private is \"private\""    

    def checkSolution(self,mainMenu):
        sudo = subprocess.run(
            ['docker', 'exec', '-it', self.name, 'grep','sudo','/etc/group'], capture_output=True, text=True)
        if("mort" in sudo.stdout):
            self.wrongAnswer("WRONG! \nMORT STILL HAS SUDO")
        elif("mort" not in sudo.stdout):
            self.correctAnswer(mainMenu)
            
class round4(round0):
    
    flg = "Qm95c18xbV9GQG1vdVM=" # --> Change for each class
    title = "How Many What?" # --> Change for each class
    description = "Skipper has a special request for Private. Skipper wants Private to find the total occurence of the string \"Skipper:\" in his home directory, for research purposes of course. Once you find the number, put it in a file named \"myFame.txt\" in Skipper's home directory."

    def checkSolution(self,mainMenu):
        textFile = subprocess.run(
            ['docker','exec','-it',self.name,'cat','/home/skipper/myFame.txt'],capture_output=True,text=True
        )

        if(textFile.returncode == 0 and "258" in textFile.stdout):
            self.correctAnswer(mainMenu)
        elif(textFile.returncode == 0 and '258' not in textFile.stdout):
            self.wrongAnswer("Error!\nThe total number is incorrect.")
        else:
            self.wrongAnswer("Error!\nThe file \"myFame.txt\" was not found.")


class round5(round0):
    
    flg = "eXVtbXlfcDNhbnV0cw==" # --> Change for each class
    title = "DUPLICATES????" # --> Change for each class
    description = "Mort is keeping tracking of what everyone is doing around the zoo. He has created a file called \"zoo.csv\" that lists the names of all inhabitants in the Central Park Zoo, their species, and what they're doing. However, zoo.csv contains duplicate name entries. King Julien wants this to happen:\n\n-Name duplicates removed.\n-The names to be rearranged in alphabetical order. \n-On a number list. \n-The file should be named as \"Names_in_the_zoo.txt\" in private's home directory and should only contain names.\n\nPassword for private is \"private\""

    def checkSolution(self,mainMenu):
        matched = False
        errorLine =""
        file = subprocess.run(
            ['docker','exec','-it',self.name,'cat','/home/private/Names_in_the_zoo.txt'],capture_output=True,text=True
        )     
        if(file.returncode == 1):
            self.wrongAnswer("Error!\nFile: \n\"Names_in_the_zoo.txt\" not found.") 
        elif(file.returncode == 0):
            nameList = ["Alex","Dave","Gloria","Joey","King Julien","Kowalski","Marlene","Marty"
                        ,"Mason","Maurice","Melman","Mort","Nana","Private","Rico","Skipper"]
            i = 1
            for line in file.stdout.split('\n'):
                if(str(i) in line and nameList[i-1] in line and i <= 16):
                    matched = True
                    i += 1
                elif(i <= 16):
                    matched = False
                    errorLine = line
                    break
            if(matched == False):
                self.wrongAnswer(f'"{errorLine}" was a missed match')
            elif(matched == True):
                self.correctAnswer(mainMenu)
        else:
            self.wrongAnswer("WHAT DID YOU DO!!")
        
        
class round6(round0):
    flg = "MG4xeV9yb290X0lT" # --> Change for each class
    title = "Who's Allowed In?" # --> Change for each class
    description = "Private made several mistakes configuring Skipper and Rico's home directory. Kowalski is responsible for reconfiguring these home directories as well as certain files in each directory. \n\n-Home directories must be owned by the corresponding owner (Skipper owns Skipper's home directory) and have full permissions. \n\n-Members of the central_park group can only view files in the each directory.\n\n-Other users cannot view the contents of each directory.\n\n-In each directory, the file \"Julien_Spy.txt\" can only be viewed by root.\nPassword for kowalski is \"kowalski\""

    def checkSolution(self, mainMenu):
        names = ["rico","skipper"]
        error = False
        for penguin in names:
            
            listOfDir = [f'/home/{penguin}',f'/home/{penguin}/Documents',f'/home/{penguin}/Downloads']
            for dir in listOfDir:
                directory = subprocess.run(['docker','exec','-it',self.name,'ls','-ld',dir],capture_output=True,text=True)
                if(directory.returncode == 2):
                    self.wrongAnswer(f'{dir} \ndoesn\'t exists.')
                    error = True
                    break
                elif(directory.returncode == 0):
                    owner = subprocess.run(['awk','-F ','{{print $3}}'],capture_output=True,text=True, input=directory.stdout)
                    
                    group = subprocess.run(['awk','-F ','{{print $4}}'],capture_output=True,text=True, input=directory.stdout)
                    if("central_park" not in group.stdout):
                        self.wrongAnswer(f'{dir} does not have the \ncorrect group member.')
                        error = True
                        break
                    if(penguin not in owner.stdout):
                        self.wrongAnswer(f'{dir} does not have \nthe correct owner.')
                        error = True
                        break
                    octal = subprocess.run(['docker','exec','-it',self.name,'stat','-c',"%a",dir],capture_output=True,text=True)
                    if("770" in octal.stdout or "750" in octal.stdout): 
                        error = False
                    else:
                        self.wrongAnswer(f'{dir} \nincorrect permissions.')
                        error = True
                        break
                    julien = f'/home/{penguin}/Julien_Spy.txt'
                    file = subprocess.run(['docker','exec','-it',self.name,'ls','-l',julien],capture_output=True,text=True)
                    owner = subprocess.run(['awk','-F ','{{print $3}}'],capture_output=True,text=True, input=file.stdout)
                    group = subprocess.run(['awk','-F ','{{print $4}}'],capture_output=True,text=True, input=file.stdout)
                    if(file.returncode == 2):
                        self.wrongAnswer("Julien_Spy.txt does not exists.")
                        error = True
                        break
                    elif(file.returncode == 0):
                        if("root" not in group.stdout):
                            self.wrongAnswer(f'{julien} does not have the \ncorrect group member.')
                            error = True
                            break
                        if("root" not in owner.stdout):
                            self.wrongAnswer(f'{julien} does not have \nthe correct owner.')
                            error = True
                            break
                        octal = subprocess.run(['docker','exec','-it',self.name,'stat','-c',"%a",julien],capture_output=True,text=True)
                        if("770" in octal.stdout or "750" in octal.stdout or "570" in octal.stdout or "550" in octal.stdout): 
                            error = False
                        else:
                            self.wrongAnswer(f'{julien} \nincorrect permissions.')
                            error = True
                            break
            if(error):
                break
            
        if(error == False):
            self.correctAnswer(mainMenu)

class round7(round0):
    flg = "T25lLXAzcnNvbi1qb2I=" # --> Change for each class
    title = "The Fired Sysadmin" # --> Change for each class
    description = "Before leaving SWIFT corp., Melmen, the previous system administrator, decided leave a surprise for Kowalski as a goodbye gift. Whenever Kowalski types a command, like ls or cd, it displays a message instead of executing the command. Help Kowalski fix this and get everything back on track.\n\nTIP: use su kowalski to check your commands\nPassword for kowalski is \"kowalski\""				
				
    def checkSolution(self, mainMenu):
        user = "kowalski"
        commands = ['ls','cat','cd','grep']
        error = False
        for com in commands:
            alias = subprocess.run(['docker','exec','-it',self.name,'grep','-E',f'^[alias]*.{com}=',f'/home/{user}/.bashrc'],capture_output=True,text=True)
            if(alias.returncode == 0 and "#" not in alias.stdout and "alias" in alias.stdout):
                error = True
                self.wrongAnswer(f'Incorrect\nThe command {com} is broken.')
                break
            elif(alias.returncode == 1):
                error = False
            elif("alias" not in alias.stdout or "#" in alias.stdout):
                error = False
            
        if(error == False):
            self.correctAnswer(mainMenu)


class round8(round0):
    flg = "cXUxY2tfYW5hbHlzMTI=" # --> Change for each class
    title = "Sudoers" # --> Change for each class
    description = "Kowalski is assigned to add more users with admin privileges. However, when using the sudo command, users are not required to enter their password. Find a way to enforce a password entry when using sudo. The users to add to the sudo group are \"king_julien\" and \"mort\". \nPassword for kowalski is \"kowalski\"\nPassword for mort is \"mort\"\nPassword for king_julien is \"king_julien\""					
	
    
    def checkSolution(self, mainMenu):
        error = False
        userList = ['king_julien','mort']
        for user in userList:
            id = subprocess.run(['docker','exec','-it',self.name,'id',f'{user}'],capture_output=True,text=True)
            if("sudo" not in id.stdout):
                self.wrongAnswer(f'{user} is not apart of the sudo group')
                error = True
                break
            else:
                YESPasswd = subprocess.run(['docker','exec','-it','-u','root',self.name,'grep','-E','^%sudo.*(ALL:ALL)','/etc/sudoers'],capture_output=True,text=True)
                noPasswd = subprocess.run(['docker','exec','-it','-u','root',self.name,'grep','-E','*%sudo.*NOPASSWD','/etc/sudoers'],capture_output=True,text=True)
                if(noPasswd.returncode == 0 and "#" not in noPasswd.stdout):
                    self.wrongAnswer("Incorrect! \nSudo users still do not require passwords.")
                    error = True
                    break
                elif((noPasswd.returncode == 1 or "#" in noPasswd.stdout) and YESPasswd.returncode == 0):
                    error = False

        if(error == False):
            self.correctAnswer(mainMenu)
                
class round9(round0):
    
    flg = "WTMyX3JpYzAta2FiMDBt" # --> Change for each class
    title = "For the Professionals" # --> Change for each class
    description = "SECURITY ALERT!! Something is causing the system to add more admin users and allowing system-breaking commands to be executed. Help Kowalski stop this and delete any users created from the cause.\n\nPassword for kowalski is \"kowalski\""					
	
    def enterImage(self):
        import time
        subprocess.run(['docker','exec','-it','-u','root',self.name,'service','cron','start'],capture_output=True)
        print("Give this round some extra time to build about 50 seconds. Remember to standup and walk around.")
        time.sleep(60)
        subprocess.run(['clear'])
        
        super().enterImage()
        

    def checkSolution(self, mainMenu):
        error = False
        aux = subprocess.run(['docker','exec','-it',self.name,'ps','aux'],capture_output=True,text=True)
        grep = subprocess.run(['grep','/root'],capture_output=True,text=True,input=aux.stdout)
        
        passwd = subprocess.run(['docker','exec','-it','-u','root',self.name,'cat','/etc/passwd'],capture_output=True,text=True)
        users = subprocess.run(['grep','-E','^user*[0-9]'],capture_output=True,text=True,input=passwd.stdout)
        kowalski = subprocess.run(['grep','kowalski'],capture_output=True,text=True,input=passwd.stdout)
        #Bug
        if((kowalski.returncode == 1)):
            print("You broke the game, my fault...\nYou can play again :))")
            mainMenu.destroy()
            client = docker.from_env()
            client.containers.get(self.name).remove(force=True)
            client.images.remove(self.name)
            client.images.remove("ubuntu:22.04")
            error = True
        if(grep.returncode == 0 and kowalski.returncode == 0):
            self.wrongAnswer("It's still adding more users!")
            error = True
        elif(users.returncode == 0 and kowalski.returncode == 0):
            self.wrongAnswer("DELETE THOSE USERS")
            
            error = True
        
        if(error == False):
            self.correctAnswer(mainMenu)
					
class round10(round0):
    flg = "ZjEyaF9JTl9wMG5k" # --> Change for each class
    title = "Something Fishy Fish Fish" # --> Change for each class
    description = "Skipper has asked Kowalski to change passwords for private and rico... again. However, something fishy is happening, like the bad kind of fishy, user passwords are being reset to a default password. \n\nFind a stop to this and set the passwords to \"Moto(Mot0)\" for skipper and private.\n\nPassword for kowalski is \"kowalski\" " 					
															 					
	
    def checkSolution(self, mainMenu):
        import pexpect
        userList = ['skipper','private']
        errorUser = []
        for user in userList:
            child = pexpect.spawn(f'docker exec -it {self.name} su - {user} ')
            child.expect("Password:")
            child.sendline("Moto(Mot0)")
            try:
                child.expect('\$')
            except:
                errorUser.append(user)
                
        if(not errorUser):
            self.correctAnswer(mainMenu)
        elif(errorUser):
            userErrors = ""
            for string in errorUser:
                userErrors += string + " "
                self.wrongAnswer(f'Incorrect! \nUsers: {userErrors} - password is incorrect')

class round11(round0):
   
    flg = "QTFvbmVfSW5fTWFkQGdhc2Nhcg==" # --> Change for each class
    title = "Skipper's Gift" # --> Change for each class
    description = "Skipper needs help setting up a service for a special someone. He wants to allow that special someone to SSH into his computer without using a password because passwords are just inconvenient. He also wants to allow this person to login as myguest. Assist Skipper with setting up a SSH service with public-key authentication on.\nNote: If you want to test ssh on host, it will be on port 2222\nPassword for skipper is \"skipper\"\nPassword for myguest is \"myguest\"\n\nPublic key: \nssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCrtW+hpjl0aUmadkY5hYssHO+lf3AbligO9JUKQaT8U1r+sgTqkBTSEaD0ASugUhIUbWzXqnzFiSUF0hnFvd723U3meRMFkBVdpx9DDF1yz5+RiDM1EY+fETkyKdS9PDU0EbiwTMI7sTj/tQRBDh5GxvxMXPEAa/u3Mav5PDzBMzcgE9mAlMGFd2Z6nCPsgNtZseHFuX5UZukBLBMhJEnG+qUWuuWJGFbYNWw/OtyQqmXhl2I4L5byPHb+cGwyBclooLyNHPN/km1kWzksHZwwB8d0zJ9G4HIcjZudtdQP8513w3YfKuj99pLOJTLWmRM/wi/RvFpD1Irz6jmAFVnmKFaLy0Qml+Ja1/h4QHd6MKoCd9BdvGvXjhRi9W7xKzgfh4rCR6bNxRzJ/Xf9eEPWFkgSfYnDNYJLy+mGhti2rlGHgJkivirJ/AFuGcU6Ei1S7deasekYzEFEdluvKexDZhPXusrkTNeDpszAYHY42qGQBzmzJLLwJVoX1+jx7Wk= player@debian11" 					
	
    def createImage(self):
        client = docker.from_env()
        client.images.build(path=self.directory, tag=self.name, rm=True)
        client.containers.run(
            detach=True,
            image=self.name,
            cap_add = "LINUX_IMMUTABLE",
            ports={'22/tcp':2222},
            command="sleep infinity",
            name=self.name,
            tty=True,
            stdin_open=True,
            hostname=self.name
        )
    
    def enterImage(self):
        super().enterImage()
        subprocess.run(['docker','exec','-it','-u','root',self.name,'service','ssh','start'],capture_output=True)

    def checkSolution(self, mainMenu):
        import paramiko
        user = 'myguest'
        host = "127.0.0.1"
        
        
        error = False
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        key = paramiko.RSAKey.from_private_key_file("/home/player/.ssh/id_rsa") #Change for workshop
        try:
            client.connect(host,username=user,pkey=key,port=2222)
        except paramiko.ssh_exception.PasswordRequiredException:
            self.wrongAnswer("It is requiring a password.\nMust be public key.")
        except paramiko.ssh_exception.AuthenticationException:
            self.wrongAnswer("Check your sshd configuration file")
        except paramiko.ssh_exception.SSHException:
            self.wrongAnswer("SSH is not open")
        _stdin, _stdout,_stderr = client.exec_command("whoami")
        print(_stdout.read().decode())
        if("myguest" in _stdout.read().decode()):
            self.correctAnswer(mainMenu)          
        client.close()
        
class round12(round0):
   
    flg = "d2ViX2Rvd25fdzNiX1VQ" # --> Change for each class
    title = "Rico" # --> Change for each class
    description = "Skipper has always wanted to build a website from scratch. To begin his journey, Skipper started learning HTML and CSS. After taking a break, Skipper finds out that his website is replaced with Rico's website. Skipper only remembers the name of the file was named \"index.html\". Help Skipper fix his website and finish what needs to be done.\n\nPassword for skipper is \"skipper\""	 					
	
    def createImage(self):
        client = docker.from_env()
        client.images.build(path=self.directory, tag=self.name, rm=True)
        client.containers.run(
            detach=True,
            image=self.name,
            cap_add = "LINUX_IMMUTABLE",
            ports={'80/tcp':80},
            command="sleep infinity",
            name=self.name,
            tty=True,
            stdin_open=True,
            hostname=self.name
        )
    
    def enterImage(self):
        super().enterImage()
        

    def checkSolution(self, mainMenu):
        curl = subprocess.run(['curl','http://localhost:80'],capture_output=True,text=True)
        
        if("<h3>Smile and wave boys, smile and wave</h3>" in curl.stdout):
            self.correctAnswer(mainMenu)
        else:
            self.wrongAnswer('This isn\'t the right website\nCheck your files')

class round13(round0):
   
    flg = "dGhhbmtfeTB1X2MwbXJhZDNz" # --> Change for each class
    title = "To The Comrades" # --> Change for each class
    description = "Skipper has been tinkering around and has created several websites. However, whenever Skipper enters localhost or his ip address in the url bar of the browser, it shows the first website Skipper worked on at the beginning. He created 3 websites and all are stored in the directory /var/www/html/. \n\n - First website is in /var/www/html \n\n - Second website is called \"HelloWorld\" \n\n - Third website is called \"Comrades\" \n\n Help Skipper make his third website display on localhost and suprise the comrades with his project.\Password for skipper is \"skipper\""	 					
	
    def createImage(self):
        client = docker.from_env()
        client.images.build(path=self.directory, tag=self.name, rm=True)
        client.containers.run(
            detach=True,
            image=self.name,
            cap_add = "LINUX_IMMUTABLE",
            ports={'80/tcp':80},
            command="sleep infinity",
            name=self.name,
            tty=True,
            stdin_open=True,
            hostname=self.name
        )
    
    def enterImage(self):
        super().enterImage()
        

    def checkSolution(self, mainMenu):
        curl = subprocess.run(['curl','http://localhost:80'],capture_output=True,text=True)
        
        if("cute and cuddly, cute and cuddly" in curl.stdout and "<h1>Farewell, Comrades" in curl.stdout):
            self.correctAnswer(mainMenu)
        else:
            self.wrongAnswer('This isn\'t the right website\nCheck configuration files')
             