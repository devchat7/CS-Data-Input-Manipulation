import requests

url = "https://nfl-team-stats1.p.rapidapi.com/v1/nfl/teamStats"

querystring = {"year":"1988"}

headers = {
    'x-rapidapi-host': "nfl-team-stats1.p.rapidapi.com",
    'x-rapidapi-key': "0b6a317377msh489ed8df96477dfp1230a8jsn6b83369deb30"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)