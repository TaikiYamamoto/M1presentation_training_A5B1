# Import packages
from flask import Flask, render_template, request

# Import functions
from img_process import preprocess
from ans_prediction import get_predicted_answer

# Instantiate your own name as "app"
app = Flask(__name__)

# Processing when accessing / (index)

# Processing when accessing /p5draw

# Processing when accessing /sketch.js

# Processing when accessing /demo_prediction with POST Method

if __name__ == '__main__':
    # Run this API
    # After running, please access 'localhost:5000/' with Web Browser.
    app.run(host = '0.0.0.0', port = 5000, threaded = True, debug = True)
