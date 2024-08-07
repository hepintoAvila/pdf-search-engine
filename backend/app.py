from flask import Flask, request
from werkzeug.utils import secure_filename
import os
from utils.pdf_utils import extract_text_from_pdf
from config.elasticsearch_config import index_document

app = Flask(__name__)

@app.route('/api/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part', 400
    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400
    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join('/path/to/save', filename)
        file.save(file_path)
        pdf_text = extract_text_from_pdf(file_path)
        index_document(filename, pdf_text)
        return 'File successfully uploaded', 200

if __name__ == '__main__':
    app.run(debug=True)
