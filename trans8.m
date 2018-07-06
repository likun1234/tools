clear;
clc;  
  


% cd('E:\HDR\HDR图像库\HDR image database\image_vqeg_ori_test'); % 设置当前目录  
% for i = 1 : 150  
%     str = sprintf('%03d',i);
%     rmdir(str); % 删除文件夹（不经过回收站）  
% end  
%cd('E:\HDR\HDR图像库\HDR image database\image_vqeg_dis_test');  % 设置当前目录：current directory  

%rootdir = 'E:\HDR\HDR图像库\HDR image database\Images-vqeg\';  
rootdir = 'E:\实习\deep_learn\test_json1\';
subdir = dir(rootdir);  
      
for i=1:length(subdir)  
    if(isequal(subdir(i),'.') || isequal(subdir(i),'..') || ~subdir(i).isdir)   
        continue;  
    end
    sub = strcat(rootdir, subdir(i).name);
    subdirpath = fullfile(sub,'label.png');
    images = dir(subdirpath); % 所有后缀为.jpg的文件  
    for j=1:length(images) 
        ImageName = fullfile(sub,images(j).name);  
        ImageData = imread(ImageName); % 依次读取图像  
        img = uint8(ImageData);
        str = subdir(i).name(1:3);
        name = strcat(str,'.png');
       % folderName{j} = str;  
       % mkdir(folderName{j});  % 新建一个文件夹  
        
        
        saveddir = 'E:\实习\matlab_test\'; % 图像新保存到的路径  
        savedname = fullfile(saveddir,name); % 图像名称不变  
        imwrite(img,savedname); % 保存图像  
             
              
       fprintf('%d %d %s\n',i,j,savedname);
       
    end
end
    
 %   https://blog.csdn.net/susu_love/article/details/53256731