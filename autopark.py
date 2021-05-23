from passengercar import PassengerCar
from truck import Truck


class TruckList(list):

    def __init__(self):
        super().__init__()

    def __sizeof__(self):
        return len(self)


class Autopark:

    def __init__(self, name: str, cars: list, trucks: TruckList):
        self.name = name
        self.cars = cars
        self.trucks = trucks

    def add_truck(self, truck: Truck):
        self.trucks.append(truck)

    def get_truck(self, index: int):
        return self.trucks[index]

    def set_truck(self, index: int, truck: Truck):
        try:
            if index < 0 or index >= len(self.trucks):
                raise ValueError('bad index in set_truck ' + str(index))

            new_trucks = list()

            for x in range(len(self.trucks)):
                if x == index:
                    new_trucks.append(truck)
                else:
                    new_trucks.append(self.trucks[x])

            self.trucks = new_trucks
        except ValueError as e:
            print('ValueError in "set_truck": ' + e.__str__())

    def del_truck(self, index: int):
        try:
            if index < 0 or index >= len(self.cars):
                raise ValueError('bad index in del_truck ' + str(index))

            new_trucks = list()

            for x in range(len(self.trucks)):
                if x != index:
                    new_trucks.append(self.trucks[x])

            self.trucks = new_trucks
        except ValueError as e:
            print('ValueError in "del_truck": ' + e.__str__())

    def add_car(self, car: PassengerCar):
        self.cars.append(car)

    def get_car(self, index: int):
        return self.cars[index]

    def set_car(self, index: int, car: PassengerCar):
        try:
            if index < 0 or index >= len(self.cars):
                raise ValueError('bad index in set_car ' + str(index))

            new_cars = list()

            for x in range(len(self.cars)):
                if x == index:
                    new_cars.append(car)
                else:
                    new_cars.append(self.cars[x])

            self.cars = new_cars
        except ValueError as e:
            print('ValueError in "set_car": ' + e.__str__())

    def del_car(self, index: int):
        try:
            if index < 0 or index >= len(self.cars):
                raise ValueError('bad index in del_car ' + str(index))

            new_cars = list()

            for x in range(len(self.cars)):
                if x != index:
                    new_cars.append(self.cars[x])

            self.cars = new_cars
        except ValueError as e:
            print('ValueError in "del_car": ' + e.__str__())

    def create_txt_file(self):
        txt = list()
        txt.append('Название автопарка: `' + self.name + '`')
        txt.append(f'\n\n\n— Список легк. авто ({len(self.cars)} шт.): ')

        for car in self.cars:
            txt.append('\n\n− Легк. Автомобиль')
            txt.append('\n Бренд: ' + car.brand)
            txt.append('\n Мощность: ' + str(car.power) + ' лс.')
            txt.append('\n Год выпуска: ' + str(car.prod_year))
            txt.append('\n Кол-во мест: ' + str(car.passengers))
            txt.append('\n Ремонтные работы: ' + car.get_all_repairs())

        txt.append('\n\n\n---------------------------------')
        txt.append(f'\n\n— Список груз. авто ({len(self.trucks)} шт.): ')

        for tr in self.trucks:
            txt.append('\n\n− Грузовик')
            txt.append('\n Бренд: ' + tr.brand)
            txt.append('\n Мощность: ' + str(tr.power) + ' лс.')
            txt.append('\n Год выпуска: ' + str(tr.prod_year))
            txt.append('\n Макс. грузоподъемность: ' + str(tr.max_capacity))
            txt.append('\n ФИ водителя: ' + tr.driver)
            txt.append('\n Перевозки: ' + tr.get_all_cargos())

        result = open('result.txt', 'w', encoding='utf-8')
        result.writelines(txt)
        result.close()

    def __str__(self):
        pass
        # todo
