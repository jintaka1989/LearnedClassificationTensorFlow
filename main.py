# -*- coding: utf-8 -*-
import sys
import os
import commands as cmd
import cv2
import numpy as np
import tensorflow as tf
import tensorflow.python.platform
from PIL import Image
import scipy
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from scipy import ndimage

flags = tf.app.flags
FLAGS = flags.FLAGS
flags.DEFINE_string('save_model', 'models/model.ckpt', 'File name of model data')
flags.DEFINE_string('train', 'data_set/train.txt', 'File name of train data')
flags.DEFINE_string('test', 'data_set/test.txt', 'File name of test data')
flags.DEFINE_string('train_dir', '/tmp/pict_data', 'Directory to put the data_set data.')
flags.DEFINE_integer('max_steps', 201, 'Number of steps to run trainer.')
flags.DEFINE_integer('batch_size', 256, 'Batch size'
                     'Must divide evenly into the dataset sizes.')
flags.DEFINE_float('learning_rate', 1e-4, 'Initial learning rate.')

IMAGE_SIZE = 28
# カラー画像だから*3？
IMAGE_PIXELS = IMAGE_SIZE*IMAGE_SIZE*3

if __name__ == '__main__':
    # ファイルを開く
    with open(FLAGS.test, 'r') as f: # test.txt
            test_image = []
            test_label = []
            test_file_passes = []
            for line in f:
                line = line.rstrip()
                l = line.split()
                test_file_passes.append(l[0])
            test_image = np.asarray(test_image)
            test_label = np.asarray(test_label)
            test_len = len(test_image)

    # os.system("python classify_image.py --image_file data_set/test/class0/search.jpg")
    n = 0
    for file_pass in test_file_passes:
        print("///////////////////////////////////////////////////////////////////////////////////////")
        print(file_pass + ":")
        print("///////////////////////////////////////////////////////////////////////////////////////")
        d = os.system("python classify_image.py --image_file " + file_pass)
        import pdb; pdb.set_trace()
        n += 1
        if n>3:
            break
