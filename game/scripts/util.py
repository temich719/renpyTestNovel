import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.setProperty("voice", "ru")
    engine.say(text)
    engine.runAndWait()
    