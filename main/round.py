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
import base64

class round0:
    flg = "UGVuZ3VpbkZsYWc=" # --> Change for each class
    title = "Getting Started" # --> Change for each class
    description = "King Julien asks you to put this string in the FirstFlag.txt: \n \"Morris give me flag\" " # --> Change for each class
    
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
        self.directory = "{}/rounds/round{}".format(scriptD, self.roundNumber)
        
    

    # static --> constant for all rounds

    def startGame(self):
        def closing_menu():
            if (messagebox.askokcancel("Quit","Are you sure?")):
                menu.destroy()
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
        text = Text(menu, width= 55, height= 10,wrap=WORD)
        text.insert(END, self.description)
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
        w = 450
        h = 150
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
            ['docker', 'exec', '-it', 'round0', 'cat', 'FirstFlag.txt'], capture_output=True, text=True)
        check = subprocess.run(
            ['grep', 'Morris give me flag'], capture_output=True, text=True, input=ls.stdout)
        if(check.returncode == 0 ):
            
            self.correctAnswer(mainMenu)
        else:
            self.wrongAnswer("Incorrect answer, check file again")
            
        

