import requests
from colorama import Fore
import pyperclip
import json
import os

if __name__ == "__main__":
     
    auth, channel_id, emoji = json.loads(open("data.json", "r").read()).values()
    headers = {'Content-Type': 'application/json', 'authorization': auth }


    def writeData() -> None: 
        newdata = {
            "auth": auth,
            "channel_id": channel_id,
            "emoji": emoji
        }
        open("data.json", "w").write(json.dumps(newdata))

    while True:
        format = lambda text, i: f"{Fore.BLUE + str(i)}. {Fore.CYAN + text} {Fore.WHITE}"
        isNotBlank = lambda variable: "✓" if len(variable) > 0 else "X"

        userInput = input(f"""
{Fore.GREEN}> getreactions{Fore.WHITE}
{format(f"set auth {isNotBlank(auth)}", 1)}
{format(f"set channel id {isNotBlank(channel_id)}", 2)}
{format(f"emoji id {isNotBlank(emoji)}", 3)}
{format(f"main script", 0)}
{format(f"save data", 4)}
input: """)

        try: int(userInput)
        except:  
           os.system('cls')
           print("not a valid choice")
           print()
           continue

        match int(userInput):
            case 1:
                auth = input("new auth: ")
                headers["authorization"] = auth 
                print("new auth set")
                print()
            case 2:
                channel_id = input("new channel_id: ")
                print("new channel id set")
                print()
            case 3:
                emoji = input("new emoji: ")
                print("new emoji set")
                print()
            case 0: 
               if len(auth) < 0 or len(channel_id) < 0 or len(emoji) < 0:
                    print("info not set")
                    continue
                os.system('cls')
                break
            case 4:
                writeData()
                print("saved data")
                print()
            case _:
                print("invalid entry")
                print()
                
    while True:
        message_id = input("message ID > ")
        url = f"https://discord.com/api/v9/channels/{channel_id}/messages/{message_id}/reactions/{emoji}?limit=100&type=0"
        r = requests.get(url, headers=headers)

        if r.status_code >= 400:
            print("fail")
            continue

        # parse request
        list = "" 
        for i in r.json():
            list += f"<@{i["id"]}> "

        pyperclip.copy(list)
        print(f"copied to clipboard: {list}")

