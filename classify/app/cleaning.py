import os
import cv2

train_dir = r"E:\AI_DS_ML\brain_tumor_detection\classify\dataset\Training"

categories = ["glioma", "meningioma", "no_tumor", "pituitary"]

size_threshold = (10,10)
valid_extensions=('.jpg', '.png', '.jpeg')

def is_image_corrupt(image_path):
    try:
        img = cv2.imread(image_path)
        if img is None:
            return True
        return False
    except:
        return True
    
def is_image_below_threshold(img_path):
    img = cv2.imread(image_path)
    if img.shape <= size_threshold:
        print(img.shape)
        return True
    return False
    

for each_category in categories:
    folder_path = os.path.join(train_dir, each_category)
    for each_file in os.listdir(folder_path):
        image_path = os.path.join(folder_path, each_file)
        if os.path.isfile(image_path) and each_file.lower().endswith(valid_extensions):
            if is_image_corrupt(image_path) or is_image_below_threshold(image_path):
                os.remove(image_path)
                print(f"Removed corrupt image: {each_file}")