# AITune
AI-based service.

https://www.figma.com/file/Fc8ElhQBpaPcGh3RhxgcoM/Untitled?type=design&node-id=112-55&mode=design&t=cvx2Be43cGXnHFpn-0

# Instalation 

1. Clone repo:
```bash
git clone https://github.com/IvanIsak2000/AITune.git
```

2. Install [flowers dataset folder](https://drive.google.com/drive/folders/1jHoqyRb_yJDNSiYhHHT8CYJ4kHlw8V9e?usp=sharing) in `src` folder

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Change folder:
```bash
cd src
```

5. Train model:

>   <picture>
>   <source media="(prefers-color-scheme: light)" srcset="https://github.com/Mqxx/GitHub-Markdown/blob/main/blockquotes/badge/light-theme/warning.svg">
>   <img alt="Warning" src="https://github.com/Mqxx/GitHub-Markdown/blob/main/blockquotes/badge/dark-theme/warning.svg">
>   </picture><br>
>   Ultralytics YOLO can be run on a variety of hardware configurations, including CPUs, GPUs, and even some edge devices. However, for optimal performance and faster training and inference, >   we recommend using a GPU with a minimum of 8GB of memory. NVIDIA GPUs with CUDA support are ideal for this purpose.

```bash
yolo task=classify mode=train model=yolov8s-cls.pt data=datasets/flowers epochs=3 imgsz=600
```
> For better result you can add epochs, but the training process will be longer.


6. Start model:
```bash
python3 start_model.py 1.jpeg
```
