import os
from llm_models import list_available_models


def setup():
    models = list_available_models()
    os.system("clear")
    for key, value in models.items():
        print(f"{key} - {value}")
    model = int(input("Option: "))
    os.system("clear")
    print("Task:\n1 - Coding\n2 - General\n")
    task = int(input("Task: "))
    os.system("clear")
    return (
        models[model],
        {
            1: "Do not write any natural language text in your response, only code. ",
            2: "",
        }[task],
    )
