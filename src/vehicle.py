"""
    Class for Vehicles
"""


class Vehicle:

    def __init__(self, vehicle_type, registration_number, color):
        self.vehicle_type = vehicle_type
        self.registration_number = registration_number
        self.color = color

    def validate_type(self):
        if self.vehicle_type not in ['Car', 'Bike', 'Truck']:
            return False
        else:
            return True
