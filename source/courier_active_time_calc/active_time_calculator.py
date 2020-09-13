"""[summary]
"""
import sys
import datetime

class DeliveryService():
    """Handles the delivery status and active time
    """
    
    def __init__(self):
        self._deliveries = []

    def add_delivery(self, id: int, timestamp: float, status: str):
        """adds a delivery to the current list of delivery states

        Args:
            id (int): the delivery id
            timestamp (float): the timestamp of the current delivery entry
            status (str): the status of the current delivery entry
        """
        delivery = (id, timestamp, status)
        self._deliveries.append(delivery)


    def active_time(self):
        """Returns the active time in seconds between pickup and dropoff

        Returns:
            int: the active time in seconds
        """
        n = []
        d = []
        isPickedup = False
        pickuptime = 0
        dropofftime = 0
        deliveryId = 0
        activetime = 0
        for i, delivery in enumerate(self._deliveries):
            if delivery[2] == "pickup" and isPickedup == False:
                isPickedup = True
                pickuptime = delivery[1]
                deliveryId = delivery[0]
                continue
                
            if delivery[2] == "dropoff" and delivery[0] == deliveryId:
                isPickedup = False
                dropofftime = delivery[1]
                activetime = activetime + (dropofftime - pickuptime)
                continue
        
        return activetime    

def main(id: int, timestamp: float, status: str):
    deliveryService = DeliveryService()
    deliveryService.add_delivery(id, timestamp, status)
    activeTime = deliveryService.active_time()
    

if __name__ == '__main__':
    main()