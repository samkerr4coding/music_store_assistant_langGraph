"""
Simple demo of integration with ChainLit and LangGraph.
"""
import datetime
import uuid

import chainlit as cl
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, ToolMessage
from langchain_core.runnables import Runnable
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import StateGraph
from langgraph.prebuilt import tools_condition

from model.agent import tools, part_1_assistant_runnable, Assistant
from model.state import State
from utils.utils import create_tool_node_with_fallback

load_dotenv()
# TODO : Enhance prompt template
# TODO : Add context memory
# TODO : Human in the loop


@cl.on_chat_start
async def on_chat_start():
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
    memory = MemorySaver()

    graph = graph_builder.compile(
        checkpointer=memory,
        # This is new!
        # interrupt_before=["tools"],
        # Note: can also interrupt __after__ actions, if desired.
        # interrupt_after=["tools"]
    )
    # initialize state
    state = State(messages=[])

    # one config per conversation
    config = await get_config()
    # save graph and state to the user session
    cl.user_session.set("graph", graph)
    cl.user_session.set("state", state)
    cl.user_session.set("config", config)


@cl.on_message
async def on_message(message: cl.Message):
    # Retrieve the graph and state from the user session
    graph: Runnable = cl.user_session.get("graph")
    state = cl.user_session.get("state")
    config = cl.user_session.get("config")

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
    async for event in graph.astream_events(latest_message_state, config,  version="v1"):
        kind = event["event"]
        if kind == "on_chat_model_stream":
            if event["event"] == "on_chat_model_stream" and event["name"] == "llm":
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


async def get_config():
    return {"configurable": {"thread_id": uuid.uuid4()}}

if __name__ == "__main__":
    from chainlit.cli import run_chainlit
    run_chainlit(__file__)