import json

def load_json():
<<<<<<< HEAD
    """
    Lädt alle Daten von Termine und To Do's aus der json-File

    Argumente:
        data/data.json --> Ist der Path zur File

    Returns:
        Dictionary mit den Daten von "termine" und "todos" wird zurückgegeben. 
        Wenn File noch leer oder nicht vorhanden ist, wird sozusagen leere json-file wiedergegeben.
    """
    
=======
>>>>>>> parent of 320547a... data.py kommentiert
    json_daten = {}
    
    try:
<<<<<<< HEAD
        #Json-File öffnen/lesen
        with open('data/data.json') as open_file:
            json_daten = json.load(open_file)
    
    #wenn data.json noch leer ist
    except FileNotFoundError:     
=======
        with open('data/data.json') as open_file:    #Json-Datei öffnen/lesen
            json_daten = json.load(open_file)
    
    except FileNotFoundError:                       #wenn json.datei noch leer ist     
>>>>>>> parent of 320547a... data.py kommentiert
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
<<<<<<< HEAD
	"""
	Summary

	Argumente:
		data/data-json ist der Path zur json-File
		daten (dict): Dictionary von Terminen und Todos
	"""
=======
>>>>>>> parent of 320547a... data.py kommentiert
    with open('data/data.json', "w", encoding="utf-8") as open_file:
        json.dump(daten, open_file)