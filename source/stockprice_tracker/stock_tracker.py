import json
import datetime

class StockPrice:
    timestamp = 0
    price = 0

def index():
    with open('stockprice_tracker/stocktracker.json', 'r') as f:
        data = f.read()
        return json.loads(data)


def add(price: float):
    stockprice = StockPrice()
    stockprice.price = price
    stockprice.timestamp = datetime.datetime.now().timestamp()
    datapoints = []
    with open('stockprice_tracker/stocktracker.json', 'r') as f:
        data = f.read()
        datapoints = json.loads(data)
        datapoints.append(json.dumps(stockprice.__dict__))
    with open('stockprice_tracker/stocktracker.json', 'w') as f:
        f.write(json.dumps(datapoints, indent=2))


def update():
    record = json.loads(request.data)