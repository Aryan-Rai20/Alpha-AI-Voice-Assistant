import speech_recognition as sr

recognizer = sr.Recognizer()

recognizer.energy_threshold = 300
recognizer.dynamic_energy_threshold = True
recognizer.pause_threshold = 0.6
recognizer.non_speaking_duration = 0.3


def listen():

    try:

        with sr.Microphone() as source:

            print("🎤 Listening...")

            recognizer.adjust_for_ambient_noise(source, duration=0.5)

            audio = recognizer.listen(
            source,
            timeout=10,
            phrase_time_limit=7
            )

        print("🧠 Recognizing...")

        command = recognizer.recognize_google(
            audio,
            language="en-IN"
        )

        print("You:", command)

        return command.lower()

    except sr.WaitTimeoutError:
        print("No Speech")
        return ""

    except sr.UnknownValueError:
        print("Didn't understand")
        return ""

    except Exception as e:
        print("ERROR:", e)
        return ""