class vehicle:
    def __init__(self,name,max_speed,mileage,brand):
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage
        self.brand=brand
class Bus(vehicle):
    pass

School_bus=Bus('School Thomas',180,13,'School Bus')
print('Vehicle Name:',School_bus.name,'\nSpeed:',School_bus.max_speed,'\nMileage:',School_bus.mileage,'\nBrand:',School_bus.brand)