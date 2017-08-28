import sys
sys.path.append('./py-faster-rcnn/tools/')
import os
os.environ["GLOG_minloglevel"] = "2"
import _init_paths
from fast_rcnn.config import cfg
import matplotlib.pyplot as plt
import numpy as np
import scipy.io as sio
import caffe

caffe.set_mode_gpu()
caffe.set_device(0)
