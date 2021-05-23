from car import Car


class PassengerCar(Car):

    def __init__(self, brand: str, power: int, prod_year: int, passengers: int, repairs: dict):
        super().__init__(brand, power, prod_year)
        self.passengers = passengers
        self.repairs = repairs

    def add_repair(self, part: str, year: int):
        self.repairs[part] = year

    def get_repair_year(self, part: str):
        return self.repairs.get(part)

    def get_all_repairs(self):
        result = ''

        for key, value in self.repairs.items():
            result += ('\n - ' + key + ': ' + str(value))

        return result

    def __str__(self):
        return 'brand: ' + self.brand + \
               '\npower: ' + str(self.power) + \
               '\nprod_year: ' + str(self.prod_year) + \
               '\npassengers: ' + str(self.passengers)
