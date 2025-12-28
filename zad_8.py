import argparse
import requests

URL_API = "https://api.openbrewerydb.org/v1/breweries"


class Brewery:

    def __init__(
        self,
        id: str,
        name: str,
        brewery_type: str,
        address_1: str | None,
        address_2: str | None,
        address_3: str | None,
        city: str,
        state_province: str,
        postal_code: str,
        country: str,
        longitude: float | None,
        latitude: float | None,
        phone: str | None,
        website_url: str | None,
        state: str,
        street: str | None,
    ):
        self.id = id
        self.name = name
        self.brewery_type = brewery_type
        self.address_1 = address_1
        self.address_2 = address_2
        self.address_3 = address_3
        self.city = city
        self.state_province = state_province
        self.postal_code = postal_code
        self.country = country
        self.longitude = longitude
        self.latitude = latitude
        self.phone = phone
        self.website_url = website_url
        self.state = state
        self.street = street

    def __str__(self) -> str:
        return (
            f"id: {self.id}, name: {self.name}, type: {self.brewery_type}, " +
            f"address: {self.address_1} {self.address_2} {self.address_3}, " +
            f"city: {self.city}, state_province: {self.state_province}, " +
            f"postal_code: {self.postal_code}, country: {self.country}, " +
            f"longitude: {self.longitude}, latitude: {self.latitude}, " +
            f"phone: {self.phone}, website_url: {self.website_url}," +
            f"state: {self.state}, street: {self.street}"
        )


def get_breweries_from_api(limit: int, city: str | None) -> list[Brewery]:
    breweries = []
    try:
        params = {
            "page": 1,
            "per_page": limit,
        }
        if city:
            params["by_city"] = city

        response = requests.get(URL_API, params=params)
        response.raise_for_status()
        data = response.json()

        for item in data:
            b = Brewery(item["id"], item["name"], item["brewery_type"], item["address_1"], item["address_2"],
                        item["address_3"], item["city"], item["state_province"], item["postal_code"],
                        item["country"], item["longitude"], item["latitude"], item["phone"],
                        item["website_url"], item["state"], item["street"])
            breweries.append(b)

        return breweries
    except requests.exceptions.RequestException as e:
        print(f"Some error occurred: {e}")
        return []


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Breweries API')
    parser.add_argument('--city', help='Filter by city', required=False)
    args = parser.parse_args()

    brewery_list = get_breweries_from_api(20, args.city)
    for brewery in brewery_list:
        print(brewery)
