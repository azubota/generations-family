import os
from flask import Flask, jsonify

app = Flask(__name__)
  
members = [{
                "id":1,
                "name":"john",
                "lastname": "Doe",
                "age":"33 Years old",
                "gender":"Male",
                "lucky_numbers":[7, 13, 22]
                },
            {
                "id":2,
                "name":"jane",
                "lastname": "Doe",
                "age":"35 Years old",
                "gender":"female",
                "lucky_numbers":[10, 14, 3]
                },
             {
                "id":3,
                "name":"jimmy",
                "lastname": "Doe",
                "age":"5 Years old",
                "gender":"Male",
                "lucky_numbers":[1]
                }
        ]


@app.route('/',methods=['GET'])

def themembers():
    return jsonify (members)

@app.route('/luckynumbers',methods=['GET'])


def theluckynumber():
    theLuckyNumbers = map(lambda obj: obj['lucky_numbers'],members)
    luckyArray = list(theLuckyNumbers)
    return jsonify (luckyArray)
    
@app.route('/sumluckynumbers',methods=['GET'])

def thesum():
    luckysum = 0
    for i in members:
     luckysum += sum(i["lucky_numbers"])
     return jsonify (luckysum)
      
      
@app.route('/members/<int:member_id>',methods=['GET'])

def getmember(member_id):
    for i in members:
        if i['id'] == member_id:
           return jsonify (i)
        
    
    

    

  
  
app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))