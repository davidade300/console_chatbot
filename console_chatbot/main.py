from openai import OpenAI  # noqa f:401
import os
from rich.console import Console
from rich.markdown import Markdown
from prompts.py_instructor import py_instructor_prompt


openai = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

chat_log = [{"role": "system", "content": py_instructor_prompt}]

console = Console()

print("digite 'sair' para  sair")
while True:
    user_input = input("usuario: ")

    if user_input.lower() == "sair":
        break

    chat_log.append({"role": "user", "content": user_input})

    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        temperature=0.7,
        messages=chat_log,
    )

    bot_response = response.choices[0].message.content
    chat_log.append({"role": "assistant", "content": bot_response})
    console.print(Markdown(bot_response))
