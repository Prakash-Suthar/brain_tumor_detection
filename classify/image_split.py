import os
import shutil
import random

# Set the path to your dataset
data_path = './dataset_brain/Test'

# Set the ratio of images to use for training
train_ratio = 0.8

# Calculate the number of images to use for training and testing
num_train = int(train_ratio * len(os.listdir(data_path)))
num_test = len(os.listdir(data_path)) - num_train

# Create the directories for the training and testing sets
train_dir = os.path.join(data_path, 'test')
test_dir = os.path.join(data_path, 'val')
os.makedirs(train_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

# Split the images into training and testing sets
class_dirs = [d for d in os.listdir(data_path) if os.path.isdir(os.path.join(data_path, d))]
for class_dir in class_dirs:
    class_path = os.path.join(data_path, class_dir)
    class_train_dir = os.path.join(train_dir, class_dir)
    class_test_dir = os.path.join(test_dir, class_dir)
    os.makedirs(class_train_dir, exist_ok=True)
    os.makedirs(class_test_dir, exist_ok=True)
    class_files = os.listdir(class_path)
    random.shuffle(class_files)
    for i, filename in enumerate(class_files):
        if i < num_train:
            src = os.path.join(class_path, filename)
            dst = os.path.join(class_train_dir, filename)
            shutil.copy(src, dst)
        else:
            src = os.path.join(class_path, filename)
            dst = os.path.join(class_test_dir, filename)
            shutil.copy(src, dst)