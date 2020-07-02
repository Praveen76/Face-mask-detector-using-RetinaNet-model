# -*- coding: utf-8 -*-
"""
Created on Fri May 29 13:03:22 2020

@author: PraveenKumar
"""
!git clone https://github.com/fizyr/keras-retinanet.git

%cd keras-retinanet/
!pip install .
!python setup.py build_ext --inplace


import numpy as np

import os, sys, random
import xml.etree.ElementTree as ET
import pandas as pd
from os import listdir
from os.path import isfile, join
import matplotlib.pyplot as plt
from PIL import Image
import requests
import urllib


from keras_retinanet.utils.visualization import draw_box, draw_caption

pngPath='../Img_data/'
annotPath='../annotations/'

data=pd.DataFrame(columns=['fileName','xmin','ymin','xmax','ymax','class'])


os.getcwd()

#read All files
allfiles = [f for f in listdir(annotPath) if isfile(join(annotPath, f))] 
#Read all pdf files in images and then in text and store that in temp folder
for file in allfiles:
    print(file)
    if (file.split(".")[1]=='xml'):
        fileName='../Img_data/'+file.replace(".xml",'.png')
        tree = ET.parse(annotPath+file)
        root = tree.getroot()
        for obj in root.iter('object'):
            cls_name = obj.find('name').text
            print(file)
            xml_box = obj.find('bndbox')
            xmin = xml_box.find('xmin').text
            ymin = xml_box.find('ymin').text
            xmax = xml_box.find('xmax').text
            ymax = xml_box.find('ymax').text
            # Append rows in Empty Dataframe by adding dictionaries
            data = data.append({'fileName': fileName, 'xmin': xmin, 'ymin':ymin,'xmax':xmax,'ymax':ymax,'class':cls_name}, ignore_index=True)

                
data.shape  
data.to_csv('data.csv',index=False)
   
               
def show_image_with_boxes(df):
  # pick a random image
  filepath = df.sample()['fileName'].values[0]

  # get all rows for this image
  df2 = df[df['fileName'] == filepath]
  im = np.array(Image.open(filepath))

  # if there's a PNG it will have alpha channel
  im = im[:,:,:3]

  for idx, row in df2.iterrows():
    box = [
      row['xmin'],
      row['ymin'],
      row['xmax'],
      row['ymax'],
    ]
    print(box)
    draw_box(im, box, color=(255, 0, 0))

  plt.axis('off')
  plt.imshow(im)
  plt.show()                  
                  
                  
show_image_with_boxes(data)                  
      

classes = ['Name','ccNumber','DOB','Address']
with open('classes.csv', 'w') as f:
  for i, class_name in enumerate(classes):
    f.write(f'{class_name},{i}\n')
            
if not os.path.exists('snapshots'):
  os.mkdir('snapshots')                  
PRETRAINED_MODEL = 'snapshots/_pretrained_model.h5'

URL_MODEL = 'https://github.com/fizyr/keras-retinanet/releases/download/0.5.1/resnet50_coco_best_v2.1.0.h5'
urllib.request.urlretrieve(URL_MODEL, PRETRAINED_MODEL)

print('Downloaded pretrained model to ' + PRETRAINED_MODEL)          




!keras-retinanet/keras_retinanet/bin/train.py --freeze-backbone \
--random-transform \
--weights {PRETRAINED_MODEL} \
--batch-size 8 \
--steps 500 \
--epochs 15 \
csv data.csv classes.csv






















        
                  