print("Witaj w naszym programie.\nDzisiaj napiszemy program do generowania zyczen urodzinowych")
imie_odbiorcy = input("Podaj imie osoby dla ktorej jest ta kartka")
rok_urodzenia = int(input("Podaj rok urodzenia osoby dla ktorej jest ta kartka"))
obecny_rok = 2023
wiek_odbiorcy = obecny_rok - rok_urodzenia
spersonalizowana_wiadomosc = input("Napisz czego zyczysz odbiorcy z okazji urodzin")
imie_nadawcy = input("Podaj imie osoby od ktorej jest ta kartka")
print(f"{imie_odbiorcy}, wszystkiego najlepszego z okazji {wiek_odbiorcy} urodzin!")

print(spersonalizowana_wiadomosc)

print(imie_nadawcy)