from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('mongodb://agapao:5561@3.34.98.182', 27017)
db = client.aunae

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index1.html')

## API 역할을 하는 부분
@app.route('/save', methods=['POST'])
def save():
    name_receive = request.form['name_give']
    age_receive = request.form['age_give']
    phone_receive = request.form['phone_give']

    doc = {
        'name':name_receive,
        'age':age_receive,
        'phone':phone_receive
    }

    db.solution.insert_one(doc)

    return jsonify({'result':'success', 'msg': '저장이 완료되었습니다'})

@app.route('/show', methods=['GET'])
def show():
    orders = list(db.solution.find({},{'_id':0}))
    return jsonify({'result':'success', 'all_orders':orders})

if __name__ == '__main__':
    app.run('0.0.0.0',port=5001,debug=True)