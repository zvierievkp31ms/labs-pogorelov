from flask import Flask, render_template, request
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
        return query_index(word, '', '')
    except:
        return f"Error: The application cannot process this request, please check the data entered.", 400

@app.route('/upload', methods=['POST'])
def upload_files():
    try:
        files = request.files.getlist('file')
        if not files:
            return 'No files selected', 400
        res_files = {}
        index_file(res_files)
    except:
        return f"Error: The application cannot process this request, please check the data entered.", 400

@app.route('/index_filenames', methods=['POST'])
def upload_config_files():
    try:
        files = request.files.getlist('file')
        if not files:
            return 'No files selected', 400
        return 'changes applied', 200
    except:
        return f"Error: The application cannot process this request, please check the data entered.", 400

if __name__ == '__main__':
    app.run(debug=True)