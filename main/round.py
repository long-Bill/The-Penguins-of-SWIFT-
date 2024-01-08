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
class round0:
    roundStatus = False
    

    def __init__(self,roundNumber,scriptD):
        self.roundNumber = roundNumber
        self.directory = f'{scriptD}/rounds/round{self.roundNumber}'

    def getNumber(self):
        print(self.directory)