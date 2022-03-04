from flask import Flask, request, render_template, jsonify
from ocr import ocr_image
from NLPmodel import nlp_check
import base64
import json

import os

from Sol_prob import get_response

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login1.html')

@app.route('/test', methods=['GET', 'POST'])
def test():
    if request.method == 'POST':
        img_base64 = request.get_json()
        # print(img_base64)
        
        decode = open('IMAGE.jpg', 'wb')
        decode.write(base64.b64decode(img_base64['png']))
        ans_string = ocr_image()
        
        print(ans_string)
        marks = nlp_check(ans_string)
        print(marks)
        
        dicto = {"marks": marks}
        
        json_object = json.dumps(dicto, indent = 1)
        
        with open("./static/json/marks.json", "w") as outfile:
            outfile.write(json_object)
        
    return render_template('index.html')   
    
@app.route('/predict', methods=['POST'])
def predict():
    text = request.get_json().get("message")
    response = get_response(text)
    print(response)
    print(type(response))
    message = {"answer": response}
    return jsonify(message)
    
if __name__ == '__main__':
    port = os.environ.get("PORT", 5000)
    app.run(debug=False, host="0.0.0.0", port=port)