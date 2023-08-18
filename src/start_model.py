from PIL import Image
import sys

from PIL import Image
from ultralytics import YOLO

model = YOLO("colab_model.pt")
im1 = Image.open(sys.argv[1])

results = model(im1)

for r in results:
    im_array = r.plot()  
    im = Image.fromarray(im_array[..., ::-1])  
    im.show()  
    # im.save('results.jpg')  