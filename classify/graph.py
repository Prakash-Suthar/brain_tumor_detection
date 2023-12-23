#-------------------------------wrong--------------------------------------

import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 

df = pd.read_csv(r"E:\AI_DS_ML\brain_tumor_detection\runs\classify\train\results.csv")
# Plotting
plt.figure(figsize=(15, 8))

# Training Loss
plt.subplot(2, 2, 1)
sns.lineplot(x=df['epoch'], y=df['train/loss'], data=df, label='Training Loss')
sns.lineplot(x=df['epoch'], y=df['val/loss'], data=df, label='Validation Loss')
plt.title('Training and Validation Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')

# Accuracy Top1
plt.subplot(2, 2, 2)
sns.lineplot(x=df['epoch'], y=df['metrics/accuracy_top1'], data=df, label='Top 1 Accuracy')
plt.title('Top 1 Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')

# Accuracy Top5
plt.subplot(2, 2, 3)
sns.lineplot(x=df['epoch'], y=df['metrics/accuracy_top5'], data=df, label='Top 5 Accuracy')
plt.title('Top 5 Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')

# Learning Rate
plt.subplot(2, 2, 4)
sns.lineplot(x=df['epoch'], y=df['lr/pg0'], data=df, label='Learning Rate - pg0')
sns.lineplot(x=df['epoch'], y=df['lr/pg1'], data=df, label='Learning Rate - pg1')
sns.lineplot(x=df['epoch'], y=df['lr/pg2'], data=df, label='Learning Rate - pg2')
plt.title('Learning Rate')
plt.xlabel('Epoch')
plt.ylabel('Learning Rate')

plt.tight_layout()
plt.show()

# print(df.describe)