import os
from datetime import datetime
from typing import List, Callable

from langchain.memory import ConversationBufferMemory
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import Runnable, RunnableConfig
from langchain_core.tools import render_text_description
from langchain_openai import AzureChatOpenAI

from model.state import State
from tools.policy_tool import lookup_policy
from tools.query_tool import execute_query


class Assistant:
    def __init__(self, runnable: Runnable):
        self.runnable = runnable

    def __call__(self, state: State, config: RunnableConfig):
        while True:
            result = self.runnable.invoke(state)
            # Reprompt if no valid output
            if not result.tool_calls and (
                    not result.content or
                    (isinstance(result.content, list) and not result.content[0].get("text"))
            ):
                messages = state["messages"] + [("user", "Respond with a real output.")]
                state = {**state, "messages": messages}
            else:
                break
        return {"messages": result}


# Utility to load model schema from SQL file
def load_db_schema(filepath: str) -> str:
    """Load SQL schema model from a file."""
    with open(filepath, "r", encoding="utf-8") as file:
        return file.read()


def create_tools() -> List[Callable]:
    """Create and return all tools required by the assistant."""
    search_tool = [TavilySearchResults(max_results=2)]
    policy_tool = [lookup_policy]
    query_tool = [execute_query]
    # Combine all tools into one list
    return search_tool + policy_tool + query_tool


def create_prompt_template(rendered_tools: str, model_sql_content: str) -> ChatPromptTemplate:
    """Create and return the primary chat prompt template."""
    return ChatPromptTemplate.from_messages(
        [
            (
                "system",
                f'You are a helpful customer support assistant for the Music store that has access to a variety of tools.'
                f'You will use the provided tools to assist users in their queries about tracks, albums, artists, genres, '
                f'customers, employees, invoices, invoice lines, media types, playlists, and playlist tracks.'
                f'Here are the names and descriptions of the tools you can use: {rendered_tools}. '
                f'For the query tool about building SQL queries, you should rely on the following database schema:\n{model_sql_content}.'
                f'As a summary, for the music store DB: '
                f'1. `artists` is linked to `albums` through `artist_id`.'
                f'2. `albums` is linked to `tracks` through `album_id`.'
                f'3. `tracks` is linked to `genres` through `genre_id`.'
                f'4. `tracks` is linked to `media_types` through `media_type_id`.'
                f'5. `tracks` is linked to `invoice_lines` through `track_id`.'
                f'6. `invoice_lines` is linked to `invoices` through `invoice_id`.'
                f'7. `invoices` is linked to `customers` through `customer_id`.'
                f'8. `customers` are linked to `employees` (support reps) through `support_rep_id`.'
                f'9. `employees` (managers) are linked to other `employees` through `reports_to`.'
                f'10. `playlist_tracks` is linked to `playlists` through `playlist_id`.'
                f'11. `playlist_tracks` is linked to `tracks` through `track_id`.'
                f'Use advanced PostgreSQL syntax to create efficient queries (e.g., COUNT, MAX, MIN, LIKE, AVERAGE).'
                f'For queries, you are allowed to run a COUNT request first to estimate the response size.'
                f'You are allowed to build complex, joined queries based on user requests, and you must adapt as required.'
                f'When your database search yields no results, use Tavily search tools to expand your query, but make sure to inform the user '
                f'that the information does not come from the database.'
                f'If the user want to insert data in the DB, please checkup all the required datas and prompt the user if you are missing datas to fullfill his demand '
                '\n\nCurrent user:\n\n{messages}\n'
                '\nCurrent time: {time}.'
            ),
            ("placeholder", "{messages}"),
        ]
    ).partial(time=datetime.now())


# Initialize memory
conversation_memory = ConversationBufferMemory()

# Initialize Azure LLM
llm = AzureChatOpenAI(
    azure_deployment=os.environ.get('AZURE_OPENAI_DEPLOYMENT_NAME'),
    api_version=os.environ.get('AZURE_OPENAI_API_VERSION'),
    name="llm"
)

# Load schema model
model_sql_content = load_db_schema("./db-init/01_model.sql")

# Create tools
tools = create_tools()
rendered_tools = render_text_description(tools).replace('\n', ' ').replace('\r', '')

# Create prompt template
primary_assistant_prompt = create_prompt_template(rendered_tools, model_sql_content)

# Create the final runnable agent
part_1_assistant_runnable = primary_assistant_prompt | llm.bind_tools(tools)
