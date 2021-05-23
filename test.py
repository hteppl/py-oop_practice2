from autopark import Autopark, TruckList
from passengercar import PassengerCar
from truck import Truck

cars = list()
cars.append(PassengerCar('Toyota Corolla XI 1.6', 122, 2014, 4,
                         dict({
                             'замена левого крыла': 2014,
                             'замена выхлопной системы': 2018,
                             'замена дифференциала': 2020
                         })))
cars.append(PassengerCar('Honda Civic VIII 1.8', 140, 2006, 4,
                         dict({
                             'замена газовых упоров задней двери багажника': 2010,
                             'замена двс': 2012,
                         })))
cars.append(PassengerCar('Skoda Octavia A8 1.4', 150, 2021, 4,
                         dict({
                             'замена педали газа': 2021,
                         })))

trucks = TruckList()
trucks.append(Truck('Scania R 730', 730, 2010, 28000, 'Волков Валерий',
                    dict({
                        'Зерновой корм для животных': 4000,
                        'Бытовые товары для интернет-магазина': 10000,
                    })))
trucks.append(Truck('Volvo FH16', 700, 2009, 85000, 'Тихонов Василий',
                    dict({
                        'Зерновой корм для животных': 4000,
                        'Бытовые товары для интернет-магазина': 10000,
                    })))
trucks.append(Truck('MAN TGX', 440, 2007, 18000, 'Николаев Федор',
                    dict({
                        'Зерновой корм для животных': 4000,
                        'Бытовые товары для интернет-магазина': 10000,
                    })))

autopark = Autopark('Название Автопарка', cars, trucks)
autopark.create_txt_file()

# вызов исключения #1 (ValueError)
autopark.del_truck(3)

# вызов исключения #2 (ValueError)
autopark.set_truck(5, Truck('MAN TGX', 440, 2007, 18000, 'Николаев Федор',
                            dict({
                                'Зерновой корм для животных': 4000,
                                'Бытовые товары интернет-магазина': 10000,
                            })))

# вызов исключения #3 (ValueError)
autopark.del_car(4)
