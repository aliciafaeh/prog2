"""Summary

Attributes: 
    app (flask.app.Flask): Der Name meiner App :)

"""
from flask import Flask, render_template, redirect, request, url_for
from libs import speichern_termine, speichern_todo, data

app = Flask("alice_plan")

@app.route("/")
def startseite():
    """
    Summary:
        Zeigt die Startseite an, wenn die url/route '/' ist.
        Auf der Startseite kann man wählen, ob ein Event oder To Do hinzugefügt werden soll.
    

    Returns:
        template: Das HTML 'index.html' wird gerendert mit der Auswahlmöglichkeit
    """
    return render_template('index.html')

@app.route("/addanevent", methods=['GET', 'POST'])
def addanevent():
    """
    Summary:
        Hier kann ein Event hinzugefügt werden.
        Die url/route ist '/addanevent'.

    Returns:
        template: Das HTML 'eventerfassen' wird gerendert, wo Form ausgefüllt werden kann.
        redirect: sobald auf 'add' geklickt wird, wird auf den Router 'monatsplananzeige' verlinkt.
    """
    if request.method == 'POST':
        print(request.form)
        category = request.form['category']
        subject = request.form['subject']
        where = request.form['where']
        date = request.form['date']
        time = request.form['time']
        returned_data = speichern_termine.termin_speichern(category, subject, where, date, time)
        return redirect(url_for('monatsplananzeige'))
    return render_template("eventerfassen.html")

@app.route("/monatsplananzeige")
@app.route("/monatsplananzeige/<categoryfilter>")
def monatsplananzeige(categoryfilter=None):
    """
    Summary:
        Hier werden alle Events angezeigt.
        Die url/route ist '/monatsplananzeige' oder wenn categoryfilter gesetzt: '/monatsplananzeige/<categoryfilter>'.
    
    Argumente:
        categoryfilter: wenn vorhanden, wird er mitgegeben, sonst nicht. --> für filtern von Events.

    Returns:
        if:
            template: Das HTML 'monatsplan' wird mit dem categoryfilter gerendert. Es werden nur Termine der Zukunft angezeigt
        else:
            template: Das HTML 'monatsplan' wird ohne categoryfilter gerendert. Es werden alle erfassten Termine angezeigt
    """
    termin_daten = data.load_json()

    if categoryfilter:
        termine_from_now = speichern_termine.get_events_from_now(termin_daten['termine'][categoryfilter])
        return render_template("monatsplan.html", daten=termine_from_now, categoryfilter=categoryfilter)
    else:
        return render_template("monatsplan.html", daten=termin_daten)


@app.route("/todoerfassen", methods=['GET', 'POST'])
def todoerfassen():
    """
    Summary:
        Hier kann ein To Do hinzugefügt werden.
        Die url/route ist '/todoerfassen'.

    Returns:
        template: Das HTML 'todoerfassen' wird gerendert, wo Form ausgefüllt werden kann.
        redirect: sobald auf 'add' geklickt wird, wird auf den Router 'todosanzeige' verlinkt.
    """
    if request.method == 'POST':
        print(request.form)
        was_machen = request.form['was_machen']
        wann_deadline = request.form['wann_deadline']
        zeitlich = request.form['zeitlich']
        returned_data = speichern_todo.todo_speichern(was_machen, wann_deadline, zeitlich)
        return redirect(url_for('todosanzeige'))

    return render_template("todoerfassen.html")


@app.route("/todosanzeige")
def todosanzeige():
    """
    Summary:
        Hier werden alle Events angezeigt.
        Die url/route ist '/monatsplananzeige' oder wenn categoryfilter gesetzt: '/monatsplananzeige/<categoryfilter>'.
    
    Argumente:
        categoryfilter: wenn vorhanden, wird er mitgegeben, sonst nicht. --> für filtern von Events.

    Returns:
        if:
            template: Das HTML 'monatsplan' wird mit dem categoryfilter gerendert. Es werden nur Termine der Zukunft angezeigt
        else:
            template: Das HTML 'monatsplan' wird ohne categoryfilter gerendert. Es werden alle erfassten Termine angezeigt
    """
    todo_daten = data.load_json()
    return render_template("todosanzeige.html", daten=todo_daten)


@app.route("/todoasdone/<todoId>")
def todoasdone(todoId=None):
    daten = data.load_json()

    todo = daten['todos']['open'][todoId]
    daten['todos']['done'][todoId] = todo
    daten['todos']['open'].pop(todoId,None)

    data.save_to_json(daten)

    return redirect(url_for('todosanzeige'))
    

if __name__ == "__main__":
    app.run(debug=True, port=5000)

