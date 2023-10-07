from TTS import TTS
from STT import STT
from DateTimeConversion import convert_mmddyy as cmdy
import wikipedia

class Execution: 
    
    wakeup_word = "ark"
        
           
    def check_wakeup_call():
        x = True
        while (x):
            TTS.tts("Listening for wakeup word...")
            text = STT.recognize_speech(True)
            print("Listening for wakeup word...")
            if text.count(Execution.wakeup_word) > 0:
                text = STT.recognize_speech(False)
                TTS.tts("Wakeup word detected!, Initializing Ark")
                x = False
                Execution.commands()

                # self.recognize_speech(False) 

    def commands():
        TTS.tts("Hello. I am Ark. What can I do for you today")
        x = True
        while (x):
            text = STT.recognize_speech(True)
            if "end" in text:
                TTS.tts("Goodbye")
                x = False
                Execution.check_wakeup_call()
            elif "how are you" in text: 

                TTS.tts("I am fine, how are you")
    
    
            elif "what is a" in text: # add variation in functionality for prompt
                # if "what is" in text: 
                #     text_cleaned = text.replace("what is", " ")
                # elif "what is  a" in text:  
                text_cleaned = text.replace("what is a", " ")
                info = wikipedia.summary(text_cleaned, 1)
                TTS.tts(info)
                continue
            elif "event adder"in text: 
                TTS.tts("Launching event adder")
                Execution.get_event_info()
                continue
            # elif "time" in text:  

    
    def get_event_info():
        TTS.tts("What's the name of the event?")
        event_name = STT.recognize_speech(True)
        TTS.tts("When is the event?")
        event_date = cmdy(str(STT.recognize_speech(True)))
        TTS.tts("What time does the event start?")
        event_start_time = STT.recognize_speech(True)
        TTS.tts("What time does the event end?")
        event_end_time = STT.recognize_speech(True)
        TTS.tts("Where is the event?")
        event_location = STT.recognize_speech(True)
        TTS.tts("Any additional information about the event?")
        event_description = STT.recognize_speech(True)
        TTS.tts(str(event_name) + str(event_date))

    def add_event_linker():  
        pass

Execution.check_wakeup_call()
