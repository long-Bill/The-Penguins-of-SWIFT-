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

class round0:
    roundStatus = False

    # static --> constant for all rounds
    def __str__(self) -> str:
        return self.directory + " " + self.name
    
    def __init__(self, roundNumber, scriptD):
        self.roundNumber = roundNumber
        self.name = "round{}".format(self.roundNumber)
        self.directory = "{}/rounds/round{}".format(scriptD, self.roundNumber)

    # static --> constant for all rounds
        
    def startGame(self):
        menu = Tk()
        menu.title('The Penguins of SWIFT')
        w = 500
        h = 500
        ws = menu.winfo_screenwidth()
        hs = menu.winfo_screenheight()

        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)

        menu.geometry('%dx%d+%d+%d' % (w, h, x, y))
        start = Button(menu, text='Check',
               command=lambda: self.checkSolution(), height=2, width=10)
        start.place(relx=0.5, rely=0.55, anchor='center')
        menu.after(2000, self.createImage())
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
            user="gamer",
            hostname=self.name
        )
        subprocess.Popen(['docker', 'exec', '-it', self.name, '/bin/bash'])

    # Will be dynamic for each round

    def checkSolution(self):
        ls = subprocess.run(
            ['docker', 'exec', '-it', 'round0', 'ls'], capture_output=True, text=True)
        check = subprocess.run(
            ['grep', 'test.txt'], capture_output=True, text=True, input=ls.stderr)
        print(check.stderr)
        # if(check.returncode == 1):
        #     print("YOU FOUND IT")
        #     #subprocess.run(['docker', 'remove', '--force','round0'])
        # elif(check.returncode == 0):
        #     print("test.txt not found try again")
