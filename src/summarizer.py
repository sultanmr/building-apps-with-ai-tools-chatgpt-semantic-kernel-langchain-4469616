import os
import openai
import semantic_kernel as sk
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion

api_key, _ = sk.openai_settings_from_dot_env()
kernel = sk.Kernel()
kernel.add_text_completion_service(
    "dv",
    OpenAIChatCompletion("gpt-4", api_key=api_key)
)
prompt = kernel.create_semantic_function(
"""
print hello world
""")
print (prompt())
