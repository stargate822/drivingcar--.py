class Car:
    def move(self):
        print("🚗 The car is driving on the road.")

class Plane:
    def move(self):
        print("✈️ The plane is flying in the sky.")

class Boat:
    def move(self):
        print("⛴️ The boat is sailing on the water.")

class Dog:
    def move(self):
        print("🐕 The dog is running on the ground.")

class Bird:
    def move(self):
        print("🐦 The bird is flying in the air.")

# Create a list of objects
objects = [Car(), Plane(), Boat(), Dog(), Bird()]

# Loop through and call move() on each
for obj in objects:
    obj.move()