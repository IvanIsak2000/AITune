# from PIL import Image
import sys

from PIL import Image
from ultralytics import YOLO
import os.path
import shutil


def main(image_path: str, model: str):
    image = Image.open(image_path)
    model = YOLO(model)

    # remove old result folder of  data
    if len(os.listdir('result')) != 0:
        for i in os.listdir('result'):
            print(i)
            shutil.rmtree('result/' + i)

    model.predict(image, save_txt=True, show=False, project='result', stream=False)

    # for r in results:
    #     im_array = r.plot()
    #     im = Image.fromarray(im_array[..., ::-1])
    #     im.show()
    # im.save('results.jpg')

    with open('result/predict/labels/' + os.listdir('result/predict/labels')[0], 'r') as file:
        text = file.read().split('\n')

        result = []

        for row in text:
            try:
                if float(row.split()[0]) != 0:
                    result.append(row)
            except IndexError:
                break

        return print(f'Most likely this {result[0].split()[1]}, accuracy {result[0].split()[0]}' if float(
            result[0].split()[0]) > 0.5 else result)


if __name__ == '__main__':
    image_path = sys.argv[1]
    try:
        model = sys.argv[2]
    except IndexError:
        model = "colab_model.pt"

    main(image_path, model)
