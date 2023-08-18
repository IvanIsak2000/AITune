from PIL import Image
import sys

from PIL import Image
from ultralytics import YOLO

model = YOLO("colab_model.pt")
im1 = Image.open(sys.argv[1])

results = model(im1)

print(results)
