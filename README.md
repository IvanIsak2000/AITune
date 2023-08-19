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

# Run
Before train check project structure:
> Note:
> Project structure show MAIN files to correct train and check model
>
``` 

├── src                     # root folder
│   └── datasets            # dataset for `yolo8` which separetad on 2 folders
|       └── flowers
|            ├── train      # train images folder: ~4222 files by 5 subfolders
|            └── test       # test images folder: by 20 images in each
│   ├── start_model.py      # main file to check model 
|   ├── 1.jpeg              # new image not from datasets to mdel test
│   └── 2.jpeg              # new image not from datasets to mdel test   
└── 
```

1. Change folder:
```bash
cd src
```

2. Train model:

>   <picture>
>   <source media="(prefers-color-scheme: light)" srcset="https://github.com/Mqxx/GitHub-Markdown/blob/main/blockquotes/badge/light-theme/warning.svg">
>   <img alt="Warning" src="https://github.com/Mqxx/GitHub-Markdown/blob/main/blockquotes/badge/dark-theme/warning.svg">
>   </picture><br>
>   Ultralytics YOLO can be run on a variety of hardware configurations, including CPUs, GPUs, and even some edge devices. However, for optimal performance and faster training and inference, >   we recommend using a GPU with a minimum of 8GB of memory. NVIDIA GPUs with CUDA support are ideal for this purpose.

```bash
yolo task=classify mode=train model=yolov8s-cls.pt data=datasets/flowers epochs=3 imgsz=600
```
> For better result you can add epochs, but the training process will be longer.

3. Start model:
```bash
python3 start_model.py 1.jpeg
```

# Result
If all done you get result:

![image](https://github.com/IvanIsak2000/AITune/assets/79650307/f993b938-a7f0-444c-8c50-045bf7b720b1)


