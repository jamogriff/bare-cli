class TablePlanner:

    def __init__(self, headers: tuple[str, ...], rows: list[list[str]]):
        self.headers = headers
        self.rows = rows

    def get_plan(self) -> list[int]:
        """Return a list of the largest string length per column."""

        column_lengths = [len(n) for n in self.headers]

        for row in self.rows:
            for i, column in enumerate(row):
                if len(column) > column_lengths[i]:
                    column_lengths[i] = len(column)

        # Adding 3 to each length to accomodate for left cell
        # character and two spaces surrounding value
        return [n + 3 for n in column_lengths]


