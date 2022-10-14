import shutil
from deep_classifier.entity.config_entity import Model_Prediction_Service_Config
import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

"""
            Deep_Learning_Classifier_Project
"""
model= tf.keras.models.load_model("prediction_service\model.h5")
uploded_file=st.file_uploader("Choose a File")
if uploded_file is not None:
    image=Image.open(uploded_file)
    img=image.resize((224,224))
    img_array=np.array(img)
    img_array=np.expand_dims(img_array,axis=0)
    result=model.predict(img_array)

    arg_max_index=np.argmax(result,axis=1)

    if arg_max_index[0]==0:
        st.image(image, caption="predicted: cat")
    else:
        st.image(image, caption='predicted: dog')
