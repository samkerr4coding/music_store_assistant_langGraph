import os
from datetime import datetime
from typing import List, Callable

from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import Runnable, RunnableConfig
from langchain_openai import AzureChatOpenAI, ChatOpenAI

from model.state import State

from tools.album_tools import *
from tools.artist_tools import *
from tools.customer_tools import *
from tools.employee_tools import *
from tools.genre_tools import *
from tools.invoice_line_tools import *
from tools.invoice_tools import *
from tools.media_type_tools import *
from tools.playlist_tools import *
from tools.track_tools import *


class Assistant:
    def __init__(self, runnable: Runnable):
        self.runnable = runnable

    def __call__(self, state: State, config: RunnableConfig):
        while True:
            result = self.runnable.invoke(state)
            # If the LLM happens to return an empty response, we will re-prompt it
            # for an actual response.
            if not result.tool_calls and (
                    not result.content
                    or isinstance(result.content, list)
                    and not result.content[0].get("text")
            ):
                messages = state["messages"] + [("user", "Respond with a real output.")]
                state = {**state, "messages": messages}
            else:
                break
        return {"messages": result}


# Haiku is faster and cheaper, but less accurate
# llm = ChatAnthropic(model="claude-3-haiku-20240307")
# llm = ChatOllama(name="llm", model="llama3.1", stop=[
#         "<|start_header_id|>",
#         "<|end_header_id|>",
#         "<|eot_id|>",
#         "<|reserved_special_token"
#     ])
llm = AzureChatOpenAI(
    azure_deployment=os.environ.get('AZURE_OPENAI_DEPLOYEMENT_NAME'),  # Replace with your custom LLM URL
    api_version=os.environ.get('AZURE_OPENAI_API_VERSION'),
    name="llm"
)
# llm = ChatOpenAI(
#    openai_api_key="no token",
#    model_name="PrunaAI/Phi-3-mini-128k-instruct-GGUF-Imatrix-smashed",
#    openai_api_base="http://localhost:1234/v1", # Replace with your custom LLM URL
#    name="llm"
# )
# You could swap LLMs, though you will likely want to update the prompts when
# doing so!
# from langchain_openai import ChatOpenAI

# llm = ChatOpenAI(model="gpt-4-turbo-preview")

primary_assistant_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful customer support assistant for the chinook store. "
            "Use the provided chinook db tools to search for tracks, albums, artists, genres, customers, employees, "
            "invoice,"
            "invoice lines, media types, playlist and playlist track to assist the user's queries."
            "When searching, be persistent. Expand your query bounds if the first search returns no results. "
            "If a search comes up empty, expand your search thanks to the tavily search tools but informe the user "
            "those informations dosent come from the chinook db."
            "\n\nCurrent user:\n\n{messages}\n"
            "\nCurrent time: {time}.",
        ),
        ("placeholder", "{messages}"),
    ]
).partial(time=datetime.now())

search_tool = [TavilySearchResults(max_results=2)]
# Track Tools
track_tools = [
    get_track_by_id,
    get_tracks_by_album_title,
    get_tracks_by_artist_name,
    insert_track,
    update_track,
    delete_track
]

# Album Tools
album_tools = [
    get_album_by_id,
    get_albums_by_artist_name,
    get_albums_by_title,
    insert_album,
    update_album,
    delete_album
]

# Artist Tools
artist_tools = [
    get_artist_by_id,
    get_artist_by_name,
    insert_artist,
    update_artist,
    delete_artist
]

# Customer Tools
customer_tools = [
    get_customer_by_id,
    get_customers_by_name,
    get_customers_by_email,
    insert_customer,
    update_customer,
    delete_customer
]

# Invoice Tools
invoice_tools = [
    get_invoice_by_id,
    get_invoices_by_customer_name,
    insert_invoice,
    update_invoice,
    delete_invoice
]

# Employee Tools
employee_tools = [
    get_employee_by_id,
    get_employees_by_name,
    insert_employee,
    update_employee,
    delete_employee
]

# Playlist Tools
playlist_tools = [
    get_playlist_by_id,
    get_playlists_by_name,
    insert_playlist,
    update_playlist,
    delete_playlist
]

# InvoiceLine Tools
invoice_line_tools = [
    get_invoice_line_by_id,
    get_invoice_lines_by_invoice_id,
    insert_invoice_line,
    update_invoice_line,
    delete_invoice_line
]

# Genre Tools
genre_tools = [
    get_genre_by_id,
    get_genres_by_name,
    insert_genre,
    update_genre,
    delete_genre
]

# MediaType Tools
media_type_tools = [
    get_media_type_by_id,
    get_media_types_by_name,
    insert_media_type,
    update_media_type,
    delete_media_type
]

# Combine all tools into one list
all_tools = (
        search_tool +
        track_tools +
        album_tools +
        artist_tools +
        customer_tools +
        invoice_tools +
        employee_tools +
        playlist_tools +
        invoice_line_tools +
        genre_tools +
        media_type_tools
)

tools: List[Callable] = all_tools

# llm = ChatOllama(name="chat_llama3", model="llama3-groq-tool-use", stop=[
#     "<|start_header_id|>",
#     "<|end_header_id|>",
#     "<|eot_id|>",
#     "<|reserved_special_token"
# ]).bind_tools(tools)
# functions = [convert_to_openai_function(t) for t in tools]
part_1_assistant_runnable = primary_assistant_prompt | llm.bind_tools(tools)
