import os.path
import shutil

train_folder = 'src/flowers/train'


for subclass in train_folder:
    train_path = 'src/flowers/train/'
    test_path = 'src/flowers/test/'
    print(f'Name: {subclass}, {len(os.listdir(train_path+subclass))}')
    images = sorted(os.listdir(train_path + subclass))[:20]
    os.mkdir(test_path+subclass)
    test = test_path + subclass

    for i in images:
        shutil.copy(train_path+subclass+'/'+i, test+'/'+i)
        os.remove(train_path+subclass+'/'+i)
