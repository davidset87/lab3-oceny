import pandas as pd

def oblicz_srednia(oceny):
    """Oblicza średnią arytmetyczną ocen"""
    return sum(oceny) / len(oceny)


def wczytaj_dane(plik):
    """Wczytuje dane z pliku CSV"""
    return pd.read_csv(plik, sep=";")


df = wczytaj_dane("oceny.csv")

df["srednia"] = df.iloc[:, 1:].apply(lambda x: oblicz_srednia(x), axis=1)

print(df[["uczen", "srednia"]])

najlepszy = df.loc[df["srednia"].idxmax()]

print("\nNajlepszy uczeń:", najlepszy["uczen"])
print("Średnia:", najlepszy["srednia"])


def test_oblicz_srednia():
    oceny = [4, 4, 4, 4]
    wynik = oblicz_srednia(oceny)
    assert wynik == 4


test_oblicz_srednia()
print("Test OK")
