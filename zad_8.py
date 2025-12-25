from typing import List, Optional
import requests
import argparse

url_API = "https://api.openbrewerydb.org/v1/breweries"


class Brewery:
    def __init__(
            self,
            name: str,
            brewery_type: str,
            city: str,
            country: str,
            **kwargs
    ):
        self.name = name
        self.brewery_type = brewery_type
        self.city = city
        self.country = country
        self.id = kwargs.get('id')

    def __str__(self) -> str:
        return (
            f"BROWAR: {self.name}\n"
            f"TYPE:   {self.brewery_type}\n"
            f"CITY:   {self.city} ({self.country})\n"
            f"ID:     {self.id}\n"
            f"{'=' * 30}"
        )


def get_breweries_from_api(city: str | None) -> list:

    params = {"per_page": 20}
    if city:
        params["by_city"] = city

    try:
        response = requests.get(url_API, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Błąd pobierania: {e}")
        return []


def brewery_factory(breweries_data: list) -> List[Brewery]:
    brewery_objects = []
    for item in breweries_data:
        brewery_objects.append(Brewery(**item))
    return brewery_objects


def get_args():
    parser = argparse.ArgumentParser(description='Browary API')
    parser.add_argument('-c', '--city', help='Filtruj po mieście', required=False)
    return vars(parser.parse_args())


def main():
    args = get_args()
    # Pobieramy dane
    raw_data = get_breweries_from_api(city=args.get('city'))
    # Tworzymy obiekty
    breweries = brewery_factory(raw_data)

    # Wyświetlamy
    for b in breweries:
        print(b)

    print(f"Pobrano: {len(breweries)} obiektów.")


if __name__ == "__main__":
    main()