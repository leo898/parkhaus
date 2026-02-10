# main.py – Hauptprogramm des Smart Parking Systems

from config import WARTUNG_CODEWORT
from storage import zustand_laden, zustand_speichern
from parking import einfahren, ausfahren
from utils import (
    status_anzeigen,
    detaillierter_report,
    hauptmenue_anzeigen,
    wartungsmenue_anzeigen,
)


def wartungsmodus(belegte_plaetze, einnahmen, fahrzeuge):
    """
    Wartungsmodus: Zugriff nur mit Codewort.
    Ermöglicht Leeren, Einnahmen entnehmen, Report.
    """
    # Codewort abfragen
    codewort = input("\nBitte Wartungs-Codewort eingeben: ").strip()
    if codewort != WARTUNG_CODEWORT:
        print(">> Falsches Codewort! Zugriff verweigert.")
        return belegte_plaetze, einnahmen, fahrzeuge

    print(">> Wartungsmodus aktiviert.")

    while True:
        wartungsmenue_anzeigen()
        befehl = input("Wartung> ").strip().lower()

        if befehl == "empty":
            # Alle Fahrzeuge entfernen
            anzahl = len(fahrzeuge)
            fahrzeuge.clear()
            belegte_plaetze = 0
            print(f">> Parkhaus geleert. {anzahl} Fahrzeug(e) entfernt.")
            zustand_speichern(belegte_plaetze, einnahmen, fahrzeuge)

        elif befehl == "take money":
            # Einnahmen entnehmen
            if einnahmen > 0:
                print(f">> Einnahmen von {einnahmen:.2f} € entnommen.")
                einnahmen = 0.0
            else:
                print(">> Keine Einnahmen vorhanden.")
            zustand_speichern(belegte_plaetze, einnahmen, fahrzeuge)

        elif befehl == "report":
            # Detaillierter Statusbericht
            detaillierter_report(belegte_plaetze, einnahmen, fahrzeuge)

        elif befehl == "exit":
            print(">> Wartungsmodus beendet.")
            zustand_speichern(belegte_plaetze, einnahmen, fahrzeuge)
            break

        else:
            print(">> Unbekannter Befehl. Bitte erneut versuchen.")

    return belegte_plaetze, einnahmen, fahrzeuge


def main():
    """Hauptprogramm-Schleife."""
    print("\n" + "=" * 50)
    print("   SMART PARKING SYSTEM – Willkommen!")
    print("=" * 50)

    # Zustand laden
    belegte_plaetze, einnahmen, fahrzeuge = zustand_laden()

    while True:
        hauptmenue_anzeigen()
        befehl = input("Eingabe> ").strip().lower()

        if befehl == "enter":
            belegte_plaetze, fahrzeuge = einfahren(belegte_plaetze, fahrzeuge)

        elif befehl == "exit":
            belegte_plaetze, einnahmen, fahrzeuge = ausfahren(
                belegte_plaetze, einnahmen, fahrzeuge
            )

        elif befehl == "status":
            status_anzeigen(belegte_plaetze, einnahmen)

        elif befehl == "maintenance":
            belegte_plaetze, einnahmen, fahrzeuge = wartungsmodus(
                belegte_plaetze, einnahmen, fahrzeuge
            )

        elif befehl == "off":
            # Zustand speichern und beenden
            zustand_speichern(belegte_plaetze, einnahmen, fahrzeuge)
            print("\n>> System wird heruntergefahren. Auf Wiedersehen!")
            break

        else:
            print(">> Unbekannter Befehl. Bitte erneut versuchen.")


if __name__ == "__main__":
    main()