import pyttsx3

def create_engine():
    engine = pyttsx3.init()
    engine.setProperty("rate", 170)
    engine.setProperty("volume", 1.0)

    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[0].id)

    return engine


def speak(text):
    print("Assistant:", text)

    engine = create_engine()   # Har baar naya engine banega

    engine.say(text)
    engine.runAndWait()
    engine.stop()