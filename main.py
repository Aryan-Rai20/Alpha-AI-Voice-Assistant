from assistant import speak
from listener import listen
from commands import execute_command

speak("Hello Sir")
speak("Alpha Assistant is ready.")

while True:

    input("\nPress ENTER to talk...")

    command = listen()

    if command == "":
        continue

    print("You:", command)

    response = execute_command(command)

    print("Assistant:", response)

    if response == "exit":
        speak("Goodbye Sir")
        break

    speak(response)
    