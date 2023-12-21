import matplotlib.pyplot as plt
import os

train_dir = r"E:\AI_DS_ML\brain_tumor_detection\classify\dataset\Training"
valid_extensions=('.jpg', '.png', '.jpeg')

categories = ["glioma", "meningioma", "no_tumor", "pituitary"]
category_count = {}

for each_category in categories:
    folder_path = os.path.join(train_dir, each_category)
    valid_images = [file for file in os.listdir(folder_path) if file.lower().endswith(valid_extensions)]
    category_count[each_category] = len(valid_images)

fig, ax = plt.subplots(figsize=(10, 4))

# Bar chart
bar_plot = plt.barh(list(category_count.keys()), list(category_count.values()), 0.5)
plt.title('Tumor Type Distribution')
plt.xlabel('Count')
plt.ylabel('Tumor Type')
for i, bar in enumerate(bar_plot):
    plt.text(bar.get_width(), bar.get_y() + bar.get_height() / 2, str(list(category_count.values())[i]), ha='left', va='center')

plt.show()



sample_size = sum(category_count.values())

class_dist = {key : val/sample_size for key, val in category_count.items()}


fig, ax = plt.subplots(figsize=(10, 4))


# Bar chart
bar_plot = plt.barh(list(class_dist.keys()), list(class_dist.values()), 0.6)
plt.title('Class Distribution')
plt.xlabel('Class')
plt.ylabel('Percentage')

for i, bar in enumerate(bar_plot):
    plt.text(bar.get_width(), bar.get_y() + bar.get_height() / 2, str(round(list(class_dist.values())[i], 3)), ha='left', va='center')

plt.show()