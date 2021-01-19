# ELO Test for M&M Candies

Candy1Score = 1200
Candy2Score = 1200

Winner_1vs2 = 1

KConstant = 25

Probability1Wins =  (1.0 / (1.0 + pow(10, ((Candy2Score-Candy1Score) / 400))))
Probability2Wins =  (1.0 / (1.0 + pow(10, ((Candy1Score-Candy2Score) / 400))))

print ("Before 1 vs 2:")
print ("Candy1: "+str(Candy1Score))
print ("Candy2: "+str(Candy2Score))

if Winner_1vs2==1:
    Candy1Score = Candy1Score + KConstant*(1 - Probability1Wins)
    Candy2Score = Candy2Score + KConstant*(0 - Probability2Wins)

print ("After 1 vs 2:")
print ("Candy1: "+str(Candy1Score))
print ("Candy2: "+str(Candy2Score))

Candy3Score = 1200

Winner_1vs3 = 3
Winner_2vs3 = 3

Probability1Wins =  (1.0 / (1.0 + pow(10, ((Candy3Score-Candy1Score) / 400))))
Probability3Wins =  (1.0 / (1.0 + pow(10, ((Candy1Score-Candy3Score) / 400))))

print ("Before 1 vs 3:")
print ("Candy1: "+str(Candy1Score))
print ("Candy3: "+str(Candy3Score))

if Winner_1vs3==3:
    Candy3Score = Candy3Score + KConstant*(1 - Probability3Wins)
    Candy1Score = Candy1Score + KConstant*(0 - Probability1Wins)

print ("After 1 vs 3:")
print ("Candy1: "+str(Candy1Score))
print ("Candy3: "+str(Candy3Score))

Probability2Wins =  (1.0 / (1.0 + pow(10, ((Candy3Score-Candy2Score) / 400))))
Probability3Wins =  (1.0 / (1.0 + pow(10, ((Candy2Score-Candy3Score) / 400))))

print ("Before 2 vs 3:")
print ("Candy2: "+str(Candy2Score))
print ("Candy3: "+str(Candy3Score))

if Winner_2vs3==3:
    Candy3Score = Candy3Score + KConstant*(1 - Probability3Wins)
    Candy2Score = Candy2Score + KConstant*(0 - Probability2Wins)

print ("After 2 vs 3:")
print ("Candy2: "+str(Candy2Score))
print ("Candy3: "+str(Candy3Score))



