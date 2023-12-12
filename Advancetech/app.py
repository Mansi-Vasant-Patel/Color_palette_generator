from os import name
import numpy as np
from flask import Flask, request, jsonify, render_template
import urllib.request
from Advancetech import app
import pandas as pd
import random
import pickle
import sklearn
import joblib
from sklearn.cluster import KMeans

from matplotlib.colors import to_hex

# Import libraries

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

from imageio import imread

from skimage.transform import resize

from sklearn.cluster import KMeans

from matplotlib.colors import to_hex

import os
import random

import io

import joblib



################################################################

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload')
def home2():
    return render_template('landingpage.html')

@app.route('/predict', methods = ['POST'])
def predict():

    path = r"Blue"

    files = os.listdir(path)
    d = random.choice(files)

    filepath = path + '/' + d

    img = imread(filepath)

    img = resize(img, (200, 200))

    data = pd.DataFrame(img.reshape(-1, 3),
                        columns=['R', 'G', 'B'])

    kmeans = KMeans(n_clusters=5,
                    random_state=0)

    # Fit and assign clusters
    data['Cluster'] = kmeans.fit_predict(data)
    palette = kmeans.cluster_centers_
    palette_list = list()
    for color in palette:
        palette_list.append([[tuple(color)]])
    # Show color palette
    col = list()
    for color in palette_list:
        print(to_hex(color[0][0]))
        col.append(to_hex(color[0][0]))
    return render_template('index.html', colour1 = col[0], colour2 = col[1], colour3 = col[2], colour4 = col[3], colour5 = col[4])

@app.route('/upload_img', methods = ['POST'])
def upload_image():
    image = request.files['file']

    img = imread(image)
  
    img = resize(img, (200, 200))

    data = pd.DataFrame(img.reshape(-1, 3),
                        columns=['R', 'G', 'B'])

    kmeans = KMeans(n_clusters=5,
                    random_state=0)

    # Fit and assign clusters
    data['Cluster'] = kmeans.fit_predict(data)
    palette = kmeans.cluster_centers_
    palette_list = list()
    for color in palette:
        palette_list.append([[tuple(color)]])
    # Show color palette
    col = list()
    for color in palette_list:
        print(to_hex(color[0][0]))
        col.append(to_hex(color[0][0]))
    return render_template('landingpage.html', colour1 = col[0], colour2 = col[1], colour3 = col[2], colour4 = col[3], colour5 = col[4], img = image)

if __name__=='__main__':
   app.run(debug=True)