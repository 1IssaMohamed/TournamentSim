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
            print(f"{self.team2.nation} wins!")
            return self.team2


#requests
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

copateamids={
    'Argentina':['f9fddd6e','ARG',''],
    'Bolivia':['1bd2760c','BOL'],
    'Brazil':['304635c3','BRA'],
    'Chile':['7fd9c2a2','CHI'],
    'Colombia':['ab73cfe5','COL'],
    'Ecuador':['123acaf8','ECU'],
    'Paraguay':['d2043442','PAR'],
    'Peru':['f711c854','PER'],
    'Uruguay':['870e020f','URU'],
    'Venezula':['df384984','VEN'],
    'Canada':['9c6d90a0','CAN'],
    'Costa-Rica':['1ea5ab66','CRC'],
    'Jamaica':['189bdbbd','JAM'],
    'Mexico':['b009a548','MEX'],
    'Panama':['6061a82d','PAN'],
    'United-States':['0f66725b','USA']
    }
t1=input("what is team 1?")
t1=t1.strip()
t1=t1.title()
t1=t1.replace(" ","-")
id11=(copateamids.get(t1))
id11=id11[0]
id12=(copateamids.get(t1))[1]
id13=(copateamids.get(t1))[2]
t2=input("What is team 2?")
t2=t2.strip()
t2=t2.title()
t2=t2.replace(" ","-")

url=f"https://fbref.com/en/squads/{id11}/{t1}-Men-Stats#all_stats_standard"
url2=f"https://inside.fifa.com/fifa-world-ranking/{id12}?gender=men"
url3=f"https://www.11v11.com/teams/{t1.lower()}"
header2 = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}
#The main difference between using requests  vs Selenium is the fact tha selenium can actually process js 
#I believe this page dosen work with requests because although it automatically opens up with the infomration necessaary
#if I go to the webpage, clicking a button compeltely changes the page (which Id assume is odne thorugh js)

#first batch of information (xG,xAG,xProgressiveCarries,xProgressivePasses (all per 90))
response1=requests.get(url,headers=header2)
print(f"stauts{response1.raise_for_status()}")
soup1 = BeautifulSoup(response1.content, 'html.parser')
footer=soup1.find("tfoot")
# could do find_all here and also utilize the opponent stats
row=footer.find("tr")
data = [td.get_text(strip=True) for td in row.find_all('td')]
xGP90=float(data[26])
xAGP90=float(data[27])
xPrgCP90=float(data[18])
xPrgPP90=float(data[19])
print(xGP90,xAGP90,xPrgPP90,xPrgCP90)
teamQuality=(xPrgCP90/100)+(xPrgPP90/150)+xGP90+xAGP90
print(teamQuality)
#second batch of information (current ranking and average ranking)
response2=requests.get(url2,headers=header2)
print(f"stauts{response2.raise_for_status()}")
# print("content:",response2.content)
soup2 = BeautifulSoup(response2.content, 'html.parser')
# print(soup2)
ranking_element = soup2.find_all('div',class_="highlights_resultItemValue__okL7z")
currentRankingString=(ranking_element[0]).text
avgRankingString=(ranking_element[3]).text
currentRanking=""
avgRanking=""
for char in currentRankingString:
    if char.isdigit():
        currentRanking+=char
for char in avgRankingString:
    if char.isdigit():
        avgRanking+=char
currentRanking=float(currentRanking)
avgRanking=float(avgRanking)
print(f"curr:{currentRanking},avg:{avgRanking}")
rankRating=5/currentRanking+3/avgRanking

#3rd batch of information (All time W/L, AvgG scored, AvgG conceeded )
# If this is messed up, go with this alternative, https://fbref.com/en/squads/1ea5ab66/history/Costa-Rica-Men-Stats-and-History#all_nat_tm_summary
response3=requests.get("https://www.footballdatabase.eu/en/club/team/455-argentine/2024#clubFixtures",headers=header2)
soup3=BeautifulSoup(response3.text,'html.parser')
# print(response3.raise_for_status())
# print(response3.content)
club_balance_section = soup3.find('div', class_='module club_balance')
rows = club_balance_section.find_all('tr', class_='line')
last_row = rows[-1]
record=[int(x.text) for x in last_row]
print(record) 
winPoints=record[1]*3
drawPoints=record[2]
#how many points have they been getting per game from the last 10 games
form=(winPoints+drawPoints)/10
print(form)

print(f"final: {form}+{rankRating}+{teamQuality}")
totalScore=form+rankRating+teamQuality
print(totalScore)

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