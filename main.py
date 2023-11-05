#definiowanie klasy
class Czlowiek:

    # self odnosi się do siebie. Tak jak this w javie. Można zmienić go na jakąkolwiek wartosc
    def przedstawSie(self, powitanie = "Cześć"): #wprowadzenie domyślej wartości dla parametru
        return powitanie + ", mam na imię " + self.imie + " oraz mam lat " + str(self.wiek)

    #specjalna metoda inicjalizacji danych - konstruktor
    def __init__(self, imie, wiek):
        self.imie = imie
        self.wiek = wiek

#tworzenie nowego obiektu
obiekt = Czlowiek("Marek", 33)
print(obiekt.imie)
print(obiekt.przedstawSie())

obiekt2 = Czlowiek("Adrian", 18)
obiekt2.imie = "Alan"
print(obiekt2.imie)
print(obiekt2.przedstawSie("Heja"))