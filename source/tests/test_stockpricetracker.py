import unittest
import json
from stockprice_tracker.stock_tracker import index
from stockprice_tracker.stock_tracker import add
    

class StockPriceTrackerTest(unittest.TestCase):

    def setUp(self):
        datapoints = []
        with open('stockprice_tracker/stocktracker.json', 'w') as f:
            f.write(json.dumps(datapoints, indent=2))


    def test_index_returns_current_records(self):
        response = index()
        self.assertEqual(len(response),0)

    def test_add_stockprice_adds_new_stockprice_object(self):
        add(100)
        datapoints = []
        with open('stockprice_tracker/stocktracker.json', 'r') as f:
            data = f.read()
            datapoints = json.loads(data)
        self.assertEqual(len(datapoints), 1)

# for running this test file separately
if __name__ == '__main__':
    unittest.main()