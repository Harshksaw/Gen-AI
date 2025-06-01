import speech_recognition as sr
import os
from langgraph.checkpoint.mongodb import MongoDBSaver
MONOGODB_URI = os.getenv("MONGODB_URI")
from .graph import create_chat_graph
def main():
    # Initialize recognizer
    
    with MongoDBSaver.from_conn_string(MONOGODB_URI ) as checkpointer:
        graph = create_chat_graph(checkpointer= checkpointer)
        recognizer = sr.Recognizer()

        # Use the microphone as the audio source
        with sr.Microphone() as source:
            print("Please speak something...")
            # Adjust for ambient noise and record audio
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
            
            sst = recognizer.recognize_google(audio)
            print("You said: " + sst)
            graph.stream
            # Save the audio to a file
            
        
        
        

    # # Recognize speech using Google Web Speech API
    # try:
    #     text = recognizer.recognize_google(audio)
    #     print("You said: " + text)
    # except sr.UnknownValueError:
    #     print("Sorry, I could not understand the audio.")
    # except sr.RequestError as e:
    #     print(f"Could not request results; {e}")
        
        
main()