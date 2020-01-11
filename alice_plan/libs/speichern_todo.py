import json

def todo_speichern(was_machen, wann_deadline, zeitlich):
    
    json_daten = data.load_json()
    alle_todos = json_daten.get("todos", {})
        
    todo = {
        "was_machen": was_machen,
        "wann_deadline": wann_deadline,
        "zeitlich": zeitlich
    }
        
    alle_todos['open'][was_machen] = todo
        
    json_daten["todos"] = alle_todos

    data.save_to_json(json_daten)
    return json_daten                        #Json-Datei mit neuer Eingabe wird zurückgegeben
