"""
    Driver function for the project
"""

"""
The functions that the parking lot system can do:
    - Create the parking lot. //
    - Add floors to the parking lot. //
    - Add a parking lot slot to any of the floors.
    - Given a vehicle, it finds the first available slot, books it, creates a ticket, parks the vehicle, and finally returns the ticket.
    - Unparks a vehicle given the ticket id.
    - Displays the number of free slots per floor for a specific vehicle type.
    - Displays all the free slots per floor for a specific vehicle type.
    - Displays all the occupied slots per floor for a specific vehicle type.
"""

from parking_lot import ParkingLot


if __name__ == '__main__':

    floors = int(input("Enter the number of floors: "))
    parkingLot = ParkingLot(floors)



