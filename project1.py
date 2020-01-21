import urllib.request
import json
import cassiopeia as cass
from cassiopeia import Summoner








# api = 'RGAPI-d5f0cdd8-82d0-4114-89cc-e42cfbe7dbbd'


def get_AccountId(Summoner_Name):
    url = 'https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/'
    api = 'RGAPI-d5f0cdd8-82d0-4114-89cc-e42cfbe7dbbd'
    final_Summoner_Name = ''
    for char in Summoner_Name:
        if char == ' ':
            final_Summoner_Name = final_Summoner_Name + '%20'
        elif char == 'ø':
            final_Summoner_Name = final_Summoner_Name + '%C3%B8'
        else:
            final_Summoner_Name = final_Summoner_Name + char  
    final_url = url + final_Summoner_Name + '?api_key=' + api

    response = urllib.request.urlopen(final_url).read()
    json_obj = str(response, 'utf-8')
    data = json.loads(json_obj)

    accountId = data["accountId"]
    return accountId


def arams_ranked_total_games_on_account(accountId):
    url = 'https://na1.api.riotgames.com/lol/match/v4/matchlists/by-account/'
    api = 'RGAPI-d5f0cdd8-82d0-4114-89cc-e42cfbe7dbbd'

    ranked_games = 0
    aram_games = 0

    final_url = url + accountId +'?api_key=' + api
    response = urllib.request.urlopen(final_url).read()
    json_obj = str(response, 'utf-8')
    data = json.loads(json_obj)

    totalGames = data["totalGames"]

    if totalGames > 100:
        final_url = url + accountId +'?beginIndex=75' + '&api_key=' + api
        response = urllib.request.urlopen(final_url).read()
        json_obj = str(response, 'utf-8')
        data = json.loads(json_obj)
    
        totalGames = data["totalGames"]
    
    for i in range(int(totalGames/100 + 1)):
        
        begin_Index = 0 + 100*i
        final_url = url + accountId +'?beginIndex=' + str(begin_Index) + '&api_key=' + api

        response = urllib.request.urlopen(final_url).read()
        json_obj = str(response, 'utf-8')
        data = json.loads(json_obj)

        matches = data["matches"]
       
        for item in matches:

            if item["queue"] == 420:
                ranked_games += 1
            elif item["queue"] == 450:
                aram_games += 1
    
    queues = {
        "total" : totalGames,
        "ranked" : ranked_games,
        "aram" : aram_games
    } 
    return queues

def gather_gameId(accountId):
    url = 'https://na1.api.riotgames.com/lol/match/v4/matchlists/by-account/'
    api = 'RGAPI-d5f0cdd8-82d0-4114-89cc-e42cfbe7dbbd'

    gameId = []
    ranked_gameId = []
    aram_gameId = []
    normal_blind_gameId = []
    normal_draft_gameId = []
    urf_gameId = []
    nexus_blitz_gameId = []
    for i in range(25):
        
        begin_Index = 0 + 100*i
        final_url = url + accountId +'?beginIndex=' + str(begin_Index) + '&api_key= ' + api

        response = urllib.request.urlopen(final_url).read()
        json_obj = str(response, 'utf-8')
        data = json.loads(json_obj)

        matches = data["matches"]
       
        for item in matches:
            gameId.append(item["gameId"])
            if item["queue"] == 400:
                normal_draft_gameId.append(item["gameId"])
            elif item["queue"] == 420:
                ranked_gameId.append(item["gameId"])
            elif item["queue"] == 430:
                normal_blind_gameId.append(item["gameId"])
            elif item["queue"] == 450:
                aram_gameId.append(item["gameId"])
            elif item["queue"] == 900:
                urf_gameId.append(item["gameId"])
            elif item["queue"] == 1200:
                nexus_blitz_gameId.append(item["gameId"])

    queues = {
        "total" : gameId,
        "ranked" : ranked_gameId,
        "aram" : aram_gameId,
        "normal blind" : normal_blind_gameId,
        "normal draft" : normal_draft_gameId,
        "urf" : urf_gameId,
        "nexus blitz" : nexus_blitz_gameId
    }     
        
    
    return queues

games = arams_ranked_total_games_on_account(get_AccountId("Adrian Seira"))
print (games)
# print (games['total'])

#print ("This account has " + str(len(gather_gameId(get_AccountId('Jon Leffy'))["urf"])) + " urf games played.")
#print ("This account has " + str(len(gather_gameId(get_AccountId('Jon Leffy'))["normal draft"])) + " normal draft games played.")
#print ("This account has " + str(len(gather_gameId(get_AccountId('Jon Leffy'))["nexus blitz"])) + " nexus blitz games played.")
#print (gather_gameId())
#print (get_AccountId('GammaRays123'))
#print (get_AccountId('Ryze Gød'))







#reksai int = 421
# ranked solo queue int = 420
# season 9 start (1/23/2019 12 am local) epoch time 1548230400000
# epoch time difference of exactly 1 week is 604800000
# season 9 end (11/19/2019 12 am local) epoch time 1574150400000
# #{
#     "profileIconId": 588,
#     "name": "Ryze Gød",
#     "puuid": "RGjbd24ZaxizENVpxVM3Uran5JULKnNWrfvjQVDuz92tEbpItaslEu_ualtlTq4yI6hhSSjKhp2pqg",
#     "summonerLevel": 209,
#     "accountId": "ItkOJp2IMmbWGdcxM9S53ZzFDeoo5tHkoSSNHe5FOiq1Rg",
#     "id": "cblmFXiFBZQQcf4p02PNrVWMZVKT81yUWE4PxWGc-5VR65I",
#     "revisionDate": 1578285866000
# }
