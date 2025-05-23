from typing import Annotated
from typing_extensions import TypedDict


class State(TypedDict):
    messages: Annotated[list[dict],add_messages]
    
    
def chatbot(state:State):
    messages = state.get("messages")
    
    #@OPENAI Call 
    
    state.messages = messages
    
    return state