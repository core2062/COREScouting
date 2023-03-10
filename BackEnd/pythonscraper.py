#!/usr/bin/env python3

import requests
import json

apiKey = input()

matches_url = "https://www.thebluealliance.com/api/v3/event/2023mosl/matches"
headers = {'X-TBA-Auth-Key': apiKey}

response = requests.get(matches_url, headers=headers)

if response.status_code == 200:
    print('Got good stuff')
    # print(response.json())
else:
    print('ooops that did not work')
    exit(1)

match_data = json.loads(response.text)
print(len(match_data))
print(match_data[0]["alliances"]["red"].keys())
print(match_data[0]["alliances"]["blue"]["team_keys"][0])

blue1 = []
blue2 = []
blue3 = []
red1 = []
red2 = []
red3 = []

for x in range(len(match_data)+1):
    blue1.append("")
    blue2.append("")
    blue3.append("")
    red1.append("")
    red2.append("")
    red3.append("")

for x in match_data:
    match_number = x["match_number"]
    blue1[match_number] = x["alliances"]["blue"]["team_keys"][0].replace("frc","")
    blue2[match_number] = x["alliances"]["blue"]["team_keys"][1].replace("frc","")
    blue3[match_number] = x["alliances"]["blue"]["team_keys"][2].replace("frc","")
    red1[match_number] = x["alliances"]["red"]["team_keys"][0].replace("frc","")
    red2[match_number] = x["alliances"]["red"]["team_keys"][1].replace("frc","")
    red3[match_number] = x["alliances"]["red"]["team_keys"][2].replace("frc","")

print('SCHEDULE = [')
for x in range(1,len(match_data)+1):
    # print(x,'(',blue1[x],",",blue2[x],",",blue3[x],",",red1[x],",",red2[x],",",red3[x],')')
    print(f'({blue1[x]}, {blue2[x]}, {blue3[x]}, {red1[x]}, {red2[x]}, {red3[x]}),')

print(']')