from distutils.log import debug
import imp
from flask import Flask,jsonify,request

app = Flask(__name__)

@app.route('/')
def about():
    profile={'name':'Rezha',
          'age':'20',
          'job':'student'}

    return jsonify(profile)

@app.rout('/submit',methods=['POST'])
def input_data():
    data = request.json
    data['info'] = 'data method post'
    # print(data)
    return jsonify(data)

app.run(debug=True)

