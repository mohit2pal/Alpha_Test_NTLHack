from flask import Flask, request, render_template
from ocr import ocr_image
from NLPmodel import nlp_check
import base64

app = Flask(__name__)

@app.route('/')
def login():
    return 'Hello'

@app.route('/test', methods=['GET', 'POST'])
def test():
    if request.method == 'POST':
        img_base64 = request.get_json()
        # print(img_base64)
        
        decode = open('IMAGE.png', 'wb')
        decode.write(base64.b64decode(img_base64['png']))
    # ans_string = ocr_image()
    # marks = nlp_check(ans_string)
    return render_template('index.html')
    
    
if __name__ == "__main__":
    app.run(debug=True)
