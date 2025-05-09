from flask import Flask, send_from_directory, jsonify, render_template_string, request
from flask_socketio import SocketIO, emit
import os, json

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    with open('index.html') as f:
        return render_template_string(f.read())

@app.route('/control')
def control():
    with open('control.html') as f:
        return render_template_string(f.read())

@app.route('/content.json')
def content():
    with open('content.json') as f:
        return jsonify(json.load(f))

@app.route('/update_content', methods=['POST'])
def update_content():
    new_content = request.json
    with open('content.json', 'w') as f:
        json.dump(new_content, f, indent=2)
    socketio.emit('content_update', new_content)
    return {'status': 'updated'}

@app.route('/media/<path:filename>')
def media(filename):
    return send_from_directory('media', filename)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
