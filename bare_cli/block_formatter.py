from colorama import Style
from .block import Block


class BlockFormatter:
    """Formats Blocks alongside main content with consistent padding.

    A typical BareCLI line is composed of a Block in a left 'sidebar' and main content on the right.
    """

    def __init__(self, *, sidebar_width: int, choice_width: int):
        self._sidebar_width = sidebar_width
        self._choice_width = choice_width

    def format_sidebar(self, block: Block, main_content: str) -> str:
        return self._format_block(block, main_content, ".", "<", self._sidebar_width)

    def format_choice(self, block: Block, main_content: str) -> str:
        return self._format_block(block, main_content, "", ">", self._choice_width)

    def _format_block(
        self, block: Block, main_content: str, fill: str, align: str, width: int
    ) -> str:
        """Format a token string by formatting the untokenized first and then replacing."""

        format_spec = f"{fill}{align}{width}"
        formatted = f"{block.raw:{format_spec}} {Style.RESET_ALL + main_content}"
        return formatted.replace(block.raw, block.coloized, 1)
