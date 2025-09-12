import unittest
from bare_cli.table_planner import TablePlanner

class TestTables(unittest.TestCase):

    def test_default_table_planning(self):
        headers = ("User", "Type", "Background", "Email")
        rows = [
            ("Jamison", "Admin", "Dev", "xxx@yahoo.com"),
            ("Steve", "User", "N/A", "y@be.co"),
            ("Gregorovich", "Mod", "N/A", "x@be.co"),
        ]
        planner = TablePlanner(headers, rows)
        plan = planner.get_plan()

        self.assertEqual(len(plan), 4)
        self.assertEqual(plan[0], 14)
        self.assertEqual(plan[1], 8)
        self.assertEqual(plan[2], 13)
        self.assertEqual(plan[3], 16)


    def test_comfortable_table_planning(self):
        headers = ("User", "Type", "Background", "Email")
        rows = [
            ("Jamison", "Admin", "Dev", "xxx@yahoo.com"),
            ("Steve", "User", "N/A", "y@be.co"),
            ("Gregorovich", "Mod", "N/A", "x@be.co"),
        ]
        planner = TablePlanner(headers, rows)
        plan = planner.get_plan(comfortable_layout=True)

        self.assertEqual(len(plan), 4)
        self.assertEqual(plan[0], 21)
        self.assertEqual(plan[1], 15)
        self.assertEqual(plan[2], 20)
        self.assertEqual(plan[3], 24)
