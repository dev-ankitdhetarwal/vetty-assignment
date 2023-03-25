from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def read_file():
    with open('example.txt', 'r') as f:
        file_contents = f.read()
    return render_template('file_contents.html', contents=file_contents)

if __name__ == '__main__':
    app.run()
