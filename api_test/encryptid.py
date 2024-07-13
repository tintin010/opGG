import urllib.parse
import requests
import test1

def getMatchId(DEVELOPMENTAPIKEY,summonerName):
    encryptedId, encryptedAccountId = encryptId.encrypt(DEVELOPMENTAPIKEY,summonerName)
    headers = {
        "Origin": "https://developer.riotgames.com",
        "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Riot-Token": DEVELOPMENTAPIKEY,
        "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"
        }
    APIURL = "https://kr.api.riotgames.com/lol/match/v4/matchlists/by-account/" + encryptedAccountId
    res = requests.get(APIURL, headers=headers)
    data = res.json()
    return data["matches"][0]["gameId"]

DEVELOPMENTAPIKEY = "RGAPI-eab999c7-926a-45fa-8db3-8716db1c09d2"
summonerName = "HIDE ON BUSH"
print(getMatchId(DEVELOPMENTAPIKEY,summonerName))


# Example usage
api_key = "RGAPI-94934317-ea53-452a-8382-2a303d54c614"
summonerName = "이순신의동기부여"
summonerTag = "KR1"
region = "ASIA"