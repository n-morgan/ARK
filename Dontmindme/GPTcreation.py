from TTS import TTS
from STT import STT
from DateTimeConversion import convert_mmddyy as cmdy
import wikipedia
import random

class Execution:
    
    wakeup_word = "ark"
        
    def check_wakeup_call():
        x = True
        greetings = ["Hello!", "Hi there!", "Hey!"]
        while x:
            TTS.tts("Listening for the wakeup word...")
            text = STT.recognize_speech(True)
            print("Listening for the wakeup word...")
            if text.count(Execution.wakeup_word) > 0:
                text = STT.recognize_speech(False)
                TTS.tts(random.choice(greetings) + " I'm Ark, your personal assistant.")
                x = False
                Execution.commands()

    def commands():
        TTS.tts("Hello! I'm Ark. How can I assist you today?")
        x = True
        while x:
            text = STT.recognize_speech(True)
            if "end" in text:
                farewells = ["Goodbye!", "Farewell!", "See you later!"]
                TTS.tts(random.choice(farewells))
                x = False
            elif "how are you" in text:
                responses = ["I'm doing great!", "I'm feeling fantastic!", "I'm good, thank you!"]
                TTS.tts(random.choice(responses))
            elif "what is a" in text:
                text_cleaned = text.replace("what is a", "")
                info = wikipedia.summary(text_cleaned, 1)
                TTS.tts("A " + text_cleaned + " is " + info)
            elif "event adder" in text:
                TTS.tts("Launching the event adder")
                Execution.get_event_info()

    # Add more functions and personality to your assistant here
Execution.check_wakeup_call()