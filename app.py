import logging
from flask import Flask, render_template, request, abort
import chardet
import os

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.DEBUG)

app.add_url_rule("/<string:filename>", endpoint="index",
                 defaults={"defaultFile": "file1.txt"})

app.add_url_rule("/", endpoint="index",
                 defaults={"defaultFile": "file1.txt"})


@app.endpoint('index')
def display_file(filename=None, defaultFile=None):

    filename = filename if filename else defaultFile

    start = request.args.get('start')
    end = request.args.get('end')
    print("filename: %s", filename)
    try:
        if not os.path.exists(filename):
            abort(404)
        with open(filename, 'rb') as f:
            file_encoding = chardet.detect(f.read())['encoding']
        print("FileEncoding: %s", file_encoding)
        with open(filename, 'r', encoding=file_encoding) as f:
            lines = f.readlines()
            if start is not None and end is not None:
                lines = lines[int(start)-1:int(end)]
            return render_template('file.html', filename=filename, lines=lines)
    except Exception as e:
        logging.exception("Error while processing file.")
        return render_template('error.html', error=str(e))


if __name__ == '__main__':
    app.run(debug=True, port=5001)