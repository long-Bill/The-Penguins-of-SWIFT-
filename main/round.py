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

class round0:
    

    # static --> constant for all rounds
    def __str__(self) -> str:
        return self.directory + " " + self.name
    
    def __init__(self, roundNumber, scriptD):
        self.roundNumber = roundNumber
        self.name = "round{}".format(self.roundNumber)
        self.roundStatus = False
        self.directory = "{}/rounds/round{}".format(scriptD, self.roundNumber)
        self.__flag = "Hi"

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
        start = Button(menu, text='Check',
               command=lambda: self.checkSolution(menu), height=2, width=10)
        start.place(relx=0.5, rely=0.55, anchor='center')
        
        
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
        messagebox.showerror("YOU ARE WRONG!", f"Error: \n{error}")
        
    def correctAnswer(self,string, roundMenu):
        
        root = Tk()
        root.config(bg="light green")
        root.title("CORRECT ANSWER")
        w = 400
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
        
        check = Label(frame, text=u'\u2713',font=("Arial",55),fg="Green",padx=20,pady=5,bg="light green")

        check.pack(side= LEFT)
        text = Label(frame, text="Correct! Here is your flag:\n" f"\'{self.__flag}\'",font=("Arial",15),bg="light green")
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
            ['grep', 'Give me flag'], capture_output=True, text=True, input=ls.stdout)
        if(check.returncode == 0 ):
            
            self.correctAnswer("you did it", mainMenu)
        else:
            self.wrongAnswer("Incorrect answer, check file again")
            
        

