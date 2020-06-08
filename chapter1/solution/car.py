from chapter1.errors import IllegalCarError

class Car:
    pax_norm = (1, 6)
    mass_norm = 2000

    def __init__(self, pax_count, car_mass, gear_count):
        self.pax_count = pax_count
        self.car_mass = car_mass
        self.gear_count = gear_count

    @property
    def total_mass(self):
        return self.car_mass + self.pax_count * 70

    def __setattr__(self, name, value):
        if name == 'pax_count':
            if value < Car.pax_norm[0]:
                raise IllegalCarError(name, value - Car.pax_norm[0])
            if value > Car.pax_norm[1]:
                raise IllegalCarError(name, value - Car.pax_norm[1])
        elif name == 'car_mass':
            if value > Car.mass_norm:
                raise IllegalCarError(name, value - Car.mass_norm)
        self.__dict__[name] = value