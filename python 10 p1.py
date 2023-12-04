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

# Main program
if __name__ == "__main__":
    # Create an elevator with bottom floor 1 and top floor 10
    elevator = Elevator(bottom_floor=1, top_floor=10)

    # Move the elevator to the 5th floor
    elevator.go_to_floor(5)

    # Move the elevator back to the bottom floor
    elevator.go_to_floor(1)
