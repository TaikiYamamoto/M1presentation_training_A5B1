# Import packages
from flask import Flask, render_template, request, jsonify
import base64
import json

# Import functions
from img_process import preprocess
from ans_prediction import get_predicted_answer

# Instantiate your own name as "app"
app = Flask(__name__)

# Processing when accessing p5draw
@app.route('/p5draw')
def p5draw():
    return render_template('p5draw.html') # Render p5draw.html

# Processing when accessing sketch.js
@app.route('/sketch.js')
def sketch():
    return render_template('/sketch.js')  # Render sketch.js

# Processing when accessing demotext
@app.route('/demotext', methods = ['POST'])
def demotext():
    img = request.get_json(force=True)
    imgData = preprocess(img)
    
    print('got it!')
    return(str(get_predicted_answer(imgData)))

if __name__ == '__main__':
    # Run this API
    # After running, please access 'localhost:5000/p5draw' with Web Browser.
    app.run(host = '0.0.0.0', port = 5000, threaded = True, debug = True)
