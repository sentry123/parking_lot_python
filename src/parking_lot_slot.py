"""
    Creates and maintains slot objects
"""

from vehicle import Vehicle


class ParkingLotSlot:

    parking_lot_vacancy = {
        'Car_Slot' : 0,
        'Bike_Slot' : 0,
        'Truck_Slot' : 0
    }

    parking_lot_vehicles = {}

    def __init__(self, car_slot=3, bike_slot=3, truck_slot=3):
        self.parking_lot_vacancy['Car_Slot'] = car_slot
        self.parking_lot_vacancy['Bike_Slot'] = bike_slot
        self.parking_lot_vacancy['Truck_Slot'] = truck_slot

    def park_a_vehicle(self, vehicle:Vehicle):
        if Vehicle.validate_type(vehicle.vehicle_type):
            self.parking_lot_vehicles[vehicle.registration_number] = vehicle
            print(f"Vehicle : {vehicle.registration_number} Parked Successfully ")
        else:
            print("Vehicle type not compatible for this parking structure")

    def unpark_a_vehicle(self, registration_number: str):
        if registration_number in self.parking_lot_vehicles:
            removed_vehicle = self.parking_lot_vehicles.pop(registration_number)
            print(f" Vehicle {removed_vehicle} has been unparked from parking structure")
