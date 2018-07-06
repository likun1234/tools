clear;
clc;
%%  set folder path
file_path =  'E:\ʵϰ\deep_learn\image\';% ԭʼͼ���ļ���·��  
img_path_list = dir(strcat(file_path,'*.jpg'));%��ȡ���ļ���������jpg��ʽ��ͼ��  

img_num = length(img_path_list);%��ȡͼ��������   
%%
sum_r=0;
sum_g=0;
sum_b=0;

mean1 = [];
mean2 = [];
mean3 = [];

tic;
%% read hdr images
if img_num > 0 %������������ͼ��  
        for j = 1:img_num %��һ��ȡͼ��  
            image_name = img_path_list(j).name;% ԭʼͼ����  
            image = double(imread(strcat(file_path,image_name))); 
            
            mean_r = mean(mean(image(:,:,1)));
            mean_g = mean(mean(image(:,:,2)));
            mean_b = mean(mean(image(:,:,3)));
            
            mean1 = [mean1, mean_r];
            mean2 = [mean2, mean_g];
            mean3 = [mean3, mean_b];
            
            sum_r = sum_r + mean_r;
            sum_g = sum_g + mean_g;
            sum_b = sum_b + mean_b;
%----------------------------------------------------------------------

            fprintf('%d %s\n',j,strcat(file_path,image_name));% ��ʾ���ڴ����ͼ����  
        end  
end  

mean_r = sum_r / img_num;
mean_g = sum_g / img_num;
mean_b = sum_b / img_num;
%%
toc;


% i = imread('E:\ʵϰ\pascal_VOC\VOCtrainval_11-May-2012\VOCdevkit\VOC2012\SegmentationClass\2007_000032.png');
% j = rgb2gray(i);
% figure, imshow(j);