import unittest
from datetime import datetime
from courier_active_time_calc.active_time_calculator import DeliveryService

class DeliveryServiceTest(unittest.TestCase):
    
    def setUp(self):
        self._deliveryService = DeliveryService()
        pickupTime = datetime(2020, 9, 12, 11, 34, 00).timestamp()
        self._deliveryService.add_delivery(1, pickupTime, "pickup")
        pickupTime = datetime(2020, 9, 12, 11, 40, 00).timestamp()
        self._deliveryService.add_delivery(2, pickupTime, "pickup")
        dropoffTime = datetime(2020, 9, 12, 11, 45,00).timestamp()
        self._deliveryService.add_delivery(2, dropoffTime, "dropoff")
        dropoffTime = datetime(2020, 9, 12, 11, 50,00).timestamp()
        self._deliveryService.add_delivery(1, dropoffTime, "dropoff")
    
    def test_active_time_between_pickup_and_dropoff(self):
        
        activeTime = self._deliveryService.active_time()
        self.assertEqual(960, activeTime)