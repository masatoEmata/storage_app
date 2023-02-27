import datetime
from flask import Flask, render_template, request
from libs.file.crud import save_svg
app = Flask(__name__)
import os


@app.route('/upload_svg', methods=['POST', 'GET'])
def upload_svg():
    if request.method == 'GET':
        return render_template('upload_svg.html')
    elif request.method == 'POST':
        files = request.files.getlist('file')
        for f in files:
            pwd = os.path.abspath(os.path.dirname(__file__))
            dir = os.path.join(pwd, 'data/svg/sample_font')
            file_path = os.path.join(dir, f.filename)
            save_svg(file_path, f.read().decode())
        return 'uploaded'

@app.route('/')
def root():
    dummy_times = [datetime.datetime(2018, 1, 1, 10, 0, 0),
                   datetime.datetime(2018, 1, 2, 10, 30, 0),
                   datetime.datetime(2018, 1, 3, 11, 0, 0),
                   ]

    return render_template('index.html', times=dummy_times)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
