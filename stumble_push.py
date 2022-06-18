import requests
import threading
import datetime
import sys
import os
import time

os.system("pip install requests")
os.system("pip install  threading")
os.system("pip install datetime")
os.system("pip install sys")
os.system("pip install os")
os.system("pip install time")
os.system("cls")
def main():
	global auth, maxerr, api, pos, dely
	os.system('cls' if os.name == 'nt' else 'clear')
print("                ╔══════════════════════════════════════════════╗")
print("                ║            Exploit Stumble iZyen             ║")
print("                ╚══════════════════════════════════════════════╝")
print("                    ╔══════════════════════════════════════╗")
print("                    ║                iZyen                 ║")
print("                    ╚══════════════════════════════════════╝")
print("                ╔══════════════════════════════════════════════╗")
print("                ║               Thanks to iZyen                ║")
print("                ╚══════════════════════════════════════════════╝")
print("="*64)
maxerr = 0 # Avoid Ban when User AFK.
api = "kitkabackend.eastus.cloudapp.azure.com:5010"
auth = str(input("╔══[MP]\n════➤ "))
pos = int(input("""
                ╔══════════════════════════════════════════════╗
0 =             ║ 1. Ronde 1 ( lose )                          ║ 
1 =             ║ 2. Ronde 2 ( lose )                          ║
2 =             ║ 3. Ronde 3 ( win )                           ║
                ╚══════════════════════════════════════════════╝
Select
Input: """))
dely = float(input("\nDelay per Requests (Ex. 0.5, 1.0, 1.5, and etc) :\n╔══[MP]\n════➤ "))
thr = int(input("\nThreads :\n╔══[MP]\n════➤ "))
print("="*64)
for _ in range(thr):
 threading.Thread(target=s).start()

def s():
        global maxerr
        while True:
                dt = datetime.datetime.now()
                try:
                        headers = {
                            'authorization': auth,
                            'use_response_compression': 'true',
                            'Accept-Encoding': 'gzip',
                            'Host': api,
                            'Connection': None,
                            'User-Agent': None,
                        }
                        response = requests.get(f'http://{api}/round/finishv2/{pos}', headers=headers)
                        if response.status_code == 200:
                                trof = response.text.split('"SkillRating":')[1].split(',')[0]
                                cro = response.text.split('"Crowns":')[1].split(',')[0]
                                sys.stdout.write(f"\r[{dt.year}-{dt.month}-{dt.day} {dt.hour}:{dt.minute}:{dt.second}] Success | Trophy: {trof} | Crowns: {cro}")
                                sys.stdout.flush()
                        elif response.status_code == 403 and response.text == "BANNED":
                                print(f"[{dt.year}-{dt.month}-{dt.day} {dt.hour}:{dt.minute}:{dt.second}] YOUR ACCOUNT HAS BEEN BANNED FROM SERVER SIDE!")
                                break
                                sys.exit(0)
                        else:
                                maxerr += 1
                                print(f"[{response.status_code}] Failed. Maybe Auth Key Expired?")
                                if maxerr >= 15: # Avoid Ban Detection
                                        break
                                        sys.exit(0)
                        if dely > 0: time.sleep(dely)
                except Exception as e:
                        pass

if __name__ == "__stumble_push__":
	main()
