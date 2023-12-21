import matplotlib.pyplot as plt
import os
train_dir = r"E:\AI_DS_ML\brain_tumor_detection\classify\dataset\Training"
valid_extensions=('.jpg', '.png', '.jpeg')

categories = ["glioma", "meningioma", "no_tumor", "pituitary"]

plt.figure(figsize=(12, 8))
for i, category in enumerate(categories):
    folder_path = os.path.join(train_dir, category)
    image_path = os.path.join(folder_path, os.listdir(folder_path)[0])
    if not image_path.lower().endswith(valid_extensions):
        continue
    img = plt.imread(image_path)
    plt.subplot(2, 2, i+1)
    plt.imshow(img)
    plt.title(category)
    plt.axis("off")
plt.tight_layout()
plt.show()