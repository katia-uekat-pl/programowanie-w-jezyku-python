from typing import List, Optional
import requests
import argparse
urlAPI = "https://api.openbrewerydb.org/v1/breweries"


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


def get_breweries_from_api(limit: int) -> list:
    try:
        response = requests.get(urlAPI)
        response.raise_for_status()
        data = response.json()

        return [Brewery(**item) for item in data]

    except requests.exceptions.RequestException as e:
        print(f"Some error occured: {e}")
        return []


if __name__ == "__main__":

    brewery_list = get_breweries_from_api(20)

    for brewery in brewery_list:
        print(brewery)
