'''
    round class:
    variables: 
        round id
        round name
        round directory
        round flag
        round scenario description

    constructors:
        
    
    methods: 
        startRound()
        check()
        showDescription()
        showFlagGUI()



'''
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
        title = Label(menu, text=f'{self.title}', font=("Monospace",20))
        title.place(relx=0.5,rely=0.05, anchor='center')
        scenario = Label(menu, text="Scenario", font=("Monospace",13))
        scenario.place(relx=0.05,rely=0.20)
        text = scrolledtext.ScrolledText(menu, width= 55, height= 10,wrap=WORD)
        text.insert(END, self.description)
        text.configure(state ='disabled')      
        text.place(relx=0.05, rely=0.25)
        start = Button(menu, text='Check', 
               command=lambda: self.checkSolution(menu), height=2, width=10)
        start.place(relx=0.5, rely=0.70, anchor='center')
        
        
        menu.after(2000, self.enterImage())
        
        menu.mainloop()
      
    def createImage(self):
        client = docker.from_env()
        client.images.build(path=self.directory, tag=self.name, rm=True)
        client.containers.run(
            detach=True,
            image=self.name,
            command="sleep infinity",
            name=self.name,
            tty=True,
            stdin_open=True,
            hostname=self.name
        )
        
    def enterImage(self):
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
        text = Label(frame, text=f'{error}',font=("Monospace",12),bg="coral1")
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
        text.insert(END, "Correct! Here is your flag:\n" f"{{{bin.decode('utf-8')}}}")
        text.pack(side= RIGHT)
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
            ['grep', 'Morris where are my party flags!'], capture_output=True, text=True, input=ls.stdout)
        if(check.returncode == 0 ):
            
            self.correctAnswer(mainMenu)
        else:
            self.wrongAnswer("Incorrect answer, check file again")
            
class round1(round0):
    flg = "QWZyMWNAX2hhc19QZW5ndTFucz8=" # --> Change for each class
    title = "Search and Retrieve" # --> Change for each class
    description = "Skipper has asked Private to search for a file entitled  \"Route-To-Madagascar\"  hidden somewhere in the system. Retrieve the file while keeping its content and place it at Skipper's home directory as a hidden file. \n  Rename the file to \"Skipper_Plan\"." # --> Change for each class

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
    description = "Skipper tasks Private to create an account on the machine for every penguin. Create users for \"kowalski\", \"rico\", and \"private\". Set their passwords to \"$butterb@11\". Create a home directory for each user, set the shell to /bin/bash, and assign them to groups respective to their names."  # --> Change for each class

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
    description = "King Julien is angered by Mort's incompetence and demands Private to have his sudo privileges revoked. Remove Mort's sudo privileges."    

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
    description = "Mort is keeping tracking of what everyone is doing around the zoo. He has created a file called zoo.csv that lists the names of all inhabitants in the Central Park Zoo, their species, and what they're doing. However, zoo.csv contains duplicate name entries. King Julien wants this to happen. \n\nName duplicates removed. \n\nThe names to be rearranged in alphabetical order. \n\nOn a number list. \n\nThe file should be named as \"Names_in_the_zoo.txt\" in private's home directory and should only contain names."

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
    description = "Private made several mistakes configuring Skipper and Rico's home directory. Kowalski is responsible for reconfiguring these home directories as well as certain files in each directory. \n\n- Home directories must be owned by the corresponding owner (Skipper owns Skipper's home directory) and have full permissions. \n\n- Members of the central_park group can only view files in the each directory.  \n\n- Other users cannot view the contents of each directories. \n\n- In each directory, the file \"Julien_Spy.txt\" can only be viewed by root."

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


                   
                
            