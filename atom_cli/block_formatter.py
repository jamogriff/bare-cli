from colorama import Style
from .block import Block


class BlockFormatter:
    """Formats Blocks alongside main content with consistent padding.

    A typical BareCLI line is composed of a Block in a left 'sidebar' and main content on the right.
    """

    SIDEBAR_WIDTH = 12
    CHOICE_WIDTH = 8

    def format_sidebar(self, block: Block, main_content: str) -> str:
        return self._format_block(block, main_content, ".", "<", self.SIDEBAR_WIDTH)

    def format_choice(self, block: Block, main_content: str) -> str:
        return self._format_block(block, main_content, "", ">", self.CHOICE_WIDTH)

    def _format_block(
        self, block: Block, main_content: str, fill: str, align: str, width: int
    ) -> str:
        """Format a token string by formatting the untokenized first and then replacing."""

        format_spec = f"{fill}{align}{width}"
        formatted = f"{block.raw:{format_spec}} {Style.RESET_ALL + main_content}"
        return formatted.replace(block.raw, block.coloized, 1)
