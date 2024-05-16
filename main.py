# SOLID
# S - single responsibility principle -
# принцип единой ответственности

# O - Open-closed principle -
# принцип открытости-закрытости

# L - Liskov Substitution Principle -
# Принцип замещения лисков

# I - Interface segregation principle -
# Принцип разделения интерфейсов

# D - Dependency Inversion Principle
# Принцип инверсии зависимостей


#1
class User:
    def __init__(self, db_conn, name, surname):
        self.db = db_conn
        self.name = name
        self.surname = surname

    def get_name(self):
        return self.name


class UserModelDB:
    def get_username(self, user):
        pass

    def save_db(self, user):
        pass


class FileManager:
    def read_file(self, filename):
        pass

    def write_file(self, filename):
        pass


class DataProcessor:
    def process_data(self, data):
        pass


class ReportGenerator:
    def generate_report(self, data):
        pass






class Discount:
    def __init__(self, customer, price):
        self.customer = customer
        self.price = price

    def give_discount(self):
        return self.price * 0.2


class VipDiscount(Discount):
    def get_discount(self):
        return super().give_discount() * 2







class Vehicle:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def get_name(self):
        return self.name

    def get_speed(self):
        return self.speed


class VehicleWithoutEngine(Vehicle):
    def start_moving(self):
        pass


class VehicleWithEngine(Vehicle):
    def engine(self):
        pass

    def start_engine(self):
        pass


class Car(VehicleWithEngine):
    def start_engine(self):
        pass


class Bicycle(VehicleWithoutEngine):
    def start_engine(self):
        pass







class Shape:
    def draw(self):
        pass


class Circle(Shape):
    def draw(self):
        pass


class Square(Shape):
    def draw(self):
        pass


class Circle(Shape):
    def draw_circle(self):
        pass

    def draw_square(self):
        pass













class LightBulb:
    def turn_on(self):
        print('Light bulb turned on')


class LightSwitch:
    def __init__(self):
        self.light_bulb = LightBulb()

    def toggle(self):
        print("Toggle the light switch")
        self.light_bulb.turn_on()


class Switchable:
    def turn_on(self):
        pass


class LightBulb(Switchable):
    def turn_on(self):
        print('Light bulb turned on')


class LightSwitch:
    def __init__(self, switchable_device):
        self.switchable_device = switchable_device

    def toggle(self):
        print('Toggle the light switch')
        self.switchable_device.turn_on()














class Shape:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, name, width, height):
        super().__init__(name)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


rect = Rectangle('Прямоугольник', 2, 8)
circ = Circle('Круг', 5)

print(rect.get_name(), rect.area())
print(circ.get_name(), circ.area())


