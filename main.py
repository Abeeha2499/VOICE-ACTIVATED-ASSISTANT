import speech_recognition as sr
import pyttsx3
import random 
from datetime import datetime

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("????? Speak Now...")
        audio = r.listen(source)

        try:
            command = r.recognize_google(audio)
            print(f"✅ YOU SAID: {command}")
            return command.lower()

        except sr.UnknownValueError:
            print("❌ Could not Understand")

        except sr.RequestError as e:
            print(f"❌ API Error: {e}")
    return ""

def respond_to_command(command):
    if "hello" in command:
        speak("Hi there! How may i help")
    elif "your name" in command:
        speak("I am your Python Voice Assistant.")
    elif "time" in command:
        now  = datetime.now().strftime("%H:%M")
        speak(f"The time right now is {now}")
    elif "joke" in command:
        speak("why do programmers wear glasses? Because they C sharp")
    elif "rid" in command:
        speak("I have keys but no locks, I have space but no room, You can enter but you cant go outside, What am I? ........... A keyboard")
    elif "date" in command:
        today = datetime.now().strftime("%d-%m-%Y")
        print("Today's date is", today)
    elif "dice" in command or "roll" in command:
        number = random.randint(1, 6)
        speak(f"You rolled a {number}")
        print("Dice number:", number)
    elif "exit" in command or "stop" in command:
        speak("! GOODBYE !")
        return False
    else:
        speak("Im not sure how to help with that")
    return True

def main():
    speak("Voice Assistant activated. Say something")

    while True:
        command = get_audio()
        if command and not respond_to_command(command):
            break

if __name__ == "__main__":
    main()
