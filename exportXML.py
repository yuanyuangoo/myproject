from xml.dom.minidom import Document
import numpy as np
def exportXMLs(pose,file):
    for i in range(len(pose)):
        filename=file+'_'+str(i+1)+'.xml'
        exportXML(pose[i],filename)

def exportXML(pose,filename):
    Index=(8,1,10,11,11,12,13,14,14,15,2,3,3,4,5,7,7,6,8,9)

    namelist=('torsoProximal','torsoDistal','upperLArmProximal','upperLArmDistal','lowerLArmProximal','lowerLArmDistal','upperRArmProximal','upperRArmDistal','lowerRArmProximal','lowerRArmDistal','upperLLegProximal','upperLLegDistal','lowerLLegProximal','lowerLLegDistal','upperRLegProximal','upperRLegDistal','lowerRLegProximal','lowerRLegDistal','headProximal','headDistal')

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

    for index in range(len(namelist)):
        name=namelist[index]
        i=Index[index]-1
        print index
        enabled=str(1)
        X=str(pose[i][0])
        Y=str(pose[i][1])
        Z=str(pose[i][2])
        creatJoint(doc,Pose,name,enabled,X,Y,Z)


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

