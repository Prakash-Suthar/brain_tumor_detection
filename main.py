# import subprocess
from fastapi import FastAPI, UploadFile, File
from ultralytics import YOLO


def model_train():
    model = YOLO('./runs/classify/train/weights/best.pt')  # load a pretrained YOLOv8n classification model
    return model


app = FastAPI()
model_data = None

@app.post("/images/")
def create_upload_file(image: UploadFile = File(...)):
    global model_data
    if model_data is None:
        model_data = model_train()

    with open(f"./images/{image.filename}", "wb+") as f:
        print(f)
        f.write(image.file.read())

    result = model_data(f"./images/{image.filename}")

    return {"result": result[0].names[result[0].probs.top1]}


# def run_uvicon():
#     uvicorn_command = [
#         "uvicorn",
#         "main:app",
#         "--host", "127.0.0.1",
#         "--port", "8000",
#         "--reload",
#     ]

#     subprocess.run(uvicorn_command, check=True)


# if __name__ == "__main__":
#     run_uvicon()