from flask import Flask, render_template 

app = Flask(__name__)

@app.route("/monatsplan")
def monatsplan():
    return render_template("index.html")

@app.route("/todo")
def todo():
    return render_template("todo.html")
    
if __name__ == "__main__":
    app.run(debug=True, port=5000)