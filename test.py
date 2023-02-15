import unittest
from unittest.mock import patch
import main


class Test(unittest.TestCase):
    def test(self):
        data = [{"username": "alvin"}]

        with patch('main.Main.get') as mock_get:
            mock_get.return_value.status_code = 200
            mock_get.return_value.json.return_value = data

            obj = main.Main()
            response = obj.get()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), data)
    
if __name__ == "__main__":
    unittest.main()