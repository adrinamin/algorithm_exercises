import unittest
import json
from stockprice_tracker.stock_tracker import index
from stockprice_tracker.stock_tracker import add
from stockprice_tracker.stock_tracker import update
from stockprice_tracker.stock_tracker import remove
from stockprice_tracker.stock_tracker import dict_to_stockprice
    

class StockPriceTrackerTest(unittest.TestCase):

    def setUp(self):
        datapoints = []
        with open('stockprice_tracker/stocktracker.json', 'w') as f:
            f.write(json.dumps(datapoints, indent=2))
            
    
    @classmethod
    def tearDownClass(cls):
        datapoints = []
        with open('stockprice_tracker/stocktracker.json', 'w') as f:
            f.write(json.dumps(datapoints, indent=2))


    def test_index_returns_current_records(self):
        response = index()
        self.assertEqual(len(response),0)

    
    def test_add_stockprice_adds_new_stockprice_object(self):
        add("MSFT",200)
        datapoints = []
        with open('stockprice_tracker/stocktracker.json', 'r') as f:
            data = f.read()
            datapoints = json.loads(data)
        self.assertEqual(len(datapoints), 1)


    def test_update_stockprice_updates_price_and_timestamp(self):
        datapoints = []
        stockprices = []
        add("TSLA", 1000)
        update("TSLA", 2000)
        with open('stockprice_tracker/stocktracker.json', 'r') as f:
            data = f.read()
            datapoints = json.loads(data)
        for datapoint in datapoints:           
            stockprices.append(json.loads(datapoint, object_hook=dict_to_stockprice))
        for sp in stockprices:
            self.assertEqual(sp.price, 2000)
            
    def test_remove_stockprice_deletes_stockprice_entry(self):
        add("TSLA", 1000)
        remove("TSLA")
        datapoints = []
        with open('stockprice_tracker/stocktracker.json', 'r') as f:
            data = f.read()
            datapoints = json.loads(data)
        self.assertEqual(len(datapoints), 0)
    
# for running this test file separately
if __name__ == '__main__':
    unittest.main()