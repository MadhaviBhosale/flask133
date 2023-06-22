from flask import Flask

app = Flask(__name__)

@app.route("/")
def first_flask():
    
    return 'Python is fun'

app.run()