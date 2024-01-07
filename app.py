import os
import json
from zipfile import ZipFile
from flask import Flask, render_template, request, send_file

from query import query_index
from indexfile import index_file


app = Flask(__name__, template_folder='templates', static_folder='staticFiles')

@app.route('/')
def index():
    return render_template('index.html'), 200

@app.route('/query', methods=['GET'])
def search():
    try:
        word = request.args.get('value')
        with open('index', 'r', encoding='utf-8') as index_file:
            index = json.load(index_file)
        with open('filenames', 'r', encoding='utf-8') as filenames_file:
            filenames = json.load(filenames_file)
        return query_index(word, index, filenames)

    except json.JSONDecodeError:
        return f"Error: JSON files index or filenames decoding problem.", 400
    except:
        return f"Error: The application cannot process this request, please check the data entered.", 400

@app.route('/upload', methods=['POST'])
def upload_files():
    try:
        files = request.files.getlist('file')
        if not files:
            return 'No files selected', 400

        res_files = {}
        for file in files:
            filename = file.filename
            content = file.read().decode('UTF-8')
            res_files[filename] = content
        
        index_file(res_files)
        file_paths = ['index', 'filenames']
        zip_filename = 'index_filenames.zip'
        with ZipFile(zip_filename, 'w') as zip_file:
            for file_path in file_paths:
                zip_file.write(file_path, arcname=os.path.basename(file_path))
        return send_file(zip_filename, as_attachment=True), 200
    except:
        return f"Error: The application cannot process this request, please check the data entered.", 400
    

@app.route('/index_filenames', methods=['POST'])
def upload_config_files():
    try:
        files = request.files.getlist('file')
        if not files:
            return 'No files selected', 400

        for file in files:
            with open(file.filename, 'w', encoding='utf-8') as new_file:
                json.dump(json.loads(file.read().decode('UTF-8')), new_file, indent=2)
        return 'changes applied', 200
    except:
        return f"Error: The application cannot process this request, please check the data entered.", 400

if __name__ == '__main__':
    app.run(debug=True)