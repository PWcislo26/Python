class Produkt:

    def __init__(self, nazwa, cena, opis, waga, kategoria):
        self._nazwa = nazwa
        self._cena = cena
        self._opis = opis
        self._waga = waga
        self._kategoria = kategoria

    def __str__(self) -> str:
        return f"{self._nazwa} z kategorii {self._kategoria} kosztuje {self._cena}."

    @property
    def nazwa(self) -> str:
        return self._nazwa

    @property
    def cena(self) -> float:
        return self._cena

    @property
    def opis(self) -> str:
        return self._opis

    @property
    def waga(self) -> float:
        return self._waga

    @property
    def kategoria(self) -> str:
        return self._kategoria


class Magazyn:

    def __init__(self, identyfikator, miasto, ulica, liczba_pracownikow, wielkosc):
        self._identyfiaktor = identyfikator
        self._miasto = miasto
        self._ulica = ulica
        self._liczba_pracownikow = liczba_pracownikow
        self._wielkosc = wielkosc

    def __str__(self) -> str:
        return f"Magazyn w {self._miasto} o powierzchni {self._wielkosc} m2."

    @property
    def identyfikator(self) -> int:
        return self._identyfiaktor

    @property
    def miasto(self) -> str:
        return self._miasto

    @property
    def ulica(self) -> str:
        return self._ulica

    @property
    def liczba_pracownikow(self) -> int:
        return self._liczba_pracownikow

    @property
    def wielkosc(self) -> int:
        return self.wielkosc


class KlientDetaliczny:

    def __init__(self, imie, nazwisko, telefon, adres, email):
        self._imie = imie
        self._nazwisko = nazwisko
        self._telefon = telefon
        self._adres = adres
        self._email = email

    def __str__(self) -> str:
        return f"Klient {self._imie} o adresie {self._adres} i telefonie {self._telefon}"

    @property
    def imie(self) -> str:
        return self._imie

    @property
    def nazwisko(self) -> str:
        return self._nazwisko

    @property
    def telefon(self) -> str:
        return self._telefon

    @property
    def email(self) -> str:
        return self._email

    @property
    def adres(self) -> str:
        return self._adres


class KlientBizensowy:

    def __init__(self, identyfikator, nazwa, adres, nip, telefon):
        self._identyfikator = identyfikator
        self._nazwa = nazwa
        self._adres = adres
        self._nip = nip
        self._telefon = telefon

    def __str__(self) -> str:
        return f"Klient {self._nazwa} o nipie {self._nip} i telefonie {self._telefon}"

    @property
    def identyfikator(self) -> int:
        return self._identyfikator

    @property
    def nazwa(self) -> str:
        return self._nazwa

    @property
    def adres(self) -> str:
        return self._adres

    @property
    def nip(self) -> str:
        return self._nip

    @property
    def telefon(self) -> str:
        return self._telefon


class Zamowienie:

    def __init__(self, klient, produkty, magazyn, data, wartosc):
        self._klient = klient
        self._produkty = produkty
        self._magazyn = magazyn
        self._data = data
        self._wartosc = wartosc

    def __str__(self) -> str:
        return f"{self._klient} zlozyl zamowienie dnia {self._data} o wartosci {self._wartosc} zł."

    @property
    def klient(self) -> str:
        return self._klient

    @property
    def produkty(self) -> list:
        return self._produkty

    @property
    def magazyn(self) -> str:
        return self._magazyn

    @property
    def data(self) -> str:
        return self._data

    @property
    def wartosc(self) -> float:
        return self._wartosc

    @klient.setter
    def klient(self, klient):
        self._klient = klient

    @produkty.setter
    def produkty(self, produkty: list):
        self._produkty = produkty

    @magazyn.setter
    def magazyn(self, magazyn: str):
        self._magazyn = magazyn

    @data.setter
    def data(self, data: str):
        self._data = data

    @wartosc.setter
    def wartosc(self, wartosc: float):
        self._wartosc = wartosc

    def oblicz_wartosc(self) -> float:
        wartosc = 0.0
        for produkt in self._produkty:
            wartosc += produkt.cena
        self._wartosc = wartosc
        return round(wartosc, 2)

    def adres_klienta(self) -> str:
        return self._klient.adres



klient = KlientDetaliczny("Piotr", "Wcislo", "123456789", "Katowice, Murckowska 17", "piotrwcislo@gmail.com")
aparat = Produkt("Canon xyz", 1430.11, "fajny aparat" , 1337, "aparaty")
telefon = Produkt("Samsung xyz", 2222.234, "super telefom", 154, "smartfony")
magazyn = Magazyn(1, "Sosnowiec", "3-maja 41", 35, 10000)
zamowienie = Zamowienie(klient, [aparat, telefon], magazyn, "11/11/2021", 100)
print(zamowienie)

