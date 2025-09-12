import math

class TablePlanner:

    COMFORTABLE_WIDTH = 80

    def __init__(self, headers: tuple[str, ...], rows: list[list[str]]):
        self.headers = headers
        self.rows = rows

    def get_plan(self, *, comfortable_layout: bool = False) -> list[int]:
        """Return a list of the largest string length per column."""

        column_lengths = [len(n) for n in self.headers]

        for row in self.rows:
            for i, column in enumerate(row):
                if len(column) > column_lengths[i]:
                    column_lengths[i] = len(column)

        # Adding 3 to each length to accomodate for left cell
        # character and two spaces surrounding value
        minimum_column_lengths: list[int] = [n + 3 for n in column_lengths]

        if not comfortable_layout or sum(minimum_column_lengths) >= self.COMFORTABLE_WIDTH:
            return minimum_column_lengths
        else:
            space_remaining = self.COMFORTABLE_WIDTH - sum(minimum_column_lengths)
            remainder = space_remaining % len(minimum_column_lengths)
            # Throw any remainder in last column
            minimum_column_lengths[len(minimum_column_lengths) - 1] += remainder
            evenly_distributed_space = math.floor(space_remaining / len(minimum_column_lengths))

            return [n + evenly_distributed_space for n in minimum_column_lengths]


