import tensorflow as tf
import numpy as np
from tensorflow import keras
from keras.utils import load_img, img_to_array
from keras.applications.resnet50 import preprocess_input
import scipy
import matplotlib.pyplot as plt
import cv2
model = tf.keras.models.load_model(r"model\finalModelWaterPollution.h5")

def getImg():
    img_path = r"testOne.jpg"
    last_layer_weights = model.layers[-1].get_weights()[0]
    img = load_img(img_path,target_size = (224,224))
    img2 = img_to_array(img)
    x = img_to_array(img) 
    x = np.expand_dims(x,axis=0)
    x = preprocess_input(x)
    conv_out ,pred_class = model.predict(x)
    pred_class = np.argmax(pred_class)
    last_layer_weights_for_pred = last_layer_weights[:, pred_class]
    last_conv_output = np.squeeze(conv_out)
    h = int(img2.shape[0]/last_conv_output.shape[0])
    w = int(img2.shape[1]/last_conv_output.shape[1])
    upsampled_last_conv_output = scipy.ndimage.zoom(last_conv_output, (h, w, 1), order=1)
    heat_map = np.dot(upsampled_last_conv_output.reshape((224 * 224, 2048)), 
                     last_layer_weights_for_pred).reshape(img2.shape[0],img2.shape[1])
    normalized_heat_map = (heat_map - np.min(heat_map)) / (np.max(heat_map) - np.min(heat_map))
    heatmap_jet = cv2.applyColorMap(np.uint8(255 * normalized_heat_map), cv2.COLORMAP_JET)
    alpha = 0.5
    heatmap_rgba = cv2.cvtColor(heatmap_jet, cv2.COLOR_BGR2RGBA)
    heatmap_alpha = heatmap_rgba[:, :, 3]
    blended_img = cv2.addWeighted(img2.astype(np.uint8), 1 - alpha, heatmap_rgba[:, :, :3], alpha, 0)

    return blended_img, heatmap_alpha

getImg()