from colorama import Fore, Back, Style
from .invalid_choice_error import InvalidChoiceError

class AtomCLI:

    def title(self, title: str):
        """Displays a yellow title with a newline for breathing room."""

        print(Fore.YELLOW + title)
        print("=" * len(title))
        print(Fore.RESET)

    def section(self, header: str):
        """Displays a section header with a newline for breathing room."""

        print(header)
        print("-" * len(header))
        print()

    def info(self, message: str):
        self._display_right_padded_color_label("INFO", Fore.BLUE, message)

    def success(self, message: str):
        self._display_right_padded_color_label("OK", Fore.GREEN, message)

    def warning(self, message: str):
        self._display_right_padded_color_label("WARNING", Fore.YELLOW, message)

    def error(self, message: str):
        self._display_right_padded_color_label("ERROR", Fore.RED, message)

    def ask(self, prompt: str) -> str:
        print(prompt)
        return input("> ")

    def confirm(self, prompt: str, *, permissive_by_default: bool = True) -> bool:
        if permissive_by_default:
            default = "yes"
        else:
            default = "no"

        displayed_default = self._get_atom_bracket_value(Fore.YELLOW, default)
        print(f"{prompt} (yes/no) {displayed_default + Style.RESET_ALL}:")
        response = input("> ")

        if response == "":
            return default == "yes"
        elif "y" in response.lower():
            return True
        else:
            return False

    def choices(self, prompt: str, choices: list[str], *, allow_chances: bool = True) -> str:
        valid_inputs = [i for i in range(0, len(choices))]
        print(prompt)
        for i, choice in enumerate(choices):
            self._display_left_padded_color_choice(i, choice)

        prompt = f"Enter a number from {valid_inputs[0]} to {valid_inputs[-1]}."
        print(prompt)
        id_input = input("> ")
        int_input = self._try_parse_int(id_input)

        # If chances not allowed, raise exception immediately
        if not allow_chances and int_input not in valid_inputs:
            self.error("Please try again later.")
            raise InvalidChoiceError()

        # If chances allowed, give user multiple chances to make a selection
        if allow_chances and int_input not in valid_inputs:
            chances = 1
            chance_limit = 3
            while int_input not in valid_inputs:
                if chances == chance_limit - 1:
                    self.warning("Please stop faffing about.")
                elif chances >= chance_limit:
                    self.error("Please try again later.")
                    raise InvalidChoiceError()

                print(prompt)
                id_input = input("> ").strip()
                int_input = self._try_parse_int(id_input)
                chances += 1

        return choices[int_input]

    def _display_right_padded_color_label(self, label: str, colorama_fore_color: str, message: str):
        """Display a right-padded colored label and a message.

        ANSI color codes will break padding because Python counts their characters as strings.
        So we format the intended label first and then replace it with the colored version.
        """

        colored_label = self._get_atom_bracket_value(colorama_fore_color, label)
        formatted = f"{label:.<8} {Style.RESET_ALL + message}"
        colored_output = formatted.replace(label, colored_label, 1)
        print(colored_output)

    def _display_left_padded_color_choice(self, index: int, choice: str):
        option_colors = [
            Fore.YELLOW,
            Fore.RED,
            Fore.GREEN,
            Fore.BLUE,
            Fore.MAGENTA,
            Fore.CYAN
        ]

        str_index = str(index)
        colored_option = self._get_atom_bracket_value(option_colors[index % len(option_colors)], str_index)
        formatted = f"{str_index:>3} {Style.RESET_ALL + choice}"
        colored_output = formatted.replace(str_index, colored_option, 1)
        print(colored_output)

    def _get_atom_bracket_value(self, colorama_color: str, value: str) -> str:
        return Style.DIM + "[" + Style.RESET_ALL + colorama_color + value + Fore.RESET + Style.DIM + "]"

    def _try_parse_int(self, string_input: str) -> int | None:
        try:
            return int(string_input)
        except ValueError:
            return None


