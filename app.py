from flask import Flask, render_template, request
from query import query_index
from indexfile import index_file
import os

app = Flask(__name__, template_folder='templates', static_folder='staticFiles')

@app.route('/')
def index():
    dir_options =[]
    index_options=[]
    return render_template('index.html', dir_options=dir_options, index_options=index_options), 200

@app.route('/query', methods=['GET'])
def search():
    try:
        word = request.args.get('value')
        return query_index(word, '', '')
    except:
        return f"Error: The application cannot process this request, please check the data entered.", 400

@app.route('/input', methods=['POST'])
def input_part():
    try:
        data = request.get_json()
        index_filename = data['index']
        filenames_filename = data['filenames']
        dir_name = data['dir']
        files = os.listdir(dir_name)
        index_file(files, index_filename, filenames_filename)
        return 'changes applied', 200
    except:
        return f"Error: The application cannot process this request, please check the data entered.", 400

if __name__ == '__main__':
    app.run(debug=True)