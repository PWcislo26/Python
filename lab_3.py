import requests


# zad 1
def nameSurname(name: str, surname: str):
    return ("Czesc {} {}".format(name, surname))


# print(nameSurname("Piotr", "Wcislo"))


# zad2
def multiply(number1: int, number2: int):
    return (number1 * number2)


# zad3
def isEven(number: int):
    if number % 2 == 0:
        return True
    else:
        return False


# czyParzysta = isEven(7)
# if czyParzysta:
#     print("Liczba parzysta")
# else:
#     print("Liczba nieparzysta")


# zad4
def zad4(number1: int, number2: int, number3: int):
    if number1 + number2 == number3:
        return True
    else:
        return False


# zad5
def inList(array: list, number: int):
    if number in array:
        return True
    else:
        return False


# zad 6
def zad6(array1: list, array2: list):
    array = list(set(array1 + array2))
    array = [number ** 3 for number in array]
    return array


#print(zad6([1, 2, 3, 4], [1, 2, 3, 4, 5, 6, 7]))


# zad 7


class Brawery():

    def __init__(self, identity, name, brewery_type, street, address_2, address_3, city, state, county_province,
                 postal_code, country, longitude, latitude, phone, website_url, updated_at, created_at):
        self.id = identity
        self.name = name
        self.brewery_type = brewery_type
        self.street = street
        self.address_2 = address_2
        self.address_3 = address_3
        self.city = city
        self.state = state
        self.county_province = county_province
        self.postal_code = postal_code
        self.country = country
        self.longitude = longitude
        self.latitude = latitude
        self.phone = phone
        self.website_url = website_url
        self.updated_at = updated_at
        self.created_at = created_at

    def __str__(self):
        return "Brewery {} is located in {} at {} long {} lat".format(self.name, self.state, self.longitude, self.latitude)



def getInfo():
    url = 'https://api.openbrewerydb.org/breweries?per_page=20'
    resp = requests.get(url)
    data = resp.json()
    listOfBreweries = []
    for i in data:
        listOfBreweries.append(
            Brawery(i['id'], i['name'], i['brewery_type'], i['street'], i['address_2'], i['address_3'],
                    i['city'], i['state'], i['county_province'], i['postal_code'], i['country'],
                    i['longitude'], i['latitude'], i['phone'], i['website_url'], i['updated_at'],
                    i['created_at']))
    for brewery in listOfBreweries:
        print(brewery)


if __name__ == "__main__":
    getInfo()