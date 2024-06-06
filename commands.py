import os

from llm_models import list_available_models

commands = {
    "limpar": lambda: os.system("clear"),
    "sair": lambda: exit(0),
    "modelos": lambda: print(list_available_models()),
}
