import json

def todo_speichern(was_machen, wann_deadline, zeitlich):
    
    json_daten = load_json()
    alle_todos = json_daten.get("todos", {})
        
    todo = {
        "was_machen": was_machen,
        "wann_deadline": wann_deadline,
        "zeitlich": zeitlich,
    }
        
    alle_todos[was_machen] = todo
        
    json_daten["todos"] = alle_todos

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