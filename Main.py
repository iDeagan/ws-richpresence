from pypresence import Presence
import time
from hmisc import API_KEY
import requests
import random

client_id = 'XXXXXX' #put the client_id from the application you created in here
RPC = Presence(client_id)
RPC.connect()


APIKEY = API_KEY.return_api_key()

#Type /api in game and go to API_KEY.py in the hmisc folder

url = f"https://api.hypixel.net/player?key={APIKEY}&name=xDeagan" #change xDeagan to your ign
res = requests.get(url)
data = res.json()

current_ws = (data["player"]["achievements"]["duels_duels_win_streak"])

                                                                                            #go to discordapp.com/developers
print("Made by Deagan#0001")                                                                                       #make an application, then go to
                                                                                            #Rich Presence > Assets and upload
                                                                                            #an image, then set the name to big-image
while True:
    RPC.update(state="Current Win Streak: " + str(current_ws), details="Hypixel Winstreak", large_image="big-image",large_text="Made by Deagan#0001")
    time.sleep(15)

    #Updates every 15 seconds