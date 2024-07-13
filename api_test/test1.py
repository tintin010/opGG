import urllib.parse
import requests

def get_summoner_puuid(api_key, summonerName, summonerTag, region):
    # Check if the summonerName contains non-ASCII characters
    if any(ord(char) > 127 for char in summonerName):
        encoded_summonerName = urllib.parse.quote(summonerName)
    else:
        encoded_summonerName = summonerName.replace(" ", "%20")

    # Generate URL
    base_url = f"https://{region.lower()}.api.riotgames.com/riot/account/v1/accounts/by-riot-id"
    url = f"{base_url}/{encoded_summonerName}/{summonerTag}?api_key={api_key}"

    # Headers
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
        "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "https://developer.riotgames.com"
    }

    # Make GET request
    res = requests.get(url, headers=headers)
    data = res.json()
    print(f"Response Data: {data}")  # 디버깅을 위한 응답 데이터 출력

    if "puuid" in data:
        return data["puuid"]
    else:
        raise ValueError("The response does not contain 'puuid'.")

def get_summoner_id(api_key, summoner_puuid):
    base_url = f"https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/{summoner_puuid}?api_key={api_key}"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
        "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "https://developer.riotgames.com"
    }

    # Make GET request
    res = requests.get(base_url, headers=headers)
    data = res.json()

    return data["id"]

def get_summoner_tier(api_key, summoner_id):
    base_url = f"https://kr.api.riotgames.com/lol/league/v4/entries/by-summoner/{summoner_id}?api_key={api_key}"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
        "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "https://developer.riotgames.com"
    }

    # Make GET request
    res = requests.get(base_url, headers=headers)
    data = res.json()

    # Check if the response contains enough data
    if len(data) > 1:
        tier = data[1]["tier"]
    elif len(data) > 0:
        tier = data[0]["tier"]
    else:
        tier = "Unranked"

    return tier

def get_summoner_tier(api_key, summoner_id):
    base_url = f"https://kr.api.riotgames.com/lol/league/v4/entries/by-summoner/{summoner_id}?api_key={api_key}"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
        "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "https://developer.riotgames.com"
    }

    # Make GET request
    res = requests.get(base_url, headers=headers)
    data = res.json()

    # Check if the response contains enough data
    if len(data) > 1:
        tier = data[1]["tier"]
    elif len(data) > 0:
        tier = data[0]["tier"]
    else:
        tier = "Unranked"

    return tier

def get_match_ids(api_key, puuid, start=0, count=20, region):
    # Generate URL
    url = f"https://{region.lower()}.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?start={start}&count={count}&api_key={api_key}"

    # Headers
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://developer.riotgames.com"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        match_ids = response.json()
        # print(f"Match IDs: {match_ids}")  # 디버깅을 위한 응답 데이터 출력
        return match_ids[:10]  # 상위 10개의 값만 반환
    else:
        print("Error:", response.json())
        return None
    
def winningCheck(api_key, puuid, gameId):

    url = f"https://{region.lower()}.api.riotgames.com/lol/match/v5/matches/{gameId}?api_key={api_key}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
        "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "https://developer.riotgames.com"
    }
    response = requests.get(url, headers=headers)
    participantId = 0

    if response.status_code == 200:
        data = response.json()

    for i in range(0,10):
        if puuid == data["metadata"]["participants"][i]:
            print(puuid)
            if(data["info"]["participants"][i]["win"] == True):
                print("WIN")
                return 1
            else:
                print("LOSE")
                return 0
            

def calculate_win_rate(api_key, puuid, region):
    # 최근 20경기의 매치 ID를 가져옴
    match_ids = get_match_ids(api_key, puuid, 0, 20, region)
    if not match_ids:
        print("No match IDs found.")
        return None

    win_count = 0
    total_matches = len(match_ids)

    for match_id in match_ids:
        win_status = winningCheck(api_key, puuid, match_id, region)
        if win_status:
            win_count += 1

    win_rate = (win_count / total_matches) * 100
    return win_rate


def get_summoner_info(api_key, summonerName, summonerTag, region):
# try:
    # Get the PUUID first
    summoner_puuid = get_summoner_puuid(api_key, summonerName, summonerTag, region)
    
    # Use the PUUID to get the summoner ID
    summoner_id = get_summoner_id(api_key, summoner_puuid)
    
    # Use the summoner ID to get the summoner tier
    summoner_tier = get_summoner_tier(api_key, summoner_id)

    # Use the PUUID to get the 10 match ID
    # match_ids = get_match_ids(api_key, summoner_puuid, 0, 20, region)
    win_rate = calculate_win_rate(api_key, summoner_puuid, region)

    #Use the PUUID to check Win
    # winning = winningCheck(api_key, summoner_puuid, "KR_7128915709")
    # print("winning : ", winning)

    print(f"The tier of the summoner {summonerName} is {summoner_tier}.")
    print("승률은 : {win_rate}")
        
    #     return summoner_tier
    # except Exception as e:
    #     print(f"An error occurred: {e}")
    #     return None
    


# Example usage
api_key = "RGAPI-6cb9b98d-2b0b-4dee-86e6-40826f465760"
summonerName = "이순신의동기부여"
summonerTag = "KR1"
region = "ASIA"

summoner_tier = get_summoner_info(api_key, summonerName, summonerTag, region)
