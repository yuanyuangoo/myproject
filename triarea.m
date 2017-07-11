function [X, R, t] = triarea(input_img,pose2d)
addpath('./camera_and_pose/release/src');
addpath('./camera_and_pose/release/data');
addpath('./camera_and_pose/release/models');
load('example1.mat');
im=imread(input_img);
imshow(im);
xy=convert(pose2d)
for i=1:size(xy,3)
    [X(:,:,i), R(:,:,i), t(:,:,i)] = recon3DPose(im,xy(:,:,i),'viz',0);
end
end


function pose2d_c= convert(pose2d)
    index=[6,7,5,2,3,4,1,8,9,9,15,14,13,10,11,12];
    for j=1:length(pose2d)
        tmp=pose2d{j};
        for i=1:16
            pos=tmp{i};
            t(:,i,j)=[pos{1},pos{2}];
        end
        tm=zeros(2,15);
        for i=1:16
            tm(:,index(i))=t(:,i,j);
        end
        pose2d_c(:,:,j)=tm;
    end
end