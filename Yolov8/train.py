from ultralytics import YOLO

model = YOLO('yolov8n.yaml')
# results = model.train(data='./classData.yaml', epochs=10)

if __name__ == '__main__':
    # Train the model using the 'coco128.yaml' dataset for 3 epochs
    # results = model.train(data=r'C:\DzinlyAiTraining\dataset\data.yaml', epochs=500, imgsz=640, device='cuda:0', batch=4, patience=0)
    results = model.train(data='./classData.yaml', epochs=3, imgsz=640, device='cpu', batch=4, patience=50,seed=0,overlap_mask=True, mask_ratio= True, nbs=64,lr0=0.001,lrf=0.01,workers=8,hsv_h=0.015,hsv_s=0.7,hsv_v = 0.4, fliplr = 0.5,translate = 0.1,degrees =0.0,scale=0.5,shear =0.0)

    # Evaluate the model's performance on the validation set
    results = model.val()
    print("results =>", results)