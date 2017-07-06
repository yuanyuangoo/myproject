function [X, R, t] = triarea(input_img,pose2d)
addpath('./camera_and_pose/release/src');
addpath('./camera_and_pose/release/data');
addpath('./camera_and_pose/release/models');
load('example1.mat');
im=imread(input_img);
imshow(im);

xy=convert(pose2d)

[X, R, t] = recon3DPose(im,xy,'viz',1);

end
function pose2d_c= convert(pose2d)
%pose2d_c=cell2mat(cellfun(@(x) cell2mat(x),pose2d,'un',0))
    pose2d_c=zeros(2,15);
    index=[6,7,5,2,3,4,1,8,9,9,15,14,13,10,11,12];
    tmp=pose2d{1};
    for i=1:16
        pos=tmp{i};
        pose2d_c(:,i)=[pos{1},pos{2}];
    end
    pose2d_c=[pose2d_c(:,1:8),pose2d_c(:,10:16)];   
    
end