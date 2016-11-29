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

os.system("python classify_image.py --image_file data_set/test/class0/search.jpg")
