# ELO Test for M&M Candies
import pyodbc 

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-7UKNGRS\\SQLEXPRESS;'
                      'Database=BRIAN;'
                      'Trusted_Connection=yes;',autocommit=True)

cursor = conn.cursor()

def getCandyName(CandyLetter):
    CandyName = VarietyListName[VarietyListID.index(CandyLetter)]
    return CandyName

def PullCandyData():

    global Candy1
    global Candy2
    global Winner
    global NumVotes
    global WinMargin
    global VarietyListID
    global VarietyListName

    query = "SELECT left(MatchID,1) as Candy1, right(left(MatchID,2),1) as Candy2, Winner,NumVotes,WinMargin FROM matchoutcomes where OutcomeWT='W'"

    cursor.execute(query)
    
    Candy1 = [i[0] for i in cursor.fetchall()]
    cursor.execute(query)
    Candy2 = [i[1] for i in cursor.fetchall()]
    cursor.execute(query)
    Winner = [i[2] for i in cursor.fetchall()]
    cursor.execute(query)
    NumVotes = [i[3] for i in cursor.fetchall()]
    cursor.execute(query)
    WinMargin = [i[4] for i in cursor.fetchall()]

    query = "Select ID,Variety from Varieties"
    cursor.execute(query)
    VarietyListID = [i[0] for i in cursor.fetchall()]
    print (VarietyListID)
    cursor.execute(query)
    VarietyListName = [i[1] for i in cursor.fetchall()]
    print (VarietyListName)

Candy1 = []
Candy2 = []
Winner = []
NumVotes = []
WinMargin = []
VarietyListID = []
VarietyListName = []
ELOScore = [1200,1200,1200,1200,1200,1200,1200,1200,1200,1200,1200,1200,1200,1200,1200]

PullCandyData()

# Determine how many matches took place
numMatches=len(NumVotes)

# Update WinMargin to account for number of votes
iLoop = 0
while iLoop < numMatches:
    if Winner[iLoop] != 'T':

        WinMargin[iLoop] = int(WinMargin[iLoop]) * int(NumVotes[iLoop])

    else: WinMargin=1
    iLoop=iLoop+1
    pass 




def EloCandy(Candy1,Candy2,Candy1Elo,Candy2Elo,Winner,NumVotes):
    
    Candy1Score = Candy1Elo
    Candy2Score = Candy2Elo

    KConstant = 100

    Probability1Wins =  (1.0 / (1.0 + pow(10, ((Candy2Score-Candy1Score) / 400))))
    Probability2Wins =  (1.0 / (1.0 + pow(10, ((Candy1Score-Candy2Score) / 400))))

    NumVoteCounter = 1

    while NumVoteCounter <= NumVotes:

        if Winner == Candy1:
            Candy1Score = Candy1Score + KConstant*(1 - Probability1Wins)
            Candy2Score = Candy2Score + KConstant*(0 - Probability2Wins)
        if Winner == Candy2:
            Candy1Score = Candy1Score + KConstant*(0 - Probability1Wins)
            Candy2Score = Candy2Score + KConstant*(1 - Probability2Wins)
        if Winner == "T":
            Candy1Score = Candy1Score + KConstant*(.5 - Probability1Wins)
            Candy2Score = Candy2Score + KConstant*(.5 - Probability2Wins)
        ELOScore[VarietyListID.index(Candy1)] = Candy1Score    
        ELOScore[VarietyListID.index(Candy2)] = Candy2Score
        NumVoteCounter=NumVoteCounter+1
        pass

def updateEloTable():
    iLoop=0
    while iLoop < 15:
        #print (VarietyListName[iLoop] + ": "+ str(round(ELOScore[iLoop],2)))
        query = "Insert into brian.dbo.ELOOutput VALUES (getdate(),'"+VarietyListName[iLoop]+"',"+str(round(ELOScore[iLoop],2))+")"
        cursor.execute(query)

        iLoop = iLoop +1
        pass

query = "DROP table if exists brian.dbo.ELOOutput; create Table brian.dbo.ELOOutput (runDate datetime,VarietyName varchar(max),ELORank float)"
cursor.execute(query)
        
iLoop=0
while iLoop < numMatches:
    #print ("This Battle was Between " + getCandyName(Candy1[iLoop]) + " and " + getCandyName(Candy2[iLoop]) + ". The winner was " + getCandyName(Winner[iLoop]) + " by " + str(WinMargin[iLoop]) + " points.")
    EloCandy(Candy1[iLoop],Candy2[iLoop],ELOScore[VarietyListID.index(Candy1[iLoop])],ELOScore[VarietyListID.index(Candy2[iLoop])],Winner[iLoop],WinMargin[iLoop])
    
    iLoop = iLoop+1
    pass

updateEloTable()