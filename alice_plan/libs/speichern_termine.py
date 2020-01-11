import json
from datetime import date
import datetime
from libs import data

def termin_speichern(category, subject, where, date, time):
    
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
    return json_daten                        #Json-Datei mit neuer Eingabe wird zurückgegeben

def get_events_from_now(termin_daten):
    now = datetime.datetime.combine(date.today(),datetime.datetime.now().time())

    filtered_events = {}
    for key, value in termin_daten.items():
        datetime_string = value['date'] + " " + value['time']
        event_datetime = datetime.datetime.strptime(datetime_string, '%Y-%m-%d %H:%M')

        if event_datetime >= now:
            filtered_events[key] = value

    return filtered_events

