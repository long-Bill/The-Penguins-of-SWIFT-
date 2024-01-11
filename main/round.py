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
    

    def __init__(self,roundNumber,scriptD):
        self.roundNumber = roundNumber
        self.name = "round{}".format(self.roundNumber)
        self.directory = "{}/rounds/round{}".format(scriptD, self.roundNumber)

    def createImage(self):
        client = docker.from_env()
        client.images.build(path=self.directory, tag=self.name, rm=True)
        client.containers.run(
            detach=True,
            image=self.name,
            command="sleep infinity",
            name="round0",
            tty=True,
            stdin_open = True
        )
        gameContainer = client.containers.get("round0").id
        
        subprocess.run(['docker', 'exec','-it',gameContainer,'/bin/bash'])
        #subprocess.run(['docker','enter',gameContainer])
        print("\n"*2)
        