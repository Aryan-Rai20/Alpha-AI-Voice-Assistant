import pyautogui
import psutil
from weather import get_weather
from ai import ask_ai
import os
import webbrowser
import subprocess
from datetime import datetime


def execute_command(command):

    command = command.lower().strip()

    # Greeting
    words = command.split()
    if "hello" in words or "hi" in words:
     return "Hello Sir! How are you?"

    # Assistant Name
    elif "what is your name" in command or "who are you" in command:
        return "My name is Alpha. I am your personal voice assistant."

    # Time
    elif "what time is it" in command or "time" in command:
        current_time = datetime.now().strftime("%I:%M %p")
        return f"The current time is {current_time}"

    # Date
    elif (
        "date" in command
        or "today's date" in command
        or "what is today's date" in command
    ):
        today = datetime.now().strftime("%d %B %Y")
        return f"Today is {today}"
    
    # Open Google
    elif "open google" in command:
        webbrowser.open("https://www.google.com")
        return "Opening Google"

    # Google Search
    elif command.startswith("search "):
        query = command.replace("search", "", 1).strip()

        if query == "":
            return "What should I search?"

        webbrowser.open(f"https://www.google.com/search?q={query}")
        return f"Searching {query} on Google"

    # Open YouTube
    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        return "Opening YouTube"

    # Play on YouTube
    elif command.startswith("play "):
        video = command.replace("play", "", 1).strip()

        if video == "":
            return "What should I play?"

        webbrowser.open(
            f"https://www.youtube.com/results?search_query={video}"
        )

        return f"Playing {video} on YouTube"

    # Calculator
    elif "open calculator" in command:
        subprocess.Popen("calc.exe")
        return "Opening Calculator"

    # Notepad
    elif "open notepad" in command:
        subprocess.Popen("notepad.exe")
        return "Opening Notepad"
    
    # Paint
    elif "open paint" in command:
        subprocess.Popen("mspaint.exe")
        return "Opening Paint"

    # Screenshot
    elif (
        "take screenshot" in command
        or "capture screen" in command
        or "screenshot" in command
    ):

        screenshot = pyautogui.screenshot()

        desktop = os.path.join(os.path.expanduser("~"), "Desktop")

        filename = datetime.now().strftime("Screenshot_%d%m%Y_%H%M%S.png")

        path = os.path.join(desktop, filename)

        screenshot.save(path)

        return "Screenshot taken successfully."
    
    # Battery Percentage
    elif (
        "battery" in command
        or "battery percentage" in command
        or "battery status" in command
    ):

        battery = psutil.sensors_battery()

        if battery is None:
            return "Battery information is not available."

        percent = battery.percent

        if battery.power_plugged:
            return f"Battery is {percent} percent and the charger is connected."

        return f"Battery is {percent} percent."
    
        # Weather
    elif "weather" in command:

        city = "Varanasi"

        if "in" in command:
            city = command.split("in", 1)[1].strip()

        return get_weather(city)
    
    # AI Mode
    elif (
        "explain" in command
        or "who is" in command
        or "what is" in command
        or "write" in command
        or "tell me" in command
    ):
        return ask_ai(command)
    
    #Developer Details
    elif "developer" in command or "who made you" in command:
     return "I was developed by Aryan Rai using Python and Google Gemini AI."
    
    #Version
    elif "version" in command:
     return "Alpha AI Voice Assistant Version 1.0"
 
    # Exit
    elif (
        "exit" in command
        or "bye" in command
        or "goodbye" in command
        or "good bye" in command
        or "close assistant" in command
    ):
        return "exit"

    else:
        return "Sorry Sir, I don't understand this command."