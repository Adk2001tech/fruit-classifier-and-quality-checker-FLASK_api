import os
import sys
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

from tensorflow.keras.models import load_model
import cv2
import numpy as np
import my_tf_mod

UPLOAD_FOLDER = 'static'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/Prediction', methods=['GET','POST'])
def pred():
    if request.method=='POST':
     if request.method == 'POST':
         file = request.files['file']
         filename = secure_filename(file.filename)
         file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
         file.save(file_path)
         print(file_path)
         img=my_tf_mod.preprocess(file_path)
         rotten=my_tf_mod.check_rotten(img)
         fruit_dict=my_tf_mod.classify_fruit(img)
         print(fruit_dict)


    return render_template('Pred.html', path='../static/'+filename, fruit_dict=fruit_dict, rotten=rotten)

if __name__=='__main__':
    app.run(debug=True)
