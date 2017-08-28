import sys
sys.path.append('./py-faster-rcnn/tools/')
sys.path.append('./pose-hg-demo/python/')
sys.path.append('./camera_and_pose/release/python/')
sys.path.append('./camera_and_pose/release/hogsvd-python/')

import os
os.environ["GLOG_minloglevel"] = "2"

import _init_paths
from fast_rcnn.config import cfg
import matplotlib.pyplot as plt
import numpy as np
import scipy.io as sio
import caffe
import cv2
import argparse
import demo1 as de
import hourglass as hg
import recon3DPose as r3p
import exportXMLs as ex
from loadGroundTruth import loadGroundTruth
from computeError3D import computeError3D
from showdemo import showdemo
import h5py

CLASSES = ('__background__',
           'aeroplane', 'bicycle', 'bird', 'boat',
           'bottle', 'bus', 'car', 'cat', 'chair',
           'cow', 'diningtable', 'dog', 'horse',
           'motorbike', 'person', 'pottedplant',
           'sheep', 'sofa', 'train', 'tvmonitor')

NETS = {'vgg16': ('VGG16',
                  'VGG16_faster_rcnn_final.caffemodel'),
        'zf': ('ZF',
               'ZF_faster_rcnn_final.caffemodel')}


def show2d(im, pose2d, box):
    pose = pose2d[0]
    pairRef = (
        (0, 1),      (1, 2),      (2, 6),
        (3, 4),      (3, 6),      (4, 5),
        (6, 8),      (8, 9),
        (13, 8),     (10, 11),    (11, 12),
        (12, 8),     (13, 14),    (14, 15)
    )
    for i in np.arange(0, len(pairRef)):
        pt1 = (int(pose[pairRef[i][0]][0]), int(pose[pairRef[i][0]][1]))
        pt2 = (int(pose[pairRef[i][1]][0]), int(pose[pairRef[i][1]][1]))
        cv2.line(im, pt1, pt2, (255, 0, 0))

    return pose2d


def parse_args():
    """Parse input arguments."""
    parser = argparse.ArgumentParser(description='Faster R-CNN demo')
    parser.add_argument('--gpu', dest='gpu_id', help='GPU device id to use [0]',
                        default=0, type=int)
    parser.add_argument('--cpu', dest='cpu_mode',
                        help='Use CPU mode (overrides --gpu)',
                        action='store_true')
    parser.add_argument('--net', dest='demo_net', help='Network to use [vgg16]',
                        choices=NETS.keys(), default='vgg16')

    args = parser.parse_args()

    return args


if __name__ == '__main__':
    cfg.TEST.HAS_RPN = True  # Use RPN for proposals

    args = parse_args()

    prototxt = os.path.join(cfg.MODELS_DIR, NETS[args.demo_net][0],
                            'faster_rcnn_alt_opt', 'faster_rcnn_test.pt')
    caffemodel = os.path.join(cfg.DATA_DIR, 'faster_rcnn_models',
                              NETS[args.demo_net][1])

    if not os.path.isfile(caffemodel):
        raise IOError(('{:s} not found.\nDid you run ./data/script/'
                       'fetch_faster_rcnn_models.sh?').format(caffemodel))

    if args.cpu_mode:
        caffe.set_mode_cpu()
    else:
        caffe.set_mode_gpu()
        caffe.set_device(args.gpu_id)
        cfg.GPU_ID = args.gpu_id
    net = caffe.Net(prototxt, caffemodel, caffe.TEST)
    filename = '/home/a/Downloads/harvesting/pose-hg-demo/annot/valid_images.txt'

    print '\n\nLoaded network {:s}'.format(caffemodel)
    model = hg.create()
    with open(filename) as f:
        ImageList = f.readlines()
        image_dir = '/media/a/07E212E807E212E8/thunder/h36m/'
        savemat_dir = './camera_and_pose/release/data/'
        index = [6, 3, 4, 5, 2, 1, 0, 8, 9, 13, 14, 15, 12, 11, 10]
        cv2.namedWindow("Display window", cv2.WINDOW_AUTOSIZE)
        result = np.zeros((len(ImageList), 2, 15))
        deletelist = np.zeros((len(ImageList), 1))
        i = 0
        for image_name in ImageList:
            print "\n"
            print (i/float(len(ImageList)))

            print image_name
            image_file = image_dir + image_name

            print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
            # print 'Demo for data/demo/{}'.format(video_file)
            im = cv2.imread(image_file.replace('\n', ''))

            # cv2.imshow("Display window", im)
            # cv2.waitKey(0)
            box = de.demo_show(net, im)
            # cv2.imshow("Display window", im)
            # cv2.waitKey(0)

            # print 'hourglass'
            if box is None:
                deletelist[i] = i
            else:
                pose2d = hg.run(model, im, box)
                result[i] = pose2d[0][index].conj().T
            i = i + 1
            # show2d(im, pose2d, box)
            # cv2.imshow("Display window", im)
            # if cv2.waitKey(0) == 27:
            #     break
        sio.savemat(savemat_dir + 'H36m2ddelete' + '.mat', {'xy': deletelist})

        sio.savemat(savemat_dir + 'H36m2d' + '.mat', {'xy': result})
