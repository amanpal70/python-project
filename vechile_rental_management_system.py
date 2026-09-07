from abc import ABC,abstractmethod

class Vehicle(ABC):
    def __init__(self, vehicle_id, model, base_rate):
        self.__vehicle_id = vehicle_id
        self.__model = model
        self.base_rate = base_rate

    @property 
    def vehicle_id(self):
        return self.__vehicle_id
    @property
    def model(self):
        return self.__model
    @property
    def base_rate(self):
        return self.__base_rate
    @base_rate.setter
    def base_rate(self,value):
        if value<=0:
            raise ValueError("Base rate must be greter than 0")
        self.__base_rate=value
    

    @abstractmethod
    def calculate_rental_cost(self,days):
        
        pass

    @abstractmethod
    def display_details(self):
        pass


        #inheritance

class Car(Vehicle):
    def __init__(self, vehicle_id, model, base_rate,num_doors,luxury_fee=0.0):
        super().__init__(vehicle_id, model, base_rate)
        self.num_doors=num_doors
        self.luxury_fee=luxury_fee

    def calculate_rental_cost(self, days):
        return (self.base_rate*days)+self.luxury_fee

    def display_details(self):
        print("Vehicle ID:", self.vehicle_id)
        print("Model:", self.model)
        print("Base Rate:", self.base_rate)
        print("Number of Doors:", self.num_doors)
        print("Luxury Fee:", self.luxury_fee)


class Bike(Vehicle):
    def __init__(self, vehicle_id, model, base_rate,engine_capacity):
        super().__init__(vehicle_id, model, base_rate)
        self.engine_capacity=engine_capacity

    def calculate_rental_cost(self, days):
        if days>5:
            return (self.base_rate*days)*0.90
        else:
            return self.base_rate*days

    def display_details(self):
        print("Vehicle ID:", self.vehicle_id)
        print("Model:", self.model)
        print("Base Rate:", self.base_rate)
        print("Engine Capacity:", self.engine_capacity)

        
car1=Car("xy01","mahindra",20000,4)
car1.display_details()

bike1=Bike("abo1","apache",1000,150)
bike1.display_details()

car2=Car("xy02","swift",15000,4)
bike2=Bike("ab02","pulsar",800,180)

fleet=[car1,car2,bike1,bike2]
for vehicle in fleet:
    vehicle.display_details()
    print("Rental Cost:", vehicle.calculate_rental_cost(7))
    print("-------------------")

