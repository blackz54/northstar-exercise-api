import unittest
from dev.TableEventHandler import TableEventHandler


class TestTableEventHandler(unittest.TestCase):

    def test_getIdRuns(self):
        table = TableEventHandler()
        beg_result = table.GetIdRuns('Beginner')
        int_result = table.GetIdRuns('Intermediate')
        adv_result = table.GetIdRuns('Advanced')
        false_result = table.GetIdRuns('BadKey')
        self.assertEqual(len(beg_result), 15)
        self.assertEqual(len(int_result), 50)
        self.assertEqual(len(adv_result), 38)
        self.assertEqual(len(false_result), 0)


if __name__ == '__main__':
    unittest.main()
