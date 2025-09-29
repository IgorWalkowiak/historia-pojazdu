### Historia Pojazdu — prosta instrukcja

Ten program pomaga znaleźć dokładną datę pierwszej rejestracji pojazdu. Wystarczy podać numer rejestracyjny, numer VIN i rok, w którym szukasz daty.

### Co potrzebujesz
- **numer rejestracyjny** (np. PKS66111)
- **numer VIN** (17 znaków, np. VF1RJB00265666700)
- **rok**, który chcesz sprawdzić (np. 2020)
- **dostęp do internetu**

### Jak uruchomić krok po kroku

1. Pobierz projekt jako ZIP (Na górze projektu zielone "<> Code", lub niżej w sekcji "Pobierz")
2. rozpakuj na komputerze (np. do folderu „historia-pojazdu”).
3. Wejdź do rozpakowanego folderu.

**Windows (najprościej, najmniej przetestowane)**
- Kliknij dwukrotnie plik `Uruchom.bat`.
- Skrypt:
  - sprawdzi, czy masz zainstalowanego Pythona,
  - zainstaluje wymagane elementy (`requirements.txt`),
  - uruchomi program.
- Jeśli pojawi się komunikat o braku Pythona, zainstaluj Python 3.10+ (zaznacz „Add Python to PATH”) i uruchom `Uruchom.bat` ponownie.

**Windows (gdyby plik .bat nie działał)**
1. Otwórz „Wiersz polecenia”.
2. Przejdź do folderu projektu, np.:
   ```bat
   cd C:\sciezka\do\historia-pojazdu
   ```
3. Zainstaluj wymagania:
   ```bat
   python -m pip install -r requirements.txt
   ```
4. Uruchom program:
   ```bat
   python src\main.py
   ```

**macOS / Linux**
1. Otwórz Terminal.
2. Przejdź do folderu projektu, np.:
   ```bash
   cd ~/Pobrane/historia-pojazdu
   ```
3. (Opcjonalnie) utwórz i włącz środowisko wirtualne, aby nie mieszać zależności w systemie:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
4. Zainstaluj wymagania:
   ```bash
   python3 -m pip install -r requirements.txt
   ```
5. Uruchom program:
   ```bash
   python3 src/main.py
   ```


### Instrukcja obsługi
1. Uruchom program.
2. Wpisz numer rejestracyjny pojazdu.
3. Wpisz numer VIN.
4. Podaj rok, w którym chcesz znaleźć datę pierwszej rejestracji.
5. Poczekaj, aż program zakończy sprawdzanie. Na ekranie zobaczysz pasek postępu.

### Pobierz
- Bezpośredni ZIP: [Pobierz ZIP](https://github.com/IgorWalkowiak/historia-pojazdu/archive/refs/heads/master.zip)
- Strona projektu: [GitHub — historia-pojazdu](https://github.com/IgorWalkowiak/historia-pojazdu) (Code → Download ZIP)

### Wskazówki
- **Nie zamykaj okna** programu, dopóki trwa wyszukiwanie.

### Uwagi
Program korzysta z publicznie dostępnych informacji. Dane, które wpisujesz, służą wyłącznie do jednorazowego sprawdzenia. Program powstał w celach edukacyjnych

