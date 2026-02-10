# storage.py – Laden und Speichern des Parkhaus-Zustands (CSV)

import csv
import os
from config import CSV_DATEI


def zustand_speichern(belegte_plaetze, einnahmen, fahrzeuge):
    """
    Speichert den aktuellen Zustand des Parkhauses in eine CSV-Datei.
    - belegte_plaetze: int
    - einnahmen: float
    - fahrzeuge: dict mit {kennzeichen: einfahrtszeit_als_timestamp}
    """
    with open(CSV_DATEI, mode="w", newline="", encoding="utf-8") as datei:
        writer = csv.writer(datei, delimiter=";")
        writer.writerow(["belegte_plaetze", "einnahmen"])
        writer.writerow([belegte_plaetze, f"{einnahmen:.2f}"])
        writer.writerow(["kennzeichen", "einfahrtszeit"])
        for kennzeichen, zeit in fahrzeuge.items():
            writer.writerow([kennzeichen, zeit])
    print(">> Zustand wurde gespeichert.")


def zustand_laden():
    """
    Lädt den Zustand aus der CSV-Datei.
    Gibt zurück: (belegte_plaetze, einnahmen, fahrzeuge_dict)
    Falls keine Datei existiert, werden Standardwerte zurückgegeben.
    """
    if not os.path.exists(CSV_DATEI):
        print(">> Keine gespeicherte Datei gefunden. Starte mit Standardwerten.")
        return 0, 0.0, {}

    with open(CSV_DATEI, mode="r", encoding="utf-8") as datei:
        reader = csv.reader(datei, delimiter=";")
        zeilen = list(reader)

    try:
        belegte_plaetze = int(zeilen[1][0])
        einnahmen = float(zeilen[1][1])
        fahrzeuge = {}
        # Ab Zeile 3 (Index 3) stehen die Fahrzeugdaten
        for i in range(3, len(zeilen)):
            if len(zeilen[i]) == 2:
                kennzeichen = zeilen[i][0]
                einfahrtszeit = float(zeilen[i][1])
                fahrzeuge[kennzeichen] = einfahrtszeit
        print(">> Gespeicherter Zustand wurde geladen.")
        return belegte_plaetze, einnahmen, fahrzeuge
    except (IndexError, ValueError) as e:
        print(f">> Fehler beim Laden der Datei: {e}")
        print(">> Starte mit Standardwerten.")
        return 0, 0.0, {}