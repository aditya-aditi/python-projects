from plyer import notification
import requests
from bs4 import BeautifulSoup
import time

def notifyMe(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = "C:\\Users\\RAKESH\\PycharmProjects\\Project\\img\\jarvis.ico" , 
        timeout = 5
    )

def getData(url):
    r = requests.get(url)
    return r.text

if __name__ == "__main__":
        # notifyMe("Aditya", "This is your class time")
        itemList = "This is your class time"

        for item in itemList:
            notifyMe("Jarvis", "This is your class time")
            time.sleep(5)