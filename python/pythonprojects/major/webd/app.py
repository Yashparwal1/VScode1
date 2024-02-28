# app.py (Flask application)

from flask import Flask, render_template, request, send_file
from PIL import Image
from stegano import lsb
import os

app = Flask(__name__)

# Home page
@app.route('/')
def index():
    return render_template('index.html')

# Perform hide or extract operation
@app.route('/operation', methods=['POST'])
def operation():
    if 'file' not in request.files:
        return render_template('index.html', error='No file part')

    file = request.files['file']

    if file.filename == '':
        return render_template('index.html', error='No selected file')

    operation_type = request.form.get('operation_type')
    message = request.form.get('message')

    if not operation_type or not message:
        return render_template('index.html', error='Operation type or message missing')

    try:
        image_path = f"static/uploads/{file.filename}"
        file.save(image_path)

        if operation_type == 'hide':
            secret = lsb.hide(image_path, message)
            
            # Convert image to RGB mode before saving
            secret = secret.convert('RGB')
            
            secret_path = f"static/uploads/hidden_{os.path.basename(image_path)}"
            secret.save(secret_path)
            return render_template('index.html', success_hide='Message hidden successfully', secret_path=secret_path)
        elif operation_type == 'extract':
            clear_message = lsb.reveal(image_path)
            return render_template('index.html', success_extract='Message extracted successfully', extracted_message=clear_message)
    except Exception as e:
        return render_template('index.html', error=str(e))

if __name__ == "__main__":
    app.run(debug=True)
