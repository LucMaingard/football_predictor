import bs4 
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import requests
import csv

#global variables
URL_PREF = "https://www.premierleague.com/clubs/" 
#URL = "https://www.premierleague.com/clubs/12/Manchester-United/stats?se=363"
URL_END = "/stats"
FILENAME = "stats.txt"
INDEX = 1

teams = ['34/Fulham', '6/Crystal-Palace', '10/Liverpool', '25/West-Ham-United', '36/West-Bromwich-Albion',
       '21/Tottenham-Hotspur', '131/Brighton-And-Hove-Albion', '18/Sheffield-United', '7/Everton', '9/Leeds-United',
       '12/Manchester-United', '1/Arsenal', '20/Southampton', '23/Newcastle', '4/Chelsea',
       '26/Leicester-City', '2/Aston-Villa', '38/Wolverhampton-Wanderers', '43/Burnley', '11/Manchester-City',
       '127/Bournemouth', '33/Watford', '14/Norwich', '159/Huddersfield-Town', '46/Cardiff-City',
       '42/Stoke', '45/Swansea', '41/Hull-City', '13/Middlesbrough', '29/Sunderland', '17/Queens-Park-Rangers',
       '40/Reading', '39/Wigan-Athletic', '3/Blackburn-Rovers', '27/Bolton-Wanderers', '35/Birmingham-City',
       '44/Blackpool']

#initialise list to check for duplicate articles
article_duplicate = []

#function to write to file
def write_file(data):
    with open(FILENAME, mode='a') as stats_file:
        stats_writer = csv.writer(stats_file, delimiter=',')

        stats_writer.writerow(data)

#function to retrieve stats
def get_stats(url):

    page = requests.get(url)
    bs = soup(page.content, 'html.parser')

    team_name = bs.find(class_="team js-team").text.strip().replace('\n', '')
    matches = float(bs.find(class_="allStatContainer statmatches_played").text.strip().replace('\n', '').replace(',',''))
    big_chances = float(bs.find(class_="allStatContainer statbig_chance_created").text.strip().replace('\n', '').replace(',',''))
    pass_per_match = float(bs.find(class_="allStatContainer stattotal_pass_per_game").text.strip().replace('\n', '').replace(',',''))
    tackle_success = float(bs.find(class_="allStatContainer stattackle_success").text.strip().replace('\n', '').replace('%',''))/100
    cross_accuracy = float(bs.find(class_="allStatContainer statcross_accuracy").text.strip().replace('\n', '').replace('%',''))/100
    headed_clearance = float(bs.find(class_="allStatContainer stateffective_head_clearance").text.strip().replace('\n', '').replace(',',''))
    interceptions = float(bs.find(class_="allStatContainer statinterception").text.strip().replace('\n', '').replace(',',''))
    clearances = float(bs.find(class_="allStatContainer stattotal_clearance").text.strip().replace('\n', '').replace(',',''))

    #convert to stats per game
    big_chances_per_game = big_chances/matches
    headed_clearance_per_game = headed_clearance/matches
    interceptions_per_game = interceptions/matches
    clearances_per_game = clearances/matches
    tackle_success_per_game = tackle_success/matches

    ##create data row
    write = (
        team_name, 
        big_chances_per_game, 
        pass_per_match, 
        tackle_success_per_game, 
        cross_accuracy, 
        headed_clearance_per_game, 
        interceptions_per_game, 
        clearances_per_game
        )

    return write

#write columns names first
write = [
    'team_name', 
    'big_chances_per_game', 
    'pass_per_match', 
    'tackle_success_per_game',
    'cross_accuracy',
    'headed_clearance_per_game',
    'interceptions_per_game', 
    'clearances_per_game'
    ]

write_file(write)

#loop through lsit of teams, create url and scrape data
for team in teams:

    url = URL_PREF + team + URL_END

    #make connection and scrape
    data = get_stats(url)

    #write data to csv
    write_file(data)




    
    


