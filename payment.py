# payment.py – Bezahlvorgang für das Parkhaus

from config import ERLAUBTE_MUENZEN


def bezahlung_durchfuehren(betrag):
    """
    Führt den Bezahlvorgang durch.
    Der Benutzer wirft Münzen ein, bis der Betrag erreicht oder überschritten ist.
    Gibt den tatsächlich gezahlten Betrag zurück (inkl. Wechselgeld-Info).
    """
    print(f"\n--- BEZAHLUNG ---")
    print(f"Zu zahlender Betrag: {betrag:.2f} €")
    print(f"Erlaubte Münzen: {', '.join(f'{m:.2f} €' for m in ERLAUBTE_MUENZEN)}")

    eingeworfen = 0.0

    while eingeworfen < betrag:
        restbetrag = betrag - eingeworfen
        print(f"\nNoch zu zahlen: {restbetrag:.2f} €")
        eingabe = input("Münze einwerfen (0.50 / 1.00 / 2.00): ").strip()

        try:
            muenze = float(eingabe)
        except ValueError:
            print(">> Ungültige Eingabe. Bitte eine Zahl eingeben.")
            continue

        # Rundung auf 2 Dezimalstellen für sauberen Vergleich
        muenze = round(muenze, 2)

        if muenze not in ERLAUBTE_MUENZEN:
            print(f">> Münze {muenze:.2f} € wird nicht akzeptiert.")
            print(f"   Erlaubt: {', '.join(f'{m:.2f} €' for m in ERLAUBTE_MUENZEN)}")
            continue

        eingeworfen = round(eingeworfen + muenze, 2)
        print(f">> {muenze:.2f} € eingeworfen. Gesamt: {eingeworfen:.2f} €")

    # Wechselgeld berechnen
    wechselgeld = round(eingeworfen - betrag, 2)
    if wechselgeld > 0:
        print(f"\n>> Wechselgeld: {wechselgeld:.2f} €")
    else:
        print(f"\n>> Passend bezahlt!")

    print(">> Bezahlung erfolgreich. Vielen Dank!")
    return betrag  # Es wird immer nur der tatsächliche Betrag als Einnahme gezählt