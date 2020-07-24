import sqlite3

from flask import Flask, render_template, request


app = Flask(__name__, static_folder='.', static_url_path='')
#app = Flask(__name__)
val = 0

@app.route('/')
def response_test():
    return render_template('index.html')
#    return app.send_static_file('index.html')

@app.route('/send/', methods=['POST'])
def send():
#    code = request.args.get('code')
    code = request.form['data']
    print("Barcode is : %s" % code)
    return render_template('code.html', code=code)

#@app.route('/send/<barcode>')
#def send(barcode):
#    print("Barcode is : %s" % barcode)
#    return render_template('code.html', code=barcode)
#    return "Barcode is : %s" % barcode

@app.route('/result')
def result():
    return render_template('code.html')

# @app.before_request
# def before_request():
#     g.db = connect_db()
#
# @app.teardown_request
# def teardown_request(exception):
#     db  = getattr(g, 'db', None)
#     if db is not None:
#         db.close()
#
# def connect_db():
#     return sqlite3.connect(app.config['DATABASE'])


if __name__ == '__main__':
    app.run('0.0.0.0',port=5004,debug=True)


