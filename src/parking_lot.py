"""
  Adds a new parking lot
"""

from parking_lot_floor import ParkingLotFloor


class ParkingLot:

    def __init__(self, floors: int):
        self.floors = []
        for _ in range(floors):
            self.floors.append(ParkingLotFloor())

    def view_parking_lot_info(self):
        count = 0
        for floor in self.floors:
            print(f"Floor {count} info => Car_Slots= {floor.parking_lot_slot.car_slot}, "
                  f"Bike_Slots= {floor.parking_lot_slot.bike_slot}, Truck_Slots= {floor.parking_lot_slot.truck_slot}")
            count += 1
