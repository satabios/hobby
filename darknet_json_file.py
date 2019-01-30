

import os
from os import walk, getcwd
from PIL import Image
import json
from pprint import pprint

with open('C:/Users/Sathyaprakash/Desktop/trucks_10_012.json') as data_file:
    data = json.load(data_file)
pprint(data)

classes = ['person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus', 'train', 'truck', 'boat', 'traffic light',
          'fire hydrant', 'stop sign', 'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow',
          'elephant', 'bear', 'zebra', 'giraffe', 'backpack', 'umbrella', 'handbag', 'tie', 'suitcase', 'frisbee',
          'skis', 'snowboard', 'sports ball', 'kite', 'baseball bat', 'baseball glove', 'skateboard', 'surfboard',
          'tennis racket', 'bottle', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple',
          'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza', 'donut', 'cake', 'chair', 'couch',
          'potted plant', 'bed', 'dining table', 'toilet', 'tv', 'laptop', 'mouse', 'remote', 'keyboard', 'cell phone',
          'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'book', 'clock', 'vase', 'scissors', 'teddy bear',
          'hair drier', 'toothbrush']


def convert(size, box):
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)


# """-------------------------------------------------------------------"""

""" Configure Paths"""
mypath = "labels/stopsign_original/"
outpath = "labels/stopsign/"

cls = ['person', 'bicycle', 'car', 'motorcycle', 'truck',  'backpack']
if cls not in classes:
    exit(0)
cls_id = classes.index(cls)

wd = getcwd()
list_file = open('%s/%s_list.txt' % (wd, cls), 'w')

""" Get input text file list """
txt_name_list = []
for (dirpath, dirnames, filenames) in walk(mypath):
    txt_name_list.extend(filenames)
    break
print(txt_name_list)

""" Process """
for txt_name in txt_name_list:
    # txt_file =  open("Labels/stop_sign/001.txt", "r")

    """ Open input text files """
    txt_path = mypath + txt_name
    print("Input:" + txt_path)
    txt_file = open(txt_path, "r")
    lines = txt_file.read().split('\r\n')  # for ubuntu, use "\r\n" instead of "\n"

    """ Open output text files """
    txt_outpath = outpath + txt_name
    print("Output:" + txt_outpath)
    txt_outfile = open(txt_outpath, "w")

#     """ Convert the data to YOLO format """





xmin = data['object'][0]['xmin']
xmax = data['object'][0]['xmax']
ymin = data['object'][0]['ymin']
ymax = data['object'][0]['ymax']

img_path = data['filename']

w = data['height']
h = data ['width']

b = (float(xmin), float(xmax), float(ymin), float(ymax))
bb = convert((w, h), b)

txt_outfile.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')

""" Save those images with bb into list"""
if (ct != 0):
list_file.write('%s/images/%s/%s.JPEG\n' % (wd, cls, os.path.splitext(txt_name)[0]))

list_file.close()