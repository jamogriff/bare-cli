import sys
from colorama import Fore, Back, Style

class Bare:

def title(self, title: str):
    """Displays a yellow title with a newline for breathing room."""

    print(Fore.YELLOW + title)
    print("=" * len(title))
    print(Fore.RESET)

def section(self, header: str):
    """Displays a section header with a newline for breathing room."""

    print("-" * len(header))
    print(header)
    print("-" * len(header))
    print()

def info(self, message: str):
    self.display_right_padded_color_label("INFO", Fore.BLUE, message)

def success(self, message: str):
    self._display_right_padded_color_label("OK", Fore.GREEN, message)

def warning(self, message: str):
    self._display_right_padded_color_label("WARNING", Fore.YELLOW, message)

def error(self, message: str):
    self._display_right_padded_color_label("ERROR", Fore.RED, message)

def ask(self, prompt: str) -> str:
    print(prompt)
    return input("> ")

def confirm(self, prompt: str, *, permissive_default: bool = True) -> bool:
    if permissive_default:
        default = "yes"
    else:
        default = "no"

    print(f"{prompt} (yes/no) [ {Fore.YELLOW default Fore.RESET} ]:")
    response = input("> ")

    if "y" in response.lower():
        return True
    else:
        return False

def choices(self, prompt: str, choices: list[str], *, allow_chances: bool = True) -> str:
    valid_inputs = [i for i in range(0, len(choices))]
    print(prompt)
    for i, choice in enumerate(choices):
        i_option = "[ " + i + " ]"
        print(f"{i_option:>3} {choice}")

    prompt = f"Enter a number from {valid_inputs[0]} to {valid_inputs[-1]}."
    print(prompt)
    id_input = input("> ")

    # If chances not allowed, exit immediately
    if not allow_chances and int(id_input) not in valid_inputs:
        self.error("Please try again later.")
        sys.exit(1)

    # If chances allowed, give user multiple chances to make a selection
    if loop and int(id_input) not in valid_inputs:
        chances = 1
        chance_limit = 3
        while int(id_input) not in valid_inputs:
            if chances == chance_limit - 1:
                self.warning("Please stop faffing about.")
            elif chances >= chance_limit:
                self.error("Please try again later.")
                sys.exit(1)

            print(prompt)
            id_input = input("> ")
            chances += 1

    return choices[int(id_input)]

def _display_right_padded_color_label(self, label: str, colorama_fore_color: str, message: str):
    """Display a right-padded colored label and a message.

    ANSI color codes will break padding because Python counts their characters as strings.
    So we format the intended label first and then replace it with the colored version.
    """

    colored_label = "[ " + colorama_fore_color + label + Fore.RESET + " ] "
    formatted = f"{label:.<8} {message}"
    colored_output = formatted.replace(label, colored_label, 1)
    print(colored_output)

