from xml.dom.minidom import Document

def exportXML(pose,filename):

    doc = Document()

    SEQUENCE = doc.createElement('SEQUENCE')    
    SEQUENCE.setAttribute('DatasetName',"HumanEvaI")
    SEQUENCE.setAttribute('FrameStart',"6")
    SEQUENCE.setAttribute('Partition',"Validate")
    SEQUENCE.setAttribute('FrameEnd',"590")
    SEQUENCE.setAttribute('Trial',"1")
    SEQUENCE.setAttribute('SubjectName',"S1")
    SEQUENCE.setAttribute('ActionType',"Walking")
    SEQUENCE.setAttribute('DatasetBasePath',"../")
    doc.appendChild(SEQUENCE)


    Camera = doc.createElement('Camera')
    SEQUENCE.appendChild(Camera)
    Camera_text=doc.createTextNode('C1')
    Camera.appendChild(Camera_text)

    Frame = doc.createElement('Frame')
    SEQUENCE.appendChild(Frame)

    Number = doc.createElement('Number')
    Frame.appendChild(Number)
    Number_text=doc.createTextNode('1')
    Number.appendChild(Number_text)

    Pose = doc.createElement('Pose')
    Frame.appendChild(Pose)

    creatJoint(doc,Pose,'torsoProximal','1','-722.810296','-773.585228','1302.923889')
    creatJoint(doc,Pose,'torsoDistal','1','-722.810296','-773.585228','1302.923889')
    creatJoint(doc,Pose,'upperLArmProximal','1','-722.810296','-773.585228','1302.923889')
    creatJoint(doc,Pose,'upperLArmDistal','1','-722.810296','-773.585228','1302.923889')
    creatJoint(doc,Pose,'lowerLArmProximal','1','-722.810296','-773.585228','1302.923889')
    creatJoint(doc,Pose,'lowerLArmDistal','1','-722.810296','-773.585228','1302.923889')
    creatJoint(doc,Pose,'upperRArmProximal','1','-722.810296','-773.585228','1302.923889')
    creatJoint(doc,Pose,'upperRArmDistal','1','-722.810296','-773.585228','1302.923889')
    creatJoint(doc,Pose,'lowerRArmProximal','1','-722.810296','-773.585228','1302.923889')
    creatJoint(doc,Pose,'lowerRArmDistal','1','-722.810296','-773.585228','1302.923889')
    creatJoint(doc,Pose,'upperLLegProximal','1','-722.810296','-773.585228','1302.923889')
    creatJoint(doc,Pose,'upperLLegDistal','1','-722.810296','-773.585228','1302.923889')
    creatJoint(doc,Pose,'lowerLLegProximal','1','-722.810296','-773.585228','1302.923889')
    creatJoint(doc,Pose,'lowerLLegDistal','1','-722.810296','-773.585228','1302.923889')
    creatJoint(doc,Pose,'upperRLegProximal','1','-722.810296','-773.585228','1302.923889')
    creatJoint(doc,Pose,'upperRLegDistal','1','-722.810296','-773.585228','1302.923889')
    creatJoint(doc,Pose,'lowerRLegProximal','1','-722.810296','-773.585228','1302.923889')
    creatJoint(doc,Pose,'lowerRLegDistal','1','-722.810296','-773.585228','1302.923889')
    creatJoint(doc,Pose,'headProximal','1','-722.810296','-773.585228','1302.923889')
    creatJoint(doc,Pose,'headDistal','1','-722.810296','-773.585228','1302.923889')


    Error = doc.createElement('Error')
    Frame.appendChild(Error)
    Error_text=doc.createTextNode('N/A')
    Error.appendChild(Error_text)

    f = open(filename,'w')
    doc.writexml(f,indent = '',newl = '\n', addindent = '\t',encoding='utf-8')
    f.close()

def creatJoint(doc,Pose,name,enabled,x,y,z):
    Joint = doc.createElement('Joint')
    Pose.appendChild(Joint)

    Name = doc.createElement('Name')
    Joint.appendChild(Name)
    Name_text=doc.createTextNode(name)
    Name.appendChild(Name_text)

    Enabled = doc.createElement('Enabled')
    Joint.appendChild(Enabled)
    Enabled_text=doc.createTextNode(enabled)
    Enabled.appendChild(Enabled_text)

    X = doc.createElement('X')
    Joint.appendChild(X)
    X_text=doc.createTextNode(x)
    X.appendChild(X_text)

    Y = doc.createElement('Y')
    Joint.appendChild(Y)
    Y_text=doc.createTextNode(y)
    Y.appendChild(Y_text)

    Z = doc.createElement('Z')
    Joint.appendChild(Z)
    Z_text=doc.createTextNode(z)
    Z.appendChild(Z_text)
def parse(filename):
# -*- coding: utf-8 -*-
#==========================
    import xml.etree.ElementTree as ET
    tree = ET.parse(filename)
    root = tree.getroot()
    print('root-tag:',root.tag,',root-attrib:',root.attrib,',root-text:',root.text)
    for child in root:
        print('child-tag is:',child.tag,',child.attrib:',child.attrib,',child.text:',child.text)
        for sub in child:
            print('sub-tag is:',sub.tag,',sub.attrib:',sub.attrib,',sub.text:',sub.text)

x=[[[-0.324509985807,1.26778440978],[-1.71821516497,-2.69897377544],[-0.755504011288,-1.54609448021]],[[0.817027930797,2.95977872606],[-3.35141325797,-3.57306241713],[0.0125967251235,-0.0417904963332]],[[-1.81214840078,3.26096021846],[-5.64572467573,-4.15985374563],[1.33079768929,2.52656274691]],[[-1.09893551267,2.82255772539],[-10.8241501776,-6.69734952518],[-0.389086392981,0.617743502008]],[[-1.98232010878,-0.509077894501],[-2.9644332368,-3.64398143194],[-0.105698000135,0.205356375219]],[[-0.962605593718,-2.13734418662],[-9.74883638393,-6.23860472317],[-0.486136770795,-3.69673422741]],[[-5.87520709079,-3.17837478086],[-10.2860679393,-6.03424372349],[0.304032783559,-1.90569993541]],[[-0.338630976538,1.12722774562],[4.47991126271,3.36339660372],[-0.730972796614,-1.15337973292]],[[-0.578815533325,0.141192892734],[9.35979454194,8.51863198837],[-2.75790578773,5.45782178904]],[[3.05472175593,4.64701982139],[5.87104639329,4.32443793282],[-0.70324116768,-0.516664402349]],[[7.00897715543,5.03422023395],[5.89132928157,2.36905364623],[4.30988323723,2.8857900978]],[[6.386774379,0.168297866703],[6.34410081362,1.90297896625],[1.20517771276,4.12957506152]],[[-3.85699392383,-2.33143049288],[4.69632546564,4.20244924812],[-1.46412930379,-1.67885929966]],[[-2.26729732425,-7.77789964189],[0.609045147923,1.29024682485],[-0.31571973553,-0.348099393301]],[[-1.32023112308,-4.60548029145],[-1.01874398336,3.24212281512],[-0.460430349617,-2.53632750399]]]

exportXML(x,'1.xml')

