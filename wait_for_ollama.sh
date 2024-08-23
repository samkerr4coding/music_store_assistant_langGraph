#!/bin/bash

# Start Ollama in the background.
ollama serve &
# Record Process ID.
pid=$!

# Pause for Ollama to start.
sleep 5

echo "🔴 Retrieving model : $LOCAL_LLM_OLLAMA_MODEL"

ollama pull $LOCAL_LLM_OLLAMA_MODEL
ollama run $LOCAL_LLM_OLLAMA_MODEL
# ollama run TinyLlama:instruct
echo "🟢 Done!"

# Wait for Ollama process to finish.
wait $pid
