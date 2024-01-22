from flask import Flask, render_template
from dotenv import load_dotenv
from database import queries
from flask_cors import CORS

load_dotenv()

app = Flask(__name__)
# This will enable CORS for all routes from localhost:8000
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})


@app.route('/')
def home():
    entries = queries.GetAllEntries()
    return render_template('index.html', entries=entries)


@app.template_filter('done')
def IsItDoneYet(input):
    if input == 1:
        return "Done"
    elif input == 0:
        return "Not Done"
    else:
        return "In Progress..."


if __name__ == "__main__":
    app.run(debug=True)
