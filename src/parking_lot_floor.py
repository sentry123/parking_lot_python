"""
    Adds a new floor to the parking lot
"""

from parking_lot_slot import ParkingLotSlot


class ParkingLotFloor:

    def __init__(self, car_slot=3, bike_slot=10, truck_slot=1):

        self.parking_lot_slot = ParkingLotSlot(car_slot, bike_slot, truck_slot)

    """
    parking_lot_slot = {
                            "Car": int,
                            "Bike": int,
                            "Truck": int
                        }
    """
