from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/<filename>')
def display_file(filename='file1.txt'):
    # filename = request.args.get('filename','file1.txt')
    start = request.args.get('start')
    end = request.args.get('end')
    print(filename)
    try:
        with open(filename, 'r',encoding="mbcs") as f:
            lines = f.readlines()
            if start is not None and end is not None:
                lines = lines[int(start)-1:int(end)]
            return render_template('file.html', filename=filename, lines=lines)
    except Exception as e:
        return render_template('error.html', error=str(e))

if __name__ == '__main__':
    app.debug=True
    app.run()
