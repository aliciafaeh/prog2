import json

def load_json():
    json_daten = {}
    try:
        with open('data/data.json') as open_file:    #Json-Datei öffnen/lesen
            json_daten = json.load(open_file)
    
    except FileNotFoundError:                       #wenn json.datei noch leer ist     
        json_daten = {
		  "termine": {
		    "Work": {
		     
		    },
		    "Lectures": {
		      
		    },
		    "LeisureTime": {
		      
		    },
		    "StudyTime": {
		      
		    },
		    "Exams": {
		      
		    }
		  },
		  "todos": {
		    "open": {
		      
		    },
		    "done": {
		      
		    }
		  }
		}

    return json_daten

def save_to_json(daten):
    with open('data/data.json', "w", encoding="utf-8") as open_file:
        json.dump(daten, open_file)