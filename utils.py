# utils.py – Hilfsfunktionen für das Parkhaus

from config import MAX_PARKPLAETZE


def status_anzeigen(belegte_plaetze, einnahmen):
    """Zeigt den aktuellen Parkhaus-Status an."""
    freie_plaetze = MAX_PARKPLAETZE - belegte_plaetze
    print("\n--- PARKHAUS STATUS ---")
    print(f"Freie Parkplätze:  {freie_plaetze}")
    print(f"Belegte Parkplätze: {belegte_plaetze}")
    print(f"Einnahmen: {einnahmen:.2f} €")
    print("------------------------")


def detaillierter_report(belegte_plaetze, einnahmen, fahrzeuge):
    """Zeigt einen detaillierten Statusbericht (für Wartungsmodus)."""
    import time
    freie_plaetze = MAX_PARKPLAETZE - belegte_plaetze

    print("\n===== DETAILLIERTER STATUSBERICHT =====")
    print(f"Maximale Parkplätze: {MAX_PARKPLAETZE}")
    print(f"Freie Parkplätze:    {freie_plaetze}")
    print(f"Belegte Parkplätze:  {belegte_plaetze}")
    print(f"Einnahmen:           {einnahmen:.2f} €")
    print(f"Anzahl Fahrzeuge:    {len(fahrzeuge)}")

    if fahrzeuge:
        print("\n-- Geparkte Fahrzeuge --")
        for kennzeichen, einfahrtszeit in fahrzeuge.items():
            dauer = (time.time() - einfahrtszeit) / 3600
            zeit_str = time.strftime("%d.%m.%Y %H:%M:%S", time.localtime(einfahrtszeit))
            print(f"  {kennzeichen}: Einfahrt {zeit_str} (seit {dauer:.2f} Std.)")
    else:
        print("\n>> Keine Fahrzeuge im Parkhaus.")

    print("========================================")


def hauptmenue_anzeigen():
    """Zeigt das Hauptmenü an."""
    print("\n========== SMART PARKING SYSTEM ==========")
    print("  enter       – Fahrzeug einfahren")
    print("  exit        – Fahrzeug ausfahren")
    print("  status      – Parkhaus-Status anzeigen")
    print("  maintenance – Wartungsmodus")
    print("  off         – System ausschalten")
    print("==========================================")


def wartungsmenue_anzeigen():
    """Zeigt das Wartungsmenü an."""
    print("\n----- WARTUNGSMODUS -----")
    print("  empty      – Parkhaus leeren")
    print("  take money – Einnahmen entnehmen")
    print("  report     – Detaillierter Bericht")
    print("  exit       – Wartungsmodus verlassen")
    print("-------------------------")