class Property:
    def __init__(self, area: float, rooms: int, price: float, address: str):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address


class House(Property):
    def __init__(
            self,
            area: float,
            rooms: int,
            price: float,
            address: str,
            plot: int):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return (f"House - Address: {self.address}, Area: {self.area} m2, "
                f"Rooms: {self.rooms}, Price: {self.price} PLN, "
                f"Plot: {self.plot}")


class Flat(Property):
    def __init__(self, area: float, rooms: int, price: float,
                 address: str, floor: int):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return (f"Flat - Address: {self.address}, Area: {self.area} m2, "
                f"Rooms: {self.rooms}, Price: {self.price} PLN, "
                f"Floor: {self.floor}")


house1 = House(100.00, 4, 50000, "Ohoho 10, Magadan", 600)
flat1 = Flat(30.0, 3, 600000, "21/12, New York", 105)

print(house1)
print(flat1)
