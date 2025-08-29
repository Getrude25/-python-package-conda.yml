# Parent Class
class Smartphone:
    def __init__(self, brand, model, storage, battery):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.battery = battery
    
    def make_call(self, number):
        print(f"{self.brand} {self.model} is calling {number} 📞")
    
    def charge(self, percent):
        self.battery += percent
        if self.battery > 100:
            self.battery = 100
        print(f"{self.brand} {self.model} charged to {self.battery}% 🔋")


# Child Class 1
class AndroidPhone(Smartphone):
    def __init__(self, brand, model, storage, battery, android_version):
        super().__init__(brand, model, storage, battery)
        self.android_version = android_version

    def show_os(self):
        print(f"{self.brand} {self.model} runs Android {self.android_version} 🤖")


# Child Class 2
class IPhone(Smartphone):
    def __init__(self, brand, model, storage, battery, ios_version):
        super().__init__(brand, model, storage, battery)
        self.ios_version = ios_version

    def show_os(self):
        print(f"{self.brand} {self.model} runs iOS {self.ios_version} 🍎")
        

# Example usage
samsung = AndroidPhone("Samsung", "S24", 256, 85, "14")
iphone = IPhone("Apple", "iPhone 15", 512, 90, "17")

samsung.make_call("123-456-789")
iphone.charge(15)
samsung.show_os()
iphone.show_os()

# Polymorphism Example
class Car:
    def move(self):
        print("Driving 🚗")

class Plane:
    def move(self):
        print("Flying ✈️")

class Boat:
    def move(self):
        print("Sailing ⛵")

class Animal:
    def move(self):
        print("Walking 🐾")

# List of objects with polymorphism
objects = [Car(), Plane(), Boat(), Animal()]

for obj in objects:
    obj.move()   # Each class responds differently