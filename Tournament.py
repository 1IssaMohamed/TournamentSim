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
class Tournament:
    def __init__(self,teams):
        self.teams=teams

    def simulateRound(self,teams):
        numOfGames=len(teams)/2
        self.teams=random.shuffle(self.teams)
        nextRound=[]
        for x in range(numOfGames):
            #temporary location that has to change
            match=Match(self.teams.pop(),self.teams.pop(),"Zimbabwe","June 1, 2052")
            nextRound.append(match.singleResult(match.t1,match.t2))
        self.teams=nextRound
        return self.teams
    
    def simulateKnockout(self,teams):
        while len(self.teams)>1:
            print("round of ",len(self.teams))
            Tournament.simulateRound(self.teams)
        return teams


class Team:
    #other aspects that could go here are team age, t10 coach, last placement
    def __init__(self, nation, rating,heritage):
        self.nation=nation
        self.heritage=heritage
        if heritage>=3:
            self.rating=(rating*.25)+rating
        else:
            self.rating=rating
        
        
        
#for euros location will be a randomly chosen european country and you get a boost if you are form that place
#for copa it will be the same, Ill prolly get the list from chat gpt inorder to randomize
#could also add ref later and see the referees history with each of the nations, possibly scraping through a data base 
class Match:
    def __init__(self,t1,t2,location, date):
        self.team1=t1
        self.team2=t2
        self.location=location
        if t1.nation==location:
            t1.rating=(t1.rating*.25)+t1.rating
        if t2.nation==location:
            t2.rating=(t2.rating*.25)+t2.rating
        self.date=date
    
    def singleResult(self,t1,t2): 
        totRange=t1.rating+t2.rating
        result=random.randint(t1.rating,totRange)
        if result<=t1.rating:
            print(f"{t1.nation} wins!")
            return t1
        else:
            print(f"{t2.nation} wins!")
            return t2



totalteams=[]
t=input("Welcome to the international tournament simulator, would you liek to simulate\n1.euros\n2.copa america?")
teams=input("how many teams would you like in this tournament\n1.8\n2.16\n3.32")
#create 2 gloabal lists for the countries in south and north america and for the countries in europe
for x in range(teams):
    #check if not in country list 
    n=input("What nation?")
    #make sure valid input
    r=input("what is the current team ranking 1-100")
    h=input("How many major trophies has your nation won in its history?")
    totalteams.append(Team(n,r,h))

sim= Tournament(totalteams)
print("and the champion isssss!!!!!",sim.simulateKnockout(teams))