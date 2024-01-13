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
class round0:
    roundStatus = False
    
    #static --> constant for all rounds
    def __init__(self,roundNumber,scriptD):
        self.roundNumber = roundNumber
        self.name = "round{}".format(self.roundNumber)
        self.directory = "{}/rounds/round{}".format(scriptD, self.roundNumber)

    #static --> constant for all rounds 
    def createImage(self):
        client = docker.from_env()
        client.images.build(path=self.directory, tag=self.name, rm=True)
        client.containers.run(
            detach=True,
            image=self.name,
            command="sleep infinity",
            name=self.name,
            tty=True,
            stdin_open = True,
            user="gamer",
            hostname=self.name
        )
        subprocess.Popen(['docker', 'exec','-it',self.name,'/bin/bash'])


    #Will be dynamic for each round
    def checkSolution(self):
        ls = subprocess.run(['docker', 'exec','-it','round0','ls'],capture_output=True, text=True)
        check = subprocess.run(['grep', 'test.txt'],capture_output=True,text=True,input=ls.stderr)
        print(check.stderr)
        # if(check.returncode == 1):
        #     print("YOU FOUND IT")
        #     #subprocess.run(['docker', 'remove', '--force','round0'])
        # elif(check.returncode == 0):
        #     print("test.txt not found try again")