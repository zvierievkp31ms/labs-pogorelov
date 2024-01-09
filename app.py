import os
import json
from flask import Flask, render_template, request

from query import query_index
from indexfile import index_file

app = Flask(__name__, template_folder='templates', static_folder='staticFiles')
dir_path = 'input_files'
result_dir = 'results/'

@app.route('/')
def index():
    sub_dir_names = os.listdir(dir_path)
    dir_options = {}
    for sub_dir in sub_dir_names:
        files = os.listdir(dir_path + '/' + sub_dir)
        dir_options[sub_dir] = files
    f = open('result.json')
    index_options = json.load(f)
    f.close()
    return render_template('index.html', dir_options=dir_options, index_options=index_options), 200

@app.route('/input', methods=['POST'])
def input_part():
    try:
        data = request.get_json()
        index_filename = data['index']
        filenames_filename = data['filenames']
        dir_name = data['dir']
        files = os.listdir(dir_path + '/' + dir_name)
        files = [ dir_path + '/' + dir_name + '/' + f for f in files]
        index_options = index_file(files, result_dir + index_filename, result_dir + filenames_filename)
        return index_options, 200
    except Exception as e:
        if e.args[0]  == 'filename exist with other index':
            return f"Error: Filename |{filenames_filename}| exist with other index, please check the data entered.", 400
        else:
            return "Error: The application cannot process this request, please check the data entered.", 400

@app.route('/query', methods=['GET'])
def search():
    try:
        index_filename = request.args.get('index')
        filenames_filename = request.args.get('filenames')
        with open('result.json', 'r', encoding='utf-8') as result_file:
            data = json.load(result_file)

        if index_filename not in data:
            return "Error: Not correct index file name, value not exist", 400
        if data[index_filename] != filenames_filename:
            return "Error: Not correct filenames file name", 400
        
        word = request.args.get('value')
        with open(result_dir + index_filename, 'r', encoding='utf-8') as index_file:
            index = json.load(index_file)
        with open(result_dir + filenames_filename, 'r', encoding='utf-8') as filenames_file:
            filenames = json.load(filenames_file)
        return query_index(word, index, filenames)
    except json.JSONDecodeError:
        return f"Error: JSON files index or filenames decoding problem.", 400
    except Exception as e:
        return f"Error: The application cannot process this request, please check the data entered.", 400

if __name__ == '__main__':
    app.run(debug=True)