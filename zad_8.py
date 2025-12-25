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
        self.id = id

    def __str__(self) -> str:
        return (
            f"BROWAR: {self.name}\n"
            f"TYPE:    {self.brewery_type}\n"
            f"CITY: {self.city} ({self.country})\n"
            f"{'=' * 30}"
        )


def get_breweries_from_api(city: str | None) -> list:
    limit_param = "per_page=20"

    if city is not None:

        url = f'{url_API}?by_city={city}&{limit_param}'
        return requests.get(url).json()

    return requests.get(f'{url_API}?{limit_param}').json()


def brewery_factory(breweries_data: list) -> List[Brewery]:

    brewery_objects = []
    for item in breweries_data:
        brewery_objects.append(Brewery(**item))
    return brewery_objects