import lsrch
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/findpath')
def findpath():
    start = request.args.get('start')
    end = request.args.get('end')
    t = lsrch.main(start, end)
    if type(t) is None or type(t) is str:
        return render_template('altpath.html', prin=0, len=1, pages=None)
    return render_template('altpath.html', prin=1, len=len(t), pages=t)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
