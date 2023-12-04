import random

class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed_change):
        # Ensure speed doesn't go below 0
        self.current_speed = max(0, self.current_speed + speed_change)
        # Ensure speed doesn't exceed the maximum
        self.current_speed = min(self.current_speed, self.max_speed)

    def drive(self, hours):
        # Calculate the distance traveled based on constant speed
        distance_traveled = self.current_speed * hours
        # Update the travelled distance
        self.travelled_distance += distance_traveled

class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            # Generate a random change of speed for each car
            speed_change = random.randint(-10, 15)
            car.accelerate(speed_change)

            # Call the drive method for each car
            car.drive(1)

    def print_status(self):
        print("{:<12} {:<15} {:<15} {:<20}".format("Registration", "Max Speed (km/h)", "Travelled Distance (km)", "Current Speed (km/h)"))
        for car in self.cars:
            print("{:<12} {:<15} {:<15} {:<20}".format(car.registration_number, car.max_speed, car.travelled_distance, car.current_speed))

    def race_finished(self):
        return any(car.travelled_distance >= self.distance for car in self.cars)

# Main program
if __name__ == "__main__":
    # Create a list of 10 cars for the race
    cars_for_race = [Car(f"Car-{i}", random.randint(100, 200)) for i in range(1, 11)]

    # Create a race with a distance of 8000 km
    grand_demolition_derby = Race(name="Grand Demolition Derby", distance=8000, cars=cars_for_race)

    # Simulate the progressing of the race
    hours_elapsed = 0
    while not grand_demolition_derby.race_finished():
        # Call hour_passes in a loop
        grand_demolition_derby.hour_passes()
        hours_elapsed += 1

        # Print the current status every ten hours
        if hours_elapsed % 10 == 0:
            print(f"\nRace Status After {hours_elapsed} Hours:")
            grand_demolition_derby.print_status()

    # Print the final status of the race
    print("\nRace Finished! Final Status:")
    grand_demolition_derby.print_status()
