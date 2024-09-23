import random


def podpowiedz_bisekcja(zgadywania, min_zakres, max_zakres):
    """Podpowiedź AI, sugerująca metodę bisekcji, gdy użytkownik zgaduje chaotycznie."""
    if len(zgadywania) > 2:
        suggested_guess = (min_zakres + max_zakres) // 2
        print(f"AI Podpowiedź: Spróbuj zgadywać w okolicach {suggested_guess}.")


def zgadywanie_liczby():
    print("Witaj w grze! Komputer wylosował liczbę z zakresu 1-100. Spróbuj ją zgadnąć!")

    liczba_do_zgadniecia = random.randint(1, 100)
    liczba_prob = 0
    zgadywania = []
    min_zakres, max_zakres = 1, 100  

    while True:
        liczba_prob += 1
        guess = int(input(f"Podaj swoją liczbę ({min_zakres}-{max_zakres}): "))
        zgadywania.append(guess)

        if guess < liczba_do_zgadniecia:
            print("Za mała!")
            min_zakres = max(min_zakres, guess + 1)
        elif guess > liczba_do_zgadniecia:
            print("Za duża!")
            max_zakres = min(max_zakres, guess - 1)
        else:
            print(f"Brawo! Zgadłeś liczbę w {liczba_prob} próbach.")
            break

        if liczba_prob > 5:
            if all(x < liczba_do_zgadniecia for x in zgadywania) or all(x > liczba_do_zgadniecia for x in zgadywania):
                print("Wygląda na to, że zgadujesz bez logiki.")
                podpowiedz_bisekcja(zgadywania, min_zakres, max_zakres)
            else:
                print("Kontynuuj, jesteś blisko!")

        if liczba_prob > 8:
            ostatnie_zgadywanie = zgadywania[-1]
            odleglosci = [abs(guess - liczba_do_zgadniecia) for guess in zgadywania]
            srednia_odleglosc = sum(odleglosci) / len(odleglosci)

            if abs(ostatnie_zgadywanie - liczba_do_zgadniecia) > srednia_odleglosc:
                print("Twoje zgadywania są trochę chaotyczne, spróbuj bardziej zbliżyć się do celu.")
                podpowiedz_bisekcja(zgadywania, min_zakres, max_zakres)


# Uruchomienie gry
zgadywanie_liczby()
