class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.current_floor = bottom_floor
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor

    def go_to_floor(self, target_floor):
        if target_floor < self.bottom_floor or target_floor > self.top_floor:
            print("Invalid floor request. The target floor is outside the valid range.")
            return

        while self.current_floor != target_floor:
            if target_floor > self.current_floor:
                self.floor_up()
            elif target_floor < self.current_floor:
                self.floor_down()

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Elevator moving up. Current floor: {self.current_floor}")
        else:
            print("Already at the top floor.")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Elevator moving down. Current floor: {self.current_floor}")
        else:
            print("Already at the bottom floor.")

class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = [Elevator(bottom_floor, top_floor) for _ in range(num_elevators)]

    def run_elevator(self, elevator_number, destination_floor):
        if elevator_number < 0 or elevator_number >= len(self.elevators):
            print("Invalid elevator number.")
            return

        elevator = self.elevators[elevator_number]
        elevator.go_to_floor(destination_floor)

# Main program
if __name__ == "__main__":
    # Create a building with bottom floor 1, top floor 10, and 2 elevators
    my_building = Building(bottom_floor=1, top_floor=10, num_elevators=2)

    # Run elevator 0 to the 5th floor
    my_building.run_elevator(0, 5)

    # Run elevator 1 to the 8th floor
    my_building.run_elevator(1, 8)
