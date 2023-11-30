class Paczka:
    def __init__(self):
        self.elements = []
        self.weight = 0

    def dodaj_element(self, waga_elementu):
        if waga_elementu < 1 or waga_elementu > 10:
            raise ValueError("Waga elementu powinna być między 1 a 10 kg")
        if self.weight + waga_elementu > 20:
            return False
        self.elements.append(waga_elementu)
        self.weight += waga_elementu
        return True

def wyslij_paczki(elementy):
    paczki = []
    suma_pustych_kg = 0
    najwiecej_pustych_kg = 0
    paczka_z_najwiecej_pustych_kg = None

    for waga_elementu in elementy:
        if waga_elementu == 0:
            break

        if waga_elementu < 1 or waga_elementu > 10:
            raise ValueError("Waga elementu powinna być między 1 a 10 kg")

        dodano_element = False
        for paczka in paczki:
            if paczka.dodaj_element(waga_elementu):
                dodano_element = True
                break

        if not dodano_element:
            nowa_paczka = Paczka()
            paczki.append(nowa_paczka)
            nowa_paczka.dodaj_element(waga_elementu)

    for paczka in paczki:
        puste_kg = 20 - paczka.weight
        suma_pustych_kg += puste_kg
        if puste_kg > najwiecej_pustych_kg:
            najwiecej_pustych_kg = puste_kg
            paczka_z_najwiecej_pustych_kg = paczka

    print("Liczba paczek wysłanych:", len(paczki))
    print("Liczba kilogramów wysłanych:", sum(paczka.weight for paczka in paczki))
    print("Suma 'pustych' kilogramów:", suma_pustych_kg)
    if paczka_z_najwiecej_pustych_kg is not None:
        print(
            "Paczka z największą ilością 'pustych' kilogramów:",
            paczki.index(paczka_z_najwiecej_pustych_kg) + 1,
        )
    else:
        print("Brak wysłanych paczek")

elementy_do_wyslania = []
while True:
    try:
        waga_elementu = float(input("Podaj wagę elementu (0 aby zakończyć): "))
        if waga_elementu == 0 and not elementy_do_wyslania:
            print("Brak elementów do wysłania. Koniec programu.")
            break
        elif waga_elementu == 0:
            break
        elementy_do_wyslania.append(waga_elementu)
    except ValueError:
        print("Błąd: Wprowadzona wartość nie jest liczbą.")

wyslij_paczki(elementy_do_wyslania)
