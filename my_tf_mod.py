from tensorflow.keras.models import load_model
import cv2
import numpy as np

quality_model=load_model('local_rotten_lr2_final.h5')
clf_model=load_model('local_fruit_final.h5')


# reads image from path and add extra 1 dim to it.
def preprocess(path):
    img=cv2.imread(path)
    img=cv2.resize(img,(100,100))
    img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    img=img.astype('float64')

    return np.expand_dims(img,axis=0)


# return [prob_for_fresh, prob_for_rotten]
def check_rotten(img):
    return [quality_model.predict(img)[0][0],1-quality_model.predict(img)[0][0]]


# return dict... {'apple':prob, 'banana':prob, 'orange':prob}
def classify_fruit(img):
    fru_dict={}
    fru_dict['apple']=clf_model.predict(img)[0][0]
    fru_dict['banana']=clf_model.predict(img)[0][1]
    fru_dict['orange']=clf_model.predict(img)[0][2]

    return fru_dict
