import json
import datetime
import uuid

class StockPrice:
    ID = ""
    symbol = ""
    timestamp = 0
    price = 0

def index():
    with open('stockprice_tracker/stocktracker.json', 'r') as f:
        data = f.read()
        return json.loads(data)


def add(symbol: str, price: float):
    stockprice = StockPrice()
    stockprice.ID = str(uuid.uuid4())
    stockprice.symbol = symbol
    stockprice.price = price
    stockprice.timestamp = datetime.datetime.now().timestamp()
    datapoints = []
    with open('stockprice_tracker/stocktracker.json', 'r') as f:
        data = f.read()
        datapoints = json.loads(data)
        datapoints.append(json.dumps(stockprice.__dict__))
    with open('stockprice_tracker/stocktracker.json', 'w') as f:
        f.write(json.dumps(datapoints, indent=4))


def update(symbol: str, price: float):
    datapoints = []
    stockprices = []
    with open('stockprice_tracker/stocktracker.json', 'r') as f:
        data = f.read()
        datapoints = json.loads(data)
    for datapoint in datapoints:           
        stockprices.append(json.loads(datapoint, object_hook=dict_to_stockprice))
    for sp in stockprices:
        if sp.symbol == symbol:
            sp.price = price
            sp.timestamp = datetime.datetime.now().timestamp()
    new_datapoints = []
    for sp in stockprices:
        new_datapoints.append(json.dumps(sp.__dict__))
    with open('stockprice_tracker/stocktracker.json', 'w') as f:
        f.write(json.dumps(new_datapoints, indent=4))
            
def remove(symbol: str):
    datapoints = []
    stockprices = []
    with open('stockprice_tracker/stocktracker.json', 'r') as f:
        data = f.read()
        datapoints = json.loads(data)
    for i, datapoint in enumerate(datapoints):
        if symbol in datapoint:
            datapoints.pop(i)
            break
    with open('stockprice_tracker/stocktracker.json', 'w') as f:
        f.write(json.dumps(datapoints, indent=4))


def dict_to_stockprice(datapoint):
    stockprice = StockPrice()
    stockprice.ID = datapoint["ID"]
    stockprice.symbol = datapoint["symbol"]
    stockprice.price = datapoint["price"]
    stockprice.timestamp = datapoint["timestamp"]
    return stockprice