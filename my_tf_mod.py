from tensorflow.keras.models import load_model
import numpy as np
from tensorflow.keras.preprocessing import image
from PIL import Image, ImageFile
from io import BytesIO

quality_model=load_model('local_rotten_lr2_final.h5')
clf_model=load_model('local_fruit_final.h5')


# reads frfom file object
# return array of original uploaded image and 1x100x100x3 processed image
def preprocess(file):
    ImageFile.LOAD_TRUNCATED_IMAGES =False
    org_img=Image.open(BytesIO(file.read()))
    org_img.load()
    img=org_img.resize((100,100), Image.ANTIALIAS)

    img=image.img_to_array(img)
    org_img=image.img_to_array(org_img)
    return org_img, np.expand_dims(img,axis=0)


# return [prob_for_fresh, prob_for_rotten]
def check_rotten(img):
    return [round(100*quality_model.predict(img)[0][0],3),round(100*(1-quality_model.predict(img)[0][0]),3)]


# return dict... {'apple':prob, 'banana':prob, 'orange':prob}
def classify_fruit(img):
    fru_dict={}
    fru_dict['apple']=round(clf_model.predict(img)[0][0]*100,4)
    fru_dict['banana']=round(clf_model.predict(img)[0][1]*100,4)
    fru_dict['orange']=round(clf_model.predict(img)[0][2]*100,4)

    for value in fru_dict:
     if fru_dict[value]<=0.001:
        fru_dict[value]=0.00

    return fru_dict
