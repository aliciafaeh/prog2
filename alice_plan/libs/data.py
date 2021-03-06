"""
Summary:

data.py ist eine Libary für das lesen und schreiben von der json-File
"""

import json

def load_json():
    """
    Lädt alle Daten von Termine und To Do's aus der json-File

    Argumente:
        data/data.json --> Ist der Path zur File

     Returns:
        Dictionary mit den Daten von "termine" und "todos" wird zurückgegeben. 
        Wenn File noch leer oder nicht vorhanden ist, wird sozusagen leere json-file wiedergegeben.
    """
    
    json_daten = {}
    
    try:
        #Json-File öffnen/lesen
        with open('data/data.json') as open_file:
            json_daten = json.load(open_file)
    
    #wenn data.json noch leer ist
    except FileNotFoundError:     
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
    """
    Summary

    Argumente:
        data/data-json ist der Path zur json-File
        daten (dict): Dictionary von Terminen und Todos
    """
    with open('data/data.json', "w", encoding="utf-8") as open_file:
        json.dump(daten, open_file)

      