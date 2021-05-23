from car import Car


class Truck(Car):

    def __init__(self, brand: str, power: int, prod_year: int, max_capacity: int, driver: str, cargos: dict):
        super().__init__(brand, power, prod_year)
        self.max_capacity = max_capacity
        self.driver = driver
        self.cargos = cargos

    def set_driver(self, driver: str):
        self.driver = driver

    def add_cargo(self, name: str, weight: int):
        self.cargos[name] = weight

    def del_cargo(self, name: str):
        del self.cargos[name]

    def get_all_cargos(self):
        result = ''

        for key, value in self.cargos.items():
            result += ('\n - ' + key + ': ' + str(value))

        return result

    def __str__(self):
        return 'brand: ' + self.brand + \
               '\npower: ' + str(self.power) + \
               '\nprod_year: ' + str(self.prod_year) + \
               '\nmax_capacity: ' + str(self.max_capacity) + \
               '\ndriver: ' + self.driver
