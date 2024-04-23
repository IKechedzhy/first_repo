from colorama import Fore
from pathlib import Path

parent_folder_path = Path('.\module_four')

def explore_dir(path):
    try:
        for element in path.iterdir():

            if element.is_dir():
                print(f"{Fore.GREEN} + {element.name}")
                explore_dir(element)

            elif element.is_file():
                print(f"{Fore.BLUE} + {element.name}")

    except Exception as warning:
        print(f"{Fore.RED} + {warning}")
    return

explore_dir(parent_folder_path)


