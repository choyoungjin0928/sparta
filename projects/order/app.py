from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb://agapao:5561@3.34.98.182', 27017)
db = client.dbsparta              # 'dbsparta'라는 이름의 db를 만듭니다.

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')

## API 역할을 하는 부분
@app.route('/save', methods=['POST'])
def save():
    me_receive = request.form['me_give']
    you_receive = request.form['you_give']
    result_receive = request.form['result_give']

    doc = {
        'Me':me_receive,
        'You':you_receive,
        'Result':result_receive,
    }

    db.match.insert_one(doc)

    return jsonify({'result':'success', 'msg': '저장이 완료되었습니다'})

@app.route('/show', methods=['GET'])
def show():
    orders = list(db.match.find({},{'_id':0}))
    return jsonify({'result':'success', 'all_orders':orders})

if __name__ == '__main__':
   app.run('localhost',port=5008,debug=True)