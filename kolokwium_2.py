class Dieta:

    def __init__(self, nazwa, kalorie, czy_wege, cena):
        self._nazwa = nazwa
        self._kalorie = kalorie
        self._czy_wege = czy_wege
        self._cena = cena

    def __str__(self) -> str:
        return f"Dieta {self._nazwa} ma {self._kalorie} kalorii i  kosztuje {self.cena} zł "

    @property
    def nazwa(self) -> str:
        return self._nazwa

    @property
    def kalorie(self) -> int:
        return self._kalorie

    @property
    def czy_wege(self) -> bool:
        return self._czy_wege

    @property
    def cena(self) -> float:
        return self._cena


class Pacjent:

    def __init__(self, imie, nazwisko, wiek, choroba):
        self._imie = imie
        self._nazwisko = nazwisko
        self._wiek = wiek
        self._choroba = choroba

    def __str__(self) -> str:
        return f"{self._imie} {self._nazwisko} cierpi na chorobe {self._choroba}"

    @property
    def imie(self) -> str:
        return self._imie

    @property
    def nazwisko(self) -> str:
        return self._nazwisko

    @property
    def wiek(self) -> int:
        return self._wiek

    @property
    def choroba(self) -> str:
        return self._choroba


class Dietetyk:

    def __init__(self, imie, nazwisko, stopien_naukowy, lokalizacja):
        self._imie = imie
        self._nazwisko = nazwisko
        self._stopien_naukowy = stopien_naukowy
        self._lokalizacja = lokalizacja

    def __str__(self) -> str:
        return f"Dietetyk {self._imie} {self._nazwisko} posiada stopień naukowy {self._stopien_naukowy}"

    @property
    def imie(self) -> str:
        return self._imie

    @property
    def nazwisko(self) -> str:
        return self._nazwisko

    @property
    def stopien_naukowy(self) -> str:
        return self._stopien_naukowy

    @property
    def lokalizacja(self) -> str:
        return self._lokalizacja


class Zamowienie:

    def __init__(self):
        self._diety = None
        self._pacjent = None
        self._dietetyk = None
        self._data = None

    def __str__(self) -> str:
        return f"Pacjent {self._pacjent} złożył zamówienie u {self._dietetyk} dnia {self._data} "

    @property
    def diety(self) -> list:
        return self._diety

    @property
    def pacjent(self) -> Pacjent:
        return self._pacjent

    @property
    def dietetyk(self) -> Dietetyk:
        return self._dietetyk

    @property
    def data(self) -> str:
        return self._data

    @diety.setter
    def diety(self, diety: list):
        self._diety = diety

    @pacjent.setter
    def pacjent(self, pacjent: Pacjent):
        self._pacjent = pacjent

    @dietetyk.setter
    def dietetyk(self, dietetyk: Dietetyk):
        self._dietetyk = dietetyk

    @data.setter
    def data(self, data: str):
        self._data = data

    def wartosc_zamowienia(self) -> float:
        cena = 0
        for dieta in self._diety:
            cena += dieta._cena
        return round(cena, 2)

    def liczba_kalorii(self) -> int:
        liczba_kalorii = 0
        for dieta in self._diety:
            liczba_kalorii += dieta._kalorie
        return liczba_kalorii


pacjent_x = Pacjent("Marek", "Wolny", 27, "Cukrzyca")
dieta1 = Dieta("Sokowa", 500, True, 15.234)
dieta2 = Dieta("Paleo", 1500, False, 35.111)
dietetyk_y = Dietetyk("Aleksandra", "Nowak", "doktor", "Szpital nr 1 w Katowicach")

zamowienie = Zamowienie()
zamowienie.diety = [dieta1, dieta2]
zamowienie.pacjent = pacjent_x
zamowienie.dietetyk = dietetyk_y
zamowienie.data = "13/03/2021"
print(zamowienie)
print(zamowienie.wartosc_zamowienia())
print(zamowienie.liczba_kalorii())
