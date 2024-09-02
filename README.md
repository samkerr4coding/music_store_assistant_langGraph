# Chainlit Langgraph integration : a Music store assistant 

## Summary


Welcome to myMusicStore, this is a demo of the usage of tool calling with :

langgraph 
langchain tools
llm
postgresql
chainlit

## Installation

### Python requirements

In your Python 3.12 virtual env, install all deps by running:

```
pip install --upgrade pip
pip install poetry
poetry install
```

### LLM models used

This demo uses remote llm with provided examples for open ai azure instance chat gpt and gemini.

See the .env.example to provide required API KEYS 

For local LLM, at this point no model was able to use propperly langchain tools

### db

https://github.com/lerocha/chinook-database/blob/master/ChinookDatabase/DataSources/Chinook_Sqlite.sqlite

```bash
python app.py
```

## Usage

```bash
chainlit run app.py --port 8000
```

## Author


invoice_line_tools.py
album_tools.py
artist_tools.py
country_tools.py
employee_tools.py
invoice_tools.py
media_type_tools.py
playlist_tools.py
track_tools.py
policy.py
policy.md
genre_tools.py


