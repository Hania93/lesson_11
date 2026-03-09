# Zadanie 1 – Klasa Film
# Zadania z gwiazdką (challenge)
# Stwórz klasę Film, która przy tworzeniu obiektu będzie przyjmować tytul, rezyser i
# rok_produkcji. Dodaj metodę informacje(), która będzie zwracać string z pełnymi
# informacjami o filmie w formacie: "Tytuł" (rok_produkcji), reżyseria: Reżyser. Stwórz dwa
# obiekty tej klasy i wydrukuj informacje o nich

def task_1():
    class Film:
        def __init__(self, tytul, rezyser, rok_produkcji):
            self.tytul = tytul
            self.rezyser = rezyser
            self.rok_produkcji = rok_produkcji

        def informacje(self):
            return f"Tytuł: {self.tytul} ({self.rok_produkcji}), reżyseria: {self.rezyser}"
        
    film_1 = Film("Tytul_1", "Rez_1", "Rok_1")
    film_2 = Film("Tytul_2", "Rez_2", "Rok_2")

    print(film_1.informacje())
    print(film_2.informacje())

# Zadanie 2 – Atrybuty Produkt
# Zdefiniuj klasę Produkt z konstruktorem init przyjmującym nazwa, cena i kategoria. Stwórz
# obiekt tej klasy, a następnie wydrukuj każdy z jego atrybutów w osobnej linii.

def task_2():
    class Produkt:
        def __init__(self, nazwa, cena, kategoria):
            self.nazwa = nazwa
            self.cena = cena
            self.kategoria = kategoria

    produkt_1 = Produkt("Produkt_1", 5, "Kategoria_1")

    print(produkt_1.cena)
    print(produkt_1.kategoria)
    print(produkt_1.nazwa)

# Zadanie 3 – Dziedziczenie Pracownik -> Programista
# Stwórz klasę bazową Pracownik z atrybutami imie i stawka_godzinowa. Dodaj metodę
# oblicz_pensje(liczba_godzin). Następnie stwórz klasę potomną Programista, która
# dziedziczy po Pracownik. W klasie Programista dodaj atrybut jezyki_programowania (lista
# stringów). Stwórz obiekt klasy Programista i wywołaj na nim metodę oblicz_pensje.

def task_3():
    class Pracownik:
        def __init__(self, imie, stawka_godzinowa):
            self.imie = imie
            self.stawka_godzinowa = stawka_godzinowa

        def oblicz_pensje(self, liczba_godzin):
            return liczba_godzin * self.stawka_godzinowa
        
    class Programista(Pracownik):
        def __init__(self, imie, stawka_godzinowa, jezyki_programowania):
            super().__init__(imie, stawka_godzinowa)
            self.jezyki_programowania = jezyki_programowania

    programista_1 = Programista("Imie_1", 10, ["Python", "JS"])
    print(f"Pensja programisty {programista_1.imie} wynosi {programista_1.oblicz_pensje(120)}")

# ✏ Zadanie 4 – Czytelny Punkt
# Stwórz klasę Punkt do reprezentowania punktu w 2D, z atrybutami x i y. Zaimplementuj
# metodę str, aby print(punkt) wyświetlał współrzędne w formacie (x, y).
# (proste)

def task_4():
    class Punkt:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __str__(self):
            return f"({self.x}, {self.y})"
        
    punkt_1 = Punkt(2, 5)
    print(punkt_1)
            

# 5. ✏ Zadanie 5 – Polimorficzna Figura
# Stwórz klasę bazową Figura z metodą oblicz_pole(), która pass (nic nie robi). Następnie
# stwórz dwie klasy potomne: Kwadrat (z atrybutem bok) i Kolo (z atrybutem promien). W obu
# klasach nadpisz metodę oblicz_pole() odpowiednimi wzorami matematycznymi (dla koła
# przyjmij PI=3.14159). Stwórz listę zawierającą jeden kwadrat i jedno koło, a następnie w
# pętli wydrukuj pole każdej figury.

def task_5():
    class Figura:
        def __init__(self):
            pass

        def oblicz_pole(self):
            pass

    class Kwadrat(Figura):
        def __init__(self, bok):
            super().__init__()
            self.bok = bok

        def oblicz_pole(self):
            return self.bok * self.bok

    class Kolo(Figura):
        def __init__(self, promien):
            super().__init__()
            self.promien = promien

        def oblicz_pole(self):
            PI = 3.14159
            return PI * self.promien * self.promien / 2
        
    figures = [
        Kwadrat(6),
        Kolo(5)
    ]

    for figure in figures:
        print(f"Pole figury wynosi: {figure.oblicz_pole()}")


# Zadanie 6 – Wektor 2D i przeciążanie operatorów
# Stwórz klasę Wektor2D z atrybutami x i y. Przeciąż następujące operatory:
# __add__(self, other) : do dodawania dwóch wektorów (dodajemy odpowiadające
# sobie współrzędne).
# __sub__(self, other) : do odejmowania wektorów.
# eq(self, other): do porównywania, czy dwa wektory są równe (mają te same x i y).
# Dodatkowo zaimplementuj str do ładnego wyświetlania. Przetestuj działanie, tworząc
# dwa wektory i wykonując na nich wszystkie zaimplementowane operacje. (challenge)

def task_6():
    class Wector2D:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __str__(self):
            return f"Wektor x = {self.x}, y = {self.y}"
        
        def __add__(self, other):
            if isinstance(other, Wector2D):
                return (self.x + other.x, self.y + other.y)
            return NotImplemented

        def __sub__(self, other):
            if isinstance(other, Wector2D):
                return (self.x - other.x, self.y - other.y)
            return NotImplemented
        
        def __eq__(self, other):
            if isinstance(other, Wector2D):
                return self.x == other.x and self.y == other.y
            return NotImplemented
        
    vec_1 = Wector2D(2,5)
    vec_2 = Wector2D(6,12)

    print(vec_1)
    print(vec_2)
    print(vec_1.__add__(vec_2))
    print(vec_2.__sub__(vec_1))
    print(vec_1.__eq__(vec_2))

# 7. 🧠 Zadanie 7 – Enkapsulacja w Telewizorze
# Stwórz klasę Telewizor. Użyj enkapsulacji, aby ukryć następujące atrybuty: kanal
# (domyślnie 1), glosnosc (domyślnie 10), __wlaczony (domyślnie False). Stwórz publiczne
# metody do zarządzania telewizorem:
# wlacz() i wylacz()
# zmien_kanal(numer) : kanał można zmienić tylko, gdy TV jest włączony.
# glosniej() i ciszej() : głośność można regulować w zakresie 0-100 i tylko, gdy TV
# jest włączony.
# info(): wyświetla aktualny stan (włączony/wyłączony, kanał, głośność). Przetestuj, czy
# nie da się zmienić kanału na wyłączonym telewizorze lub ustawić głośności powyżej
# 100. (challenge)

def task_7():
    class Telewizor:
        def __init__(self, kanal = 1, glosnosc = 10, wlaczony = False):
            self.kanal = kanal
            self.glosnosc = glosnosc
            self.__wlaczony = wlaczony

        def wlacz(self):
            self.__wlaczony = True

        def wylacz(self):
            self.__wlaczony = False

        def zmien_kanal(self, numer):
            if self.__wlaczony:
                self.kanal = numer 

        def glosniej(self):
            if self.__wlaczony:
                if self.glosnosc + 1 <= 100:
                    self.glosnosc += 1

        def ciszej(self):
            if self.__wlaczony:
                if self.glosnosc - 1 >= 0:
                    self.glosnosc -= 1
        
        def info(self):
            print(f"Telewizor jest {"włączony" if self.__wlaczony else "wyłączony"}, głośność: {self.glosnosc}, kanal: {self.kanal}")

    telewizor_1 = Telewizor()
    telewizor_1.info()
    telewizor_1.glosniej()
    telewizor_1.info()
    telewizor_1.wlacz()
    telewizor_1.info()
    telewizor_1.glosniej()
    telewizor_1.info()
    telewizor_1.zmien_kanal(5)
    telewizor_1.info()

    for _ in range(120):
        telewizor_1.glosniej()

    telewizor_1.info()

    for _ in range(150):
        telewizor_1.ciszej()

    telewizor_1.info()
    telewizor_1.wylacz()
    telewizor_1.info()

# 8. 🧠 Zadanie 8 – Hierarchia instrumentów muzycznych
# Zaprojektuj hierarchię klas: Instrument -> Strunowy i Dety. Następnie Gitara (dziedziczy po
# Strunowy) i Trabka (dziedziczy po Dety). Klasa Instrument powinna mieć metodę graj(),
# która zwraca ogólny komunikat. Każda kolejna klasa w hierarchii powinna nadpisywać tę
# metodę, dodając coś od siebie i wywołując wersję z klasy nadrzędnej za pomocą
# super().graj().
# Instrument.graj() -> "Wydaje dźwięk."
# Strunowy.graj() -> "Wydaje dźwięk. [Szarpnięcie struny]"
# Gitara.graj() -> "Wydaje dźwięk. [Szarpnięcie struny] [Akord G-dur]" (challenge)

def task_8():
    class Instrument:
        def graj(self):
            return "Wydaje dźwięk"
        
    class Dety(Instrument):
        def graj(self):
            super().graj()

    class Trabka(Dety):
        def graj(self):
            super().graj()
        
    class Strunowy(Instrument):
        def graj(self):
            return f"{super().graj()} [Szarpnięcie struny]"
        
    class Gitara(Strunowy):
        def graj(self):
            return f"{super().graj()} [Akord G-dur]"
        
    gitara = Gitara()
    print(f"{gitara.graj()}")

# 9. 🧠 Zadanie 9 – Walidacja danych w init
# Stwórz klasę RejestracjaUzytkownika. W konstruktorze init przyjmuj email i haslo.
# Wewnątrz konstruktora dodaj walidację:
# Sprawdź, czy email zawiera znak @ . Jeśli nie, podnieś wyjątek ValueError z
# odpowiednim komunikatem.
# Sprawdź, czy haslo ma co najmniej 8 znaków. Jeśli nie, podnieś ValueError. Użyj bloku
# try...except, aby przetestować tworzenie obiektów z poprawnymi i niepoprawnymi
# danymi. (challenge)

def task_9():
    class RejestracjaUzytkownika:
        def __init__(self, email, haslo):
            if not '@' in email:
                raise ValueError("Błąd! Nieprawidłowy email!")
            
            if len(haslo) >= 8:
                raise ValueError("Błąd! Haslo musi miec conajmniej 8 znaków!")
            
            self.email = email
            self.haslo = haslo

    def main():        
        wrong_mail = "mail"
        wrong_password = "haslo"
        good_mail = "mail@"
        good_password = "password"

        try:
            RejestracjaUzytkownika(wrong_mail, wrong_password)            
            print("Poprawnie zarejestrowano użytkownika.")
        except Exception as e:
            print(e)
        try:
            RejestracjaUzytkownika(good_mail, wrong_password)            
            print("Poprawnie zarejestrowano użytkownika.")
        except Exception as e:
            print(e)
        try:
            RejestracjaUzytkownika(good_mail, good_password)
            print("Poprawnie zarejestrowano użytkownika.")
        except Exception as e:
            print(e)

    main()


# 10. 🧠 Zadanie 10 – Eksploracja MRO
# Stwórz następującą, złożoną hierarchię dziedziczenia:
# class A
# class B(A)
# class C(A)
# class D(B)
# class E(C)
# class F(D, E) Narysuj schemat tej hierarchii w mermaid. Następnie, nie uruchamiając
# kodu, spróbuj przewidzieć, jakie będzie MRO dla klasy F. Na koniec sprawdź swoją
#odpowiedź, używając print(F.mro()). (challenge)

def task_10():
    class A:
        pass
    class B(A):
        pass
    class C(A):
        pass
    class D(B):
        pass
    class E(C):
        pass
    class F(D, E):
        pass
    
    # MRO : F -> D -> B -> E -> C -> A
    print(F.mro())

task_10()

