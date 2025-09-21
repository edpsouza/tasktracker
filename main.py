import os
import json
from rich.console import Console
from rich.markdown import Markdown
from functions import add_task


def main():
    print_markdown_file("markdown/intro.md")
    startup_check()
    command_check(input("\nPlease input your command: "))



def startup_check():
    # Check if tasks.json exists and is readable
    if os.path.isfile("tasks.json") and os.access("tasks.json", os.R_OK):
        print("\nFile exists and is readable")
    else:
        print("\nEither file is missing or not readable. Creating file...")
        # Create an empty tasks.json file
        with open("tasks.json", "w") as db_file:
            json.dump([], db_file)

# Takes the path to a markdown file as an argument
def print_markdown_file(path):
    # Create console object to be used to print markdown
    console = Console()
    # Read the markdown file
    with open(path, "r") as md_file:
        # Read the content of the markdown file and assign it
        markdown_content = md_file.read()
    # Print the markdown content to the console
    console.print(Markdown(markdown_content))


def command_check(command):
    if command == "add":
        add_task()
    else:
        pass

main()
