clear;
clc;  
  


% cd('E:\HDR\HDRͼ���\HDR image database\image_vqeg_ori_test'); % ���õ�ǰĿ¼  
% for i = 1 : 150  
%     str = sprintf('%03d',i);
%     rmdir(str); % ɾ���ļ��У�����������վ��  
% end  
%cd('E:\HDR\HDRͼ���\HDR image database\image_vqeg_dis_test');  % ���õ�ǰĿ¼��current directory  

%rootdir = 'E:\HDR\HDRͼ���\HDR image database\Images-vqeg\';  
rootdir = 'E:\ʵϰ\deep_learn\test_json1\';
subdir = dir(rootdir);  
      
for i=1:length(subdir)  
    if(isequal(subdir(i),'.') || isequal(subdir(i),'..') || ~subdir(i).isdir)   
        continue;  
    end
    sub = strcat(rootdir, subdir(i).name);
    subdirpath = fullfile(sub,'label.png');
    images = dir(subdirpath); % ���к�׺Ϊ.jpg���ļ�  
    for j=1:length(images) 
        ImageName = fullfile(sub,images(j).name);  
        ImageData = imread(ImageName); % ���ζ�ȡͼ��  
        img = uint8(ImageData);
        str = subdir(i).name(1:3);
        name = strcat(str,'.png');
       % folderName{j} = str;  
       % mkdir(folderName{j});  % �½�һ���ļ���  
        
        
        saveddir = 'E:\ʵϰ\matlab_test\'; % ͼ���±��浽��·��  
        savedname = fullfile(saveddir,name); % ͼ�����Ʋ���  
        imwrite(img,savedname); % ����ͼ��  
             
              
       fprintf('%d %d %s\n',i,j,savedname);
       
    end
end
    
 %   https://blog.csdn.net/susu_love/article/details/53256731