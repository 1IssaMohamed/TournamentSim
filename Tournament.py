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
    'argentina':['f9fddd6e','ARG'],
    'Bolivia':0,
    'Brazil':0,
    'chile':0,
    'colombia':0,
    'ecuador':0,
    'Paraguay':0,
    'peru':0,
    'urugay':0,
    'venezula':0,
    'Canada':0,
    'Costa-Rica':0,
    'Haitit':0,
    "honduras":0,
    'Jamaica':0,
    'Mexico':0,
    'Panama':0,
    'Uniuted-States':0
    }
t1=input("what is team 1?")
t2=input("What is team 2?")
id1=(copateamids.get(t1))
id1=id1[0]
id2=(copateamids.get(t1))[1]
url=f"https://fbref.com/en/squads/{id1}/{t1}-Men-Stats#all_stats_standard"
url2=f"https://inside.fifa.com/fifa-world-ranking/{id2}?gender=men"
url3=f"https://www.11v11.com/teams/{t1.lower()}"
header2 = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}
header3={
    'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:129.0) Gecko/20100101 Firefox/129.0" ,
    "Referer":"https://footystats.org/world-cup"
}
#The main difference between using requests  vs Selenium is the fact tha selenium can actually process js 
#I believe this page dosen work with requests because although it automatically opens up with the infomration necessaary
#if I go to the webpage, clicking a button compeltely changes the page (which Id assume is odne thorugh js)

#first batch of information (xG,xAG,xProgressiveCarries,xProgressivePasses (all per 90))
response1=requests.get(url,headers=header2)
print(f"stauts{response1.raise_for_status()}")
soup1 = BeautifulSoup(response1.content, 'html.parser')
print(soup1.prettify())
# driver = webdriver.Firefox() 
# driver.get(url)
# #wait for complete load
# time.sleep(5)
# page_source = driver.page_source
# soup = BeautifulSoup(page_source, 'html.parser')
# # Locate the specific row with data-row="26"
# row = soup.find('tr', attrs={'data-row': '26'})
# if row:
#     data = [td.get_text(strip=True) for td in row.find_all('td')]
#     xGP90=data[26]
#     xAGP90=data[27]
#     xPrgCP90=data[18]
#     xPrgPP90=data[19]
#     print(xGP90,xAGP90,xPrgPP90,xPrgCP90)
# else:
#     print("Row with data-row='26' not found.")
# driver.quit()

#second batch of information (current ranking and average ranking)
response2=requests.get(url2,headers=header2)
print(f"stauts{response2.raise_for_status()}")
# print("content:",response2.content)
soup2 = BeautifulSoup(response2.content, 'html.parser')
# print(soup2)
ranking_element = soup2.find_all('div',class_="highlights_resultItemValue__okL7z")
currentRanking=(ranking_element[0]).text
avgRanking=(ranking_element[3]).text
print(f"curr:{currentRanking},avg:{avgRanking}")

#3rd batch of information (All time W/L, AvgG scored, AvgG conceeded )
# response3=requests.get("https://www.footballdatabase.eu/en/club/team/455-argentine/2024#clubFixtures",headers=header2)
# soup3=BeautifulSoup(response3.text,'html.parser')
# print(response3.raise_for_status())
# print(response3.content)
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

# for x in last_row:
#     print(x.text)



# print(response3.content.decode("utf-8"))
# print(response3.content)

# with sync_playwright() as p:
#     # Launch the browser
#     browser = p.chromium.launch(headless=False)  # Run in headful mode for debugging
#     page = browser.new_page()
#     page.goto("https://footystats.org/clubs/argentina-national-team-8625")

euroTeamIds={
}
# copateamids={
# 'united-states': 3505,
# 'mexico': 6303,
# 'canada': 2316,
# 'costa-rica': 4563,
# 'honduras': 4564,
# 'el-salvador': 4565,
# 'jamaica': 3671,
# 'panama': 4567,
# 'trinidad-and-tobago': 4568,
# 'guatemala': 4569,
# 'haiti': 4570,
# 'nicaragua': 4571,
# 'cuba': 4572,
# 'suriname': 7936,
# 'curaçao': 7717,
# 'antigua-and-barbuda': 4574,
# 'saint-kitts-and-nevis': 4575,
# 'grenada': 4576,
# 'saint-vincent-and-the-grenadines': 4577,
# 'saint-lucia': 4578,
# 'dominica': 4579,
# 'barbados': 4580,
# 'belize': 4581,
# 'bermuda': 4582,
# 'guyana': 4583,
# 'montserrat': 4584,
# 'bahamas': 4585,
# 'aruba': 7632,
# 'cayman-islands': 4586,
# 'turks-and-caicos-islands': 4587,
# 'british-virgin-islands': 4588,
# 'us-virgin-islands': 4589,
# 'anguilla': 4590,
# 'brazil': 3439,
# 'argentina': 3437,
# 'uruguay': 3449,
# 'colombia': 3442,
# 'chile': 3440,
# 'peru': 3436,
# 'venezuela': 3448,
# 'paraguay': 3447,
# 'ecuador': 3441,
# 'bolivia': 3437,
# }

# euroTeamIds={
# 'albania': 3502,
# 'andorra': 6168,
# 'armenia': 3814,
# 'austria': 3388,
# 'azerbaijan': 3815,
# 'belarus': 3816,
# 'belgium': 3382,
# 'bosnia-herzegovina': 3501,
# 'bulgaria': 3389,
# 'croatia': 3556,
# 'cyprus': 5594,
# 'czech-republic': 3445,
# 'denmark': 3434,
# 'england': 3299,
# 'estonia': 5783,
# 'faroe-islands': 6088,
# 'finland': 3570,
# 'france': 3377,
# 'georgia': 3833,
# 'germany': 3262,
# 'gibraltar': 16154,
# 'greece': 3379,
# 'hungary': 3698,
# 'iceland': 6714,
# 'ireland': 3515,
# 'italy': 3376,
# 'kazakhstan': 3838,
# 'kosovo': 15488,
# 'latvia': 3821,
# 'liechtenstein': 3817,
# 'lithuania': 3834,
# 'luxembourg': 3845,
# 'malta': 3853,
# 'moldova': 3832,
# 'monaco': 16223,
# 'montenegro': 10750,
# 'netherlands': 3378,
# 'north-macedonia': 3557,
# 'norway': 3516,
# 'poland': 3444,
# 'portugal': 3300,
# 'romania': 3446,
# 'russia': 3443,
# 'san-marino': 3836,
# 'scotland': 3708,
# 'serbia': 3435,
# 'slovakia': 3803,
# 'slovenia': 3671,
# 'spain': 3375,
# 'sweden': 3554,
# 'switzerland': 3555,
# 'turkey': 3433,
# 'ukraine': 3707,
# 'wales': 3575,
# }
# id=euroTeamIds.get(realTeamName)
# searchingUrl=f"https://www.transfermarkt.us/{realTeamName}/legionaere/verein/{id}"
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    
# }
# response=requests.get(searchingUrl,headers=headers)
# response.raise_for_status()
# # print("content:",response.content)
# soup = BeautifulSoup(response.content, 'html.parser')
# print(soup)
# ranking_element = soup.find(class_='team_ranking_class')
# if ranking_element:
#     ranking = ranking_element.text.strip()
#     print(f"Team Ranking: {ranking}")
# else:
#     print("DNE!")

# market_value = soup.find(class_='market_value_class')
# if market_value:
#     market_value = market_value.text.strip()
# else:
#     print("DNE!!")
# print(f"{realTeamName} market value:{market_value}")
# trophy_count = soup.find(id='trophy_count_id')
# if trophy_count:
#     trophy_count = trophy_count.text.strip()
# else:
#     print("DNE!!!")


# url = "https://www.transfermarkt.us/wettbewerbe/fifa"
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    
# }

# response = requests.get(url, headers=headers)

# if response.status_code == 200:
#     print("Request successful!")
#     html_content=response.content  # or response.text for a human-readable format
# else:
#     print(f"Error: {response.status_code}")
# print(html_content)
# soup = BeautifulSoup(html_content, 'html.parser')

# # Example: Scraping team names
# team_names = soup.find_all('td', class_='hauptlink')

# for team in team_names:
#     print(team.text.strip())
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