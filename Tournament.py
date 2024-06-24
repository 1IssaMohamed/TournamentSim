#Why?
#This project will teach me to actually apply all the OOP that Ive learnt whether that be polymorphism, inheritance, encapsulation etc.

#Requirements
# 1. Simulate a 8 team bootleg champions leauge tourney tournament from quareters to semis to finals
# 2. Be able to choose the sport and 8 teams that are in your tourny 
# 3. After doing so, the bracket should randomize and you should output the differetn matchups
# 4. Do the computations, re randomize, output and compute again
# 5.Once complete crown the champs and ask the user if theyd like to restart
# 0.1 Later on you should add a feature to allow you to run larger, 16,32,64 team tournaments
# 0.2 also would like to add a group stage that can be used to 

#roughdraft
# main:
# itll call on tournye continously througha while loop taking in all the necessary attributes for the tourney class

# Tourney(tourneyName, tourneySport, tourneyLoacation, tourneyGender, trophyName):
#     gets input for (numOfTeams (8,16,32) and sends over to the team class)
#     chooses x teams, calls on leauge 4 times to choose the top 2 teams from each leauge
#     prem, laliga, bundesliga, and serie a
#     then simulates the tournament wiht all th einformtion that they hav erecieved 

# Team(numOfTeams):
#     gives option of the 4 leauges, depending on wha tyou choose you have a greater chance of winning (depending on how strong your leauge is)
#     teamRating, (you get to chose this on a scale of 1-100), loweky after you choose youre leauge yI may force you to schoose one of the 20 teams in tihe leauge adn base your rating off that
#     averageAge
#     teamTrophies (heritage increases total chance of winning)


class Tournament:
    def __init__(self,numOfPlayers,teamName,teamRating):
        pass

class Team:
    def __init__():
        pass

class main:
    