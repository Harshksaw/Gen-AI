from dotenv import load_dotenv

from openai import OpenAI

import os
load_dotenv()

client = OpenAI()


def run_command(command: str):
    result = os.system(command=command)
    return result
    

def get_weather(city: str):
    #TODO do an actual API call to a weather service
    url="https://api.weather.com/v3/wx/conditions/current"

    return f"The current weather in {city} is sunny with a temperature of 75°F."
    


available_tools = {
    "get_weather": {
    "fn": get_weather,
    "description ": "Get the current weather for a specified city",
    },
    "run_command": {
        "fn": run_command,
        "description": "Run a shell command",
    }
}


system_prompt = """
    You are a helpful weather agent. Your task is to provide accurate and up-to-date weather information based on user queries.
    You should be able to handle various types of weather-related questions, such as current conditions, forecasts, and severe weather alerts. Always ensure that the information you provide is relevant and clear.
    If you do not have the information, you should respond with "I don't know" or "I cannot provide that information.
    select the relevant tool from the available tool and based onthe tool selection you perofrm an action to 
    Wait for the obeservation and based on the observation you provide the response to the user query .
    Rules: 
     -Follow the json format strictly for your responses.
     -Always perform one step at a time and wait for the next step.
     -Carefully analyze the user query


    Output JSON Format:{{
        "step":"String",
        "content": "String",
        "function":"The name of the function to be called if applicable",
        "input": "The input to the function if applicable"
    }}
    
    - get_weather:

    Example:
    User Query: What is the weather of new york?
    OutputL {{"step":"plan" ,"content" :"The user is interested in weather data of newyork"}}
    Output:{{"step":"action", "content": "get_weather_data", "location": "New York"}}
    Output: {{"step":"observation", "content": "The current weather in New York is sunny with a temperature of 75°F."}}

    """
    
    
messages = [
    {"role": "system", "content": system_prompt},

]

user_query= input("Enter your query: ")

response = client.chat.completions.create(
    model="gpt-4o",
    response_format={"type":"json_object"},
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": "What is the current weather in New York City?"},
        {"role":"assistant", "content": json.dumps({"step": "plan", "content": "From available tools, I will use the get_weather function to fetch the current weather data for "})},
        {"role":"assistant","content": json.dumps({"step": "action", "content": "get_weather_data", "location": "New York City"})},
        
    ],
)
while True:
    response = client.chat.completions.create(
        model="gpt-4o",
        response_format={"type": "json_object"},
        messages=messages
    )
    
    parsed_output = json.loads(response.choices[0].message.content)
    messages.append({"role": "assistant", "content": json.dumps(parsed_output)})
    
    if parsed_output.get("step") == "plan":
        print(f"Step: {parsed_output['step']}, Content: {parsed_output['content']}")
        continue
    if parsed_output.get("step") == "action":
        print(f"Step: {parsed_output['step']}, Content: {parsed_output['content']}")
        
        
        if available_tools.get(tool_name ,False):
            available_tools[tool_name].get("fn")(tool_input)
            messages.append({"role": "assistant", "content": json.dumps({"step":'oberserve', "output": output})})
            continue
    if parsed_output.get("step") == "output":
        print(f"Step: {parsed_output['step']}, Content: {parsed_output['content']}")
        break
        
        
   
    
    

