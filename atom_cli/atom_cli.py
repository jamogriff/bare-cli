from colorama import Fore, Back, Style
from .invalid_choice_error import InvalidChoiceError
from .styled_string_factory import StyledStringFactory
from .styled_string_formatter import StyledStringFormatter

class AtomCLI:

    def __init__(self):
        self.accent_color = Fore.YELLOW
        self.styled_string_factory = StyledStringFactory()
        self.styled_string_formatter = StyledStringFormatter()

    def title(self, title: str):
        """Displays a title in accent color."""

        print(self.styled_string_factory.make_bracket(self.accent_color, title) + Style.RESET_ALL)

    def info(self, message: str):
        self._display_right_padded_color_label("INFO", Fore.BLUE, message)

    def success(self, message: str):
        self._display_right_padded_color_label("OK", Fore.GREEN, message)

    def warning(self, message: str):
        self._display_right_padded_color_label("WARNING", Fore.YELLOW, message)

    def error(self, message: str):
        self._display_right_padded_color_label("ERROR", Fore.RED, message)

    def ask(self, prompt: str) -> str:
        self._display_right_padded_color_label("INPUT", self.accent_color, prompt)
        input_prompt = self._get_signature_bracket_format("INPUT", self.accent_color, "")
        return input(input_prompt)

    def confirm(self, prompt: str, *, permissive_by_default: bool = True) -> bool:
        if permissive_by_default:
            default = "yes"
        else:
            default = "no"

        displayed_default = self.styled_string_factory.make_bracket(self.accent_color, default)
        message = f"{prompt} (yes/no) {displayed_default + Style.RESET_ALL}"
        self._display_right_padded_color_label("INPUT", self.accent_color, message)
        input_prompt = self._get_signature_bracket_format("INPUT", self.accent_color, "")
        response = input(input_prompt)

        if response == "":
            return default == "yes"
        elif "y" in response.lower():
            return True
        else:
            return False

    def choices(self, prompt: str, choices: list[str], *, allow_chances: bool = True) -> str:
        self._display_right_padded_color_label("INPUT", self.accent_color, prompt)

        valid_inputs = [i for i in range(0, len(choices))]
        for i, choice in enumerate(choices):
            self._display_left_padded_color_choice(i, choice)

        prompt = f"Enter a number from {valid_inputs[0]} to {valid_inputs[-1]}."
        self._display_right_padded_color_label("INPUT", self.accent_color, prompt)
        input_prompt = self._get_signature_bracket_format("INPUT", self.accent_color, "")
        id_input = input(input_prompt).strip()
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

                self._display_right_padded_color_label("INPUT", self.accent_color, prompt)
                id_input = input(input_prompt).strip()
                int_input = self._try_parse_int(id_input)
                chances += 1

        return choices[int_input]

    def _display_right_padded_color_label(self, label: str, colorama_fore_color: str, message: str):
        """Display a right-padded colored label and a message.

        ANSI color codes will break padding because Python counts their characters as strings.
        So we format the intended label first and then replace it with the colored version.
        """

        formatted = self._get_signature_bracket_format(label, colorama_fore_color, message)
        print(formatted)

    def _display_left_padded_color_choice(self, index: int, choice: str):
        option_colors = [
            Fore.RESET,
            Fore.YELLOW,
            Fore.RED,
            Fore.GREEN,
            Fore.BLUE,
            Fore.MAGENTA,
            Fore.CYAN
        ]

        str_index = str(index)
        styled_string = self.styled_string_factory.make_bracket(option_colors[index % len(option_colors)], str_index)
        formatted_option = self.styled_string_formatter.add_left_padding(styled_string, choice)
        open_bracket = self.styled_string_factory.make_open_bracket("INPUT")
        formatted_block_line = self.styled_string_formatter.add_right_padding(open_bracket, formatted_option)
        print(formatted_block_line)

    def _get_signature_bracket_format(self, label: str, colorama_fore_color: str, message: str) -> str:
        styled_string = self.styled_string_factory.make_bracket(colorama_fore_color, label)
        return self.styled_string_formatter.add_right_padding(styled_string, message)

    def _try_parse_int(self, string_input: str) -> int | None:
        try:
            return int(string_input)
        except ValueError:
            return None


