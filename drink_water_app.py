import time
from plyer import notification

while True:
    print("Its Time to  Drink water")
    notification.notify(title = "drink water",
                        message = "Bro its time to hydarte your body",)
    time.sleep(60*60)