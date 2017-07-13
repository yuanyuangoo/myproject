import sys 
sys.path.append('./py-faster-rcnn/tools/') 
sys.path.append('./pose-hg-demo/python/') 
sys.path.append('./camera_and_pose/release/python/')


import _init_paths
from fast_rcnn.config import cfg
from fast_rcnn.test import im_detect
from fast_rcnn.nms_wrapper import nms
from utils.timer import Timer
import matplotlib.pyplot as plt
import numpy as np
import scipy.io as sio
import caffe, os, cv2
import argparse
import demo1 as de
import hourglass as hg
import cameraAndPose as cp
import exportXML as ex
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

    #print '\n\nLoaded network {:s}'.format(caffemodel)

    #im_names = ['004545.jpg']
    im_names = ['1.jpg']

    im_file = os.path.join(cfg.DATA_DIR, 'demo', im_names[0])
    im_file = os.path.join('images', im_names[0])

    im = cv2.imread(im_file)

#    cv2.namedWindow("Image")  
#    cv2.imshow("Image", im)
#    cv2.waitKey (0)
    
    for im_name in im_names:
        print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
        print 'Demo for data/demo/{}'.format(im_name)
        box=de.demo_show(net, im)


        print 'hourglass'
        pose2d=hg.run(im_file,box)

        print 'camera and pose'
        pose3d, R, t=cp.getPose(im_file,pose2d)
        pose3d=np.asarray(pose3d)
        print pose3d

        print 'exporting XMLs'
        ex.exportXMLs(pose3d,'pose')
#        cv2.waitKey (0)
#        cv2.destroyAllWindows()
