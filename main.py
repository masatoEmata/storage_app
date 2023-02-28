from flask import Flask, render_template, request
from libs.storage.base import gcs_upload
app = Flask(__name__)

BACKET_NAME = 'emata-example-bucket'

@app.route('/upload_svg', methods=['POST', 'GET'])
def upload_svg():
    if request.method == 'GET':
        return render_template('upload_svg.html')
    elif request.method == 'POST':
        cnt = uploader('image/svg+xml')
        return f'{cnt} svg(s) uploaded'

@app.route('/upload_csv', methods=['POST', 'GET'])
def upload_csv():
    if request.method == 'GET':
        return render_template('upload_csv.html')
    elif request.method == 'POST':
        cnt = uploader('text/csv')
        return f'{cnt} csv(s) uploaded'

def uploader(content_type: str):
    files = request.files.getlist('file')
    cnt = 0
    for f in files:
        backet_name = BACKET_NAME
        if f.content_type == content_type:
            gcs_upload(backet_name, f.filename, f.read(), f.content_type)
            cnt += 1
    return cnt

@app.route('/hello')
def root():
    return 'hello'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
