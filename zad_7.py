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


    #def __init__(self, data: dict):
        #self.name: str = data.get("name")
        #self.id: str = data.get("id")
        #self.brewery_type: str = data.get("brewery_type")
        #self.address1: Optional[str] = data.get("address_1")
        #self.address2: Optional[str] = data.get("address2")
        #self.address3: Optional[str] = data.get("address3")
        #self.city: str = data.get("city")
        #self.state_province: str = data.get("state_province")
        #self.postal_code: str = data.get("postal_code")
        #self.country: str = data.get("country")
        #self.latitude: float = data.get("latitude")
        #self.longitude: float = data.get("longitude")
        #self.phone: Optional[str] = data.get("phone")
        #self.website_url: Optional[str] = data.get("website_url")
        #self.state: str = data.get("state")
        #self.street: Optional[str] = data.get("street")

    #def __str__(self) -> str:
         #return (f"[Name:{self.name}],[ID:{self.id}],[BreweryType:{self.brewery_type}],[Address1:{self.address1}],[Address2:{self.address2}],[Address3:{self.address3}],[City:{self.city}],[StateProvince:{self.state_province}],[PostalCode:[{self.postal_code}],[Country:{self.country}]")
         #pass
    def __str__(self) -> str:
        return (
            f"BROWAR: {self.name}\n"
            f"TYPE:    {self.brewery_type}\n"
            f"CITY: {self.city} ({self.country})\n"
            f"{'=' * 30}"
        )

#def fetch_breweries(limit: int):
def get_breweries_from_api(limit: int ) -> list:

        try:
            response = requests.get(urlAPI)
            response.raise_for_status()
            data = response.json()

            return [Brewery(**item) for item in data]

        except requests.exceptions.RequestException as e:
            print(f"Some error occured: {e}")
            return[]

if __name__ == "__main__":

        brewery_list = get_breweries_from_api(20)

        for brewery in brewery_list:
            print(brewery)










