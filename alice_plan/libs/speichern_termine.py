import json

def termin_speichern(category, subject, where, date, time):
    
    json_daten = load_json()
    alle_termine = json_daten.get("termine", {})
        
    termin = {
        "category": category,
        "subjects": subject,
        "where": where,
        "date": date,
        "time": time
    }
        
    alle_termine[category] = termin
        
    json_daten["termine"] = alle_termine

    save_to_json(json_daten)
    return json_daten                        #Json-Datei mit neuer Eingabe wird zurückgegeben

def load_json():
    json_daten = {}
    try:
        with open('data/data.json') as open_file:    #Json-Datei öffnen/lesen
            json_daten = json.load(open_file)
    
    except FileNotFoundError:                       #wenn json.datei noch leer ist     
        print("File not found")

    return json_daten

def save_to_json(daten):
    with open('data/data.json', "w") as open_file:
        json.dump(daten, open_file)




# youtube-Tutorial dazu: https://www.youtube.com/watch?v=drord9gbr3Y