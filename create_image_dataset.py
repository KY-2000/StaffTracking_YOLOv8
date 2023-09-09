# import open cv
import cv2
import os

# load the video using path of video
model_path = "C:\\Users\\KenYuen\\OneDrive - sjtu.edu.cn\\Desktop\\Work\\FreshGrad Application\\FootfallCam Technical Interview"
video_path = os.path.join(model_path,"sample.mp4")
dataset_path = os.path.join(model_path, "Dataset")
video = cv2.VideoCapture(video_path)

success = True
count = 1
image_id = 1

while success:
    success , frame = video.read()
    
    if success == True:
        # i want every 5th frame from video
        # thats why i used following line of code
        # i dont want all frames from video
        # so we can decide the outpt frames count according to us.
            
        # specify the output path and file name
        # i used count as a file name
        # you can use any
        name = str(image_id)+".jpg"
        image_id += 1
        if not os.path.exists(dataset_path):
            os.makedirs(dataset_path)
        img_filename = os.path.join(dataset_path, name)
        
        # save the image
        cv2.imwrite(img_filename,frame)
        
        count += 1

print("Total Extracted Frames :",image_id)  