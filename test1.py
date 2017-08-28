import sys
sys.path.append('./py-faster-rcnn/tools/')
sys.path.append('./c2f-vol-demo/python/')
sys.path.append('./pose-hg-demo/python/')

import os
os.environ["GLOG_minloglevel"] = "2"
sys.path.append('./camera_and_pose/release/python/')
from loadGroundTruth import loadGroundTruth
from computeError3D import computeError3D
from showdemo import showdemo
import _init_paths
from fast_rcnn.config import cfg
import matplotlib.pyplot as plt
import numpy as np
import scipy.io as sio
import caffe
import cv2
import argparse
import demo1 as de
import exportXMLs as ex
import c2f as c2f
import hourglass as hg
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

    print '\n\nLoaded network {:s}'.format(caffemodel)

    name = (['/media/a/74D48535D484FA9E/Humaneva/',
             'S2', '/Image_Data/', 'Box', '_1_(C3).avi'])
    video_file = (
        ['/media/a/74D48535D484FA9E/Humaneva/S1/Image_Data/Walking_1_(C1).avi'])
    Num_Frames = 6
    datapath = '/media/a/07E212E807E212E8/myproject/c2f-vol-demo/data/h36m-sample/images/'
    imagename = 'S9_Posing_1.55011271_000001.jpg'
#    cv2.imshow("Image", im)
#    cv2.waitKey (0)
    cv2.namedWindow("Display window", cv2.WINDOW_AUTOSIZE)
    #index = [6, 3, 4, 5, 2, 0, 1, 7, 8, 13, 14, 15, 12, 11, 10]
    index = [6, 3, 4, 5, 2, 1, 0, 8, 9, 13, 14, 15, 12, 11, 10]

    for video in video_file:
        print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
        print 'Demo for data/demo/{}'.format(video)
        i = 0
        # cap = cv2.VideoCapture(video)

        # while (i < Num_Frames):
        #     cap.read()
        #     i += 1
        #     t, im = cap.read()
        # im = cv2.imread(
        #    './c2f-vol-demo/data/h36m-sample/images/S9_Posing_1.55011271_000001.jpg')
        #cv2.imshow("Display window", im)
        # cv2.waitKey(0)
        #im = ld.loadvideo(Num_Frames, video_file)
        #cv2.imwrite("1.jpg", im)
        im = cv2.imread(datapath + imagename)
        box = de.demo_show(net, im)
        cv2.imshow("Display window", im)
        cv2.waitKey(0)
        print 'hourglass'
        pose2d = hg.run(im, box)
        show2d(im, pose2d, box)
        cv2.imshow("Display window", im)
        cv2.waitKey(0)
        print 'c2f'
        pose3d = c2f.run(im, box)

        # print pose3d

        groudtruth = loadGroundTruth('./camera_and_pose/release/data/pose.mat')
        #showdemo(groudtruth[:, :, 0], pose3d * 68)
        #error = computeError3D(pose3d, groudtruth[:, :, 0])
        #print(pose3d, error)
        plt.show()
        plt.pause(1)

        # print pose3d
        # print R
        # print t
        # print 'exporting XMLs'
        # ex.exportXMLs(pose3d, name, Num_Frames)
    plt.show()
