"""
    Creates and maintains slot objects
"""

import uuid
from vehicle import Vehicle


def generate_ticket():
    return uuid.uuid4()


class ParkingLotSlot:

    parking_lot_vacancy = {
        'Car': 0,
        'Bike': 0,
        'Truck': 0
    }

    parking_lot_vehicles = {}

    def __init__(self, car_slot=3, bike_slot=3, truck_slot=3):
        self.parking_lot_vacancy['Car'] = car_slot
        self.parking_lot_vacancy['Bike'] = bike_slot
        self.parking_lot_vacancy['Truck'] = truck_slot

    def park_a_vehicle(self, vehicle: Vehicle):

        if Vehicle.validate_type(vehicle.vehicle_type) and self.parking_lot_vacancy[vehicle.vehicle_type] > 0:
            parking_ticket_id = generate_ticket()
            self.parking_lot_vehicles[parking_ticket_id] = vehicle
            self.parking_lot_vacancy[vehicle.vehicle_type] -= 1
            print(f"Vehicle : {vehicle.registration_number} Parked Successfully with ticket id : {parking_ticket_id}")
        else:
            print("No suitable vacancy")

    def unpark_a_vehicle(self, parking_ticket_id: str):
        if parking_ticket_id in self.parking_lot_vehicles:
            removed_vehicle = self.parking_lot_vehicles.pop(parking_ticket_id)
            self.parking_lot_vacancy[self.parking_lot_vehicles[parking_ticket_id]] += 1
            print(f" Vehicle {removed_vehicle} has been unparked from parking structure")
