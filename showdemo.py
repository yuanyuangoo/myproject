import sys
sys.path.append('./camera_and_pose/release/python/')
import cv2
from loadGroundTruth import loadGroundTruth
from setK import setK
from loadmat import loadmat
import numpy as np
from visualizeGaussianModel import visualizeGaussianModel
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
from plot2Dskeleton import plot2Dskeleton


def showdemo(xy1, xy2):
    video_file = (
        ['/media/a/74D48535D484FA9E/Humaneva/S1/Image_Data/Walking_1_(C1).avi'])

    cap = cv2.VideoCapture(video_file[0])
    i = 0
    Num_Frames = 6
    while (i < Num_Frames):
        cap.read()
        i += 1
        t, im = cap.read()
    basis = loadmat('./camera_and_pose/release/models/mocapReducedModel.mat')
    pose = {
        'lambda2': 0.01,
        'lambda1': 0.01,
        'K': setK(im.shape[1], im.shape[0], 2),
        'numIter': 20,
        'numIters2': 30,
        'tol1': 500,
        'tol2': 1,
        'ks': 10,
        'optType': 1,
        'viz': 0,
        'annoids': np.arange(0, xy1.shape[1]),
        'numPoints': xy1.shape[1],
        'im': im,
        'xy': np.vstack((xy1, np.ones(xy1.shape[1]))),
        'BOMP': basis['B'],
        'mu': basis['mu'],
        'skel': basis['skel'],
        'numPoints': xy1.shape[1],
        'annoids': np.arange(0, xy1.shape[1])
    }
    cam = loadmat('./camera_and_pose/release/data/frontCam.mat')
    fig = plt.figure(1)
    ax = Axes3D(fig)
    #plot2Dskeleton(1, xy, pose['skel'], 'red', ax)
    visualizeGaussianModel(xy1, pose['skel'], ax)
    visualizeGaussianModel(xy2, pose['skel'], ax)
    fig.canvas.draw()
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.axis('equal')
    plt.draw()


# groundtruth = loadGroundTruth('./camera_and_pose/release/data/pose.mat')
# pose2d = [[344,  303],
#           [315,  261],
#           [334,  218],
#           [339,  218],
#           [353,  265],
#           [353,  307],
#           [334,  218],
#           [344,  143],
#           [339,  129],
#           [320,  111],
#           [339,  214],
#           [344,  186],
#           [344,  143],
#           [344,  143],
#           [344,  186],
#           [339,  214]]
# pose2d = np.asarray(pose2d)
# index = [6, 3, 4, 5, 2, 0, 1, 7, 8, 13, 14, 15, 12, 11, 10]

# pose2d = pose2d[index]


# groundtruthv = groundtruth - groundtruth[0, :, :]
# pose2dv = groundtruthv[:, :, 0]

# pose2dv = pose2dv.reshape(pose2dv.shape[0] * pose2dv.shape[1], 1, order='F')
# groundtruthv = groundtruthv.reshape(
#     groundtruthv.shape[0] * groundtruthv.shape[1], groundtruthv.shape[2], order='F')
# a = np.outer(pose2dv.conj().T, groundtruthv[:, 0])
# # a = np.dot(pose2dv.conj().T, groundtruthv)
# print a.shape
# print a
