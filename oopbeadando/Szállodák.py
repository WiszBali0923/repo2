from datetime import datetime

class Szoba:
    def __init__(self, szobaszam, ar):
        self.szobaszam = szobaszam
        self.ar = ar

class EgyagyasSzoba(Szoba):
    def __init__(self, szobaszam, ar):
        super().__init__(szobaszam, ar)
        self.tipus = 'Egyagyas'

class KetagyasSzoba(Szoba):
    def __init__(self, szobaszam, ar):
        super().__init__(szobaszam, ar)
        self.tipus = 'Ketagyas'
class Foglalas:
    def __init__(self, szoba, datum, ar):
        self.szoba = szoba
        self.datum = datum
        self.ar = ar

class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []
        self.foglalasok = []

    def hozzaad_szoba(self, szoba):
        self.szobak.append(szoba)

    def foglalas(self, szobaszam, datum):
        for szoba in self.szobak:
            if szoba.szobaszam == szobaszam:
                ar = szoba.ar
                uj_foglalas = Foglalas(szoba, datum, ar)
                self.foglalasok.append(uj_foglalas)
                return ar
        return None

    def lemondas(self, szobaszam, datum):
        for foglalas in self.foglalasok:
            if foglalas.szoba.szobaszam == szobaszam and foglalas.datum == datum:
                self.foglalasok.remove(foglalas)
                return True
        return False

    def listazas(self):
        return [(f.szoba.szobaszam, f.datum, f.ar) for f in self.foglalasok]
class FelhasznaloiInterfesz:
    def __init__(self, szalloda):
        self.szalloda = szalloda

    def menu(self):
        while True:
            print("\n1. Foglalás létrehozása")
            print("2. Foglalás lemondása")
            print("3. Foglalások listázása")
            print("4. Kilépés")
            valasztas = input("Válassz egy műveletet: ")

            if valasztas == '1':
                szobaszam = int(input("Add meg a szobaszámot: "))
                datum_str = input("Add meg a dátumot (YYYY-MM-DD): ")
                datum = datetime.strptime(datum_str, '%Y-%m-%d').date()
                if datum > datetime.now().date():
                    ar = self.szalloda.foglalas(szobaszam, datum)
                    if ar is not None:
                        print(f"Foglalás létrehozva, ára: {ar}")
                    else:
                        print("Hiba: a szoba nem található vagy már foglalt.")
                else:
                    print("Hiba: a dátumnak a jövőben kell lennie.")

            elif valasztas == '2':
                szobaszam = int(input("Add meg a szobaszámot: "))
                datum_str = input("Add meg a dátumot (YYYY-MM-DD): ")
                datum = datetime.strptime(datum_str, '%Y-%m-%d').date()
                siker = self.szalloda.lemondas(szobaszam, datum)
                if siker:
                    print("Foglalás lemondva.")
                else:
                    print("Hiba: a foglalás nem található.")

            elif valasztas == '3':
                foglalasok = self.szalloda.listazas()
                if foglalasok:
                    for foglalas in foglalasok:
                        print(f"Szoba: {foglalas[0]}, Dátum: {foglalas[1]}, Ár: {foglalas[2]}")
                else:
                    print("Nincs foglalás.")

            elif valasztas == '4':
                break

            else:
                print("Érvénytelen választás, próbáld újra.")

# Példányosítás és tesztelés
szalloda = Szalloda("Hotel Budapest")
szalloda.hozzaad_szoba(EgyagyasSzoba(101, 10000))
szalloda.hozzaad_szoba(KetagyasSzoba(102, 15000))
szalloda.hozzaad_szoba(EgyagyasSzoba(103, 10000))

interfesz = FelhasznaloiInterfesz(szalloda)
interfesz.menu()
