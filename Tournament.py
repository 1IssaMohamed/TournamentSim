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
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
copaTeamIds={
    'Argentina':['f9fddd6e','ARG',''],
    'Bolivia':['1bd2760c','BOL'],
    'Brazil':['304635c3','BRA'],
    'Chile':['7fd9c2a2','CHI'],
    'Colombia':['ab73cfe5','COL'],
    'Ecuador':['123acaf8','ECU'],
    'Paraguay':['d2043442','PAR'],
    'Peru':['f711c854','PER'],
    'Uruguay':['870e020f','URU'],
    'Venezuela':['df384984','VEN'],
    'Canada':['9c6d90a0','CAN'],
    'Costa-Rica':['1ea5ab66','CRC'],
    'Jamaica':['189bdbbd','JAM'],
    'Mexico':['b009a548','MEX'],
    'Panama':['6061a82d','PAN'],
    'United-States':['0f66725b','USA']
    }
copaTeams = ["Argentina","Bolivia","Brazil","Chile","Colombia","Ecuador","Paraguay","Peru","Uruguay","Venezuela","Mexico","United-States","Canada","Costa-Rica","Panama","Jamaica"]
euroTeamIds = {
    "Germany":['c1e40422',"GER"],
    "Portugal":['4a1b4ea8',"POR"],
    "Spain":['b561dd30',"ESP"],
    "France":['b1b36dcd',"FRA"],
    "Italy":['998c5958',"ITA"],
    "Netherlands":['5bb5024a',"NED"],
    "Belgium":['361422b9',"BEL"],
    "Croatia":['7b08e376',"CRO"],
    "England":['1862c019',"ENG"],
    "Switzerland":['81021a70',"SUI"],
    "Denmark":['29a4e4af',"DEN"],
    "Poland":['8912dcf0',"POL"],
    "Austria":['d5121f10',"AUT"],
    "Turkiye":['ac6bcf92',"TUR"],
    "Czechia":['2740937c',"CZE"],
    "Serbia":['1d6f5c9b',"SRB"],
    "Georgia":['7158b127',"GEO"],
    "Ukraine":['afa29a3e',"UKR"],
    "Scotland":['602d3994',"SCO"],
    "Hungary":['b4ac5e97',"HUN"],
    "Romania":['7def9493',"ROU"],
    "Slovakia":['66cff10b',"SVK"],
    "Slovenia":['6b9f868f',"SVN"],
    "Albania":['b44b9eb7',"ALB"]
}

euroTeams = ["Germany","Portugal","Spain","France","Italy","Netherlands","Belgium","Croatia","England","Switzerland","Denmark","Poland","Austria","Turkiye","Czechia","Serbia","Georgia","Ukraine","Scotland","Hungary","Romania","Slovakia","Slovenia","Albania"]

class Tournament:
    def __init__(self,teams):
        self.teams=teams
        
    def createGroups(self):
        random.shuffle(self.teams)
        self.totalGroups=[]
        self.groupA=[self.teams.pop(),self.teams.pop(),self.teams.pop(),self.teams.pop()]
        self.totalGroups.append(self.groupA)
        self.groupB=[self.teams.pop(),self.teams.pop(),self.teams.pop(),self.teams.pop()]
        self.totalGroups.append(self.groupB)
        self.groupC=[self.teams.pop(),self.teams.pop(),self.teams.pop(),self.teams.pop()]
        self.totalGroups.append(self.groupC)
        self.groupD=[self.teams.pop(),self.teams.pop(),self.teams.pop(),self.teams.pop()]
        self.totalGroups.append(self.groupD)
        if EuroOrCopa==1:
                self.groupE=[self.teams.pop(),self.teams.pop(),self.teams.pop(),self.teams.pop()]
                self.totalGroups.append(self.groupE)
                self.groupF=[self.teams.pop(),self.teams.pop(),self.teams.pop(),self.teams.pop()]
                self.totalGroups.append(self.groupF)
    
    def simulateGroups(self):
        self.createGroups()
        print("starting group stage!!!")
        for num , group in enumerate(self.totalGroups):
            print(f"group:{chr(num+97).upper}{group[0].nation}{group[1].nation}{group[2].nation}{group[3].nation}")
            matchups=[[group[0],group[1]],[group[0],group[2]],[group[0],group[3]],[group[1],group[2]],[group[1],group[3]],[group[2],group[3]]]
            for teams in matchups:
                 one=teams[0]
                 two=teams[1]
                 location=random.choice(regionTeams)
                 match=Match(one,two,location)
                 winner=match.singleResult()
                 winner.points+=3
                 time.sleep(1)
            print("final group standings:")
            group=sorted(group,key=lambda team:team.points)
            for x in group:
                print(x.nation,x.points)
        return 0
    
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
            location=random.choice(regionTeams)
            match=Match(a,b,location)
            nextRound.append(match.singleResult())
        self.teams=nextRound
        print(f"ROUND COMPLETE!\n------------------------------------------------------------------------------------")
        time.sleep(1)
        return self.teams
    
    def simulateKnockout(self):
        while len(self.teams)>1:
            print(f"round of {len(self.teams)} current teams are:")
            for x in self.teams:
                print(x.nation)
            self.simulateRound()
        return self.teams[0]


class Team:
    #Would like to end up overall team rating, made up of xg,xga,xpp,xpc,form, and fifa ranking
    #end up with teamQuality and rankRating ->lead to totalForm
    def __init__(self, nation, id1, id2,points):
        self.nation=nation
        print(nation)
        # required if you go through group stage
        self.points=0
        url=f"https://fbref.com/en/squads/{id1}/2024/{nation}-Men-Stats#all_stats_standard"
        url2=f"https://inside.fifa.com/fifa-world-ranking/{id2}?gender=men"
        header2 = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        #The main difference between using requests  vs Selenium is the fact tha selenium can actually process js I believe this page dosen work with requests because although it automatically opens up with the infomration necessaary if I go to the webpage, clicking a button compeltely changes the page (which Id assume is odne thorugh js)

        #first batch of information (xG,xAG,xProgressiveCarries,xProgressivePasses (all per 90))
        response1=requests.get(url,headers=header2)
        soup1 = BeautifulSoup(response1.content, 'html.parser')
        footer=soup1.find("tfoot")
        row=footer.find("tr")
        data = [td.get_text(strip=True) for td in row.find_all('td')]
        print(data,len(data))
        xGP90=float(data[26])
        xAGP90=float(data[27])
        xPrgCP90=float(data[18])
        xPrgPP90=float(data[19])
        self.teamQuality=(xPrgCP90/100)+(xPrgPP90/150)+xGP90+xAGP90
        print(f"Team Quality:{self.teamQuality}")

        #second batch of information (current ranking and average ranking)
        response2=requests.get(url2,headers=header2)
        soup2 = BeautifulSoup(response2.content, 'html.parser')
        ranking_element = soup2.find_all('div',class_="highlights_resultItemValue__okL7z")
        currentRankingString=(ranking_element[0]).text
        avgRankingString=(ranking_element[3]).text
        #Formatting the strings of data into usable floats for calcualtions
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
        # print(f"curr:{currentRanking},avg:{avgRanking}")
        self.rankRating=5/currentRanking+3/avgRanking
        print(f"rank rating:{self.rankRating}")
        self.teamRating=self.rankRating+self.teamQuality
        print(f"final team rating: {self.teamRating}")
    
    def getNation(self):
        return self.nation
    
    def getTeamQuality(self):
        return self.teamQuality
    
    def getRankRating(self):
        return self.rankRating
    
    def getTeamRating(self):
        return self.teamRating
        
        
#for euros location will be a randomly chosen european country and you get a boost if you are form that place
#for copa it will be the same, Ill prolly get the list from chat gpt inorder to randomize
#could also add ref later and see the referees history with each of the nations, possibly scraping through a data base 
class Match:
    def __init__(self,t1,t2,location):
        self.team1=t1
        self.team2=t2
        self.location=location
        #if home field advantage, 
        if self.team1.nation==location:
            self.team1.teamRating*=.15
        if self.team2.nation==location:
            self.team2.teamRating*=.15
    
    def singleResult(self): 
        totRange=self.team1.teamRating+self.team2.teamRating
        #remove the actual "totRange" over here late
        print(f"{self.team1.nation} ({self.team1.teamRating})vs {self.team2.nation} ({self.team2.teamRating}) \n{totRange}")
        result=(random.uniform(self.team1.teamRating,totRange))
        print(result)
        if result<=self.team1.teamRating:
            print(f"{self.team1.nation} wins!")
            return self.team1
        else:
            print(f"{self.team2.nation} wins!")
            return self.team2


#3rd batch of information (All time W/L, AvgG scored, AvgG conceeded )
# If this is messed up, go with this alternative, https://fbref.com/en/squads/1ea5ab66/history/Costa-Rica-Men-Stats-and-History#all_nat_tm_summary
# response3=requests.get("https://footystats.org/clubs/canada-national-team-8655",headers=header2)
# print(response3)
# soup3=BeautifulSoup(response3.text,"html.parser")
# print(soup3.prettify)
# print(soup3.prettify)
# table=soup3.find_all("tbody")
# for x in table:
#     print(f"big body benz:{x}")

# table=soup3.find_all('table')
# # print(table)
# print('kallabunga dude')
# for x in table:
#     print(f"112313:{x}")
#     allTables=x.find_all("tr",class_="rowSum")
#     print(f"table123:{allTables}")

# row=table.find('tr',{'data-row':'0'})



# response3=requests.get("https://www.footballdatabase.eu/en/club/team/455-argentine/2024#clubFixtures",headers=header2)
# soup3=BeautifulSoup(response3.text,'html.parser')
# # print(response3.raise_for_status())
# # print(response3.content)
# club_balance_section = soup3.find('div', class_='module club_balance')
# rows = club_balance_section.find_all('tr', class_='line')
# last_row = rows[-1]
# record=[int(x.text) for x in last_row]
# print(record) 
# winPoints=record[1]*3
# drawPoints=record[2]
# #how many points have they been getting per game from the last 10 games
# form=(winPoints+drawPoints)/10
# print(form)

# print(f"final: {form}+{rankRating}+{teamQuality}")
# totalScore=form+rankRating+teamQuality
# print(totalScore)

figlet = pyfiglet.Figlet(font='slant')
print(colored(figlet.renderText("Welcome to Euro/Copa Tournament simulator!"),"red",on_color="on_black",attrs=["bold"]))
totalteams=[]

EuroOrCopa=int(input("Would you like to simulate\n1.euros\n2.copa america?\n"))
while EuroOrCopa!=1 and EuroOrCopa!=2:
    EuroOrCopa=int(input("invalid input, try again!\n"))
if EuroOrCopa==1:
    ManualOrAutomatic=int(input("Would you like to \n1.Manually choose the 16 teams in the knockout stage\n2.Automatically run the tournament from scratch\n"))
    numOfTeams=16
    regionTeams=euroTeams
    regionIds=euroTeamIds
else:
    ManualOrAutomatic=int(input("Would you like to \n1.Manually choose the 8 teams in the knockout stage\n2.Automatically run the tournament from scratch\n"))
    numOfTeams=8
    regionTeams=copaTeams
    regionIds=copaTeamIds

    
if ManualOrAutomatic==1:
    nationsSeen=[]
    finalTeamList=[]
    for x in range(numOfTeams):
        #check if not in country list 
        n=input(f"Nation #{x+1}?\n")
        n=n.strip()
        n=n.title()
        n=n.replace(" ","-")
        print(n)
        while n in nationsSeen or n not in regionTeams:
            n= input("Invalid entry,\nretry")
            n=n.strip()
            n=n.title()
            n=n.replace(" ","-")
        nationsSeen.append(n)
        id1=(regionIds.get(n))
        id1=id1[0]
        id2=(regionIds.get(n))[1]
        finalTeamList.append(Team(n,id1,id2,0))
        sim= Tournament(finalTeamList)
        for x in finalTeamList:
            print(x.nation)
        print(f"and the champion isssss...\n{sim.simulateKnockout().nation}!!!!!")
else:
    finalTeamList=[]
    for x in regionTeams:
        finalTeamList.append(Team(x,(regionIds.get(x))[0],(regionIds.get(x))[1],0))
        time.sleep(3)
    sim=Tournament(finalTeamList)
    print("Starting group stage:", sim.simulateGroups())