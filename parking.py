# parking.py – Parklogik (Einfahren / Ausfahren)

import time
import math
from config import MAX_PARKPLAETZE, GEBUEHR_PRO_STUNDE
from payment import bezahlung_durchfuehren


def einfahren(belegte_plaetze, fahrzeuge):
    """
    Ein Fahrzeug fährt ins Parkhaus ein.
    Gibt zurück: (neue_belegte_plaetze, aktualisierte_fahrzeuge)
    """
    print("\n--- EINFAHRT ---")

    if belegte_plaetze >= MAX_PARKPLAETZE:
        print(">> Parkhaus voll! Es sind keine freien Plätze mehr verfügbar.")
        return belegte_plaetze, fahrzeuge

    kennzeichen = input("Bitte Kennzeichen eingeben: ").strip().upper()

    if not kennzeichen:
        print(">> Ungültiges Kennzeichen.")
        return belegte_plaetze, fahrzeuge

    if kennzeichen in fahrzeuge:
        print(f">> Fahrzeug {kennzeichen} ist bereits im Parkhaus!")
        return belegte_plaetze, fahrzeuge

    # Einfahrtszeit speichern (Unix-Timestamp)
    fahrzeuge[kennzeichen] = time.time()
    belegte_plaetze += 1

    freie_plaetze = MAX_PARKPLAETZE - belegte_plaetze
    print(f">> Fahrzeug {kennzeichen} ist eingefahren.")
    print(f">> Freie Plätze: {freie_plaetze}/{MAX_PARKPLAETZE}")

    return belegte_plaetze, fahrzeuge


def ausfahren(belegte_plaetze, einnahmen, fahrzeuge):
    """
    Ein Fahrzeug verlässt das Parkhaus.
    Berechnet Parkdauer und Gebühr, führt Bezahlung durch.
    Gibt zurück: (neue_belegte_plaetze, neue_einnahmen, aktualisierte_fahrzeuge)
    """
    print("\n--- AUSFAHRT ---")

    if belegte_plaetze <= 0:
        print(">> Das Parkhaus ist leer. Keine Fahrzeuge zum Ausfahren.")
        return belegte_plaetze, einnahmen, fahrzeuge

    kennzeichen = input("Bitte Kennzeichen eingeben: ").strip().upper()

    if kennzeichen not in fahrzeuge:
        print(f">> Fahrzeug {kennzeichen} wurde nicht im Parkhaus gefunden.")
        return belegte_plaetze, einnahmen, fahrzeuge

    # Parkdauer berechnen
    einfahrtszeit = fahrzeuge[kennzeichen]
    ausfahrtszeit = time.time()
    dauer_sekunden = ausfahrtszeit - einfahrtszeit
    dauer_stunden = dauer_sekunden / 3600

    # Angebrochene Stunden zählen als volle Stunden
    angefangene_stunden = math.ceil(dauer_stunden)
    # Mindestens 1 Stunde berechnen
    if angefangene_stunden < 1:
        angefangene_stunden = 1

    gebuehr = angefangene_stunden * GEBUEHR_PRO_STUNDE

    print(f"\nFahrzeug: {kennzeichen}")
    print(f"Parkdauer: {dauer_stunden:.2f} Stunden ({angefangene_stunden} angefangene Stunde(n))")
    print(f"Gebühr: {gebuehr:.2f} € ({GEBUEHR_PRO_STUNDE:.2f} € pro Stunde)")

    # Bezahlung durchführen
    gezahlt = bezahlung_durchfuehren(gebuehr)

    # Fahrzeug entfernen
    del fahrzeuge[kennzeichen]
    belegte_plaetze -= 1
    einnahmen = round(einnahmen + gezahlt, 2)

    freie_plaetze = MAX_PARKPLAETZE - belegte_plaetze
    print(f"\n>> Fahrzeug {kennzeichen} hat das Parkhaus verlassen.")
    print(f">> Freie Plätze: {freie_plaetze}/{MAX_PARKPLAETZE}")

    return belegte_plaetze, einnahmen, fahrzeuge