from colorama import Fore, Back, Style
from .invalid_choice_error import InvalidChoiceError
from .status import Status
from .blocks.status_block import StatusBlock
from .blocks.open_status_block import OpenStatusBlock
from .blocks.choice_block import ChoiceBlock
from .blocks.misc_block import MiscBlock


class BareCLI:

    def __init__(self):
        self.accent_color = Fore.YELLOW

    def title(self, title: str):
        """Displays a title in accent color."""

        print(MiscBlock(title, self.accent_color, add_spacing=True))

    def info(self, message: str):
        print(self._get_bareline(Status.INFO, Fore.BLUE, message))

    def success(self, message: str):
        print(self._get_bareline(Status.SUCCESS, Fore.GREEN, message))

    def warning(self, message: str):
        print(self._get_bareline(Status.WARNING, Fore.YELLOW, message))

    def error(self, message: str):
        print(self._get_bareline(Status.ERROR, Fore.RED, message))

    def ask(self, prompt: str) -> str:
        print(self._get_bareline(Status.INPUT, self.accent_color, prompt))
        input_prompt = self._get_bareline(
            Status.INPUT, self.accent_color, ""
        )
        return input(input_prompt)

    def confirm(self, prompt: str, *, permissive_by_default: bool = True) -> bool:
        if permissive_by_default:
            default = "yes"
        else:
            default = "no"

        displayed_default = MiscBlock(default, self.accent_color)
        message = f"{prompt} (yes/no) {displayed_default}"
        print(self._get_bareline(Status.INPUT, self.accent_color, message))
        input_prompt = self._get_bareline(
            Status.INPUT, self.accent_color, ""
        )
        response = input(input_prompt)

        if response == "":
            return default == "yes"
        elif "y" in response.lower():
            return True
        else:
            return False

    def choices(
        self, prompt: str, choices: list[str], *, allow_chances: bool = True
    ) -> str:
        status_block = StatusBlock(Status.INPUT, self.accent_color)
        print(f"{status_block} {prompt}")

        valid_inputs = [i for i in range(0, len(choices))]
        for i, choice in enumerate(choices):
            print(self._get_choice_line(i, choice, status_block))

        prompt = f"Enter a number from {valid_inputs[0]} to {valid_inputs[-1]}."
        print(self._get_bareline(Status.INPUT, self.accent_color, prompt))
        input_prompt = self._get_bareline(
            Status.INPUT, self.accent_color, ""
        )
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

                print(self._get_bareline(
                    Status.INPUT, self.accent_color, prompt
                ))
                id_input = input(input_prompt).strip()
                int_input = self._try_parse_int(id_input)
                chances += 1

        return choices[int_input]

    def _get_choice_line(self, index: int, choice: str, parent_block: StatusBlock):
        option_colors = [
            Fore.RESET,
            Fore.YELLOW,
            Fore.RED,
            Fore.GREEN,
            Fore.BLUE,
            Fore.MAGENTA,
            Fore.CYAN,
        ]

        choice_block = ChoiceBlock(index, option_colors[index % len(option_colors)])
        choice_line = f"{choice_block} {choice}"
        open_block = OpenStatusBlock(parent_block)
        return f"{open_block} {choice_line}"

    def _get_bareline(
        self, status: Status, colorama_fore_color: str, message: str
    ) -> str:
        """A Bareline is composed of a StatusBlock in a sidebar and main content to the right."""

        status_block = StatusBlock(status, colorama_fore_color)
        return f"{status_block} {message}"

    def _try_parse_int(self, string_input: str) -> int | None:
        try:
            return int(string_input)
        except ValueError:
            return None
