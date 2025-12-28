class Library:
    def __init__(
            self, city: str, street: str, zip_code: str,
            open_hours: str, phone: str):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self) -> str:
        return (
            f"city: {self.city}, street: {self.street}, zip: {self.zip_code}, "
            f"open: {self.open_hours}, phone: {self.phone}"
        )