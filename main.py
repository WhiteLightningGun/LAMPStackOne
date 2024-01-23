from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from database import queries
from flask_cors import CORS, cross_origin

load_dotenv()

app = Flask(__name__)
# This will enable CORS for all routes from localhost
CORS(app, origins=["http://localhost:3000", "localhost/:1"])


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


@app.route('/api/hello')
def hello_world():
    return 'Hello World from the Flask API!'


@app.route('/api/entries')
def get_all_entries():
    entries = queries.GetAllEntries()
    return {"entries": entries}


@app.route('/api/newtodo', methods=['POST'])
def new_todo():
    data = request.get_json()
    title = data.get('todoInput', None)
    if title is None:
        return jsonify({'error': 'No title provided'}), 400
    queries.InsertNewEntry(title, 0)
    return jsonify({'message': 'New todo created'}), 201


@app.route('/api/deletetodo', methods=['POST'])
def delete_todo():
    data = request.get_json()  # get data from post request, will be an integer
    if data is None:
        return jsonify({'error': 'error'}), 400
    queries.DeleteTodoEntry(data)
    return jsonify({'message': 'New todo deleted'}), 201


if __name__ == "__main__":
    app.run(debug=True)
