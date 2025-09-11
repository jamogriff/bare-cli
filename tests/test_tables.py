import unittest
from bare_cli.table_planner import TablePlanner

class TestTables(unittest.TestCase):

    def test_table_planning(self):
        headers = ("User", "Type", "Background", "Email")
        rows = [
            ("Jamison", "Admin", "Dev", "xxx@yahoo.com"),
            ("Steve", "User", "N/A", "y@be.co"),
            ("Gregorovich", "Mod", "N/A", "x@be.co"),
        ]
        planner = TablePlanner(headers, rows)
        plan = planner.get_plan()

        self.assertEqual(len(plan), 4)
        self.assertEqual(plan[0], 11)
        self.assertEqual(plan[1], 5)
        self.assertEqual(plan[2], 10)
        self.assertEqual(plan[3], 13)

