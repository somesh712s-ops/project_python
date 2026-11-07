
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import textwrap
import webbrowser
from urllib.parse import quote_plus
import os
import pyautogui
import time


# Text to Speech
def speak(audio):
    engine = pyttsx3.init('sapi5')

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)

    for chunk in textwrap.wrap(str(audio), width=180):
        engine.say(chunk)
        engine.runAndWait()

    engine.stop()


# Greeting Function
def wish():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good morning!")

    elif hour >= 12 and hour < 18:
        speak("Good afternoon!")

    else:
        speak("Good evening!")

    speak("I am AMIS. How can I help you?")


# Speech Recognition
def takecommand(energy_threshold=None):
    r = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("Listening.. Speak now.")
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(source, duration=0.5)
            if energy_threshold is not None:
                r.energy_threshold = min(r.energy_threshold, energy_threshold)
                r.dynamic_energy_threshold = False
                print(f"Reply microphone threshold: {r.energy_threshold}")
            audio = r.listen(source, timeout=5, phrase_time_limit=20)

        print("Recognizing..")
        query = r.recognize_google(audio, language="en-IN")
        print(f"User said: {query}\n")
    except Exception as error:
        print(f"Speech recognition failed: {error}")
        return "None"

    return query

def play_on_youtube(video):
    speak("opening youtube")
    search = quote_plus(video)
    url = f"https://www.youtube.com/results?search_query={search}"

    webbrowser.open(url)
    time.sleep(5)
    pyautogui.click(450,250)
    speak("Enjoy your video sir")


def open_whatsapp():
    try:
        os.startfile("whatsapp://")
        speak("Opening WhatsApp")
    except OSError as error:
        print(f"Could not open WhatsApp desktop: {error}")
        speak("I could not open the desktop app. Opening WhatsApp Web.")
        webbrowser.open("https://web.whatsapp.com/")


def whatsapp_reply(person):
    open_whatsapp()
    time.sleep(3)

    pyautogui.hotkey("ctrl", "f")
    time.sleep(2)
    pyautogui.hotkey("ctrl", "a")
    pyautogui.write(person, interval=0.05)
    time.sleep(1)
    pyautogui.press("Down")
    pyautogui.press("enter")
    time.sleep(1)
    # pyautogui.press("esc")

    screen_width, screen_height = pyautogui.size()
    message_box_x = screen_width // 2
    message_box_y = screen_height - 80
    pyautogui.click(message_box_x, message_box_y)

    speak("Say the message you want to reply with.")
    message = takecommand(energy_threshold=100)
    if message.strip().lower() == "none":
        speak("I didn't catch your message. I have not typed or sent anything.")
        return

    print(f"Reply captured: {message}")
    pyautogui.click(message_box_x, message_box_y)
    pyautogui.write(message, interval=0.03)
    speak("Your message is typed. Check it in WhatsApp, then press Enter to send.")
    


# Main Program
if __name__ == "__main__":

    wish()

    while True:

        recognized = takecommand()
        if recognized == "None":
            continue
        query = recognized.lower()

        if query in ("exit", "quit", "stop"):
            speak("Goodbye Sir")
            break

        elif "wikipedia" in query:

            speak("Searching Wikipedia")

            title = query.replace("wikipedia", "").strip()

            try:
                result = wikipedia.summary(
                    title,
                    sentences=2,
                    auto_suggest=False
                )

                print(f"Wikipedia result: {title}\n{result}")

                speak(result)

            except Exception as e:
                print("Error:", e)
                speak("Sorry, something went wrong.")

        elif  "play" in query and "youtube" in query:
            video = query.replace("play", "").replace("youtube", "").strip()
            play_on_youtube(video)

        elif "open google" in query:
            webbrowser.open("google.com")

        elif "open instagram" in query:
            webbrowser.open("https://www.instagram.com/")

        elif "open chat gpt" in query:
            webbrowser.open("https://chatgpt.com/")

        elif "whatsapp" in query and any(
            action in query for action in ("open", "launch", "start")
        ):
            print(f"Opening WhatsApp for command: {query}")
            open_whatsapp()

        elif "the time " in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strtime}")
        
        elif "reply to" in query:
            person = query.split("reply to", 1)[1].strip()
            if person:
                whatsapp_reply(person)
            else:
                speak("Say reply to followed by the contact name.")

        



