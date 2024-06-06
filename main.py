import os

from api import generate
from commands import commands
from setup import setup


def main():
    model, task = setup()
    while True:
        prompt = input("\n\nPrompt: ")
        if len(prompt) > 0:
            if prompt[0] == "/" and prompt[1:] in commands:
                commands[prompt[1:]]()
            else:
                generate(model, prompt=f"{task}{prompt}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        os.system("clear")
