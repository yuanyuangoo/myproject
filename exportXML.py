from xml.dom.minidom import Document
import numpy as np
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

x=[[[-0.324509985807,-1.71821516497,-0.755504011288],[0.817027930797,-3.35141325797,0.0125967251235],[-1.81214840078,-5.64572467573,1.33079768929],[-1.09893551267,-10.8241501776,-0.389086392981],[-1.98232010878,-2.9644332368,-0.105698000135],[-0.962605593718,-9.74883638393,-0.486136770795],[-5.87520709079,-10.2860679393,0.304032783559],[-0.338630976538,4.47991126271,-0.730972796614],[-0.578815533325,9.35979454194,-2.75790578773],[3.05472175593,5.87104639329,-0.70324116768],[7.00897715543,5.89132928157,4.30988323723],[6.386774379,6.34410081362,1.20517771276],[-3.85699392383,4.69632546564,-1.46412930379],[-2.26729732425,0.609045147923,-0.31571973553],[-1.32023112308,-1.01874398336,-0.460430349617]],[[1.26778440978,-2.69897377544,-1.54609448021],[2.95977872606,-3.57306241713,-0.0417904963332],[3.26096021846,-4.15985374563,2.52656274691],[2.82255772539,-6.69734952518,0.617743502008],[-0.509077894501,-3.64398143194,0.205356375219],[-2.13734418662,-6.23860472317,-3.69673422741],[-3.17837478086,-6.03424372349,-1.90569993541],[1.12722774562,3.36339660372,-1.15337973292],[0.141192892734,8.51863198837,5.45782178904],[4.64701982139,4.32443793282,-0.516664402349],[5.03422023395,2.36905364623,2.8857900978],[0.168297866703,1.90297896625,4.12957506152],[-2.33143049288,4.20244924812,-1.67885929966],[-7.77789964189,1.29024682485,-0.348099393301],[-4.60548029145,3.24212281512,-2.53632750399]]]
x=np.asarray(x)

exportXML(x,'1.xml')

