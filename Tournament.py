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


#ok lost most of my data at home cause Ithought I comitted my work corectly but guess not? 
import random
import pyfiglet
from termcolor import colored

class Tournament:
    def __init__(self,teams):
        self.teams=teams

    def simulateRound(self):
        numOfGames=int(len(self.teams)/2)
        random.shuffle(self.teams)
        nextRound=[]
        for x in range(numOfGames):
            print(f"Game #{x+1}")
            #temporary location that has to change
            #popping the 2 teams that will be playing each other out
            a=self.teams.pop()
            b=self.teams.pop()
            match=Match(a,b,"Zimbabwe","June 1, 2052")
            nextRound.append(match.singleResult(match.team1,match.team2))
        self.teams=nextRound
        print(f"ROUND COMPLETE!\n------------------------------------------------------------------------------------")
        return self.teams
    
    def simulateKnockout(self):
        while len(self.teams)>1:
            print(f"round {len(self.teams)} current teams is:")
            for x in self.teams:
                print(x.nation)
            self.simulateRound()
        return self.teams[0]


class Team:
    #other aspects that could go here are team age, t10 coach, last placement
    def __init__(self, nation, rating,heritage):
        self.nation=nation
        self.heritage=heritage
        if heritage>=3:
            self.rating=(rating*.25)+rating
        else:
            self.rating=rating
    def getNation(self):
        return self.nation
    def getHeritage(self):
        return self.heritage
    def getRating(self):
        return self.heritage
        
        
#for euros location will be a randomly chosen european country and you get a boost if you are form that place
#for copa it will be the same, Ill prolly get the list from chat gpt inorder to randomize
#could also add ref later and see the referees history with each of the nations, possibly scraping through a data base 
class Match:
    def __init__(self,t1,t2,location, date):
        self.team1=t1
        self.team2=t2
        self.location=location
        if self.team1.nation==location:
            self.team1.rating=(self.team1.rating*.25)+self.team1.rating
        if self.team2.nation==location:
            self.team2.rating=(self.team2.rating*.25)+self.team2.rating
        self.date=date
    
    def singleResult(self,t1,t2): 
        totRange=self.team1.rating+self.team2.rating
        #remove the actual "totRange" over here late
        print(f"{self.team1.nation} ({self.team1.rating})vs {self.team2.nation} ({self.team2.rating}) \n{totRange}")
        result=int(random.randint(int(self.team1.rating),int(totRange)))
        print(result)
        if result<=self.team1.rating:
            print(f"{self.team1.nation} wins!")
            return self.team1
        else:
            print(f"{t2.nation} wins!")
            return self.team2


figlet = pyfiglet.Figlet(font='slant')
print(colored(figlet.renderText("Welcome to Euro/Copa Tournament simulator!"),"red",on_color="on_black",attrs=["bold"]))
totalteams=[]

t=int(input("Would you like to simulate\n1.euros\n2.copa america?\n"))
while t!=1 or t!=2:
    t=int(input("invalid input, try again!\n"))
numOfTeams=int(input("how many teams would you like in this tournament\n1.8\n2.16\n3.32\n"))
while numOfTeams<1 or numOfTeams>3:
    numOfTeams=int(input("invalid input, try again\n"))
if numOfTeams==1:
    numOfTeams=8
elif numOfTeams==2:
    numOfTeams=16
elif numOfTeams==3:
    numOfTeams=32

#create 2 gloabal lists for the countries in south and north america and for the countries in europe
rankingSeen=[]
nationsSeen=[]
for x in range(numOfTeams):
    #check if not in country list 
    n=input(f"Nation #{x+1}?")
    while n in nationsSeen:
        n= int(input("The same team cant get placed 2 times in the same tournament!\n, retry"))
    nationsSeen.append(n)
    #make sure valid input
    r=int(input("what is the current team ranking 1-211"))
    while r in rankingSeen or r>211 or r<1:
        r= int(input("invalid input, retry\n, retry"))
    rankingSeen.append(r)
    r=(211-r)
    h=int(input("How many major trophies has your nation won in its history?"))

    
    totalteams.append(Team(n,r,h))

sim= Tournament(totalteams)
print(f"and the champion isssss...\n{sim.simulateKnockout().nation}!!!!!")