
clc;
close all;
clear all;
[ImageName, ImagePath]=uigetfile({'*.jpg';'*.bmp';'*.gif'},'Pick a Image File');
SelectImage = imread([ImagePath,ImageName]);

ImageFiles = dir(ImagePath );
No_files = length(ImageFiles);    % Number of files found 

for Index=1:No_files
    try
        currentfilename = ImageFiles(Index).name;
        if(currentfilename=='.')
            continue
        end
        Image = imread([ImagePath,currentfilename]); %Reading of image acoording to Index 
        imshow(Image);
        
        [Width,Height,Channel]=size(Image);
        if(Channel==3)
            RedChannel=Image(:,:,1);
            GreenChannel=Image(:,:,2);
            BlueChannel=Image(:,:,3);
            
            %% Using HSV (Hue, Saturation, Value) Color model. V(Value= Brightness)
            for i=1:Width
                for j=1:Height
                    P=RedChannel(i,j);
                    Q=GreenChannel(i,j);
                    R=BlueChannel(i,j);
                    Vchannel(i,j) = max(P,Q); % Convertion of RGB to HSV color space.
                    
                end
            end
            %hsvImage=rgb2hsv(Image)
            %brightness = uint8(hsvImage(:, :, 3));  % Extract the V(Brightness) channel.
            
            Brightness_of_Image=  mean2(Vchannel);  
            
        elseif(Channel==1)
            Brightness_of_Image=mean2(Image);
        end
        if (Brightness_of_Image>=0 && Brightness_of_Image<24)
            Brightness_Image=0
        elseif(Brightness_of_Image>=24 && Brightness_of_Image<48)
            Brightness_Image=1
        elseif(Brightness_of_Image>=48 && Brightness_of_Image<72)
            Brightness_Image=2
        elseif(Brightness_of_Image>=77 && Brightness_of_Image<96)
            Brightness_Image=3
        elseif(Brightness_of_Image>=96 && Brightness_of_Image<120)
            Brightness_Image=4
        elseif(Brightness_of_Image>=120 && Brightness_of_Image<144)
            Brightness_Image=5
        elseif(Brightness_of_Image>=144 && Brightness_of_Image<168)
            Brightness_Image=6
        elseif(Brightness_of_Image>=168 && Brightness_of_Image<192)
            Brightness_Image=7
        elseif(Brightness_of_Image>=192 && Brightness_of_Image<216)
            Brightness_Image=8
        elseif(Brightness_of_Image>=216 && Brightness_of_Image<240)
            Brightness_Image=9
        elseif(Brightness_of_Image>=240)
            Brightness_Image=10
        end
    catch
    end
end   % If want to check the result for single images put the breackpoint here...
