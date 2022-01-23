import pyttsx3

engine = pyttsx3.init('espeak')
engine.say("hello, world. My name is Ubuntu")
engine.runAndWait()
