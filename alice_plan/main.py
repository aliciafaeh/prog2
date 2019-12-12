from flask import Flask, render_template, redirect, request, url_for
from libs import speichern_termine

app = Flask(__name__)

@app.route("/")
def startseite():
	return render_template('index.html')

@app.route("/addanevent", methods=['GET', 'POST'])
def addanevent():
    if request.method == 'POST':
        print(request.form)
        category = request.form['category']
        subject = request.form['subject']
        where = request.form['where']
        date = request.form['date']
        time = request.form['time']
        returned_data = speichern_termine.termin_speichern(category, subject, where, date, time)
    return render_template("eventerfassen.html")


@app.route("/monatsplananzeige")
def monatsplananzeige():
    termin_daten = speichern_termine.load_json()
    return render_template("monatsplan.html", daten=termin_daten)


@app.route("/todo", methods=['GET', 'POST'])
def todo():
    if request.method == 'POST':
        print(request.form)
        category = request.form['category']
        was_machen = request.form['was_machen']
        wann_deadline = request.form['wann_deadline']
        zeitlich = request.form['zeitlich']
        returned_data = speichern_todo.todo_speichern(category, subject, where, date, time)
    return render_template("todo.html")


@app.route("/todos")
def todos():
    todo_daten = speichern_todos.load_json()
    return render_template("todos.html", daten=todo_daten)

    
if __name__ == "__main__":
    app.run(debug=True, port=5000)

