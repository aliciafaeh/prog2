from flask import Flask, render_template, redirect, request, url_for
from libs import speichern_termine

app = Flask(__name__)

@app.route("/")
def startseite():
	return render_template('index.html')

@app.route("/monatsplan", methods=['GET', 'POST'])
def monatsplan():
    if request.method == 'POST':
        print(request.form)
        category = request.form['category']
        subject = request.form['subject']
        where = request.form['where']
        date = request.form['date']
        time = request.form['time']
        returned_data = speichern_termine.termin_speichern(category, subject, where, date, time)
    return render_template("index.html")


@app.route("/monatsplan")
def monatsplan_uebersicht():
    termin_daten = speichern_termine.load_json()
    return render_template("index.html", daten=termin_daten)


@app.route("/todo")
def todo():
    return render_template("todo.html")
    
if __name__ == "__main__":
    app.run(debug=True, port=5000)