import os
import shutil
import tempfile
from rich.console import Console
from rich.panel import Panel
from rich import box
from rich.prompt import Prompt
from rich.text import Text
from rich.style import Style
from datetime import datetime

# MADE BY MOSES

console = Console()

EXCLUDED_PATHS = [
    os.path.expandvars(r'%SYSTEMROOT%'),
    os.path.expandvars(r'%PROGRAMFILES%'),
    os.path.expandvars(r'%USERPROFILE%\\AppData\\Local\\Microsoft\\Windows\\Explorer'),
    os.path.expandvars(r'%APPDATA%\\Mozilla\\Firefox\\Profiles'),
    os.path.expandvars(r'%LOCALAPPDATA%\\Google\\Chrome\\User Data\\Default\\Cookies'),
    os.path.expandvars(r'%LOCALAPPDATA%\\Microsoft\\Edge\\User Data\\Default\\Cookies'),
]

def is_important(path):
    for excluded_path in EXCLUDED_PATHS:
        if os.path.commonpath([path, excluded_path]) == excluded_path:
            return True
    return False

def clean_temp_files():
    temp_dir = tempfile.gettempdir()
    not_cleaned_files = []
    deleted_files = []
    try:
        for item in os.listdir(temp_dir):
            item_path = os.path.join(temp_dir, item)
            if os.path.isfile(item_path) and not is_important(item_path):
                try:
                    os.remove(item_path)
                    deleted_files.append(item_path)
                    console.print(f"Deleted file: {item_path}", style="bold green")
                except PermissionError:
                    not_cleaned_files.append(item_path)
            elif os.path.isdir(item_path) and not is_important(item_path):
                try:
                    shutil.rmtree(item_path)
                    deleted_files.append(item_path)
                    console.print(f"Deleted directory: {item_path}", style="bold green")
                except PermissionError:
                    not_cleaned_files.append(item_path)

        if not_cleaned_files:
            not_cleaned_message = f"[bold red]Some files could not be cleaned because they are in use:[/bold red]"
            for file in not_cleaned_files:
                console.print(f"{file}", style="bold red")
            return f"[INFO] Temp files cleaned successfully, but the following could not be cleaned."
        return "[INFO] Temp files cleaned successfully!"
    except Exception as e:
        console.print(f"[ERROR] Error cleaning temp files: {e}", style="bold red")
        return f"[ERROR] Error cleaning temp files: {e}"

def apply_gradient_ascii(ascii_art, start_color, end_color):
    start_r, start_g, start_b = start_color
    end_r, end_g, end_b = end_color
    gradient = []
    
    for i, char in enumerate(ascii_art):
        r = int(start_r + (end_r - start_r) * (i / len(ascii_art)))
        g = int(start_g + (end_g - start_g) * (i / len(ascii_art)))
        b = int(start_b + (end_b - start_b) * (i / len(ascii_art)))
        
        gradient.append(f"[rgb({r},{g},{b})]{char}[/rgb({r},{g},{b})]")
        
    return ''.join(gradient)

ascii_art = """
███████╗██╗   ██╗███████╗████████╗███████╗███╗   ███╗     ██████╗██╗     ███████╗ █████╗ ███╗   ██╗███████╗██████╗ 
██╔════╝╚██╗ ██╔╝██╔════╝╚══██╔══╝██╔════╝████╗ ████║    ██╔════╝██║     ██╔════╝██╔══██╗████╗  ██║██╔════╝██╔══██╗
███████╗ ╚████╔╝ ███████╗   ██║   █████╗  ██╔████╔██║    ██║     ██║     █████╗  ███████║██╔██╗ ██║█████╗  ██████╔╝
╚════██║  ╚██╔╝  ╚════██║   ██║   ██╔══╝  ██║╚██╔╝██║    ██║     ██║     ██╔══╝  ██╔══██║██║╚██╗██║██╔══╝  ██╔══██╗
███████║   ██║   ███████║   ██║   ███████╗██║ ╚═╝ ██║    ╚██████╗███████╗███████╗██║  ██║██║ ╚████║███████╗██║  ██║
╚══════╝   ╚═╝   ╚══════╝   ╚═╝   ╚══════╝╚═╝     ╚═╝     ╚═════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝
"""

start_color = (255, 0, 0)
end_color = (128, 0, 128)

def gradient_text(text, color1, color2):
    return Text.from_markup(f"[{color1}]{text}[/{color1}]")

def main():
    console.clear()

    gradient_ascii = apply_gradient_ascii(ascii_art, start_color, end_color)

    console.print(gradient_ascii)

    options = {
        "1": "Clean Temp Files",
        "2": "Exit"
    }

    while True:
        console.print("\n[bold blue]Choose an option from the menu:[/bold blue]")
        for key, value in options.items():
            console.print(f"{key}. {value}")

        choice = Prompt.ask("Enter your choice", choices=["1", "2"], default="1")

        if choice == "1":
            message = clean_temp_files()
            console.print(message, style="bold green")
        elif choice == "2":
            console.print("\nExiting.", style="bold yellow")
            break

if __name__ == "__main__":
    main()
