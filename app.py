"""
Simple demo of integration with ChainLit and LangGraph.
"""
import sqlite3

import chainlit as cl
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langchain_core.runnables import Runnable
from langgraph.graph import StateGraph
from langgraph.prebuilt import tools_condition

from model.agent import tools, part_1_assistant_runnable, Assistant
from model.state import State
from utils.utils import create_tool_node_with_fallback

load_dotenv()
# TODO : use Gemini
# TODO : use Google search tools
# TODO : enhance tools + add playlist track tool
# TODO : multi node agents with :
#  - one to search on the web
#  - one to handle songs tracks etc
#  - one to handle customer , invoices etcs
#  - one to handle employee
#  - on to handle audit tracking

def init_db():
    conn = sqlite3.connect("Chinook_Sqlite.sqlite")
    return conn



@cl.on_chat_start
async def on_chat_start():
    conn = init_db()
    cl.user_session.set("db_conn", conn)

    graph_builder = StateGraph(State)
    # start graph
    graph_builder.add_node("chatbot", Assistant(part_1_assistant_runnable))

    graph_builder.add_node("tools", create_tool_node_with_fallback(tools))

    graph_builder.add_conditional_edges(
        "chatbot",
        tools_condition,
    )
    graph_builder.add_edge("tools", "chatbot")
    graph_builder.set_entry_point("chatbot")
    # TODO : Use checkpointer
    graph = graph_builder.compile(
        # checkpointer=memory,
        # This is new!
        # interrupt_before=["tools"],
        # Note: can also interrupt __after__ actions, if desired.
        # interrupt_after=["tools"]
    )
    # initialize state
    state = State(messages=[])
    # save graph and state to the user session
    cl.user_session.set("graph", graph)
    cl.user_session.set("state", state)


@cl.on_message
async def on_message(message: cl.Message):
    # Retrieve the graph and state from the user session
    graph: Runnable = cl.user_session.get("graph")
    state = cl.user_session.get("state")

    # Append the new message to the state
    state["messages"].append(HumanMessage(content=message.content))

    # Process only the last human message
    last_human_message = state["messages"][-1]

    # Create a new state with only the last human message
    latest_message_state = State(messages=[last_human_message])
    # Stream the response to the UI
    ui_message = cl.Message(content="")
    await ui_message.send()


    # TODO : review the way messages are passed
    async for event in graph.astream_events(latest_message_state, version="v1"):
        kind = event["event"]
        if kind == "on_chat_model_stream":
            if event["event"] == "on_chat_model_stream" and event["name"] == "llm": # event["name"] == "AzureChatOpenAI": #and event["name"] == "chat_llama3":
                content = event["data"]["chunk"].content or ""
                await ui_message.stream_token(token=content)
                print(content, end="|")
        elif kind == "on_tool_start":
            print("--")
            print(
                f"Starting tool: {event['name']} with inputs: {event['data'].get('input')}"
            )
        elif kind == "on_tool_end":
            print(f"Done tool: {event['name']}")
            print(f"Tool output was: {event['data'].get('output')}")
            print("--")


    await ui_message.update()

if __name__ == "__main__":
    from chainlit.cli import run_chainlit
    run_chainlit(__file__)