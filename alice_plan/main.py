from flask import Flask

app = Flask(__name__)

@app.route("/monatsplan")
def monatsplan():
    return "Hello, World!"

@app.route("/todo")
def todo():
    return "Hello, Salvador"
    
if __name__ == "__main__":
    app.run(debug=True, port=5000)