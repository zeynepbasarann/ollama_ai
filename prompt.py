# -*- coding: utf-8 -*-
#prompt.py


def prompt(user_prompt):
    return (
        "You are a professional Python developer assistant.\n\n"
        "ONLY respond with Python code based on the following user request. "
        "Do NOT add any explanation, greeting, or extra text. "
        "Respond ONLY with the Python code inside triple backticks.\n\n"
        "User Request: \"{}\"\n\n"
        "Format your response strictly as:\n"
        "```python\n"
        "<your code here>\n"
        "```"
    ).format(user_prompt)
