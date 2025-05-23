from typing import Annotated
from typing_extensions import  TypedDict
from langraph.graph.message import add_messages
from langraph.graph.message import Message
from langraph.graph.node import ToolNode
from langraph.graph.state import StateGraph
from langraph.graph.state import START, END
from langraph.graph.state import tools_condition
from langraph.llm import init_chat_model
from langraph.llm import LLM
from langraph.llm import init_tool_model


llm = init_chat_model(
    model_provider = "openai",
    model = "gpt-4.1",
)

class State(TypedDict):
    messages: Annotated[list, add_messages]
    
    
    
def chatbot(state):
    message - llm.invoke(state['messages'])
    assert len(message.took_calls) <= 1
    return {"messages": [message]}

tool_node = ToolNode(tools = [])

graph_builder =  StateGraph(State)

graph_builder.add_node('chatbot', chatbot)
graph_builder.add_node('tool_node', tool_node)

graph_builder.add_edge(START, 'chatbot')
graph_builder.add_conditional_edges('chatbot', tools_condition)
graph_builder.add_edge("tools", "chatbot")
graph_builder.add_edge("chatbot",END)

graph  = graph_builder.compile()