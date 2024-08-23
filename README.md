# Chainlit Langgraph integration : a Music store assistant 

## Summary

langgraph 
langchain tools
llm
sqlite chinook db
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
Kerroumi Samir samir.kerr@gmail.com