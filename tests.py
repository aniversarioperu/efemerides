import unittest

from efemerides_bot.validate import validate_data


class TestJsonData(unittest.TestCase):
    def setUp(self):
        pass

    def test_and_validate_json_data(self):
        expected = 'Valid'
        result = validate_data()
        self.assertEqual(expected, result)
