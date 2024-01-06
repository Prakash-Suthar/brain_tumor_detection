# brain_tumor_detection
 brain tumor detection using differet algorithms in differernt three angles

CLI training : yolo detect train data=classData.yaml model=yolov8n.yaml epochs=100 imgsz=640 lr0=0.001 lrf=0.01 fliplr = 0.5 workers=8 hsv_h=0.015 hsv_s=0.7 hsv_v=0.4 val=True plots=True seed=0


TASK (optional) is one of ('detect', 'segment', 'classify', 'pose')
MODE (required) is one of ('train', 'val', 'predict', 'export', 'track', 'benchmark')
ARGS (optional) are any number of custom 'arg=value' pairs like 'imgsz=320' that override defaults.

# AMD Ryzen 5 3500U with Radeon Vega Mobile Gfx