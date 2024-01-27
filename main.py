import sys
import logging

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

import os
from flask import Flask, render_template, request, jsonify, send_from_directory
from flask_socketio import SocketIO, send, emit
from dotenv import load_dotenv
from database import queries
from flask_cors import CORS

load_dotenv()

app = Flask(__name__, static_folder='react-client/build')

socketio = SocketIO(app)

# cors_allowed_origins="http://localhost:3000"
# This will enable CORS for all routes from localhost
CORS(app, origins=["http://localhost:3000", "localhost/:1"])

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')


@app.template_filter('done')
def IsItDoneYet(input):
    if input == 1:
        return "Done"
    elif input == 0:
        return "Not Done"
    else:
        return "In Progress..."


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
    entries = queries.GetAllEntries()
    socketio.emit('database_updated', {'entries': entries})
    return jsonify({'message': 'New todo created'}), 201


@app.route('/api/deletetodo', methods=['POST'])
def delete_todo():
    data = request.get_json()  # get data from post request, will be an integer
    if data is None:
        return jsonify({'error': 'error'}), 400
    queries.DeleteTodoEntry(data)
    entries = queries.GetAllEntries()
    socketio.emit('database_updated', {'entries': entries})
    return jsonify({'message': 'New todo deleted'}), 201


if __name__ == "__main__":
    app.run(debug=True)
