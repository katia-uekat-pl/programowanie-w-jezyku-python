from classes.library import Library


class Book:
    def __init__(
            self, library: Library, publication_date: str, author_name: str,
            author_surname: str, number_of_pages: str):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self) -> str:
        return (
            f"author name: {self.author_name}, "
            f"author surname: {self.author_surname}, "
            f"pages: {self.number_of_pages}, library: `{self.library}`"
        )
