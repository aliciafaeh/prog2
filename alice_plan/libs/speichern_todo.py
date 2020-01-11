import json

def todo_speichern(was_machen, wann_deadline, zeitlich):
    """
    Summary:
        Hier wird angegeben wie, dass die eingegeben To Do's in die json-File gespeicherten werden.

    Argumente:
        was_machen(string): Was muss gemacht werden
        wann_deadline(date): Bis zu welchem Datum muss es erledigt werden
        zeitlich(time): Bis zu welcher Uhrzeit soll es erledigt werden?

    Returns:
        Dictionary: Alle To Do-Daten werden aus json-File wiedergegeben.

    """
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
    return json_daten                        
