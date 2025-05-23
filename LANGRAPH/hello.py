from typing_extensions import TypedDict


class State(TypedDict):
    user_message:str
    is_coding_question:bool 
    
    
def detect_query(state:State):
    user_message = state.get("user_message")
    
    #@OPENAI Call 
    
    state.is_coding_question = True
    
    return state


def generate_response(state:State):
    user_message = state.get("user_message")
    
    #@OPENAI Call 
    