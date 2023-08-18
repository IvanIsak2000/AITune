# AITune
AI-based music selection service.

https://www.figma.com/file/Fc8ElhQBpaPcGh3RhxgcoM/Untitled?type=design&node-id=112-55&mode=design&t=cvx2Be43cGXnHFpn-0

# Instalation 
1. Clone repo

2. Install [flowers dataset](https://www.kaggle.com/datasets/alxmamaev/flowers-recognition/download?datasetVersionNumber=2) in `src` folder

3. Install `requirements.txt`

4. Change dir: `cd src`
   
5. Train model:
   
```bash
yolo task=classify mode=train model=yolov8s-cls.pt data=datasets/flowers epochs=10 imgsz=600
```
6. Start model:
   
```bash
python3 start_model.py 1.jpeg
```
