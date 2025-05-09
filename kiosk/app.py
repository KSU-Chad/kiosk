
from flask import Flask, request, render_template, redirect, url_for
import json
import os
from werkzeug.utils import secure_filename

app = Flask(__name__, static_url_path='/static', static_folder='.')

MEDIA_FOLDER = 'media'
PHOTO_EXTS = ('.png', '.jpg', '.jpeg', '.webp')
VIDEO_EXTS = ('.mp4', '.mov', '.avi')

@app.route('/')
def index():
    with open(os.path.join(MEDIA_FOLDER, 'text.json')) as f:
        content = json.load(f)
    return render_template("templates/main_template.html", content=content)

@app.route('/update', methods=['POST'])
def update():
    category = request.json.get("category", "default")
    with open(os.path.join(MEDIA_FOLDER, 'text.json'), 'w') as f:
        json.dump({"category": category, "text": f"Showing {category} info"}, f)
    return "OK"

@app.route('/admin')
def admin():
    return render_template("templates/upload.html")

@app.route('/upload', methods=['POST'])
def upload_file():
    category = request.form.get('category', 'default')
    file = request.files['media_file']
    filename = secure_filename(file.filename)

    ext = os.path.splitext(filename)[1].lower()
    if ext in PHOTO_EXTS:
        save_path = os.path.join(MEDIA_FOLDER, 'photos', filename)
    elif ext in VIDEO_EXTS:
        save_path = os.path.join(MEDIA_FOLDER, 'videos', filename)
    else:
        return "Unsupported file type", 400

    file.save(save_path)
    return redirect(url_for('admin'))

if __name__ == '__main__':
    os.makedirs(os.path.join(MEDIA_FOLDER, 'photos'), exist_ok=True)
    os.makedirs(os.path.join(MEDIA_FOLDER, 'videos'), exist_ok=True)
    app.run(host='0.0.0.0', port=5000)
