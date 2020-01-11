"""
Summary:
speichern_termine.py ist für das Erfassen und Ausgeben von Events zuständig
"""

import json
from datetime import date
import datetime
from libs import data

def termin_speichern(category, subject, where, date, time):
    """Summary
    Gibt an, wie die eingegebenen Daten in das json-File gespeichert wird.
    Argumente:
        category(string): Terminkategorie
        subject(string): Was für ein Termin ist es, Beschreibung
        where(string): Wo wird Termin stattfinden
        date(date): An welchem Datum Termin stattfinden wird
        time(time): Um welche Uhrzeit Termin beginnt

    Returns:
        Dictionary: Alle Termindaten werden aus json-File wiedergegeben.
    """
    json_daten = data.load_json()
    alle_termine = json_daten.get("termine", {})
        
    termin = {
        "category": category,
        "subjects": subject,
        "where": where,
        "date": date,
        "time": time
    }
        
    alle_termine[category][str(datetime.datetime.now())] = termin
        
    json_daten["termine"] = alle_termine

    data.save_to_json(json_daten)
    return json_daten                        

def get_events_from_now(termin_daten):
    """Summary
    Bei den gefilterten Terminen nach Kategorie werden jeweils nur Termine wiedergegeben
    die in der Zukunft liegen.

    Argumente:
        termin_daten(dict): Alle Termine

    Returns:
        Alle gefilterten Termine, also sobald event_datetime grösser ist,
        wie das Datum von Heute, werden diese ausgegeben.
    """
    now = datetime.datetime.combine(date.today(),datetime.datetime.now().time())

    filtered_events = {}
    for key, value in termin_daten.items():
        datetime_string = value['date'] + " " + value['time']
        event_datetime = datetime.datetime.strptime(datetime_string, '%Y-%m-%d %H:%M')

        if event_datetime >= now:
            filtered_events[key] = value

    return filtered_events

